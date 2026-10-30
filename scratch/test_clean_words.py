# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

sentences_clean = [
    "Hạnh phúc đích thực không phải là sự đáp trả trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình.",
    "Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép.",
    "Bạch Thư Dao co rúm lại dưới chân bàn tiệc, chiếc trâm cài ngọc bích như lạnh buốt tâm can ả."
]

async def test_s(idx, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural")
        await comm.save(f"test_clean_{idx}.mp3")
        print(f"Clean Sentence {idx}: SUCCESS, size: {Path(f'test_clean_{idx}.mp3').stat().st_size}")
    except Exception as e:
        print(f"Clean Sentence {idx}: FAILED ({e})")

async def main():
    for i, s in enumerate(sentences_clean):
        await test_s(i, s)

asyncio.run(main())
