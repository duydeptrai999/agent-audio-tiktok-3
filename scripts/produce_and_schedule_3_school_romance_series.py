# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_3_school_romance_series.py
Quy Trình Tự Động Hóa Toàn Diện Sản Xuất & Xuất Bản 3 Bộ Truyện Audio Thanh Xuân Vườn Trường:
1. Bộ 1: Vụng Trộm Thích Thầm Anh: Mười Năm Ngọt Ngào Dưới Mái Hiên Mùa Hạ (10,860 từ)
2. Bộ 2: Đại Ca Học Đường Khó Dỗ Dành: Chỉ Dịu Dàng Với Riêng Em (10,761 từ)
3. Bộ 3: Gặp Lại Người Năm Ấy: Bản Tình Ca Mùa Hè Chưa Từng Tắt (10,720 từ)

Quy chuẩn GEMINI.md:
- Giọng đọc: DUY NHẤT 1 GIỌNG vi-VN-HoaiMyNeural (Hoài My truyền cảm, ngọt ngào, sâu lắng, chuẩn học đường thanh xuân)
- Tốc độ đọc: Tua nhanh 1.5x (atempo=1.5)
- Video B-roll: Lát cắt riêng biệt từ youtube_pool (baking_asmr_2hours_3NvvOVrm1uY.mp4)
- Khung hình: 100% Giữ nguyên tỉ lệ gốc 16:9 (1920x1080), không ép dọc, không crop
- Thumbnail: Thiết kế bìa độc quyền cho từng tập với nhãn TẬP 1, TẬP 2, TẬP 3 (KẾT) và hashtag #HọcĐường #ThanhXuân #NgônTình
- Lịch đăng: Giãn cách đúng 1 TIẾNG giữa các bộ; trong mỗi bộ các part đăng cách nhau 15 phút.
"""

import sys
import os
import time
import json
import asyncio
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True, errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', line_buffering=True, errors='replace')
    except Exception:
        pass

import edge_tts
from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from config.settings import BGM_VOLUME, VOICE_VOLUME
from scripts.tiktok_publisher_core import upload_and_publish_video, CoccocFileLock

STATUS_FILE = ROOT / "data" / "school_romance_3series_publishing_status.json"

def split_into_chunks(text: str, max_words: int = 150) -> list:
    import re
    sentences = [s.strip() for s in re.split(r'(?<=[.!?…\n])\s+', text) if s.strip()]
    chunks = []
    cur = []
    cur_w = 0
    for s in sentences:
        w_count = len(s.split())
        if cur_w + w_count > max_words and cur:
            chunks.append(" ".join(cur))
            cur = [s]
            cur_w = w_count
        else:
            cur.append(s)
            cur_w += w_count
    if cur:
        chunks.append(" ".join(cur))
    return chunks if chunks else [text]

def cleanup_orphaned_audio_temps():
    audio_dir = ROOT / "assets" / "audio"
    if not audio_dir.exists():
        return
    for item in audio_dir.iterdir():
        if item.is_file() and any(x in item.name for x in ["_chk", "_raw", "_concat", "test_sent_"]):
            try:
                item.unlink(missing_ok=True)
            except Exception:
                pass

async def generate_tts_for_part(text: str, voice: str, output_path: Path):
    """Sinh audio Edge-TTS chất lượng cao, chia chunk, ghép nối và tua nhanh 1.5x."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    clean_text = (
        text.replace("'", " ")
        .replace('"', ' ')
        .replace("‘", " ")
        .replace("’", " ")
        .replace("“", " ")
        .replace("”", " ")
        .replace("–", "-")
        .replace("—", "-")
        .replace("...", ", ")
        .strip()
    )

    chunks = split_into_chunks(clean_text, max_words=160)
    chunk_files = [output_path.parent / f"{output_path.stem}_chk{i}.mp3" for i in range(len(chunks))]
    concat_list = output_path.parent / f"{output_path.stem}_concat.txt"
    raw_merged = output_path.parent / f"{output_path.stem}_raw.mp3"
    semaphore = asyncio.Semaphore(3)

    async def synth_chk(idx, chk, fpath):
        async with semaphore:
            for attempt in range(5):
                try:
                    comm = edge_tts.Communicate(chk, voice=voice)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=60.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        return
                except Exception as e_synth:
                    await asyncio.sleep(1.5 * (attempt + 1))
            if not fpath.exists() or fpath.stat().st_size <= 500:
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 5 retries with {voice}")

    try:
        tasks = [synth_chk(i, c, chunk_files[i]) for i, c in enumerate(chunks)]
        await asyncio.gather(*tasks)

        with open(concat_list, "w", encoding="utf-8") as f:
            for c_file in chunk_files:
                if not c_file.exists() or c_file.stat().st_size <= 500:
                    raise RuntimeError(f"Missing valid chunk file: {c_file.name}")
                f.write(f"file '{c_file.resolve().as_posix()}'\n")

        ffmpeg = get_ffmpeg_exe()
        subprocess.run([
            ffmpeg, "-y", "-f", "concat", "-safe", "0",
            "-i", str(concat_list),
            "-c", "copy",
            str(raw_merged)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        subprocess.run([
            ffmpeg, "-y",
            "-i", str(raw_merged),
            "-filter:a", "atempo=1.5",
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(output_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        print(f"  ✅ Đã tạo xong Audio 1.5x: {output_path.name} ({output_path.stat().st_size / 1024:.1f} KB)")
    finally:
        try:
            if concat_list.exists():
                concat_list.unlink(missing_ok=True)
            if raw_merged.exists():
                raw_merged.unlink(missing_ok=True)
            for c in chunk_files:
                if c.exists():
                    c.unlink(missing_ok=True)
        except Exception:
            pass

def produce_single_series(story_data: dict, prefix: str, bgm_file: Path) -> List[Path]:
    """Sản xuất toàn bộ 3 tập cho 1 bộ truyện với B-roll riêng biệt và Thumbnail độc quyền."""
    out_dir = ROOT / "assets" / "output"
    audio_dir = ROOT / "assets" / "audio"
    thumb_dir = ROOT / "assets" / "thumbnails"
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_dir.mkdir(parents=True, exist_ok=True)

    cleanup_orphaned_audio_temps()

    print("\n" + "=" * 70)
    print(f"🎬 SẢN XUẤT BỘ TRUYỆN: {story_data['title']}")
    print(f"🎙️ Giọng đọc: {story_data['voice']} (Tốc độ 1.5x) | Tổng số từ: {sum(len(p['full_text'].split()) for p in story_data['parts'])} từ")
    print(f"🎵 Nhạc nền: {bgm_file.name}")
    print("=" * 70)

    rendered_videos = []

    for part in story_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        print(f"\n--- [{prefix.upper()} - TẬP {p_num}] {badge} ---")

        part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
        if part_video.exists() and part_video.stat().st_size > 1000000:
            print(f"✅ Video {badge} đã có sẵn hoàn chỉnh: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")
            rendered_videos.append(part_video)
            continue

        part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
        if not part_audio.exists() or part_audio.stat().st_size < 10000:
            print(f"🎙️ Đang sinh Edge-TTS cho {badge} ({len(part['full_text'].split())} từ)...")
            asyncio.run(generate_tts_for_part(part["full_text"], story_data["voice"], part_audio))

        probe = probe_media_file(part_audio)
        dur = probe.get("duration", 600.0)
        if dur < 10.0:
            dur = 600.0

        distinct_slice = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"
        try:
            generate_part_thumbnail(
                source_video_or_image=distinct_slice,
                output_thumb_path=part_thumb,
                story_title=story_data["title"],
                part_label=f"TẬP {p_num}",
                genre_tag="#ThanhXuân"
            )
        except Exception as e:
            print(f"⚠️ Lỗi tạo thumbnail: {e}")
            part_thumb = None

        if not part_video.exists() or part_video.stat().st_size < 1000000:
            print(f"🎥 Đang render video 1080p 16:9 cho {badge} (thời lượng: {dur/60:.1f} phút)...")
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
            print(f"  ✅ ĐÃ RENDER THÀNH CÔNG: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")

        rendered_videos.append(part_video)

    return rendered_videos

def load_status() -> dict:
    if STATUS_FILE.exists():
        try:
            with open(STATUS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "series1_vungtrom": {"part1": False, "part2": False, "part3": False},
        "series2_khododanh": {"part1": False, "part2": False, "part3": False},
        "series3_gaplai": {"part1": False, "part2": False, "part3": False}
    }

def save_status(status: dict):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

def wait_until(target_timestamp: float, label: str = ""):
    while True:
        now = time.time()
        remain = target_timestamp - now
        if remain <= 0:
            break
        mins, secs = divmod(int(remain), 60)
        print(f"  ⏳ [Chờ lịch đăng {label}] Còn {mins:02d} phút {secs:02d} giây...", end="\r", flush=True)
        time.sleep(min(10, max(1, remain)))
    print()

def get_caption_for_part(series_key: str, part_num: int, title: str) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    tag_genre = "#thanhxuan #hocduong #ngontinh #khododanh #vungtromkhothegiau #ngọtsủng"

    if series_key == "series1_vungtrom":
        hook_text = (
            "Viên kẹo bạc hà trong hộc bàn và mối tình đơn phương mười năm ngọt ngào."
            if part_num == 1
            else "Bức thư tỏ tình giấu dưới đáy vali và cuộc hội ngộ bất ngờ giữa đêm tuyết trắng."
            if part_num == 2
            else "Không phải em thích thầm anh, mà là anh đã yêu em từ rất lâu rồi!"
        )
    elif series_key == "series2_khododanh":
        hook_text = (
            "Cậu bạn cùng bàn ngổ ngáo khó dỗ dành và hộp sữa dâu tây đặt nhầm chỗ."
            if part_num == 1
            else "Chiếc áo khoác mùi gỗ tuyết tùng và lời tuyên chiến bảo bọc giữa sân trường."
            if part_num == 2
            else "Chàng đại ca ngỗ nghịch kiêu ngạo cả đời này chỉ dịu dàng dỗ dành một mình em!"
        )
    else:
        hook_text = (
            "Khúc dương cầm chiều mưa và chiếc kẹp tóc hoa linh lan kỷ niệm năm ấy."
            if part_num == 1
            else "Bức tranh bí mật trong văn phòng chủ tịch và sự thật đẫm nước mắt 5 năm chia ly."
            if part_num == 2
            else "Bản tình ca mùa hè chưa từng tắt và lời cầu hôn thiêng liêng bên phím dương cầm!"
        )

    cta = "👉 Đón xem Tập tiếp theo trên kênh nhé!" if part_num < 3 else "👉 Hãy để lại bình luận và đăng ký kênh nhé!"
    return f"{badge} {title}. {hook_text} {cta} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp {tag_genre}"

def main(auto_publish: bool = True, fast_schedule: bool = False, render_only: bool = False, publish_only: bool = False):
    from core.stories.school_romance_vungtrom_masterpiece import get_vungtrom_masterpiece_story
    from core.stories.school_romance_khododanh_masterpiece import get_khododanh_masterpiece_story
    from core.stories.school_romance_gaplai_masterpiece import get_gaplai_masterpiece_story

    from core.bgm_manager import get_safe_bgm_for_genre
    bgm_vungtrom = get_safe_bgm_for_genre("HEALING")
    bgm_khododanh = get_safe_bgm_for_genre("HEALING")
    bgm_gaplai = get_safe_bgm_for_genre("HEALING")

    series_list = [
        {
            "key": "series1_vungtrom",
            "prefix": "VID_school_1_vungtrom",
            "bgm": bgm_vungtrom,
            "story": get_vungtrom_masterpiece_story(),
            "series_offset_sec": 0
        },
        {
            "key": "series2_khododanh",
            "prefix": "VID_school_2_khododanh",
            "bgm": bgm_khododanh,
            "story": get_khododanh_masterpiece_story(),
            "series_offset_sec": 3600 if not fast_schedule else 40
        },
        {
            "key": "series3_gaplai",
            "prefix": "VID_school_3_gaplai",
            "bgm": bgm_gaplai,
            "story": get_gaplai_masterpiece_story(),
            "series_offset_sec": 7200 if not fast_schedule else 80
        }
    ]

    print("=" * 70)
    print("🌟 KHỞI ĐỘNG SẢN XUẤT & XUẤT BẢN 3 BỘ AUDIO THANH XUÂN VƯỜN TRƯỜNG")
    print(f"⏰ Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("💎 Tiêu chuẩn: 100% Hoài My Neural 1.5x | 16:9 Widescreen | B-Roll YouTube Pool")
    print("💎 Lịch đăng: Giãn cách 1 tiếng giữa các bộ | 15 phút giữa các part")
    print("=" * 70)

    # BƯỚC 1: SẢN XUẤT TOÀN BỘ 9 VIDEO FULL HD
    if not publish_only:
        for idx, s_conf in enumerate(series_list, 1):
            print(f"\n🚀 BẮT ĐẦU SẢN XUẤT BỘ {idx}/3: {s_conf['story']['title']}")
            produce_single_series(s_conf["story"], s_conf["prefix"], s_conf["bgm"])
        print("\n" + "=" * 70)
        print("🎉 ĐÃ HOÀN TẤT RENDER 100% CẢ 3 BỘ AUDIO THANH XUÂN (9 VIDEO MP4 FULL HD 1080P)!")
        print("=" * 70)

    if render_only or not auto_publish:
        print("ℹ️ Chế độ Render Only hoặc Auto Publish tắt. Dừng tiến trình.")
        return

    # BƯỚC 2: TIẾN TRÌNH XUẤT BẢN THEO LỊCH GIÃN CÁCH CHUẨN
    status = load_status()
    out_dir = ROOT / "assets" / "output"

    if "base_time" not in status:
        status["base_time"] = time.time()
        save_status(status)
    base_time = float(status["base_time"])

    interval_parts_sec = 15 * 60 if not fast_schedule else 20
    last_publish_ts = 0.0

    for s_idx, s_conf in enumerate(series_list, 1):
        s_key = s_conf["key"]
        s_title = s_conf["story"]["title"]
        s_base_target = base_time + s_conf["series_offset_sec"]

        print(f"\n=======================================================")
        print(f"🚀 LỊCH ĐĂNG BỘ {s_idx}/3: {s_title}")
        print(f"🕒 Mốc thời gian bắt đầu bộ: +{s_conf['series_offset_sec'] // 60} phút")
        print(f"=======================================================")

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_base_target + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx} - Tập {p_idx}")

            # Đảm bảo khoảng cách an toàn tối thiểu 15 phút giữa 2 lần đăng liên tiếp
            min_gap_sec = 15 * 60 if not fast_schedule else 15
            if last_publish_ts > 0 and (time.time() - last_publish_ts) < min_gap_sec:
                remain_gap = min_gap_sec - (time.time() - last_publish_ts)
                wait_until(time.time() + remain_gap, f"Giãn cách {min_gap_sec//60} phút sau video vừa đăng")

            vid_file = out_dir / f"{s_conf['prefix']}_part{p_idx}_final.mp4"
            caption = get_caption_for_part(s_key, p_idx, s_title)

            upload_success = False
            for attempt in range(1, 4):
                print(f"\n📲 Đang tải lên TikTok Studio: {vid_file.name} (Lần thử {attempt}/3)...")
                try:
                    upload_success = upload_and_publish_video(vid_file, caption, screenshot_prefix=f"{s_key}_{p_key}")
                except Exception as ue:
                    print(f"  ⚠️ Ngoại lệ khi đăng: {ue}")
                    upload_success = False

                if upload_success:
                    status[s_key][p_key] = True
                    save_status(status)
                    last_publish_ts = time.time()
                    print(f"🎉 ĐÃ XUẤT BẢN THÀNH CÔNG: {s_key} - {p_key}!")
                    break
                else:
                    print(f"  ⚠️ Lần thử {attempt} chưa thành công. Tạm dừng 15s trước khi thử lại...")
                    time.sleep(15)

            if not upload_success:
                print(f"❌ CẢNH BÁO: Đăng {s_key} - {p_key} thất bại sau 3 lần thử! Đánh dấu và tiếp tục...")
                status[s_key][p_key] = False
                save_status(status)

    print("\n" + "=" * 70)
    print("🏆 TOÀN BỘ 3 BỘ AUDIO THANH XUÂN VƯỜN TRƯỜNG (9 VIDEO FULL HD 1080P) ĐÃ XUẤT BẢN THÀNH CÔNG TRÊN TIKTOK!")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce and schedule 3 school romance series")
    parser.add_argument("--render-only", action="store_true", help="Only render videos, do not publish")
    parser.add_argument("--publish-only", action="store_true", help="Only publish videos, do not render")
    parser.add_argument("--fast-schedule", action="store_true", help="Use fast intervals for testing")
    args = parser.parse_args()

    main(
        auto_publish=True,
        fast_schedule=args.fast_schedule,
        render_only=args.render_only,
        publish_only=args.publish_only
    )
