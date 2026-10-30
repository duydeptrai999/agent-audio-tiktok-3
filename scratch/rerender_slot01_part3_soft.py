# -*- coding: utf-8 -*-
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.stories.daily_story_factory import get_daily_10_series
from core.ffmpeg_utils import render_playable_video, probe_media_file
from core.bgm_manager import get_safe_bgm_for_genre
from core.background_manager import background_manager
from config.settings import BGM_VOLUME, VOICE_VOLUME

def main():
    target_date = "2026-10-25"
    series = get_daily_10_series(target_date)[0] # Slot 1
    prefix = series["prefix"]
    title = series["title"]
    bgm_file = get_safe_bgm_for_genre("ROMANCE")
    
    part = series["parts"][2] # Part 3
    p_num = 3
    badge = part["badge_label"]

    part_audio = ROOT / "assets" / "audio" / f"{prefix}_part{p_num}_cinema.mp3"
    part_video = ROOT / "assets" / "output" / f"{prefix}_part{p_num}_final.mp4"

    probe = probe_media_file(part_audio)
    dur = probe.get("duration", 300.0)

    print(f"🎬 Đang cắt slice B-roll ({dur:.1f}s)...")
    slice_path = background_manager.get_distinct_slice_for_part(
        series_id=prefix,
        part_number=p_num,
        duration_seconds=dur
    )

    print(f"🎬 Đang render video mới với âm thanh êm dịu, nhẹ nhàng...")
    render_playable_video(
        output_file=part_video,
        voice_audio_path=str(part_audio),
        clean_footage_path=str(slice_path),
        bgm_audio_path=str(bgm_file),
        badge_label=badge,
        bgm_volume=BGM_VOLUME,
        voice_volume=VOICE_VOLUME,
        enable_subtitles=False,
        title_text=title
    )

    print(f"✅ Hoàn tất render Slot 1 - Tập 3: {part_video.name} ({part_video.stat().st_size / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    main()
