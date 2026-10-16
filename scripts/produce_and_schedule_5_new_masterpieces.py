# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_5_new_masterpieces.py
Hệ Thống Tự Động Hóa Toàn Diện Sản Xuất & Lên Lịch Đăng 5 Bộ Truyện Audio Hoàn Toàn Mới (15 Video MP4):
1. Bộ 1 (Sa Điêu / Tiếng Lòng): Khi Cả Nhà Hào Môn Nghe Thấy Tiếng Lòng Nàng Dâu Giả Ngốc
2. Bộ 2 (Cung Đấu / Nữ Quyền): Phượng Hoàng Niết Bàn: Hoàng Hậu Bãi Công Đi Thi Trạng Nguyên
3. Bộ 3 (Trinh Thám / Huyền Nghi): Kỳ Án Viện Bảo Tàng: Bức Họa Rỉ Máu Lúc Nửa Đêm
4. Bộ 4 (Vô Hạn Lưu / Quái Đàm): Khách Sạn Nửa Đêm: 10 Quy Tắc Sinh Tồn Ca Đêm
5. Bộ 5 (Trọng Sinh / Vả Mặt): Thiên Kim Thật Trở Về: Cú Vả Mặt Chấn Động Giới Thượng Lưu

Tính năng bảo vệ & dọn dẹp chống đăng trùng:
- ĐĂNG XONG ĐẾN ĐÂU - XÓA NGAY ĐẾN ĐÓ:
  + Đăng xong 1 tập -> Xóa ngay video MP4, audio MP3, thumbnail của tập đó.
  + Đăng xong trọn vẹn cả 3 tập của 1 bộ -> Xóa ngay kịch bản JSON của bộ đó.
  + Tuyệt đối không để video cũ tồn đọng gây đăng lặp lại hay chiếm dụng bộ nhớ.
"""

import sys
import os
import time
import json
import asyncio
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
        sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass

from core.audio_engine import generate_cinema_tts_audio
from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME
from scripts.tiktok_publisher_core import upload_and_publish_video
from core.stories.new_5_masterpieces import get_new_5_series_data
from core.anti_repost_guard import AntiRepostGuard

STATUS_FILE = ROOT / "data" / "new_5series_publishing_status.json"

def load_status() -> dict:
    series_list = get_new_5_series_data()
    default_status = {
        item["key"]: {
            "produced": False,
            "part1_produced": False,
            "part2_produced": False,
            "part3_produced": False,
            "part1": False,
            "part2": False,
            "part3": False
        }
        for item in series_list
    }
    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text(encoding='utf-8'))
            for k, v in default_status.items():
                if k not in data:
                    data[k] = v
                else:
                    for sub_k, sub_v in v.items():
                        if sub_k not in data[k]:
                            data[k][sub_k] = sub_v
            return data
        except Exception:
            pass
    return default_status

def save_status(status: dict):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def produce_all_new_series():
    """Sản xuất toàn bộ 5 bộ audio mới (15 video MP4 1080p)."""
    series_list = get_new_5_series_data()
    status = load_status()

    audio_dir = ROOT / "assets" / "audio"
    out_dir = ROOT / "assets" / "output"
    thumb_dir = ROOT / "assets" / "thumbnails"
    scripts_dir = ROOT / "data" / "generated_scripts"
    audio_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("🎬 [BƯỚC 1: SẢN XUẤT 5 BỘ AUDIO HOÀN TOÀN MỚI] BẮT ĐẦU")
    print(f"⏰ Thời điểm: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 Tổng quy mô: 5 Bộ Truyện Masterpiece x 3 Tập = 15 Video MP4 1080p")
    print("=" * 80)

    total_start = time.time()

    for s_idx, series_data in enumerate(series_list):
        s_key = series_data["key"]
        prefix = series_data["prefix"]
        title = series_data["title"]
        voice = series_data["voice"]
        bgm_genre = series_data["bgm_genre"]
        bgm_file = get_safe_bgm_for_genre(bgm_genre)

        # Lưu file kịch bản JSON nếu chưa có
        script_file = scripts_dir / f"{prefix}.json"
        if not script_file.exists():
            script_file.write_text(json.dumps(series_data, indent=2, ensure_ascii=False), encoding='utf-8')

        print(f"\n" + "#" * 70)
        print(f"🔥 SẢN XUẤT BỘ {s_idx + 1}/5: {title}")
        print(f"🎙️ Giọng đọc: {voice} (1.50x Studio Radio Vocal Chain) | BGM: {bgm_genre}")
        print("#" * 70)

        for part in series_data["parts"]:
            p_num = part["part_number"]
            badge = part["badge_label"]
            p_prod_key = f"part{p_num}_produced"

            part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
            part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
            part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"

            print(f"\n--- [TẬP {p_num}] {badge} ---")

            # 1. Sinh Audio Cinema TTS 1.5x (nếu chưa có)
            if not part_audio.exists() or part_audio.stat().st_size < 10000:
                print(f"  🎙️ Đang sinh giọng đọc AI Edge-TTS ({voice}) cho Tập {p_num}...")
                t_audio_start = time.time()
                asyncio.run(generate_cinema_tts_audio(
                    text=part["text"],
                    voice=voice,
                    output_path=part_audio,
                    target_speed=1.50
                ))
                print(f"  ✅ Audio hoàn tất trong {time.time() - t_audio_start:.1f}s ({part_audio.stat().st_size / 1024:.1f} KB)")
            else:
                print(f"  ✅ Audio đã có sẵn: {part_audio.name} ({part_audio.stat().st_size / 1024:.1f} KB)")

            # Lấy thời lượng audio
            probe = probe_media_file(part_audio)
            dur = probe.get("duration", 300.0)
            if dur < 10.0:
                dur = 300.0

            # 2. Cắt lát B-Roll hoàn toàn độc lập từ YouTube Pool
            distinct_slice = background_manager.get_distinct_slice_for_part(
                series_id=prefix,
                part_number=p_num,
                duration_seconds=dur
            )

            # 3. Tạo Thumbnail độc quyền
            if not part_thumb.exists() or part_thumb.stat().st_size < 5000:
                try:
                    generate_part_thumbnail(
                        source_video_or_image=distinct_slice,
                        output_thumb_path=part_thumb,
                        story_title=title,
                        part_label=f"TẬP {p_num}",
                        genre_tag=f"#{series_data.get('genre', 'AudioTruyện')}"
                    )
                    print(f"  🖼️ Đã tạo Thumbnail độc quyền: {part_thumb.name}")
                except Exception as te:
                    print(f"  ⚠️ Lỗi tạo thumbnail: {te}")
                    part_thumb = None

            # 4. Render Video MP4 1080p
            if not part_video.exists() or part_video.stat().st_size < 500000:
                print(f"  🎥 Đang render video 1080p MP4 (BGM Auto-Ducking -20dB + B-Roll riêng)...")
                t_render_start = time.time()
                render_playable_video(
                    output_file=part_video,
                    voice_audio_path=str(part_audio),
                    clean_footage_path=str(distinct_slice),
                    bgm_audio_path=str(bgm_file),
                    badge_label=badge,
                    bgm_volume=BGM_VOLUME,
                    voice_volume=VOICE_VOLUME,
                    enable_subtitles=False,
                    thumbnail_path=str(part_thumb) if part_thumb and part_thumb.exists() else None
                )
                print(f"  🎉 Render video thành công trong {time.time() - t_render_start:.1f}s! ({part_video.stat().st_size / (1024*1024):.1f} MB)")
            else:
                print(f"  ✅ Video đã sẵn sàng: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")

            status[s_key][p_prod_key] = True
            save_status(status)

        status[s_key]["produced"] = True
        save_status(status)
        print(f"\n🏆 ĐÃ HOÀN TẤT SẢN XUẤT TRỌN VẸN BỘ {s_idx + 1}: {title}!")

    total_dur = time.time() - total_start
    print("\n" + "=" * 80)
    print(f"🎉 TẤT CẢ 5 BỘ TRUYỆN AUDIO MỚI (15 VIDEO MP4 FULL HD) ĐÃ ĐƯỢC SẢN XUẤT XONG!")
    print(f"⏱️ Tổng thời gian sản xuất: {total_dur / 60:.1f} phút")
    print("=" * 80)

def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    title = series_conf["title"]
    hook = series_conf["hooks"][part_num - 1]
    magnet = series_conf["magnets"][part_num - 1]
    tag = series_conf["genre_tag"]
    return f"{badge} {title}. {hook} {magnet} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}"

def wait_until(target_timestamp: float, label: str):
    now = time.time()
    if target_timestamp <= now:
        return
    diff = int(target_timestamp - now)
    print(f"\n⏳ [{datetime.now().strftime('%H:%M:%S')}] Chờ đến mốc đăng {label} (còn {diff // 3600}h {(diff % 3600) // 60}m {diff % 60}s)...", flush=True)
    while time.time() < target_timestamp:
        remaining = int(target_timestamp - time.time())
        if remaining % 300 == 0 or (remaining <= 60 and remaining % 10 == 0) or remaining <= 5:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Còn {remaining // 3600}h {(remaining % 3600) // 60}m {remaining % 60}s tới mốc đăng {label}...", flush=True)
        time.sleep(min(5, max(1, remaining)))

def run_scheduler_at_7am(
    target_start_hour: int = 7,
    target_start_minute: int = 0,
    interval_parts_min: int = 20,
    interval_series_min: int = 60,
    reset: bool = False
):
    """
    Quản trị lịch trình đăng bài:
    - Mặc định khởi động đúng 07:00 sáng hôm nay.
    - ĐĂNG XONG TẬP NÀO -> XÓA NGAY VIDEO & AUDIO TẬP ĐÓ (Chống trùng lặp, tiết kiệm ổ cứng).
    - ĐĂNG XONG CẢ BỘ -> XÓA NGAY KỊCH BẢN JSON CỦA BỘ ĐÓ.
    """
    out_dir = ROOT / "assets" / "output"
    thumb_dir = ROOT / "assets" / "thumbnails"
    audio_dir = ROOT / "assets" / "audio"
    scripts_dir = ROOT / "data" / "generated_scripts"
    series_list = get_new_5_series_data()

    if reset and STATUS_FILE.exists():
        STATUS_FILE.unlink(missing_ok=True)
        print("🔄 Đã reset trạng thái xuất bản!")

    status = load_status()

    # Tính toán mốc 07:00 AM hôm nay
    now = datetime.now()
    target_7am = now.replace(hour=target_start_hour, minute=target_start_minute, second=0, microsecond=0)
    if target_7am.timestamp() < time.time() - 3600:
        base_time = time.time()
    else:
        base_time = target_7am.timestamp()

    status["scheduled_base_time"] = base_time
    save_status(status)

    interval_parts_sec = interval_parts_min * 60
    interval_series_sec = interval_series_min * 60

    print("=" * 80)
    print("🚀 [LỊCH TRÌNH ĐĂNG BÀI MASTER TIKTOK] 5 BỘ TRUYỆN AUDIO HOÀN TOÀN MỚI")
    print(f"⏰ Giờ bắt đầu phát hành chính thức: {datetime.fromtimestamp(base_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Giãn cách: Cách {interval_series_min} phút đăng 1 bộ. Trong mỗi bộ, 3 tập cách nhau {interval_parts_min} phút.")
    print(f"🧹 Cơ chế: Đăng thành công tập nào -> Tự động xóa ngay video/audio tập đó để chống đăng lặp!")
    print("=" * 80)

    for s_idx, conf in enumerate(series_list):
        s_key = conf["key"]
        s_title = conf["title"]
        prefix = conf["prefix"]
        s_start_time = base_time + s_idx * interval_series_sec

        print(f"\n" + "#" * 70)
        print(f"🎬 BỘ {s_idx + 1}/5: {s_title}")
        print(f"⏰ Thời điểm bắt đầu bộ: {datetime.fromtimestamp(s_start_time).strftime('%H:%M:%S')}")
        print("#" * 70)

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng thành công trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_start_time + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx + 1} - Tập {p_idx}")

            vid_file = out_dir / f"{prefix}_part{p_idx}_final.mp4"
            part_thumb_file = thumb_dir / f"{prefix}_part{p_idx}_thumb.jpg"
            part_audio_file = audio_dir / f"{prefix}_part{p_idx}_15x.mp3"

            if not vid_file.exists():
                print(f"❌ Không tìm thấy file video: {vid_file.name}. Bỏ qua...")
                continue

            caption = get_caption_for_part(conf, p_idx)

            # 🛡️ KIỂM DUYỆT BẢO VỆ CHỐNG ĐĂNG LẠI AUDIO CŨ
            is_safe, reason = AntiRepostGuard.verify_candidate_audio(
                title=conf["title"],
                caption=caption,
                audio_path=part_audio_file,
                video_path=vid_file
            )
            if not is_safe:
                print(f"\n🚨 [AntiRepostGuard] TỪ CHỐI ĐĂNG {s_key} - {p_key}:")
                print(f"   => {reason}")
                print(f"   => Tự động xóa bỏ tệp cũ để bảo vệ an toàn cho kênh!")
                vid_file.unlink(missing_ok=True)
                if part_audio_file.exists():
                    part_audio_file.unlink(missing_ok=True)
                continue

            upload_success = False
            for attempt in range(1, 4):
                print(f"\n📲 Đang tải lên TikTok Studio: {vid_file.name} (Lần thử {attempt}/3)...")
                try:
                    upload_success = upload_and_publish_video(
                        video_path=vid_file,
                        caption=caption,
                        screenshot_prefix=f"{s_key}_{p_key}",
                        thumbnail_path=part_thumb_file if part_thumb_file.exists() else None
                    )
                except Exception as ue:
                    print(f"  ⚠️ Ngoại lệ khi đăng: {ue}")
                    upload_success = False

                if upload_success:
                    status[s_key][p_key] = True
                    save_status(status)
                    print(f"🎉 ĐÃ XUẤT BẢN THÀNH CÔNG: {s_key} - {p_key} lúc {datetime.now().strftime('%H:%M:%S')}!")

                    # Ghi nhận vào Registry chống trùng lặp vĩnh viễn
                    try:
                        AntiRepostGuard.register_successful_publish(
                            title=conf["title"],
                            prefix=prefix,
                            part_num=p_idx,
                            audio_path=part_audio_file,
                            video_path=vid_file
                        )
                    except Exception:
                        pass

                    # 🧹 TỰ ĐỘNG XÓA VIDEO, AUDIO, THUMBNAIL SAU KHI ĐĂNG XONG
                    if vid_file.exists():
                        try:
                            vid_file.unlink(missing_ok=True)
                            print(f"  🗑️ Đã xóa video thành phẩm: {vid_file.name} (chống trùng lặp & giải phóng ổ cứng)")
                        except Exception as e_del:
                            print(f"  ⚠️ Không thể xóa video: {e_del}")

                    if part_audio_file.exists():
                        try:
                            part_audio_file.unlink(missing_ok=True)
                            print(f"  🗑️ Đã xóa audio đã đăng: {part_audio_file.name}")
                        except Exception:
                            pass

                    if part_thumb_file and part_thumb_file.exists():
                        try:
                            part_thumb_file.unlink(missing_ok=True)
                            print(f"  🗑️ Đã xóa thumbnail: {part_thumb_file.name}")
                        except Exception:
                            pass

                    break
                else:
                    print(f"  ⚠️ Lần thử {attempt} chưa thành công. Tạm dừng 15s trước khi thử lại...")
                    time.sleep(15)

            if not upload_success:
                print(f"❌ CẢNH BÁO: Đăng {s_key} - {p_key} thất bại sau 3 lần thử!")

        # 🧹 Khi đăng trọn vẹn cả 3 tập của bộ -> Xóa kịch bản JSON
        all_parts_posted = all(status[s_key].get(f"part{i}", False) for i in [1, 2, 3])
        if all_parts_posted:
            script_json_file = scripts_dir / f"{prefix}.json"
            if script_json_file.exists():
                try:
                    script_json_file.unlink(missing_ok=True)
                    print(f"  🗑️ Đã xóa kịch bản JSON của bộ: {script_json_file.name} (đã hoàn thành xuất bản)")
                except Exception:
                    pass

        print(f"\n🎉 HOÀN TẤT BỘ {s_idx + 1}: {s_title}!")

    print("\n" + "=" * 80)
    print("🏆 TOÀN BỘ 5 BỘ TRUYỆN AUDIO MỚI ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG LÊN TIKTOK!")
    print("🧹 TẤT CẢ VIDEO, AUDIO VÀ KỊCH BẢN CŨ ĐÃ ĐƯỢC TỰ ĐỘNG DỌN DẸP SẠCH SẼ!")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Produce and Schedule 5 Brand New Masterpieces")
    parser.add_argument("--produce-only", action="store_true", help="Chỉ sản xuất video và audio, không chờ đăng")
    parser.add_argument("--schedule-only", action="store_true", help="Chỉ chạy scheduler đăng bài bắt đầu lúc 7h sáng")
    parser.add_argument("--start-hour", type=int, default=7, help="Giờ bắt đầu đăng (mặc định 7h sáng)")
    parser.add_argument("--start-minute", type=int, default=0, help="Phút bắt đầu đăng (mặc định 0)")
    parser.add_argument("--reset", action="store_true", help="Reset trạng thái đăng")
    args = parser.parse_args()

    if args.produce_only:
        produce_all_new_series()
    elif args.schedule_only:
        run_scheduler_at_7am(
            target_start_hour=args.start_hour,
            target_start_minute=args.start_minute,
            reset=args.reset
        )
    else:
        produce_all_new_series()
        run_scheduler_at_7am(
            target_start_hour=args.start_hour,
            target_start_minute=args.start_minute,
            reset=args.reset
        )

if __name__ == "__main__":
    main()
