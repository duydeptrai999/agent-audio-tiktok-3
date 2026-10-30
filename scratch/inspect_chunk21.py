# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.audio_engine import split_into_tts_chunks

series_list = get_daily_10_series("2026-10-25")
s6 = next(s for s in series_list if s["slot_index"] == 6)
p1_text = s6["parts"][0]["text"]

chunks = split_into_tts_chunks(p1_text, max_words=150)
print(f"Total chunks: {len(chunks)}")
if len(chunks) > 21:
    print(f"Chunk 21 words: {len(chunks[21].split())}")
    print("Chunk 21 content:\n", repr(chunks[21]))
