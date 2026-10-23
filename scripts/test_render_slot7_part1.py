# -*- coding: utf-8 -*-
import sys
import asyncio
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.stories.daily_story_factory import get_daily_10_series
from core.audio_engine import generate_cinema_tts_audio
from core.background_manager import background_manager
from core.thumbnail_generator import generate_part_thumbnail
from core.ffmpeg_utils import render_playable_video, probe_media_file
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME

series_list = get_daily_10_series("2026-10-19")
s7 = next(s for s in series_list if s["slot_index"] == 7)

prefix = s7["prefix"]
title = s7["title"]
bgm_file = get_safe_bgm_for_genre(s7["bgm_genre"])
part1 = s7["parts"][0]

print("=== SẢN XUẤT THỬ NGHIỆM TẬP 1 BỘ 7 VỚI CẬP NHẬT MỚI ===")
print("Tựa đề:", title)
print("BGM mới:", bgm_file.name if bgm_file else "None")
print("Câu mở đầu kịch tính:", part1["text"][:120])

part_audio = ROOT / f"assets/audio/{prefix}_part1_15x.mp3"
part_video = ROOT / f"assets/output/{prefix}_part1_final.mp4"
part_thumb = ROOT / f"assets/thumbnails/{prefix}_part1_thumb.jpg"

print("\n1. Sinh Voice Audio Edge-TTS 1.5x...")
asyncio.run(generate_cinema_tts_audio(
    text=part1["text"],
    voice=s7["voice"],
    output_path=part_audio,
    target_speed=1.50
))
print("Audio size:", part_audio.stat().st_size // 1024, "KB")

probe = probe_media_file(part_audio)
dur = probe.get("duration", 600.0)
print(f"Audio duration: {dur:.1f}s ({dur/60:.2f} phút)")

print("\n2. Cắt B-Roll Slice...")
slice_path = background_manager.get_distinct_slice_for_part(
    series_id=prefix,
    part_number=1,
    duration_seconds=dur
)

print("\n3. Tạo Thumbnail...")
generate_part_thumbnail(
    source_video_or_image=slice_path,
    output_thumb_path=part_thumb,
    story_title=title,
    part_label="TẬP 1",
    genre_tag="#GiaDauMeChong"
)

print("\n4. Render MP4 với BGM mới & Cinema Sidechain Ducking...")
render_playable_video(
    output_file=part_video,
    voice_audio_path=str(part_audio),
    clean_footage_path=str(slice_path),
    bgm_audio_path=str(bgm_file),
    badge_label="TẬP 1",
    bgm_volume=BGM_VOLUME,
    voice_volume=VOICE_VOLUME,
    enable_subtitles=False,
    thumbnail_path=str(part_thumb)
)
print("\nRENDER HOÀN TẤT:", part_video, f"({part_video.stat().st_size // 1024} KB)")
