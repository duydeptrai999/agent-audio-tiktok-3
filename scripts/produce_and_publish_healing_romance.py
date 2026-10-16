# -*- coding: utf-8 -*-
"""
scripts/produce_and_publish_healing_romance.py
Quy Trình Tự Động Hóa Sản Xuất & Xuất Bản Bộ Audio Ngôn Tình Chữa Lành:
"Ánh Sáng Nơi Tận Cùng Đêm Tối: 100 Ngày Cứu Rỗi Trái Tim Họa Sĩ" (3 Tập Video MP4)

Tích hợp toàn diện các chuẩn tối ưu triệu view:
- Động cơ Phụ đề Động Kinetic Subtitles High-CTR (chữ vàng viền đen 28pt)
- Chiến thuật Nam Châm Bình Luận (Comment Magnet) ở cuối mỗi tập và caption
- Nhạc nền an toàn bản quyền 100% (Anti-Copyright BGM Guard + Ducking -24dB)
- Lát cắt B-Roll riêng biệt từ background pool & Thumbnail bìa độc quyền cho từng tập
- Đăng tải tự động an toàn qua Cốc Cốc Browser Profile vào TikTok Studio
"""

import sys
import os
import time
import json
import asyncio
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
        sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)
    except Exception:
        pass

import edge_tts
from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from core.subtitle_engine import generate_srt_from_text_and_duration
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME, ENABLE_SUBTITLES
from scripts.tiktok_publisher_core import upload_and_publish_video, CoccocFileLock
from core.stories.romance_chualanh_tuyetpham import get_romance_chualanh_tuyetpham_story

STATUS_FILE = ROOT / "data" / "healing_romance_publishing_status.json"

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

    rate_val = "+20%"
    pitch_val = "+1Hz"

    async def synth_chk(idx, chk, fpath):
        async with semaphore:
            for attempt in range(5):
                try:
                    comm = edge_tts.Communicate(chk, voice=voice, rate=rate_val, pitch=pitch_val)
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
            "-filter:a", "atempo=1.25",
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(output_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        print(f"  ✅ Đã tạo xong Audio 1.5x Studio: {output_path.name} ({output_path.stat().st_size / 1024:.1f} KB)")
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

def load_status() -> dict:
    default_status = {
        "part1": False,
        "part2": False,
        "part3": False
    }
    if STATUS_FILE.exists():
        try:
            return json.loads(STATUS_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return default_status

def save_status(status: dict):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def get_caption_for_part(part_num: int, title: str) -> str:
    badge = f"[TẬP {part_num}]" if part_num < 3 else "[TẬP 3 - KẾT]"
    tag_genre = "#ngontinh #chualanh #songhuongcuuroi #ngotsung #cotruchanh #lamanha #audiotruyen #reviewtruyen"
    
    if part_num == 1:
        hook_text = "Cánh cửa gỗ sồi giam cầm 5 năm bị phá tung trong đêm bão và hơi ấm cứu rỗi chàng họa sĩ thiên tài."
        magnet_q = "👉 Nếu người bạn yêu thương tự nhốt mình trong bóng tối, bạn có đủ kiên nhẫn ở bên cạnh chữa lành không? Bình luận 1 (Có, kiên nhẫn đến cùng) hay 2 (Sợ bị tổn thương lây) nhé!"
    elif part_num == 2:
        hook_text = "Chàng họa sĩ sợ lửa lao mình qua đám cháy bảo vệ người thương và bức tranh bình minh đầu tiên sau 5 năm."
        magnet_q = "👉 Bạn nghĩ sự dũng cảm của người đàn ông thể hiện rõ nhất khi nào: 1 (Khi kiếm được nhiều tiền) hay 2 (Khi sẵn sàng xả thân che chở người mình yêu)? Bình luận 1 hoặc 2 nhé!"
    else:
        hook_text = "Trọn bộ 3 tập đã lên sóng! Màn vạch trần kẻ ác chấn động truyền hình và lời cầu hôn bên cánh đồng hướng dương ngập nắng."
        magnet_q = "👉 Cái kết ngọt ngào này có làm bạn rung động không? Chấm điểm cho tình yêu của Trực Hành và An Hạ từ 1 đến 10 dưới bình luận nhé!"

    return f"{badge} {title}. {hook_text} {magnet_q} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp {tag_genre}"

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Sản xuất và đăng tải bộ truyện ngôn tình chữa lành tuyệt phẩm")
    parser.add_argument("--fast-schedule", action="store_true", default=True, help="Đăng tải ngay với giãn cách an toàn 20s")
    parser.add_argument("--render-only", action="store_true", help="Chỉ render video không đăng")
    parser.add_argument("--publish-only", action="store_true", help="Chỉ đăng video đã render")
    args = parser.parse_args()

    story = get_romance_chualanh_tuyetpham_story()
    bgm_file = get_safe_bgm_for_genre("HEALING")
    prefix = "VID_romance_chualanh"

    out_dir = ROOT / "assets" / "output"
    audio_dir = ROOT / "assets" / "audio"
    thumb_dir = ROOT / "assets" / "thumbnails"
    sub_dir = ROOT / "assets" / "subtitles"
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_dir.mkdir(parents=True, exist_ok=True)
    sub_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 75)
    print("🌟 SẢN XUẤT & XUẤT BẢN BỘ TRUYỆN NGÔN TÌNH CHỮA LÀNH TUYỆT PHẨM")
    print(f"📖 Tác phẩm: {story['title']}")
    print(f"🎙️ Giọng đọc: {story['voice']} (Tốc độ 1.5x)")
    print(f"🎵 Nhạc nền an toàn: {bgm_file.name}")
    print(f"⏰ Bắt đầu lúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    status = load_status()

    # 1. QUY TRÌNH RENDER TỪNG TẬP
    if not args.publish_only:
        for part in story["parts"]:
            p_num = part["part_number"]
            badge = part["badge_label"]
            print(f"\n--- [TẬP {p_num}] {badge} ---")

            part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
            part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
            part_srt = sub_dir / f"{prefix}_part{p_num}.srt"

            # 1.1 Audio Edge-TTS 1.5x
            if not part_audio.exists() or part_audio.stat().st_size < 10000:
                print(f"🎙️ Đang sinh Edge-TTS Studio cho Tập {p_num} ({len(part['full_text'].split())} từ)...")
                asyncio.run(generate_tts_for_part(part["full_text"], story["voice"], part_audio))
            else:
                print(f"🎙️ Audio Tập {p_num} đã có sẵn: {part_audio.name}")

            probe = probe_media_file(part_audio)
            dur = probe.get("duration", 600.0)
            if dur < 10.0:
                dur = 600.0

            # 1.2 Phụ đề động Kinetic Subtitles
            if not part_srt.exists() or part_srt.stat().st_size < 10:
                print(f"📝 Đang tạo phụ đề động chuẩn TikTok High-CTR cho Tập {p_num}...")
                try:
                    generate_srt_from_text_and_duration(part["full_text"], dur, part_srt)
                except Exception as e_srt:
                    print(f"⚠️ Lỗi sinh phụ đề: {e_srt}")

            # 1.3 Lát cắt B-roll video riêng biệt
            distinct_slice = background_manager.get_distinct_slice_for_part(
                series_id=prefix,
                part_number=p_num,
                duration_seconds=dur
            )

            # 1.4 Thumbnail bìa độc quyền
            part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"
            try:
                generate_part_thumbnail(
                    source_video_or_image=distinct_slice,
                    output_thumb_path=part_thumb,
                    story_title=story["title"],
                    part_label=f"TẬP {p_num}",
                    genre_tag="#ChữaLành"
                )
            except Exception as e:
                print(f"⚠️ Lỗi tạo thumbnail: {e}")
                part_thumb = None

            # 1.5 Render Video 1080p 16:9 hoàn chỉnh
            if not part_video.exists() or part_video.stat().st_size < 1000000:
                print(f"🎥 Đang render video 1080p cho Tập {p_num} (thời lượng: {dur/60:.1f} phút)...")
                render_playable_video(
                    output_file=part_video,
                    voice_audio_path=str(part_audio),
                    clean_footage_path=str(distinct_slice),
                    bgm_audio_path=str(bgm_file),
                    badge_label=badge,
                    bgm_volume=BGM_VOLUME,
                    voice_volume=VOICE_VOLUME,
                    srt_path=str(part_srt) if part_srt.exists() else None,
                    enable_subtitles=True,
                    thumbnail_path=str(part_thumb) if part_thumb and part_thumb.exists() else None
                )
                print(f"  ✅ ĐÃ RENDER THÀNH CÔNG: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")
            else:
                print(f"  ✅ Video Tập {p_num} đã có sẵn hoàn chỉnh: {part_video.name}")

    if args.render_only:
        print("\n🎉 ĐÃ RENDER XONG TOÀN BỘ 3 TẬP! (Chế độ render-only)")
        return

    # 2. ĐĂNG TẢI LÊN TIKTOK STUDIO
    print("\n" + "=" * 75)
    print("📲 BẮT ĐẦU ĐĂNG TẢI 3 TẬP LÊN TIKTOK STUDIO QUA CỐC CỐC BROWSER")
    print("=" * 75)

    last_publish_ts = 0.0
    for p_idx in [1, 2, 3]:
        p_key = f"part{p_idx}"
        if status.get(p_key, False):
            print(f"  ✅ Tập {p_idx} đã được đăng trước đó, bỏ qua.")
            continue

        vid_file = out_dir / f"{prefix}_part{p_idx}_final.mp4"
        if not vid_file.exists():
            print(f"❌ Không tìm thấy file video: {vid_file.name}")
            continue

        # Giãn cách an toàn giữa 2 lần đăng
        gap_sec = 25
        if last_publish_ts > 0 and (time.time() - last_publish_ts) < gap_sec:
            wait_s = gap_sec - (time.time() - last_publish_ts)
            print(f"⏳ Giãn cách an toàn {wait_s:.0f}s...")
            time.sleep(wait_s)

        caption = get_caption_for_part(p_idx, story["title"])
        upload_success = False

        for attempt in range(1, 4):
            print(f"\n📲 Đang tải lên TikTok Studio: Tập {p_idx} ({vid_file.name}) (Lần thử {attempt}/3)...")
            try:
                part_thumb_file = thumb_dir / f"{prefix}_part{p_idx}_thumb.jpg"
                upload_success = upload_and_publish_video(
                    video_path=vid_file,
                    caption=caption,
                    screenshot_prefix=f"romance_chualanh_part{p_idx}",
                    thumbnail_path=part_thumb_file if part_thumb_file.exists() else None
                )
                if upload_success:
                    print(f"  🎉 XUẤT BẢN THÀNH CÔNG Tập {p_idx} lên TikTok Studio!")
                    status[p_key] = True
                    save_status(status)
                    last_publish_ts = time.time()
                    break
                else:
                    print(f"  ⚠️ Lần {attempt} chưa thành công.")
            except Exception as e_up:
                print(f"  ⚠️ Ngoại lệ khi đăng Tập {p_idx} (Lần {attempt}): {e_up}")
            time.sleep(5)

        if not upload_success:
            print(f"❌ Không thể đăng tải Tập {p_idx} sau 3 lần thử! Dừng để kiểm tra.")
            break

    all_done = all(status.get(f"part{i}", False) for i in [1, 2, 3])
    if all_done:
        print("\n" + "=" * 75)
        print("🎉🎉🎉 HOÀN THÀNH XUẤT SẮC TOÀN BỘ BỘ TRUYỆN NGÔN TÌNH CHỮA LÀNH!")
        print("Tất cả 3 tập đã được dựng hoàn chỉnh và đăng tải thành công lên TikTok Studio!")
        print("=" * 75)
    else:
        print("\n⚠️ Một số tập chưa được đăng thành công, vui lòng kiểm tra status file.")

if __name__ == "__main__":
    main()
