# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

text = 'Trên bàn đàm phán, kẻ yếu đuối rơi nước mắt chỉ nhận lại sự giẫm đạp không thương tiếc.'

async def test_p(pitch_val):
    try:
        kwargs = {"voice": "vi-VN-HoaiMyNeural", "rate": "+1%", "volume": "-15%"}
        if pitch_val is not None:
            kwargs["pitch"] = pitch_val
        comm = edge_tts.Communicate(text, **kwargs)
        await comm.save(f"test_p_{pitch_val}.mp3")
        print(f"Pitch {pitch_val}: SUCCESS")
    except Exception as e:
        print(f"Pitch {pitch_val}: FAILED ({e})")

async def main():
    for p in [None, "+0Hz", "-0Hz", "-1Hz", "-2Hz", "-5Hz", "+1Hz", "-1%", "-2%", "+1%"]:
        await test_p(p)

asyncio.run(main())
