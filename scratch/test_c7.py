# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import edge_tts

text = 'Trên bàn đàm phán, kẻ yếu đuối rơi nước mắt chỉ nhận lại sự giẫm đạp không thương tiếc. Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật. Lục Diễm run rẩy lấy khăn tay lau mồ hôi trên trán, ánh mắt căm hận nhưng bất lực nhìn về phía tôi. Gió đêm từ dòng sông Nam Giang thổi qua ô cửa kính sát đất, mang theo hơi ẩm mằn mặn của cơn mưa đầu đông. Những năm tháng gian khó đã tôi luyện cho tôi một trái tim sắt đá, không còn chỗ cho lòng trắc ẩn mù quáng. Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật.'

async def test():
    print("Testing chunk 7 synthesis...")
    try:
        comm = edge_tts.Communicate(text, voice="vi-VN-HoaiMyNeural", rate="+1%", pitch="-1Hz", volume="-15%")
        await comm.save("test_chunk7.mp3")
        print("Success! File size:", Path("test_chunk7.mp3").stat().st_size)
    except Exception as e:
        print("Failed with error:", type(e), e)

asyncio.run(test())
