# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

tests = [
    ("chê trách", "Các vị quan khách lắc đầu chê trách hành động vô ơn."),
    ("bất bình", "Các vị quan khách thi nhau bày tỏ sự bất bình trước việc làm của Lục gia."),
    ("công lý", "Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng của lẽ phải và công lý.")
]

async def test_s(name, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural", rate="+5%")
        await comm.save(f"test_sub3_{name}.mp3")
        print(f"[{name}] SUCCESS")
    except Exception as e:
        print(f"[{name}] FAILED ({e})")

async def main():
    for name, s in tests:
        await test_s(name, s)

asyncio.run(main())
