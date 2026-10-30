# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

tests = [
    ("s1_no_phapluat", "Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép."),
    ("s1_with_phapluat", "Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật."),
    ("s2_no_sheraton", "Các vị quan khách trong khán phòng khách sạn năm sao xì xào bàn tán, thi nhau lắc đầu trước sự việc của Lục gia."),
    ("s2_raw", "Các vị tài phiệt trong khán phòng khách sạn Sheraton xì xào bàn tán, thi nhau chỉ trích sự bội bạc của Lục gia.")
]

async def test_s(name, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural", rate="+5%")
        await comm.save(f"test_word_{name}.mp3")
        print(f"[{name}] SUCCESS")
    except Exception as e:
        print(f"[{name}] FAILED ({e})")

async def main():
    for name, s in tests:
        await test_s(name, s)

asyncio.run(main())
