# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_4_romance_series.py
Quy Trình Tự Động Hóa Toàn Diện Sản Xuất & Xuất Bản 4 Bộ Truyện Audio Ngôn Tình (12 Video):
1. Bộ 1: Bản Hợp Đồng Hôn Nhân 100 Tỷ: Vị Hôn Thê Giả Mạo Của Tổng Tài Tàn Tật (11,142 từ)
2. Bộ 2: Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp (10,517 từ)
3. Bộ 3: Khi Hoa Sơn Tra Tàn Lụi: Nỗi Oan Khuất 7 Năm Của Cô Dâu Thế Thân (10,964 từ)
4. Bộ 4: Ánh Sáng Nơi Tận Cùng Đêm Tối: Bản Hợp Đồng Cứu Rỗi Trái Tim Tổn Thương (10,916 từ)

Quy chuẩn GEMINI.md:
- Giọng đọc: DUY NHẤT 1 GIỌNG vi-VN-HoaiMyNeural (Hoài My truyền cảm, 100% Single Voice)
- Tốc độ đọc: Tua nhanh 1.5x (atempo=1.5)
- Video B-roll: Lát cắt riêng biệt từ youtube_pool (baking_asmr_2hours_3NvvOVrm1uY.mp4)
- Khung hình: 100% Giữ nguyên tỉ lệ gốc 16:9 (1920x1080), không ép dọc, không crop
- Thumbnail: Thiết kế bìa độc quyền cho từng tập với Part badge và Story title
- Lịch đăng: Giãn cách 1 tiếng giữa các bộ, rải đều 3 part trong mỗi tiếng, kèm Hashtags #audio #xuhuong #ngontinh...
"""

import sys
import os
import time
import json
import asyncio
import subprocess
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

import edge_tts
from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from config.settings import BGM_VOLUME, VOICE_VOLUME
from scripts.tiktok_publisher_core import upload_and_publish_video, CoccocFileLock

STATUS_FILE = ROOT / "data" / "romance_4series_publishing_status.json"

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
    print("=" * 70)

    rendered_videos = []

    for part in story_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        print(f"\n--- [{prefix.upper()} - TẬP {p_num}] {badge} ---")

        # 1. Sinh Audio TTS 1.5x
        part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
        if not part_audio.exists() or part_audio.stat().st_size < 10000:
            print(f"🎙️ Đang sinh Edge-TTS cho {badge} ({len(part['full_text'].split())} từ)...")
            asyncio.run(generate_tts_for_part(part["full_text"], story_data["voice"], part_audio))
        part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
        if part_video.exists() and part_video.stat().st_size > 1000000:
            print(f"✅ Video {badge} đã có sẵn hoàn chỉnh: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")
            rendered_videos.append(part_video)
            continue

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
                genre_tag=f"#{story_data.get('genre', 'NgônTình')}"
            )
        except Exception as e:
            print(f"⚠️ Lỗi tạo thumbnail: {e}")
            part_thumb = None

        # 4. Sinh Phụ đề Động Kinetic Subtitles chuẩn TikTok High-CTR
        sub_dir = ROOT / "assets" / "subtitles"
        sub_dir.mkdir(parents=True, exist_ok=True)
        part_srt = sub_dir / f"{prefix}_part{p_num}.srt"
        try:
            from core.subtitle_engine import generate_srt_from_text_and_duration
            dur_probe = probe_media_file(part_audio).get("duration", 600.0)
            if not part_srt.exists() or part_srt.stat().st_size < 10:
                print(f"📝 Đang tạo phụ đề động chuẩn TikTok High-CTR cho {badge}...")
                generate_srt_from_text_and_duration(part["full_text"], dur_probe, part_srt)
        except Exception as e_srt:
            print(f"⚠️ Không thể sinh phụ đề: {e_srt}")

        # 5. Render Video MP4 1080p 16:9
        part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
        if not part_video.exists() or part_video.stat().st_size < 1000000:
            print(f"🎥 Đang render video 1080p 16:9 cho {badge}...")
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
        "series1_haomon": {"part1": False, "part2": False, "part3": False},
        "series2_thanhxuan": {"part1": False, "part2": False, "part3": False},
        "series3_nguoctam": {"part1": False, "part2": False, "part3": False},
        "series4_chualanh": {"part1": False, "part2": False, "part3": False}
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
    
    if "haomon" in series_key:
        tag_genre = "#haomon #tongtai #cuoituocyeusau #audiotruyen #reviewtruyen"
        hook_text = (
            "Hợp đồng hôn nhân 100 tỷ và đêm tân hôn giông bão."
            if part_num == 1
            else "Bí mật người đàn ông đứng dậy trong đêm tối."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Tình yêu đích thực chiến thắng mọi toan tính hào môn!"
        )
        magnet_q = (
            "👉 Nếu được trả 100 tỷ để kết hôn hợp đồng, bạn có đồng ý không? Bình luận 1 (Có) hoặc 2 (Không) nhé!"
            if part_num == 1
            else "👉 Theo bạn anh ấy giả vờ tàn tật để làm gì? Bình luận 1 (Bảo vệ bản thân) hay 2 (Bắt kẻ phản bội)!"
            if part_num == 2
            else "👉 Bạn có tin vào tình yêu chân thành chốn hào môn không? Để lại quan điểm dưới bình luận nhé!"
        )
    elif "thanhxuan" in series_key:
        tag_genre = "#thanhxuan #moitinhdau #tuoitre #hocduong #audiotruyen"
        hook_text = (
            "Lời hứa 10 năm dưới cơn mưa tốt nghiệp năm mười bảy tuổi."
            if part_num == 1
            else "Mảnh giấy chuyển tiền chu cấp bí mật suốt 10 năm."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Mối tình thanh xuân trọn vẹn nhất cuộc đời!"
        )
        magnet_q = (
            "👉 Bạn còn nhớ tên mối tình đầu năm 17 tuổi không? Bình luận 1 (Còn nhớ) hoặc 2 (Đã quên) nhé!"
            if part_num == 1
            else "👉 10 năm âm thầm hy sinh không một lời kể công, người như vậy có thật không? Bình luận 1 hoặc 2 nhé!"
            if part_num == 2
            else "👉 Nếu gặp lại mối tình đầu năm ấy, bạn sẽ nói câu gì đầu tiên? Chia sẻ dưới bình luận nhé!"
        )
    elif "nguoctam" in series_key:
        tag_genre = "#nguoctam #hoatang #nguocluyen #danong #audiotruyen"
        hook_text = (
            "5 năm oan khuất nhận tội thay và thiệp cưới mạ vàng ngày trở về."
            if part_num == 1
            else "Sự thật hồ sơ bệnh án hiến tủy và biển axit trả giá."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Đại kết cục sám hối đẫm nước mắt!"
        )
        magnet_q = (
            "👉 Đổi 5 năm thanh xuân đi tù thay người yêu, đáng hay ngu ngốc? Bình luận 1 (Đáng) hoặc 2 (Ngu ngốc) nhé!"
            if part_num == 1
            else "👉 Khi biết sự thật hiến tủy, bạn có tha thứ không? Bình luận 1 (Tha thứ) hay 2 (Không bao giờ)!"
            if part_num == 2
            else "👉 Sự sám hối muộn màng có bù đắp được 5 năm cay đắng? Để lại bình luận cho mình biết nhé!"
        )
    else:
        tag_genre = "#chualanh #tinhcam #tamly #healing #langnghe #audiotruyen"
        hook_text = (
            "Bản hợp đồng trị liệu tâm lý 100 ngày bên hồ sương mù."
            if part_num == 1
            else "Tiếng súng trong đêm bão tuyết và sự trỗi dậy của thiên tài."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Ánh sáng dịu dàng xua tan bóng tối tâm hồn!"
        )
        magnet_q = (
            "👉 Bạn có tin mỗi người đều có một 'bác sĩ tâm hồn' của riêng mình? Bình luận 1 (Có) hoặc 2 (Không) nhé!"
            if part_num == 1
            else "👉 Khi bị tổn thương, bạn chọn một mình chịu đựng hay chia sẻ? Bình luận 1 hoặc 2 nhé!"
            if part_num == 2
            else "👉 Câu chuyện này có chữa lành tâm trạng hôm nay của bạn không? Hãy để lại cảm nghĩ nhé!"
        )

    return f"{badge} {title}. {hook_text} {magnet_q} #audio #xuhuong #ngontinh #audiotruyen #kểchuyện #podcast #fyp #tamtrang {tag_genre}"

# ==============================================================================
# 3. TIẾN TRÌNH THỰC THI CHÍNH
# ==============================================================================

def main(auto_publish: bool = True, dynamic_schedule: bool = True):
    from core.stories.romance_haomon_masterpiece import get_haomon_masterpiece_story
    from core.stories.romance_school import get_30min_school_romance_story
    from core.stories.romance_nguoctam_masterpiece import get_nguoctam_masterpiece_story
    from core.stories.romance_chualanh_masterpiece import get_chualanh_masterpiece_story

    from core.bgm_manager import get_safe_bgm_for_genre
    bgm_romance = get_safe_bgm_for_genre("HEALING")

    all_series_configs = [
        {
            "key": "series1_haomon",
            "prefix": "VID_romance_1_haomon",
            "story": get_haomon_masterpiece_story()
        },
        {
            "key": "series2_thanhxuan",
            "prefix": "VID_romance_2_thanhxuan",
            "story": get_30min_school_romance_story()
        },
        {
            "key": "series3_nguoctam",
            "prefix": "VID_romance_3_nguoctam",
            "story": get_nguoctam_masterpiece_story()
        },
        {
            "key": "series4_chualanh",
            "prefix": "VID_romance_4_chualanh",
            "story": get_chualanh_masterpiece_story()
        }
    ]

    print("=" * 70)
    print("🌟 KHỞI ĐỘNG XƯỞNG SẢN XUẤT & XUẤT BẢN 4 BỘ TRUYỆN AUDIO NGÔN TÌNH")
    print(f"⏰ Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("💎 Tiêu chuẩn: 100% Hoài My Neural 1.5x | 16:9 Widescreen | B-Roll YouTube Pool")
    print("=" * 70)

    # BƯỚC 1: SẢN XUẤT TRỌN VẸN CẢ 4 BỘ (12 VIDEO FULL HD)
    for conf in all_series_configs:
        produce_single_series(conf["story"], conf["prefix"], bgm_romance)

    print("\n" + "=" * 70)
    print("🎉 ĐÃ HOÀN TẤT RENDER 100% CẢ 4 BỘ TRUYỆN AUDIO NGÔN TÌNH (12 VIDEO MP4 FULL HD 1080P)!")
    print("=" * 70)

    if not auto_publish:
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
    interval_parts_sec = 15 * 60 if not dynamic_schedule else 15
    interval_series_sec = 60 * 60 if not dynamic_schedule else 60

    for s_idx, conf in enumerate(all_series_configs):
        s_key = conf["key"]
        s_title = conf["story"]["title"]
        s_start_time = base_time + s_idx * interval_series_sec

        print(f"\n=======================================================")
        print(f"🚀 LỊCH ĐĂNG BỘ {s_idx + 1}/4: {s_title}")
        print(f"=======================================================")

        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_start_time + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx + 1} - Tập {p_idx}")

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
    print("🏆 TOÀN BỘ 4 BỘ AUDIO NGÔN TÌNH (12 VIDEO FULL HD) ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 70)

if __name__ == "__main__":
    main(auto_publish=True, dynamic_schedule=False)
