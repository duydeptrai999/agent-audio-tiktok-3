# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from core.stories.doraemon import get_30min_doraemon_mystery_story
from core.audio_engine import split_into_tts_chunks

s = get_30min_doraemon_mystery_story()
for i, p in enumerate(s.get("parts", [])):
    txt = p.get("full_text") or p.get("text") or p.get("body") or ""
    print(f"Part {i+1} keys: {list(p.keys())}, text len: {len(txt.split())}")
    chunks = split_into_tts_chunks(txt)
    print(f"  Chunk 0: {repr(chunks[0][:100])}")
