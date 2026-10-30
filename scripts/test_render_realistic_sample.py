# -*- coding: utf-8 -*-
"""
scripts/test_render_realistic_sample.py
Tạo bản nghe thử thực tế (Audio Sample) cho kịch bản mới vừa tối ưu:
- Giọng đọc: vi-VN-HoaiMyNeural (rate="+6%", pitch="+0Hz")
- Nhạc nền: 12 - The Truth That You Leave - Pianoboy.mp3 (Ducking -23dB)
- Lưu vào: assets/audio/test_codex8_realistic_hoaimy.mp3
"""

import sys
import asyncio
import subprocess
import imageio_ffmpeg
from pathlib import Path
import edge_tts

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story

story = get_man_tra_thu_masterpiece_story()
part1_text = story["parts"]["part1"]

# Lấy 500 từ đầu tiên làm bản showcase mẫu
words = part1_text.split()
sample_text = " ".join(words[:450])

output_dir = root_dir / "assets" / "audio"
output_dir.mkdir(parents=True, exist_ok=True)
raw_tts_file = output_dir / "temp_raw_sample.mp3"
final_sample_file = output_dir / "test_codex8_realistic_hoaimy.mp3"
bgm_file = root_dir / "TikTok_BGM_Audio" / "12 - The Truth That You Leave - Pianoboy.mp3"

async def generate():
    print(f"1. Dang sinh giọng đọc Edge-TTS HoaiMyNeural ({len(sample_text.split())} từ)...")
    comm = edge_tts.Communicate(sample_text, voice="vi-VN-HoaiMyNeural", rate="+6%", pitch="+0Hz")
    await comm.save(str(raw_tts_file))
    print(f"-> Da sinh raw TTS: {raw_tts_file.stat().st_size} bytes")

    print(f"2. Dang ghep nhac nen Pianoboy ducking -23dB...")
    # FFmpeg filter: BGM lặp lại, giảm âm lượng xuống -23dB (volume=0.07), mix cùng giọng đọc (volume=1.0)
    cmd = [
        ffmpeg_exe, "-y",
        "-i", str(raw_tts_file),
        "-stream_loop", "-1", "-i", str(bgm_file),
        "-filter_complex",
        "[1:a]volume=0.07,aloop=loop=-1:size=2e+09[bgm];[0:a]volume=1.0[voice];[voice][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]",
        "-map", "[aout]",
        "-c:a", "libmp3lame", "-b:a", "192k",
        str(final_sample_file)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if raw_tts_file.exists():
        raw_tts_file.unlink()
    print(f"-> HOAN TAT BAN NGHE THU: {final_sample_file} ({final_sample_file.stat().st_size} bytes)!")

asyncio.run(generate())
