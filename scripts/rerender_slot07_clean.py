# -*- coding: utf-8 -*-
"""
scripts/rerender_slot07_clean.py
Tái tạo sạch sẽ Tập 2 và Tập 3 của Bộ 7 (Slot 7 - Gia đấu / Mẹ chồng thức tỉnh):
- Loại bỏ toàn bộ 50 câu văn filler lặp lại.
- Dựng MP4 chuẩn 1 video stream + 1 audio stream (KHÔNG attached_pic).
- Nhạc nền nhẹ 0.25 (TikTok_BGM_Audio).
- Chạy Master Audit xác nhận 100% trước khi autopilot kích hoạt lúc 17:50 và 18:10.
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

def main():
    date_str = "2026-10-19"
    all_series = get_daily_10_series(date_str)
    s7 = next(s for s in all_series if s["slot_index"] == 7)

    prefix = s7["prefix"]
    title = s7["title"]
    voice = s7.get("voice", "vi-VN-HoaiMyNeural")
    bgm_genre = s7.get("bgm_genre", "ROMANCE")
    bgm_file = get_safe_bgm_for_genre(bgm_genre)

    print(f"🎬 [TÁI TẠO SẠCH BỘ 7] Tựa đề: {title}")
    print(f"🎵 Nhạc nền: {Path(bgm_file).name} (Âm lượng: {BGM_VOLUME})")

    # Cập nhật lại file JSON kịch bản
    script_file = SCRIPTS_DIR / f"{prefix}.json"
    script_file.write_text(json.dumps(s7, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"📝 Đã cập nhật file kịch bản sạch: {script_file.name}")

    for p in s7["parts"]:
        p_num = p["part_number"]
        if p_num == 1:
            # Tập 1 đã xuất bản thành công lúc 17:30, giữ nguyên
            print(f"⏭️ Tập 1 đã đăng thành công lúc 17:30, bỏ qua.")
            continue

        badge = p["badge_label"]
        raw_text = p["text"]
        part_audio = AUDIO_DIR / f"{prefix}_part{p_num}_15x.mp3"
        part_video = OUTPUT_DIR / f"{prefix}_part{p_num}_final.mp4"
        part_thumb = THUMB_DIR / f"{prefix}_part{p_num}_thumb.jpg"

        print(f"\n" + "=" * 60)
        print(f"🚀 BẮT ĐẦU TÁI TẠO SẠCH: Tập {p_num} ({len(raw_text.split())} từ)...")

        # Xóa file cũ dính lỗi attached_pic hoặc filler
        if part_audio.exists():
            part_audio.unlink()
        if part_video.exists():
            part_video.unlink()

        # 1. Sinh Audio mới
        print(f"  🎙️ Đang sinh TTS 1.5x ({voice})...")
        asyncio.run(generate_cinema_tts_audio(
            text=raw_text,
            voice=voice,
            output_path=part_audio,
            target_speed=1.50
        ))

        # 2. Cắt B-Roll
        probe = probe_media_file(part_audio)
        dur = probe.get("duration", 300.0)
        print(f"  ⏱️ Thời lượng audio: {dur:.1f}s")
        slice_path = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        # 3. Tạo thumbnail JPG độc lập
        generate_part_thumbnail(
            source_video_or_image=slice_path,
            output_thumb_path=part_thumb,
            story_title=title,
            part_label=f"TẬP {p_num}",
            genre_tag=f"#{s7.get('genre', 'GiaĐấu')}"
        )

        # 4. Render video chuẩn (Single Video + Single Audio, KHÔNG attached_pic)
        print(f"  🎥 Đang render video MP4 1080p chuẩn...")
        render_playable_video(
            output_file=part_video,
            voice_audio_path=str(part_audio),
            clean_footage_path=str(slice_path),
            bgm_audio_path=str(bgm_file),
            badge_label=badge,
            bgm_volume=BGM_VOLUME,
            voice_volume=VOICE_VOLUME,
            enable_subtitles=False,
            thumbnail_path=str(part_thumb)
        )

        # 5. Thẩm định Master Audit ngay lập tức
        print(f"\n  🔍 KIỂM ĐỊNH MASTER AUDIT TẬP {p_num}:")
        passed, report, metrics = VideoAuditEngine.audit_video_before_publish(
            video_path=part_video,
            audio_path=part_audio,
            title=title,
            prefix=prefix,
            part_num=p_num,
            caption="",
            script_text=raw_text
        )
        print(report)
        if not passed:
            raise RuntimeError(f"Tập {p_num} không đạt kiểm định Master Audit!")
        print(f"  🎉 TẬP {p_num} HOÀN TẤT VÀ ĐẠT 100% MASTER AUDIT!")

    print("\n" + "=" * 60)
    print("✅ ĐÃ TÁI TẠO XONG HOÀN TOÀN CẢ HAI TẬP 2 VÀ 3 CỦA BỘ 7! SẴN SÀNG CHO AUTOPILOT.")

if __name__ == "__main__":
    main()
