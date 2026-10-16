# -*- coding: utf-8 -*-
"""
scripts/produce_and_schedule_4_masterpieces.py
Quy Trình Tự Động Hóa Sản Xuất & Xuất Bản 4 Bộ Truyện Audio Kiệt Tác (12 Video):
1. Bộ 1: Trọng Sinh Sen Lửa: Thẩm Băng Tuyết Báo Thù Hào Môn (Hoài My Neural 1.5x)
2. Bộ 2: Đêm Mưa Thức Tỉnh: Bản Khế Ước Gia Tộc Đòi Lại 50 Tỷ (Hoài My Neural 1.5x)
3. Bộ 3: Kỳ Án Biệt Thự Trăng Máu: Tiếng Gõ Cửa Lúc 2h Sáng (Nam Minh Neural 1.5x)
4. Bộ 4: Huyết Nguyện Lúc Nửa Đêm: Chiếc Gương Âm Dương Biệt Thự Cổ (Nam Minh Neural 1.5x)

Tích hợp toàn diện các chuẩn tối ưu triệu view:
- Động cơ Phụ đề Động Kinetic Subtitles High-CTR (chữ vàng viền đen 28pt)
- Chiến thuật Nam Châm Bình Luận (Comment Magnet) ở cuối mỗi tập và caption
- Nhạc nền an toàn bản quyền 100% (Anti-Copyright BGM Guard + Ducking -20dB)
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

STATUS_FILE = ROOT / "data" / "masterpiece_4series_publishing_status.json"

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

    rate_val = "+18%" if "NamMinh" in voice else "+20%"
    pitch_val = "-2Hz" if "NamMinh" in voice else "+1Hz"

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

def produce_single_series(story_data: dict, prefix: str, bgm_file: Path) -> List[Path]:
    out_dir = ROOT / "assets" / "output"
    audio_dir = ROOT / "assets" / "audio"
    thumb_dir = ROOT / "assets" / "thumbnails"
    sub_dir = ROOT / "assets" / "subtitles"
    out_dir.mkdir(parents=True, exist_ok=True)
    thumb_dir.mkdir(parents=True, exist_ok=True)
    sub_dir.mkdir(parents=True, exist_ok=True)

    cleanup_orphaned_audio_temps()

    print("\n" + "=" * 70)
    print(f"🎬 SẢN XUẤT BỘ TRUYỆN: {story_data['title']}")
    print(f"🎙️ Giọng đọc: {story_data['voice']} (Tốc độ 1.5x)")
    print(f"🎵 Nhạc nền an toàn: {bgm_file.name}")
    print("=" * 70)

    rendered_videos = []

    for part in story_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        print(f"\n--- [{prefix.upper()} - TẬP {p_num}] {badge} ---")

        part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
        part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
        part_srt = sub_dir / f"{prefix}_part{p_num}.srt"

        # 1. Sinh Audio TTS 1.5x
        if not part_audio.exists() or part_audio.stat().st_size < 10000:
            print(f"🎙️ Đang sinh Edge-TTS Studio cho {badge} ({len(part['full_text'].split())} từ)...")
            asyncio.run(generate_tts_for_part(part["full_text"], story_data["voice"], part_audio))
        else:
            print(f"🎙️ Audio {badge} đã có sẵn: {part_audio.name}")

        probe = probe_media_file(part_audio)
        dur = probe.get("duration", 600.0)
        if dur < 10.0:
            dur = 600.0

        # 2. Sinh Phụ đề Động Kinetic Subtitles High-CTR
        if not part_srt.exists() or part_srt.stat().st_size < 10:
            print(f"📝 Đang tạo phụ đề động chuẩn TikTok High-CTR cho {badge}...")
            try:
                generate_srt_from_text_and_duration(part["full_text"], dur, part_srt)
            except Exception as e_srt:
                print(f"⚠️ Lỗi sinh phụ đề: {e_srt}")

        # 3. Cắt lát Video B-roll riêng biệt
        distinct_slice = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        # 4. Tạo Thumbnail độc quyền
        part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"
        genre_label = "#TrọngSinh" if "trongsinh" in prefix else ("#GiaĐấu" if "mechong" in prefix else ("#TrinhThám" if "trangmau" in prefix else "#KinhDị"))
        try:
            generate_part_thumbnail(
                source_video_or_image=distinct_slice,
                output_thumb_path=part_thumb,
                story_title=story_data["title"],
                part_label=f"TẬP {p_num}",
                genre_tag=genre_label
            )
        except Exception as e:
            print(f"⚠️ Lỗi tạo thumbnail: {e}")
            part_thumb = None

        # 5. Render Video 1080p 16:9 hoàn chỉnh
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
                srt_path=str(part_srt) if part_srt.exists() else None,
                enable_subtitles=True,
                thumbnail_path=str(part_thumb) if part_thumb and part_thumb.exists() else None
            )
            print(f"  ✅ ĐÃ RENDER THÀNH CÔNG: {part_video.name} ({part_video.stat().st_size / (1024*1024):.1f} MB)")
        else:
            print(f"  ✅ Video {badge} đã có sẵn hoàn chỉnh: {part_video.name}")

        rendered_videos.append(part_video)

    return rendered_videos

def load_status() -> dict:
    default_status = {
        "series1_trongsinh": {"part1": False, "part2": False, "part3": False},
        "series2_mechong": {"part1": False, "part2": False, "part3": False},
        "series3_trangmau": {"part1": False, "part2": False, "part3": False},
        "series4_huyetnguyen": {"part1": False, "part2": False, "part3": False}
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
    
    if "trongsinh" in series_key:
        tag_genre = "#trongsinh #vamat #haomon #nuphucuong #audiotruyen #reviewtruyen"
        hook_text = (
            "Mở mắt trong đêm đính hôn mười năm trước và cú vả mặt hủy hôn chấn động giới tài phiệt."
            if part_num == 1
            else "Đấu trí thương trường vạch trần con chip bí mật trong chiếc trâm cài ngọc bích."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Đóa sen lửa hào môn kiêu hãnh đòi lại toàn bộ công lý!"
        )
        magnet_q = (
            "👉 Nếu được trọng sinh về 10 năm trước, việc đầu tiên bạn làm là gì? Bình luận ngay nhé!"
            if part_num == 1
            else "👉 Theo bạn kẻ phản bội nguy hiểm nhất là trà xanh hay bảo mẫu thân cận? Bình luận 1 hay 2!"
            if part_num == 2
            else "👉 Màn vả mặt này đã đủ thỏa mãn chưa? Để lại cảm nghĩ của bạn dưới bình luận nhé!"
        )
    elif "mechong" in series_key:
        tag_genre = "#mechong #giadau #haccuong #doisong #audiotruyen #reviewtruyen"
        hook_text = (
            "Đêm mưa bão bị mẹ chồng đuổi khỏi nhà và sự xuất hiện chấn động của chiếc Rolls-Royce cứu vớt."
            if part_num == 1
            else "Phiên đấu giá 120 tỷ mua đứt căn biệt thự ven sông và cú sụp đổ của gia tộc bội bạc."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Nàng dâu thức tỉnh biến biệt thự 50 tỷ thành trung tâm bảo trợ!"
        )
        magnet_q = (
            "👉 Mẹ chồng đuổi nàng dâu đêm mưa vì không đẻ được con trai, đáng trách không? Bình luận 1 (Có) hay 2 (Quá tàn nhẫn)!"
            if part_num == 1
            else "👉 Bỏ ra 120 tỷ mua lại nhà của chồng cũ để trả thù, ngầu hay phí tiền? Bình luận 1 hoặc 2 nhé!"
            if part_num == 2
            else "👉 Bạn có ủng hộ việc phụ nữ tự chủ tài chính để không bị khinh thường không? Bình luận quan điểm nhé!"
        )
    elif "trangmau" in series_key:
        tag_genre = "#trinhtham #phapan #kyan #hinhsu #audiotruyen #reviewtruyen"
        hook_text = (
            "Chiếc điện thoại bàn đứt dây bỗng đổ chuông lúc 2h sáng và lời cảnh báo của thám tử đã chết 5 năm."
            if part_num == 1
            else "Đột kích hầm ngầm biệt thự Ba Vì và giải mã vali rửa tiền nghìn tỷ của ông trùm giấu mặt."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Vạch trần chân tướng kẻ hai mặt đứng sau vụ án đồi thông!"
        )
        magnet_q = (
            "👉 Nếu nửa đêm điện thoại bàn đứt dây đổ chuông, bạn có dám nhấc máy không? Bình luận 1 (Dám) hay 2 (Không) nhé!"
            if part_num == 1
            else "👉 Bạn đoán xem kẻ chủ mưu là Viện phó hay Trưởng phòng điều tra? Bình luận số 1 hoặc 2 nào!"
            if part_num == 2
            else "👉 Bạn thấy cái kết của kẻ phản bội đã xứng đáng chưa? Để lại bình luận cho mình biết nhé!"
        )
    else:
        tag_genre = "#kinhdi #truyenma #tamlinh #quykhe #guongco #audiotruyen"
        hook_text = (
            "Tấm vải đỏ phủ chiếc gương cổ tự tuột lúc 2h45 sáng và bóng ma không mặt dưới căn phòng số 44."
            if part_num == 1
            else "Bí mật chiếc hòm gỗ sơn son thiếp vàng dưới nền nhà và quỷ khế trói buộc 7 mạng người."
            if part_num == 2
            else "Trọn bộ 3 tập đã lên sóng! Ngọn lửa tam muội thiêu rụi chiếc gương ma quái lúc rạng đông!"
        )
        magnet_q = (
            "👉 Đố bạn dám trùm chăn ngủ một mình sau khi nghe tập này không? Bình luận 1 (Dám) hay 2 (Bật đèn ngủ) nhé!"
            if part_num == 1
            else "👉 Theo bạn ma quỷ trong gương hay lòng tham của chủ nhà đáng sợ hơn? Bình luận 1 hoặc 2 để tranh luận!"
            if part_num == 2
            else "👉 Bạn có tin vào những lời nguyền cổ truyền miệng không? Để lại câu chuyện của bạn dưới bình luận nhé!"
        )

    return f"{badge} {title}. {hook_text} {magnet_q} #audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp {tag_genre}"

def main(auto_publish: bool = True, fast_schedule: bool = False, render_only: bool = False, publish_only: bool = False):
    from core.stories.trong_sinh_hoa_sen_lua_masterpiece import get_trong_sinh_hoa_sen_lua_masterpiece_story
    from core.stories.me_chong_thuc_tinh_masterpiece import get_me_chong_thuc_tinh_masterpiece_story
    from core.stories.huyen_nghi_trang_mau_masterpiece import get_huyen_nghi_trang_mau_masterpiece_story
    from core.stories.kinh_di_huyet_nguyen_masterpiece import get_kinh_di_huyet_nguyen_masterpiece_story

    bgm_trongsinh = get_safe_bgm_for_genre("HEALING")
    bgm_mechong = get_safe_bgm_for_genre("ME_CHONG")
    bgm_trangmau = get_safe_bgm_for_genre("HUYEN_NGHI")
    bgm_huyetnguyen = get_safe_bgm_for_genre("KINH_DI")

    series_list = [
        {
            "key": "series1_trongsinh",
            "prefix": "VID_masterpiece_1_trongsinh",
            "bgm": bgm_trongsinh,
            "story": get_trong_sinh_hoa_sen_lua_masterpiece_story(),
            "series_offset_sec": 0
        },
        {
            "key": "series2_mechong",
            "prefix": "VID_masterpiece_2_mechong",
            "bgm": bgm_mechong,
            "story": get_me_chong_thuc_tinh_masterpiece_story(),
            "series_offset_sec": 3600 if not fast_schedule else 30
        },
        {
            "key": "series3_trangmau",
            "prefix": "VID_masterpiece_3_trangmau",
            "bgm": bgm_trangmau,
            "story": get_huyen_nghi_trang_mau_masterpiece_story(),
            "series_offset_sec": 7200 if not fast_schedule else 60
        },
        {
            "key": "series4_huyetnguyen",
            "prefix": "VID_masterpiece_4_huyetnguyen",
            "bgm": bgm_huyetnguyen,
            "story": get_kinh_di_huyet_nguyen_masterpiece_story(),
            "series_offset_sec": 10800 if not fast_schedule else 90
        }
    ]

    print("=" * 75)
    print("🌟 KHỞI ĐỘNG SẢN XUẤT & XUẤT BẢN 4 BỘ AUDIO KIỆT TÁC (12 VIDEO MP4)")
    print(f"⏰ Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("💎 Tiêu chuẩn: Kinetic Subtitles High-CTR | Comment Magnets | BGM An Toàn")
    print(f"💎 Chế độ: auto_publish={auto_publish}, fast_schedule={fast_schedule}")
    print("=" * 75)

    status = load_status()
    out_dir = ROOT / "assets" / "output"

    if "base_time" not in status:
        status["base_time"] = time.time()
        save_status(status)
    base_time = float(status["base_time"])

    interval_parts_sec = 15 * 60 if not fast_schedule else 20
    last_publish_ts = 0.0

    # TIẾN TRÌNH CUỐN CHIẾU: SẢN XUẤT ĐẾN ĐÂU ĐĂNG ĐẾN ĐÓ (PIPELINE STREAMING)
    for s_idx, s_conf in enumerate(series_list, 1):
        s_key = s_conf["key"]
        s_title = s_conf["story"]["title"]
        s_base_target = base_time + s_conf["series_offset_sec"]

        print(f"\n=======================================================")
        print(f"🚀 TIẾN TRÌNH BỘ {s_idx}/4: {s_title}")
        print(f"=======================================================")

        # 1. Sản xuất trọn bộ nếu chưa render
        if not publish_only:
            produce_single_series(s_conf["story"], s_conf["prefix"], s_conf["bgm"])

        if render_only or not auto_publish:
            print("ℹ️ Render Only hoặc Auto Publish tắt, chuyển tiếp...")
            continue

        # 2. Xuất bản từng tập lên TikTok Studio
        for p_idx in [1, 2, 3]:
            p_key = f"part{p_idx}"
            if status[s_key].get(p_key, False):
                print(f"  ✅ Đã đăng trước đó: {s_key} - {p_key}")
                continue

            target_ts = s_base_target + (p_idx - 1) * interval_parts_sec
            wait_until(target_ts, f"Bộ {s_idx} - Tập {p_idx}")

            # Đảm bảo khoảng cách an toàn giữa 2 lần đăng
            min_gap_sec = 15 * 60 if not fast_schedule else 15
            if last_publish_ts > 0 and (time.time() - last_publish_ts) < min_gap_sec:
                remain_gap = min_gap_sec - (time.time() - last_publish_ts)
                wait_until(time.time() + remain_gap, f"Giãn cách {min_gap_sec//60} phút an toàn")

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
                    print(f"  🎉 XUẤT BẢN THÀNH CÔNG: {s_key} - {p_key}!")
                    status[s_key][p_key] = True
                    save_status(status)
                    last_publish_ts = time.time()
                    break
                else:
                    print(f"  ❌ Lần {attempt} thất bại. Chờ 5s thử lại...")
                    time.sleep(5)

            if not upload_success:
                print(f"  🚨 Bỏ qua {s_key} - {p_key} sau 3 lần thử thất bại.")

    print("\n" + "=" * 75)
    print("🎉 HOÀN TẤT 100% TIẾN TRÌNH SẢN XUẤT & XUẤT BẢN CẢ 4 BỘ AUDIO KIỆT TÁC!")
    print("=" * 75)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast-schedule", action="store_true", help="Chạy lịch nhanh để đăng ngay các video")
    parser.add_argument("--render-only", action="store_true", help="Chỉ render video, không đăng")
    parser.add_argument("--publish-only", action="store_true", help="Chỉ đăng video đã render sẵn")
    args = parser.parse_args()

    main(
        auto_publish=True,
        fast_schedule=args.fast_schedule,
        render_only=args.render_only,
        publish_only=args.publish_only
    )
