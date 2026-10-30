# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.audio_engine import sanitize_tts_text
import edge_tts

raw_text = 'Hạnh phúc đích thực không phải là sự đáp trả trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình. Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật. Các vị tài phiệt trong khán phòng khách sạn Sheraton xì xào bàn tán, thi nhau chỉ trích sự bội bạc của Lục gia. Ánh đèn chùm pha lê rọi xuống những tia sáng lấp lánh lên tà váy nhung đỏ rực rỡ như một đóa hồng kiêu hãnh. Hạnh phúc đích thực không phải là sự đáp trả trong hả hê, mà là sự thanh thản khi tìm lại được chính bản thân mình. Mọi toan tính xấu xa cuối cùng đều phải phơi bày dưới ánh sáng công lý đanh thép của pháp luật.'

text = sanitize_tts_text(raw_text)

async def test():
    print("Testing c17 with rate=+5%...")
    try:
        comm = edge_tts.Communicate(text, voice="vi-VN-HoaiMyNeural", rate="+5%")
        await comm.save("test_c17_rate5.mp3")
        print("Success! Size:", Path("test_c17_rate5.mp3").stat().st_size)
    except Exception as e:
        print("Failed:", type(e), e)

asyncio.run(test())
