# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import edge_tts

text = 'Hạnh phúc đích thực không phải là sự trả thù trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình. Mọi toan tính bẩn thỉu cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật. Bạch Thư Dao co rúm lại dưới chân bàn tiệc, chiếc trâm cài ngọc bích như thiêu đốt da thịt ả. Tiếng nhạc khiêu vũ du dương bỗng im bặt, nhường chỗ cho một sự im lặng nghẹt thở bao trùm khắp đại sảnh.'

async def main():
    print("Testing chunk 21 with rate=+1% and no pitch/volume...")
    comm = edge_tts.Communicate(text, voice='vi-VN-HoaiMyNeural', rate='+1%')
    await comm.save('test_c21.mp3')
    print("Success! Size:", Path('test_c21.mp3').stat().st_size)

asyncio.run(main())
