# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

sentences = [
    "Hạnh phúc đích thực không phải là sự đáp trả trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình.",
    "Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật.",
    "Các vị tài phiệt trong khán phòng khách sạn Sheraton xì xào bàn tán, thi nhau chỉ trích sự bội bạc của Lục gia.",
    "Các vị tài phiệt trong khán phòng khách sạn năm sao xì xào bàn tán, thi nhau chỉ trích sự bội bạc của Lục gia.",
    "Ánh đèn chùm pha lê rọi xuống những tia sáng lấp lánh lên tà váy nhung đỏ rực rỡ như một đóa hồng kiêu hãnh."
]

async def test_s(idx, s):
    try:
        comm = edge_tts.Communicate(s, voice="vi-VN-HoaiMyNeural", rate="+1%")
        await comm.save(f"test_s17_{idx}.mp3")
        print(f"Sentence {idx}: SUCCESS")
    except Exception as e:
        print(f"Sentence {idx}: FAILED ({e})")

async def main():
    for i, s in enumerate(sentences):
        await test_s(i, s)

asyncio.run(main())
