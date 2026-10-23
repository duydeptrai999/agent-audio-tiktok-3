# -*- coding: utf-8 -*-
"""
scripts/pre_produce_night_slots.py
Sản xuất trước toàn bộ các bộ video ban đêm (Slot 8, 9, 10) cho ngày hôm nay:
- Kịch bản kịch tính, mở đầu cuốn hút, KHÔNG ngày giờ / mở đầu máy móc.
- Audio đọc 1.5x NamMinh trầm ấm, không filler lặp lại.
- Video 1080p MP4 chuẩn 1 video stream + 1 audio stream (tuyệt đối KHÔNG attached_pic).
- Nhạc nền nhẹ 0.25 từ Horror_BGM_Audio/
- Thumbnail JPG độc lập.
- Thẩm định 100% qua VideoAuditEngine trước khi sẵn sàng cho Autopilot.
"""

import sys
import json
import asyncio
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.audio_engine import generate_cinema_tts_audio
from core.ffmpeg_utils import render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME
from core.stories.daily_story_factory import get_daily_10_series
from core.video_audit_engine import VideoAuditEngine

DATA_DIR = ROOT / "data"
AUDIO_DIR = ROOT / "assets" / "audio"
OUTPUT_DIR = ROOT / "assets" / "output"
THUMB_DIR = ROOT / "assets" / "thumbnails"
SCRIPTS_DIR = DATA_DIR / "generated_scripts"

for d in [DATA_DIR, AUDIO_DIR, OUTPUT_DIR, THUMB_DIR, SCRIPTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def update_status_produced(date_str: str, s_key: str):
    status_file = DATA_DIR / f"daily_schedule_status_{date_str}.json"
    if status_file.exists():
        try:
            status = json.loads(status_file.read_text(encoding="utf-8"))
            if s_key in status:
                status[s_key]["produced"] = True
                status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
                print(f"  💾 Đã cập nhật status: {s_key} -> produced = True")
        except Exception as e:
            print(f"  ⚠️ Lỗi cập nhật status file: {e}")

def main():
    date_str = "2026-10-19"
    all_series = get_daily_10_series(date_str)
    night_series = [s for s in all_series if s["slot_index"] in [9, 10]]

    print("=" * 80)
    print(f"🎬 [TIỀN SẢN XUẤT BAN ĐÊM] BẮT ĐẦU DỰNG TOÀN BỘ CÁC BỘ CÒN LẠI CỦA NGÀY {date_str}")
    print(f"📋 Danh sách slot: {[s['slot_index'] for s in night_series]}")
    print("=" * 80)

    for s in night_series:
        slot_idx = s["slot_index"]
        s_key = s["key"]
        prefix = s["prefix"]
        title = s["title"]
        voice = s.get("voice", "vi-VN-NamMinhNeural")
        bgm_genre = s.get("bgm_genre", "HORROR")
        bgm_file = get_safe_bgm_for_genre(bgm_genre)

        print(f"\n" + "#" * 70)
        print(f"🔥 SẢN XUẤT SLOT {slot_idx}/10: {title} ({s.get('genre', '')})")
        print(f"🎵 Nhạc nền đêm: {Path(bgm_file).name} (Âm lượng: {BGM_VOLUME}) | Giọng: {voice}")
        print("#" * 70)

        # Lưu file kịch bản
        script_file = SCRIPTS_DIR / f"{prefix}.json"
        script_file.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")

        for part in s["parts"]:
            p_num = part["part_number"]
            badge = part["badge_label"]
            raw_text = part["text"]

            part_audio = AUDIO_DIR / f"{prefix}_part{p_num}_15x.mp3"
            part_video = OUTPUT_DIR / f"{prefix}_part{p_num}_final.mp4"
            part_thumb = THUMB_DIR / f"{prefix}_part{p_num}_thumb.jpg"

            print(f"\n--- [TẬP {p_num}] ({len(raw_text.split())} từ) ---")

            # 1. Sinh audio TTS
            if not part_audio.exists() or part_audio.stat().st_size < 10000:
                print(f"  🎙️ Đang sinh TTS 1.5x ({voice})...")
                asyncio.run(generate_cinema_tts_audio(
                    text=raw_text,
                    voice=voice,
                    output_path=part_audio,
                    target_speed=1.50
                ))
            else:
                print(f"  ✅ Audio đã tồn tại ({part_audio.stat().st_size / 1024:.1f} KB).")

            # Kiểm tra nếu video đã hoàn thành và đạt chuẩn từ trước
            if part_video.exists():
                vprobe = probe_media_file(part_video)
                if vprobe.get("is_valid") and vprobe.get("duration", 0) >= 180.0:
                    passed, report, metrics = VideoAuditEngine.audit_video_before_publish(
                        video_path=part_video,
                        audio_path=part_audio,
                        title=title,
                        prefix=prefix,
                        part_num=p_num,
                        caption=f"[TẬP {p_num}] {title}"
                    )
                    if passed:
                        print(f"  ⏭️ Video đã có sẵn và ĐẠT MASTER AUDIT 100%: {part_video.name} ({metrics['duration']:.1f}s)")
                        continue
                    else:
                        print(f"  🗑️ Xóa video không đạt audit ({part_video.name}) để dựng lại...")
                        part_video.unlink()
                else:
                    print(f"  🗑️ Xóa video dở dang ({part_video.name}) để dựng lại...")
                    part_video.unlink()

            # 2. Đo thời lượng & cắt Footage B-Roll
            probe = probe_media_file(part_audio)
            dur = probe.get("duration", 300.0)
            print(f"  ⏱️ Thời lượng audio: {dur:.1f}s (~{dur/60:.1f} phút)")

            slice_path = background_manager.get_distinct_slice_for_part(
                series_id=prefix,
                part_number=p_num,
                duration_seconds=dur
            )

            # 3. Tạo Thumbnail độc lập
            if not part_thumb.exists() or part_thumb.stat().st_size < 5000:
                try:
                    generate_part_thumbnail(
                        source_video_or_image=slice_path,
                        output_thumb_path=part_thumb,
                        story_title=title,
                        part_label=f"TẬP {p_num}",
                        genre_tag=f"#{s.get('genre', 'TrinhThám')}"
                    )
                    print(f"  🖼️ Đã tạo thumbnail: {part_thumb.name}")
                except Exception as e:
                    print(f"  ⚠️ Lỗi tạo thumbnail: {e}")

            # 4. Render Video MP4 (1080p, 1 Video + 1 Audio, KHÔNG attached_pic)
            print(f"  🎥 Đang render video 1080p...")
            render_playable_video(
                output_file=part_video,
                voice_audio_path=str(part_audio),
                clean_footage_path=str(slice_path),
                bgm_audio_path=str(bgm_file),
                badge_label=badge,
                bgm_volume=BGM_VOLUME if bgm_file else 0.0,
                voice_volume=VOICE_VOLUME,
                enable_subtitles=False,
                thumbnail_path=None  # Cấm gắn attached_pic
            )
            print(f"  ✅ Render video hoàn tất: {part_video.name} ({part_video.stat().st_size / 1024 / 1024:.2f} MB)")

            # 5. Master Audit thẩm định chất lượng ngay tại chỗ
            print(f"  🔍 Bắt đầu Master Audit cho {part_video.name}...")
            passed, report, metrics = VideoAuditEngine.audit_video_before_publish(
                video_path=part_video,
                audio_path=part_audio,
                title=title,
                prefix=prefix,
                part_num=p_num,
                caption=f"[TẬP {p_num}] {title}"
            )
            if passed:
                print(f"  🏆 MASTER AUDIT ĐẠT 100%: Duration={metrics['duration']:.1f}s | MeanVol={metrics['mean_volume_db']:.1f}dB | MaxVol={metrics['max_volume_db']:.1f}dB")
            else:
                print(f"  🚨 MASTER AUDIT THẤT BẠI: {report}")
                sys.exit(1)

        # Cập nhật status
        update_status_produced(date_str, s_key)
        print(f"\n🎉 HOÀN TẤT TRỌN VẸN 3 TẬP SẠCH CHO: {title}!")

    print("\n" + "=" * 80)
    print("🌟 ĐÃ HOÀN TẤT SẢN XUẤT VÀ MASTER AUDIT CHO TOÀN BỘ CÁC BỘ ĐÊM NAY (SLOT 8, 9, 10)!")
    print("=" * 80)

if __name__ == "__main__":
    main()
