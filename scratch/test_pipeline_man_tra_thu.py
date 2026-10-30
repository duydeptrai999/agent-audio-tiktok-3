# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story
from core.stories.script_quality_gate import validate_story_series
from core.audio_engine import generate_cinema_tts_audio
from core.ffmpeg_utils import render_playable_video, probe_media_file
from core.thumbnail_generator import generate_part_thumbnail

async def run_pipeline_test():
    print("=" * 80)
    print("BẮT ĐẦU KIỂM TRA QUY TRÌNH SẢN XUẤT END-TO-END (MASTER CODEX 7.0)")
    print("=" * 80)

    # 1. Kiểm tra kịch bản qua Quality Gate
    print("\n--- BƯỚC 1: KIỂM ĐỊNH KỊCH BẢN QUA CỔNG CHẤT LƯỢNG SCRIPT QUALITY GATE ---")
    story = get_man_tra_thu_masterpiece_story()
    story = validate_story_series(story)
    title = story["title"]
    genre = story["genre"]
    voice = story["voice"]
    print(f"Tiêu đề: {title}")
    print(f"Thể loại: {genre} | Giọng đọc chuẩn: {voice}")

    p1 = story["parts"][0]
    p1_text = p1["full_text"]
    words_count = len(p1_text.split())
    print(f"Tập 1 word count: {words_count} từ")
    print(f"Câu Hook 3s: {p1['hook'][:120]}")

    # 2. Sinh Audio Edge-TTS
    # Chúng ta test đoạn mở đầu 350 từ (~2 phút audio) để kiểm tra tốc độ, âm sắc, BGM ducking nhanh và chuẩn
    print("\n--- BƯỚC 2: SINH AUDIO EDGE-TTS (vi-VN-HoaiMyNeural, rate=+8%) ---")
    test_audio_path = ROOT / "assets" / "audio" / "test_man_tra_thu_part1.mp3"
    
    # Chọn đoạn mở đầu 380 từ bao gồm Hook 3s + Mâu thuẫn kịch tính
    sample_text = " ".join(p1_text.split()[:380])
    
    t0 = time.time()
    await generate_cinema_tts_audio(
        text=sample_text,
        voice=voice,
        output_path=test_audio_path,
        target_speed=1.08, # rate +8% tự nhiên, ấm áp
        genre=genre
    )
    t_tts = time.time() - t0
    print(f"Sinh Audio thành công trong {t_tts:.2f}s!")
    print(f"File audio: {test_audio_path} ({test_audio_path.stat().st_size // 1024} KB)")

    probe_audio = probe_media_file(test_audio_path)
    audio_dur = probe_audio.get("duration", 0.0)
    print(f"Thời lượng audio: {audio_dur:.2f} giây ({audio_dur/60:.2f} phút)")

    # 3. Lựa chọn BGM và Video nền ASMR Dọc 9:16
    print("\n--- BƯỚC 3: LỰA CHỌN B-ROLL ASMR VÀ BGM CHỐNG BẢN QUYỀN ---")
    footage_path = ROOT / "assets" / "footage" / "baking_vertical.mp4"
    if not footage_path.exists():
        print(f"Lỗi: Không tìm thấy {footage_path}")
        return

    probe_foot = probe_media_file(footage_path)
    print(f"Footage: {footage_path.name} ({probe_foot.get('width')}x{probe_foot.get('height')})")

    bgm_candidates = [
        ROOT / "TikTok_BGM_Audio" / "02 - Thu Qua Dong Sang Ha Nho (Instrumental) - Sad Romance.mp3",
        ROOT / "TikTok_BGM_Audio" / "05 - Da Lau Khong Gap - Ben Nhau Tron Doi OST.mp3",
        ROOT / "TikTok_BGM_Audio" / "04 - Fox Rain Acoustic - Romance BGM.mp3"
    ]
    bgm_path = next((b for b in bgm_candidates if b.exists()), None)
    print(f"BGM được chọn: {bgm_path.name if bgm_path else 'None'}")

    # 4. Tạo Thumbnail
    print("\n--- BƯỚC 4: SINH THUMBNAIL TẬP 1 ---")
    thumb_path = ROOT / "assets" / "thumbnails" / "test_man_tra_thu_part1_thumb.jpg"
    generate_part_thumbnail(
        source_video_or_image=footage_path,
        output_thumb_path=thumb_path,
        story_title=title,
        part_label="TẬP 1",
        genre_tag="#GiaDauMeChong #TraThu"
    )
    print(f"Thumbnail sinh thành công: {thumb_path.name} ({thumb_path.stat().st_size // 1024} KB)")

    # 5. Ráp nối và Render Video MP4 với Cinema Ducking
    print("\n--- BƯỚC 5: RENDER VIDEO MP4 HOÀN CHỈNH VỚI DUCKING (-22dB) ---")
    output_video_path = ROOT / "assets" / "output" / "test_man_tra_thu_part1_final.mp4"
    
    t0_render = time.time()
    render_playable_video(
        output_file=output_video_path,
        voice_audio_path=str(test_audio_path),
        clean_footage_path=str(footage_path),
        bgm_audio_path=str(bgm_path) if bgm_path else "",
        badge_label="TẬP 1",
        bgm_volume=0.18, # -22dB ducking
        voice_volume=1.0,
        enable_subtitles=False,
        thumbnail_path=str(thumb_path),
        title_text=title
    )
    t_render = time.time() - t0_render
    print(f"Render video thành công trong {t_render:.2f}s!")
    print(f"File video: {output_video_path} ({output_video_path.stat().st_size // 1024} KB)")

    # 6. Kiểm định chất lượng video đầu ra
    print("\n--- BƯỚC 6: KIỂM ĐỊNH VIDEO ĐẦU RA ---")
    probe_out = probe_media_file(output_video_path)
    print(f"Kiểm tra Video MP4: {probe_out}")
    assert probe_out.get("is_valid", False), "Video output không hợp lệ!"
    assert probe_out.get("has_audio", False), "Video output thiếu audio!"
    assert probe_out.get("duration", 0) > 30.0, "Thời lượng video quá ngắn!"
    assert probe_out.get("width") == 1080 and probe_out.get("height") == 1920, "Video không đúng chuẩn dọc 1080x1920 (9:16)!"

    print("\n" + "=" * 80)
    print("KIỂM TRA HOÀN TẤT 100%! TẤT CẢ TIÊU CHUẨN MASTER CODEX 7.0 ĐÃ ĐƯỢC CHỨNG THỰC!")
    print("=" * 80)

if __name__ == "__main__":
    asyncio.run(run_pipeline_test())
