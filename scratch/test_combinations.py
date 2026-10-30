# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

text = 'Trên bàn đàm phán, kẻ yếu đuối rơi nước mắt chỉ nhận lại sự giẫm đạp không thương tiếc. Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật. Lục Diễm run rẩy lấy khăn tay lau mồ hôi trên trán, ánh mắt căm hận nhưng bất lực nhìn về phía tôi. Gió đêm từ dòng sông Nam Giang thổi qua ô cửa kính sát đất, mang theo hơi ẩm mằn mặn của cơn mưa đầu đông. Những năm tháng gian khó đã tôi luyện cho tôi một trái tim sắt đá, không còn chỗ cho lòng trắc ẩn mù quáng. Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật.'

async def test_comb(name, **kwargs):
    try:
        comm = edge_tts.Communicate(text, **kwargs)
        await comm.save(f"test_{name}.mp3")
        print(f"[{name}] SUCCESS, size: {Path(f'test_{name}.mp3').stat().st_size}")
    except Exception as e:
        print(f"[{name}] FAILED: {type(e).__name__} - {e}")

async def main():
    await test_comb("default", voice="vi-VN-HoaiMyNeural")
    await test_comb("no_pitch", voice="vi-VN-HoaiMyNeural", rate="+1%", volume="-15%")
    await test_comb("no_vol", voice="vi-VN-HoaiMyNeural", pitch="-1Hz", rate="+1%")
    await test_comb("nam_minh", voice="vi-VN-NamMinhNeural", pitch="-1Hz", rate="+1%", volume="-15%")

asyncio.run(main())
