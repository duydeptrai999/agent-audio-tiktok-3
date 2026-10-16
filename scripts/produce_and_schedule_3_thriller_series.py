# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_3_thriller_series.py
Quy Trình Tự Động Hóa Sản Xuất & Xuất Bản 3 Bộ Truyện Audio Trinh Thám / Kinh Dị / Truyện Ma (9 Video):
1. Bộ 1 (Trinh Thám / Kỳ Án Đấu Trí): Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất (10,762 từ)
2. Bộ 2 (Kinh Dị Rùng Rợn / Căn Phòng Số 44): Quỷ Khế Giao Ước: Căn Nhà Số 44 Và Chiếc Gương Âm Hồn Không Có Đáy (10,768 từ)
3. Bộ 3 (Truyện Ma Ban Đêm / Gầm Giường): Tiếng Cào Cửa Lúc 2 Giờ Sáng: Bí Ẩn Hũ Tro Cốt Dưới Gầm Giường (10,634 từ)

Quy chuẩn GEMINI.md:
- Giọng đọc: DUY NHẤT 1 GIỌNG vi-VN-NamMinhNeural (Nam trầm ấm, uy quyền, chuẩn trinh thám/kinh dị, 100% Single Voice)
- Tốc độ đọc: Tua nhanh 1.5x (atempo=1.5)
- Video B-roll: Lát cắt riêng biệt từ youtube_pool
- Khung hình: 100% Giữ nguyên tỉ lệ gốc 16:9 (1920x1080), không ép dọc, không crop
- Thumbnail: Thiết kế bìa độc quyền cho từng tập với nhãn TẬP 1, TẬP 2, TẬP 3 / KẾT và hashtag thể loại
- Lịch đăng: Giãn cách 1 tiếng giữa các bộ (60 phút), rải đều 3 part trong mỗi tiếng (cách nhau 15 phút)
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

STATUS_FILE = ROOT / "data" / "thriller_3series_publishing_status.json"

# ==============================================================================
# 1. HÀM SINH AUDIO VÀ RENDER VIDEO CHUẨN GEMINI.MD
# ==============================================================================

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
        genre_tag = "#TrinhThám" if "TRINH" in story_data.get("genre", "") else ("#KinhDị" if "KINH" in story_data.get("genre", "") else "#TruyệnMa")
        try:
            generate_part_thumbnail(
                source_video_or_image=distinct_slice,
                output_thumb_path=part_thumb,
                story_title=story_data["title"],
                part_label=f"TẬP {p_num}",
                genre_tag=genre_tag
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

# ==============================================================================
# 2. QUẢN LÝ TRẠNG THÁI & LỊCH XUẤT BẢN MASTER
# ==============================================================================

def load_status() -> dict:
    default_status = {
        "series1_phapan": {"part1": False, "part2": False, "part3": False},
        "series2_guongquy": {"part1": False, "part2": False, "part3": False},
        "series3_trocot": {"part1": False, "part2": False, "part3": False}
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
    
    if "phapan" in series_key:
        tag_genre = "#trinhtham #phapan #vuan #kyan #hinhsu"
        hook_text = "Cuộc gọi tử thần lúc 2h sáng từ người đồng đội đã mất 5 năm trước." if part_num == 1 else "Đột phá hầm ngầm Ba Vì và giải mã vali danh sách rửa tiền nghìn tỷ." if part_num == 2 else "Trọn bộ 3 tập đã lên sóng! Bạn nghĩ gì về sự trả giá của kẻ phản bội?"
    elif "guongquy" in series_key:
        tag_genre = "#kinhdi #truyenma #tamlinh #quykhe #guongquy"
        hook_text = "Chiếc gương cổ tự động tuột lụa đỏ lúc 2h sáng và bóng ma cào kính rợn tóc gáy." if part_num == 1 else "Bóng ma bẻ ngược khớp bò trên trần nhà và sự thật quỷ khế 7 mạng người." if part_num == 2 else "Trọn bộ 3 tập đã lên sóng! Bạn nghĩ ma quỷ hay lòng tham con người đáng sợ hơn?"
    else:
        tag_genre = "#truyenma #kinhdi #tamlinh #trocot #kethuac"
        hook_text = "Tiếng cào cửa lúc 2h15 sáng và dấu chân bùn đen dẫn vào gầm giường." if part_num == 1 else "Oan hồn cô gái áo trắng 3 năm trước và đạo bùa Kumanthong giam giữ tro cốt." if part_num == 2 else "Trọn bộ 3 tập đã lên sóng! Bạn có tin vào luật nhân quả báo ứng ở đời không?"

    cta = "👉 Đón xem Tập tiếp theo trên kênh!" if part_num < 3 else "👉 Hãy để lại bình luận và đăng ký kênh nhé!"
    return f"{badge} {title}. {hook_text} {cta} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #banđêm {tag_genre}"

# ==============================================================================
# 3. TIẾN TRÌNH THỰC THI CHÍNH
# ==============================================================================

def main(auto_publish: bool = True, fast_schedule: bool = False, render_only: bool = False, publish_only: bool = False):
    from core.stories.detective_masterpiece import get_detective_masterpiece_story
    from core.stories.horror_guongquy_masterpiece import get_horror_guongquy_masterpiece_story
    from core.stories.horror_trocot_masterpiece import get_horror_trocot_masterpiece_story

    from core.bgm_manager import ensure_safe_bgm
    bgm_detective = Path(ensure_safe_bgm(str(ROOT / "assets" / "bgm" / "suspense" / "moonlight_suspense.mp3"), "HUYEN_NGHI"))
    bgm_horror1 = Path(ensure_safe_bgm(str(ROOT / "assets" / "bgm" / "horror_mystery" / "the_house_of_leaves.mp3"), "KINH_DI"))
    bgm_horror2 = Path(ensure_safe_bgm(str(ROOT / "assets" / "bgm" / "suspense" / "tiktok_horror_suspense.mp3"), "KINH_DI"))

    all_series_configs = [
        {
            "key": "series1_phapan",
            "prefix": "VID_thriller_1_phapan",
            "bgm": bgm_detective,
            "story": get_detective_masterpiece_story()
        },
        {
            "key": "series2_guongquy",
            "prefix": "VID_horror_2_guongquy",
            "bgm": bgm_horror1,
            "story": get_horror_guongquy_masterpiece_story()
        },
        {
            "key": "series3_trocot",
            "prefix": "VID_horror_3_trocot",
            "bgm": bgm_horror2,
            "story": get_horror_trocot_masterpiece_story()
        }
    ]

    print("=" * 70)
    print("🌟 KHỞI ĐỘNG XƯỞNG SẢN XUẤT & XUẤT BẢN 3 BỘ AUDIO TRINH THÁM / KINH DỊ / TRUYỆN MA")
    print(f"⏰ Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("💎 Tiêu chuẩn: 100% Nam Minh Neural 1.5x | 16:9 Widescreen | B-Roll YouTube Pool")
    print("=" * 70)

    # BƯỚC 1: SẢN XUẤT TRỌN VẸN CẢ 3 BỘ (9 VIDEO FULL HD)
    if not publish_only:
        for conf in all_series_configs:
            produce_single_series(conf["story"], conf["prefix"], conf["bgm"])

        print("\n" + "=" * 70)
        print("🎉 ĐÃ HOÀN TẤT RENDER 100% CẢ 3 BỘ TRUYỆN AUDIO TRINH THÁM / KINH DỊ (9 VIDEO MP4 FULL HD 1080P)!")
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

    # Khoảng cách giữa các bộ: 60 phút (1 tiếng)
    # Rải đều 3 part trong mỗi tiếng: Part 1 (T), Part 2 (T+15m), Part 3 (T+30m)
    interval_parts_sec = 15 * 60 if not fast_schedule else 20
    interval_series_sec = 60 * 60 if not fast_schedule else 60
    last_publish_ts = 0.0

    for s_idx, conf in enumerate(all_series_configs):
        s_key = conf["key"]
        s_title = conf["story"]["title"]
        s_start_time = base_time + s_idx * interval_series_sec

        print(f"\n=======================================================")
        print(f"🚀 LỊCH ĐĂNG BỘ {s_idx + 1}/3: {s_title}")
        print(f"=======================================================")

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_start_time + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx + 1} - Tập {p_idx}")

            # Đảm bảo khoảng cách an toàn tối thiểu giữa 2 lần đăng liên tiếp
            min_gap_sec = 15 * 60 if not fast_schedule else 15
            if last_publish_ts > 0 and (time.time() - last_publish_ts) < min_gap_sec:
                remain_gap = min_gap_sec - (time.time() - last_publish_ts)
                wait_until(time.time() + remain_gap, f"Giãn cách {min_gap_sec//60} phút sau video vừa đăng")

            vid_file = out_dir / f"{conf['prefix']}_part{p_idx}_final.mp4"
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

        print(f"🎉 HOÀN TẤT ĐĂNG ĐỦ 3 TẬP CỦA BỘ {s_idx + 1}!")

    print("\n" + "=" * 70)
    print("🏆 TOÀN BỘ 3 BỘ AUDIO TRINH THÁM / KINH DỊ / TRUYỆN MA (9 VIDEO FULL HD) ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce and schedule 3 thriller audio series")
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
