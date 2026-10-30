# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.audio_engine import split_into_tts_chunks, sanitize_tts_text

series_list = get_daily_10_series("2026-10-25")
s6 = next(s for s in series_list if s["slot_index"] == 6)
p1_text = s6["parts"][0]["text"]
chunks = split_into_tts_chunks(p1_text, max_words=150)
c17 = chunks[17]

print(f"Chunk 17 words: {len(c17.split())}")
print("Chunk 17 raw:\n", repr(c17))
print("\nChunk 17 sanitized:\n", repr(sanitize_tts_text(c17)))
