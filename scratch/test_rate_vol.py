# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

text = 'Trên bàn đàm phán, kẻ yếu đuối rơi nước mắt chỉ nhận lại sự giẫm đạp không thương tiếc.'

async def test_rv(rate, vol):
    try:
        comm = edge_tts.Communicate(text, voice="vi-VN-HoaiMyNeural", rate=rate, volume=vol)
        await comm.save(f"test_rv_{rate}_{vol}.mp3")
        print(f"Rate {rate}, Vol {vol}: SUCCESS, size: {Path(f'test_rv_{rate}_{vol}.mp3').stat().st_size}")
    except Exception as e:
        print(f"Rate {rate}, Vol {vol}: FAILED ({e})")

async def main():
    await test_rv("+0%", "-15%")
    await test_rv("+1%", "-15%")
    await test_rv("-2%", "-18%")
    await test_rv("+3%", "-14%")
    await test_rv("-4%", "-14%")

asyncio.run(main())
