# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")

from core.ffmpeg_utils import render_playable_video, probe_media_file, get_ffmpeg_exe
from core.background_manager import extract_video_slice
from core.bgm_manager import get_safe_bgm_for_genre
from config.settings import BGM_VOLUME, VOICE_VOLUME, ENABLE_SUBTITLES

AUDIO_DIR = ROOT / "assets" / "audio"
OUTPUT_DIR = ROOT / "assets" / "output"
SLICES_DIR = ROOT / "assets" / "footage" / "slices"

def render_s06():
    print("=" * 60)
    print("🚀 [RERENDER 16:9] BẮT ĐẦU TÁI TẠO BỘ 6 (HEALING - Ánh Sáng Nơi Tận Cùng Đêm Tối)")
    print("=" * 60)
    
    script_file = ROOT / "data" / "generated_scripts" / "VID_20261027_s06_slot_06_haomon.json"
    s6_data = json.loads(script_file.read_text(encoding="utf-8"))
    prefix = s6_data["prefix"]
    title = s6_data["title"]
    genre = s6_data.get("genre", "HEALING")
    bgm_file = get_safe_bgm_for_genre(s6_data.get("bgm_genre", "ROMANCE"))
    
    # Nguồn video nền 16:9 gốc: cooking_home_meals_3_raw.mp4 (1920x1080)
    raw_source = ROOT / "assets" / "footage" / "raw_downloaded" / "cooking_home_meals_3_raw.mp4"
    if not raw_source.exists():
        raw_source = ROOT / "assets" / "footage" / "youtube_pool" / "baking_asmr_2hours_3NvvOVrm1uY.mp4"
    
    print(f"🎬 Nguồn B-roll 16:9: {raw_source.name}")
    probe_raw = probe_media_file(raw_source)
    print(f"   Độ phân giải nguồn: {probe_raw.get('width')}x{probe_raw.get('height')} (16:9)")
    
    offset = 0.0
    for part in s6_data["parts"]:
        p_num = part["part_number"]
        badge = part["badge_label"]
        part_audio = AUDIO_DIR / f"{prefix}_part{p_num}_cinema.mp3"
        part_srt = AUDIO_DIR / f"{prefix}_part{p_num}_cinema.srt"
        part_video = OUTPUT_DIR / f"{prefix}_part{p_num}_final.mp4"
        
        probe_a = probe_media_file(part_audio)
        dur = probe_a.get("duration", 400.0)
        
        # 1. Cắt slice 16:9 giữ nguyên vẹn 100%
        slice_name = f"slice_{prefix}_p{p_num}_16x9.mp4"
        slice_path = SLICES_DIR / slice_name
        if slice_path.exists():
            slice_path.unlink()
            
        print(f"\n✂️ Đang cắt slice 16:9 cho Tập {p_num} (Offset: {offset:.1f}s, Dur: {dur:.1f}s)...")
        extract_video_slice(
            source_path=raw_source,
            slice_path=slice_path,
            start_sec=offset,
            duration_seconds=dur
        )
        offset += dur + 5.0
        
        probe_sl = probe_media_file(slice_path)
        print(f"   Slice đã cắt: {probe_sl.get('width')}x{probe_sl.get('height')} ({probe_sl.get('duration'):.1f}s)")
        
        # 2. Xóa video cũ nếu bị dọc 9:16
        if part_video.exists():
            part_video.unlink()
            
        # 3. Render video 16:9
        print(f"🎥 Đang render video hoàn chỉnh 16:9 cho Tập {p_num}...")
        render_playable_video(
            output_file=part_video,
            voice_audio_path=str(part_audio),
            clean_footage_path=str(slice_path),
            bgm_audio_path=str(bgm_file),
            srt_path=str(part_srt) if (ENABLE_SUBTITLES and part_srt.exists()) else None,
            badge_label=badge,
            bgm_volume=BGM_VOLUME,
            voice_volume=VOICE_VOLUME,
            enable_subtitles=ENABLE_SUBTITLES,
            title_text=title,
            genre=genre
        )
        
        probe_out = probe_media_file(part_video)
        print(f"✅ HOÀN THÀNH Tập {p_num}: {part_video.name}")
        print(f"   Độ phân giải video xuất: {probe_out.get('width')}x{probe_out.get('height')} (Chuẩn 16:9)")
        print(f"   Thời lượng: {probe_out.get('duration'):.1f}s | Dung lượng: {part_video.stat().st_size / 1024 / 1024:.1f} MB")

def render_s07_part3():
    print("\n" + "=" * 60)
    print("🚀 [RERENDER 16:9] TÁI TẠO BỘ 7 - TẬP 3 (Màn Trả Thù Đã Nhất Đời Tôi)")
    print("=" * 60)
    
    script_file = ROOT / "data" / "generated_scripts" / "VID_20261027_s07_slot_07_giadau.json"
    s7_data = json.loads(script_file.read_text(encoding="utf-8"))
    prefix = s7_data["prefix"]
    title = s7_data["title"]
    genre = s7_data.get("genre", "GIA_DAU")
    bgm_file = get_safe_bgm_for_genre(s7_data.get("bgm_genre", "ME_CHONG"))
    
    raw_source = ROOT / "assets" / "footage" / "youtube_pool" / "traditional_pottery_teapot_asmr_AGVNlB400qI.mp4"
    probe_raw = probe_media_file(raw_source)
    print(f"🎬 Nguồn B-roll 16:9: {raw_source.name} ({probe_raw.get('width')}x{probe_raw.get('height')})")
    
    p3 = s7_data["parts"][2]
    badge = p3["badge_label"]
    part_audio = AUDIO_DIR / f"{prefix}_part3_cinema.mp3"
    part_srt = AUDIO_DIR / f"{prefix}_part3_cinema.srt"
    part_video = OUTPUT_DIR / f"{prefix}_part3_final.mp4"
    
    probe_a = probe_media_file(part_audio)
    dur = probe_a.get("duration", 405.0)
    
    slice_name = f"slice_{prefix}_p3_16x9.mp4"
    slice_path = SLICES_DIR / slice_name
    if slice_path.exists():
        slice_path.unlink()
        
    print(f"\n✂️ Đang cắt slice 16:9 cho Tập 3 (Start: 427s, Dur: {dur:.1f}s)...")
    extract_video_slice(
        source_path=raw_source,
        slice_path=slice_path,
        start_sec=427.0,
        duration_seconds=dur
    )
    
    if part_video.exists():
        part_video.unlink()
        
    print(f"🎥 Đang render video hoàn chỉnh 16:9 cho Tập 3...")
    render_playable_video(
        output_file=part_video,
        voice_audio_path=str(part_audio),
        clean_footage_path=str(slice_path),
        bgm_audio_path=str(bgm_file),
        srt_path=str(part_srt) if (ENABLE_SUBTITLES and part_srt.exists()) else None,
        badge_label=badge,
        bgm_volume=BGM_VOLUME,
        voice_volume=VOICE_VOLUME,
        enable_subtitles=ENABLE_SUBTITLES,
        title_text=title,
        genre=genre
    )
    
    probe_out = probe_media_file(part_video)
    print(f"✅ HOÀN THÀNH Tập 3: {part_video.name}")
    print(f"   Độ phân giải video xuất: {probe_out.get('width')}x{probe_out.get('height')} (Chuẩn 16:9)")
    print(f"   Thời lượng: {probe_out.get('duration'):.1f}s | Dung lượng: {part_video.stat().st_size / 1024 / 1024:.1f} MB")

if __name__ == "__main__":
    render_s06()
    render_s07_part3()
    print("\n🎉🎉 TOÀN BỘ VIDEO ĐÃ ĐƯỢC TRẢ VỀ CHUẨN 16:9 (1920x1080) NGUYÊN BẢN HOÀN TOÀN! 🎉🎉")
