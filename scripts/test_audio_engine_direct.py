# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")
import asyncio
from pathlib import Path
from core.audio_engine import generate_cinema_tts_audio

async def main():
    out = Path("assets/audio/test_direct_ae.mp3")
    text = "Vừa sinh mổ ngày thứ hai, mẹ chồng đứng ngoài hành lang bảo lại là vịt trời."
    print("Calling generate_cinema_tts_audio...")
    try:
        res = await generate_cinema_tts_audio(
            text=text,
            voice="vi-VN-HoaiMyNeural",
            output_path=out,
            target_speed=1.05
        )
        print("Success! Generated:", res, "Size:", res.stat().st_size)
    except Exception as e:
        import traceback
        traceback.print_exc()

asyncio.run(main())
