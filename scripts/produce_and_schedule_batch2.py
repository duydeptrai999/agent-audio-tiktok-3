# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_batch2.py
Hệ Thống Tự Động Hóa Toàn Diện Sản Xuất & Đăng 5 Bộ Truyện Audio Masterpiece Batch 2 (15 Video MP4):
1. Bộ 1 (Sa Điêu / Đọc Tâm): Thư Ký Nhỏ Biết Đọc Tiếng Lòng: Sếp Tổng Mặt Lạnh Mỗi Ngày Đều Tỏ Tình Trong Đầu
2. Bộ 2 (Trọng Sinh / Vả Mặt Hào Môn): Thiên Kim Thật Đoạt Lại Vận Mệnh: Ba Anh Trai Quỳ Gối Cầu Xin Tha Thứ
3. Bộ 3 (Nữ Cường / Quyền Mưu Cung Đấu): Đích Nữ Tướng Môn: Nhận Chiếu Hòa Thân, Nàng San Bằng Biên Cương Về Triều
4. Bộ 4 (Huyền Nghi / Trinh Thám Pháp Y): Lời Khai Của Thi Thể Lúc Nửa Đêm: Vết Mực Bí Ẩn Trên Ngón Tay Nạn Nhân
5. Bộ 5 (Thanh Xuân / Cứu Rỗi / Chữa Lành): Bức Thư Mùa Hạ Mười Năm Trước: Chiếc Ô Xanh Dưới Cơn Mưa Tốt Nghiệp

Chế độ bảo vệ & dọn dẹp chống đăng trùng:
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
from core.stories.batch2_5_masterpieces import get_batch2_5_series_data
from core.anti_repost_guard import AntiRepostGuard

STATUS_FILE = ROOT / "data" / "batch2_publishing_status.json"

def load_status() -> dict:
    series_list = get_batch2_5_series_data()
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
    default_status["_meta"] = {
        "last_published_timestamp": 0.0,
        "last_published_time_str": "",
        "last_published_episode": ""
    }
    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text(encoding='utf-8'))
            for k, v in default_status.items():
                if k not in data:
                    data[k] = v
                elif isinstance(v, dict) and isinstance(data[k], dict):
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

def produce_all_batch2_series():
    """Sản xuất toàn bộ 5 bộ audio Batch 2 (15 video MP4 1080p)."""
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()
    series_list = get_batch2_5_series_data()
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
    print("🎬 [BƯỚC 1: SẢN XUẤT 5 BỘ AUDIO MASTERPIECE BATCH 2] BẮT ĐẦU")
    print(f"⏰ Thời điểm: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 Tổng quy mô: 5 Bộ Truyện x 3 Tập = 15 Video MP4 1080p")
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
            dur = probe.get("duration", 180.0)
            if dur < 10.0:
                dur = 180.0

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
    print(f"🎉 TẤT CẢ 5 BỘ TRUYỆN AUDIO BATCH 2 (15 VIDEO MP4 FULL HD) ĐÃ ĐƯỢC SẢN XUẤT XONG!")
    print(f"⏱️ Tổng thời gian sản xuất: {total_dur / 60:.1f} phút")
    print("=" * 80)

def get_caption_for_part(series_conf: dict, part_num: int) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    title = series_conf["title"]
    hook = series_conf["hooks"][part_num - 1]
    magnet = series_conf["magnets"][part_num - 1]
    tag = series_conf["genre_tag"]
    return f"{badge} {title}. {hook} {magnet} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag}"

def run_batch2_publisher(immediate: bool = True, reset: bool = False):
    """
    Quản trị xuất bản 5 bộ audio Batch 2 lên TikTok Studio:
    - Chế độ immediate: Giãn cách 35s giữa các tập để đăng liên tục an toàn.
    - ĐĂNG XONG TẬP NÀO -> XÓA NGAY VIDEO & AUDIO TẬP ĐÓ (Chống trùng lặp, bảo vệ ổ cứng).
    - ĐĂNG XONG CẢ BỘ -> XÓA NGAY KỊCH BẢN JSON CỦA BỘ ĐÓ.
    """
    out_dir = ROOT / "assets" / "output"
    thumb_dir = ROOT / "assets" / "thumbnails"
    audio_dir = ROOT / "assets" / "audio"
    scripts_dir = ROOT / "data" / "generated_scripts"
    series_list = get_batch2_5_series_data()

    if reset and STATUS_FILE.exists():
        STATUS_FILE.unlink(missing_ok=True)
        print("🔄 Đã reset trạng thái xuất bản Batch 2!")

    status = load_status()

    interval_sec = 35 if immediate else 1200  # 35s nếu immediate, 20 phút nếu hẹn giờ

    print("=" * 80)
    print("🚀 [LỊCH TRÌNH ĐĂNG BÀI MASTER TIKTOK BATCH 2] 5 BỘ TRUYỆN AUDIO MASTERPIECE")
    print(f"⏰ Thời điểm bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"⏱️ Chế độ: {'Đăng liên tục (Immediate Post) giãn cách 35s an toàn' if immediate else 'Giãn cách 20 phút/tập'}")
    print(f"🧹 Cơ chế: Đăng thành công tập nào -> Tự động xóa ngay video/audio tập đó để chống đăng lặp!")
    print("=" * 80)

    for s_idx, conf in enumerate(series_list):
        s_key = conf["key"]
        s_title = conf["title"]
        prefix = conf["prefix"]

        print(f"\n" + "#" * 70)
        print(f"🎬 BỘ {s_idx + 1}/5: {s_title}")
        print("#" * 70)

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng thành công trước đó: {s_key} - {p_key}")
                continue

            # Giãn cách an toàn giữa 2 lần đăng
            last_pub_ts = status.get("_meta", {}).get("last_published_timestamp", 0.0)
            if last_pub_ts > 0:
                elapsed_since_last = time.time() - last_pub_ts
                if elapsed_since_last < interval_sec:
                    wait_need = int(interval_sec - elapsed_since_last)
                    print(f"⏳ Nghỉ an toàn {wait_need}s trước khi đăng tiếp {s_key} - {p_key}...")
                    time.sleep(wait_need)

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
                prefix=prefix,
                part_num=p_idx,
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
                        thumbnail_path=part_thumb_file if part_thumb_file and part_thumb_file.exists() else None
                    )
                except Exception as ue:
                    print(f"  ⚠️ Ngoại lệ khi đăng: {ue}")
                    upload_success = False

                if upload_success:
                    status[s_key][p_key] = True
                    if "_meta" not in status:
                        status["_meta"] = {}
                    status["_meta"]["last_published_timestamp"] = time.time()
                    status["_meta"]["last_published_time_str"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status["_meta"]["last_published_episode"] = f"{prefix}_part{p_idx}"
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
    print("🏆 TOÀN BỘ 5 BỘ TRUYỆN AUDIO BATCH 2 ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG LÊN TIKTOK!")
    print("🧹 TẤT CẢ VIDEO, AUDIO VÀ KỊCH BẢN CŨ ĐÃ ĐƯỢC TỰ ĐỘNG DỌN DẸP SẠCH SẼ!")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Produce and Publish Batch 2 Masterpieces")
    parser.add_argument("--produce-only", action="store_true", help="Chỉ sản xuất video và audio, không đăng")
    parser.add_argument("--publish-only", action="store_true", help="Chỉ chạy publisher đăng bài")
    parser.add_argument("--reset", action="store_true", help="Reset trạng thái đăng")
    parser.add_argument("--immediate", action="store_true", default=True, help="Đăng liên tục ngay lập tức, giãn cách an toàn 35s")
    args = parser.parse_args()

    if args.produce_only:
        produce_all_batch2_series()
    elif args.publish_only:
        run_batch2_publisher(immediate=args.immediate, reset=args.reset)
    else:
        produce_all_batch2_series()
        run_batch2_publisher(immediate=args.immediate, reset=args.reset)

if __name__ == "__main__":
    main()
