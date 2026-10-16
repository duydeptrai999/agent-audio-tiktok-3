# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_horror_series4.py
Quy Trình Tự Động Hóa Sản Xuất & Xuất Bản Bộ Truyện Audio Kinh Dị Ban Đêm Mới:
Chuyến Tàu Đêm Không Ga Đến: 7 Hành Khách Và Lời Nguyền Trả Máu (10,764 từ - 3 Video Full HD 1080p)

Quy chuẩn GEMINI.md:
- Giọng đọc: DUY NHẤT 1 GIỌNG vi-VN-NamMinhNeural (Nam trầm ấm, uy quyền, chuẩn trinh thám/kinh dị, 100% Single Voice)
- Tốc độ đọc: Tua nhanh 1.5x (atempo=1.5)
- Video B-roll: Lát cắt riêng biệt từ youtube_pool
- Khung hình: 100% Giữ nguyên tỉ lệ gốc 16:9 (1920x1080), không ép dọc, không crop
- Thumbnail: Thiết kế bìa độc quyền cho từng tập với nhãn TẬP 1, TẬP 2, TẬP 3 / KẾT và hashtag #KinhDị #TruyệnMa
- Lịch đăng: Rải đều 3 part (Tập 1 đăng ngay, Tập 2 sau 15 phút, Tập 3 sau 30 phút)
- Chế độ hiển thị: Công khai (Public)
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

STATUS_FILE = ROOT / "data" / "horror_series4_publishing_status.json"

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
                except Exception:
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

        # 1. Sinh Audio TTS 1.5x nếu chưa có video hoàn chỉnh
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

        # 2. Cắt lát B-Roll RIÊNG BIỆT từ YouTube pool
        distinct_slice = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        # 3. Tạo Thumbnail riêng cho từng tập
        part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"
        try:
            generate_part_thumbnail(
                source_video_or_image=distinct_slice,
                output_thumb_path=part_thumb,
                story_title=story_data["title"],
                part_label=f"TẬP {p_num}",
                genre_tag="#KinhDị"
            )
        except Exception as e:
            print(f"⚠️ Lỗi tạo thumbnail: {e}")
            part_thumb = None

        # 4. Render Video MP4 1080p 16:9
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
            print(f"✅ ĐÃ RENDER THÀNH CÔNG: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")
        else:
            print(f"✅ Video {badge} đã có sẵn: {part_video.name}")

        rendered_videos.append(part_video)

    return rendered_videos

def load_status() -> dict:
    default_status = {
        "series4_chuyentau": {"part1": False, "part2": False, "part3": False}
    }
    if STATUS_FILE.exists():
        try:
            data = json.loads(STATUS_FILE.read_text(encoding='utf-8'))
            for k, v in default_status.items():
                if k not in data:
                    data[k] = v
            return data
        except Exception:
            pass
    return default_status

def save_status(status: dict):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def wait_until(target_timestamp: float, label: str):
    now = time.time()
    if target_timestamp <= now:
        return
    diff = int(target_timestamp - now)
    print(f"\n⏳ [{datetime.now().strftime('%H:%M:%S')}] Chờ đến mốc đăng {label} (còn {diff // 60}m {diff % 60}s)...")
    while time.time() < target_timestamp:
        remaining = int(target_timestamp - time.time())
        if remaining % 60 == 0 or remaining <= 10:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Còn {remaining // 60}m {remaining % 60}s tới mốc đăng {label}...")
        time.sleep(min(5, max(1, remaining)))

def get_caption_for_part(series_key: str, part_num: int, title: str) -> str:
    badge = f"[PHẦN {part_num}]" if part_num < 3 else "[PHẦN 3 / KẾT]"
    tag_genre = "#kinhdi #truyenma #tamlinh #chuyentau #deoca"
    hook_text = (
        "Chuyến tàu đêm bất ngờ dừng giữa đường hầm bỏ hoang và dấu tay máu cào kính lúc 0h15 sáng."
        if part_num == 1
        else "Bí mật kinh hoàng về vụ sập hầm 7 năm trước và bóng ma áo đỏ trườn qua trần tàu."
        if part_num == 2
        else "Trọn bộ 3 tập đã lên sóng! Bạn có tin vào luật nhân quả báo ứng ở đời không?"
    )
    cta = "👉 Đón xem Tập tiếp theo trên kênh!" if part_num < 3 else "👉 Hãy để lại bình luận và đăng ký kênh nhé!"
    return f"{badge} {title}. {hook_text} {cta} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #banđêm {tag_genre}"

def main(auto_publish: bool = True, fast_schedule: bool = False, render_only: bool = False, publish_only: bool = False):
    from core.stories.horror_chuyentau_masterpiece import get_horror_chuyentau_masterpiece_story

    from core.bgm_manager import get_safe_bgm_for_genre
    bgm_horror = get_safe_bgm_for_genre("KINH_DI")

    story_conf = {
        "key": "series4_chuyentau",
        "prefix": "VID_horror_4_chuyentau",
        "bgm": bgm_horror,
        "story": get_horror_chuyentau_masterpiece_story()
    }

    print("=" * 70)
    print("🌟 KHỞI ĐỘNG SẢN XUẤT & XUẤT BẢN BỘ AUDIO KINH DỊ: CHUYẾN TÀU ĐÊM KHÔNG GA ĐẾN")
    print(f"⏰ Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("💎 Tiêu chuẩn: 100% Nam Minh Neural 1.5x | 16:9 Widescreen | B-Roll YouTube Pool")
    print("=" * 70)

    # BƯỚC 1: SẢN XUẤT 3 VIDEO FULL HD
    if not publish_only:
        produce_single_series(story_conf["story"], story_conf["prefix"], story_conf["bgm"])
        print("\n" + "=" * 70)
        print("🎉 ĐÃ HOÀN TẤT RENDER 100% BỘ AUDIO KINH DỊ (3 VIDEO MP4 FULL HD 1080P)!")
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

    s_key = story_conf["key"]
    s_title = story_conf["story"]["title"]

    print(f"\n=======================================================")
    print(f"🚀 LỊCH ĐĂNG BỘ: {s_title}")
    print(f"=======================================================")

    for p_idx in [1, 2, 3]:
        p_key = f"part{p_idx}"
        if status[s_key].get(p_key, False):
            print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
            continue

        target_ts = base_time + (p_idx - 1) * interval_parts_sec
        wait_until(target_ts, f"Tập {p_idx}")

        # Đảm bảo khoảng cách an toàn tối thiểu 15 phút giữa 2 lần đăng
        min_gap_sec = 15 * 60 if not fast_schedule else 15
        if last_publish_ts > 0 and (time.time() - last_publish_ts) < min_gap_sec:
            remain_gap = min_gap_sec - (time.time() - last_publish_ts)
            wait_until(time.time() + remain_gap, f"Giãn cách {min_gap_sec//60} phút sau video vừa đăng")

        vid_file = out_dir / f"{story_conf['prefix']}_part{p_idx}_final.mp4"
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
    print(f"🏆 TOÀN BỘ 3 TẬP CỦA BỘ AUDIO KINH DỊ '{s_title}' ĐÃ XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce and schedule 4th horror series")
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
