# -*- coding: utf-8 -*-
import sys
import io
import asyncio
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.audio_engine import split_into_tts_chunks
import edge_tts

series_list = get_daily_10_series("2026-10-25")
s6 = next(s for s in series_list if s["slot_index"] == 6)
p1_text = s6["parts"][0]["text"]
chunks = split_into_tts_chunks(p1_text, max_words=150)
c21 = chunks[21]

print("Chunk 21 length:", len(c21))
print("Content:", c21)

async def test():
    try:
        comm = edge_tts.Communicate(c21, voice="vi-VN-HoaiMyNeural")
        await comm.save("test_exact_c21.mp3")
        print("Success! Size:", Path("test_exact_c21.mp3").stat().st_size)
    except Exception as e:
        print("Failed:", type(e), e)

asyncio.run(test())
