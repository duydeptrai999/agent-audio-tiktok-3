# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

text = 'Ánh đèn chùm pha lê rọi xuống những tia sáng lấp lánh lên tà váy nhung đỏ rực rỡ như một đóa hồng kiêu hãnh.'

async def test_r(rate_val):
    try:
        kwargs = {"voice": "vi-VN-HoaiMyNeural"}
        if rate_val is not None:
            kwargs["rate"] = rate_val
        comm = edge_tts.Communicate(text, **kwargs)
        await comm.save(f"test_rate_{rate_val}.mp3")
        print(f"Rate {rate_val}: SUCCESS")
    except Exception as e:
        print(f"Rate {rate_val}: FAILED ({e})")

async def main():
    for r in [None, "+0%", "+1%", "+2%", "+5%", "+8%", "-1%", "-2%", "-5%", "+10%"]:
        await test_r(r)

asyncio.run(main())
