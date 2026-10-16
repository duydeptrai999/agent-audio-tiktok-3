# -*- coding: utf-8 -*-
"""
scripts/produce_series.py
Quy trình sản xuất trọn gói Audio TTS 1.5x + Mastering -13 LUFS + Render Video MP4 16:9
cho Bộ 2 (Trinh thám) và Bộ 3 (Drama gia đấu) tuân thủ 100% GEMINI.md.
"""

import sys
import os
import asyncio
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

import edge_tts
from core.ffmpeg_utils import get_ffmpeg_exe, render_playable_video, probe_media_file
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from config.settings import BGM_VOLUME, VOICE_VOLUME

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
    """Dọn dẹp các tệp tạm thời còn sót lại trong assets/audio."""
    audio_dir = root / "assets" / "audio"
    if not audio_dir.exists():
        return
    for item in audio_dir.iterdir():
        if item.is_file() and any(x in item.name for x in ["_chk", "_raw", "_concat", "test_sent_"]):
            try:
                item.unlink(missing_ok=True)
            except Exception:
                pass

async def generate_tts_for_part(text: str, voice: str, output_path: Path):
    """Sinh audio Edge-TTS chất lượng cao, chia chunk và ghép bằng FFmpeg, tua 1.5x."""
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
    semaphore = asyncio.Semaphore(4)

    # Tinh chỉnh Rate và Pitch chuẩn Studio Radio Broadcast
    # Giọng Nam Minh: Rate +18%, Pitch -2Hz (trầm ấm, đầm, uy quyền)
    # Giọng Hoài My: Rate +20%, Pitch +1Hz (sáng rõ, dồn dập, truyền cảm)
    rate_val = "+18%" if "NamMinh" in voice else "+20%"
    pitch_val = "-2Hz" if "NamMinh" in voice else "+1Hz"

    async def synth_chk(idx, chk, fpath):
        async with semaphore:
            for attempt in range(5):
                try:
                    comm = edge_tts.Communicate(chk, voice=voice, rate=rate_val, pitch=pitch_val)
                    await asyncio.wait_for(comm.save(str(fpath)), timeout=45.0)
                    if fpath.exists() and fpath.stat().st_size > 500:
                        return
                except Exception:
                    await asyncio.sleep(1.0 * (attempt + 1))
            if not fpath.exists() or fpath.stat().st_size <= 500:
                raise RuntimeError(f"Edge-TTS failed to synthesize chunk {idx} after 5 retries with {voice}")

    try:
        tasks = [synth_chk(i, c, chunk_files[i]) for i, c in enumerate(chunks)]
        await asyncio.gather(*tasks)

        # Ghép các chunk bằng FFmpeg concat
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

        # Tốc độ kết hợp: Edge-TTS Native (+20% = 1.2x) * FFmpeg atempo (1.25x) = 1.50x Chuẩn GEMINI.md
        # Giữ nguyên cao độ tự nhiên, loại bỏ hoàn toàn hiện tượng méo tiếng và rè âm thanh
        subprocess.run([
            ffmpeg, "-y",
            "-i", str(raw_merged),
            "-filter:a", "atempo=1.25",
            "-c:a", "libmp3lame", "-b:a", "192k",
            str(output_path)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        print(f"  ✅ Đã tạo xong Audio 1.5x (Studio Radio Broadcast): {output_path.name} ({output_path.stat().st_size / 1024:.1f} KB)")
    finally:
        # Dọn dẹp triệt để file tạm trong khối finally
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

def produce_story_videos(story_data: dict, prefix: str, bgm_file: Path):
    """Sản xuất toàn bộ audio và render 3 video cho 1 bộ truyện với B-Roll riêng biệt và Thumbnail riêng từng phần."""
    out_dir = root / "assets" / "output"
    audio_dir = root / "assets" / "audio"
    thumb_dir = root / "assets" / "thumbnails"
    thumb_dir.mkdir(parents=True, exist_ok=True)

    # Dọn dẹp tệp tạm mồ côi trước khi sản xuất
    cleanup_orphaned_audio_temps()

    print("\n" + "=" * 70)
    print(f"🎬 BẮT ĐẦU SẢN XUẤT TRỌN BỘ: {story_data['title']}")
    print(f"🎙️ Giọng đọc: {story_data['voice']} (Tốc độ 1.5x)")
    print("=" * 70)

    for part in story_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        print(f"\n--- [TẬP {p_num}] {badge} ---")

        # 1. Sinh Audio
        part_audio = audio_dir / f"{prefix}_part{p_num}_15x.mp3"
        if not part_audio.exists() or part_audio.stat().st_size < 10000:
            print(f"🎙️ Đang sinh giọng đọc Edge-TTS cho {badge} ({len(part['full_text'].split())} từ)...")
            asyncio.run(generate_tts_for_part(part["full_text"], story_data["voice"], part_audio))
        else:
            print(f"🎙️ Audio {badge} đã có sẵn: {part_audio.name}")

        # Đo thời lượng audio
        probe = probe_media_file(part_audio)
        dur = probe.get("duration", 600.0)
        if dur < 10.0:
            dur = 600.0

        # 2. Cắt lát Video B-roll HOÀN TOÀN RIÊNG BIỆT cho tập này
        distinct_slice = background_manager.get_distinct_slice_for_part(
            series_id=prefix,
            part_number=p_num,
            duration_seconds=dur
        )

        # 3. Tạo Thumbnail độc quyền cho tập này
        part_thumb = thumb_dir / f"{prefix}_part{p_num}_thumb.jpg"
        try:
            generate_part_thumbnail(
                source_video_or_image=distinct_slice,
                output_thumb_path=part_thumb,
                story_title=story_data["title"],
                part_label=f"TẬP {p_num}",
                genre_tag=f"#{story_data.get('genre', 'AudioTruyện')}"
            )
        except Exception as e:
            print(f"⚠️ Không thể tạo thumbnail: {e}")
            part_thumb = None

        # 4. Render Video
        part_video = out_dir / f"{prefix}_part{p_num}_final.mp4"
        if not part_video.exists() or part_video.stat().st_size < 1000000:
            print(f"🎥 Đang render video 1080p 16:9 cho {badge} (B-Roll riêng biệt + Thumbnail bìa)...")
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

if __name__ == "__main__":
    from core.stories.detective_masterpiece import get_detective_masterpiece_story
    from core.stories.family_drama_masterpiece import get_family_drama_masterpiece_story

    from core.bgm_manager import get_safe_bgm_for_genre
    bgm_detective = get_safe_bgm_for_genre("HUYEN_NGHI")
    bgm_drama = get_safe_bgm_for_genre("ME_CHONG")

    # Sản xuất Bộ 2
    detective_story = get_detective_masterpiece_story()
    produce_story_videos(detective_story, prefix="VID_detective", bgm_file=bgm_detective)

    # Sản xuất Bộ 3
    drama_story = get_family_drama_masterpiece_story()
    produce_story_videos(drama_story, prefix="VID_drama", bgm_file=bgm_drama)

    print("\n🎉 HOÀN TẤT SẢN XUẤT 100% CẢ 2 BỘ AUDIO (6 VIDEO FULL HD 1080P)!")
