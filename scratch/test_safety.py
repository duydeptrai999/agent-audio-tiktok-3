# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

sentences = [
    "Hạnh phúc đích thực không phải là sự trả thù trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình.",
    "Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật.",
    "Bạch Thư Dao co rúm lại dưới chân bàn tiệc, chiếc trâm cài ngọc bích như thiêu đốt da thịt ả.",
    "Tiếng nhạc khiêu vũ du dương bỗng im bặt, nhường chỗ cho một sự im lặng nghẹt thở bao trùm khắp đại sảnh."
]

async def test_s(idx, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural")
        await comm.save(f"test_s_{idx}.mp3")
        print(f"Sentence {idx}: SUCCESS")
    except Exception as e:
        print(f"Sentence {idx}: FAILED ({e}) - Text: {s}")

async def main():
    for i, s in enumerate(sentences):
        await test_s(i, s)

asyncio.run(main())
