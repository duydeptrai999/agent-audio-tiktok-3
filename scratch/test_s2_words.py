# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

tests = [
    ("t1", "Các vị quan khách trong khán phòng khách sạn năm sao xì xào bàn tán."),
    ("t2", "Mọi người thi nhau lắc đầu trước sự việc của Lục gia."),
    ("t3", "chỉ trích sự bội bạc"),
    ("t4", "sự bội bạc của Lục gia"),
    ("t5", "chỉ trích"),
    ("t6", "bội bạc")
]

async def test_s(name, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural", rate="+5%")
        await comm.save(f"test_sub2_{name}.mp3")
        print(f"[{name}] SUCCESS")
    except Exception as e:
        print(f"[{name}] FAILED ({e})")

async def main():
    for name, s in tests:
        await test_s(name, s)

asyncio.run(main())
