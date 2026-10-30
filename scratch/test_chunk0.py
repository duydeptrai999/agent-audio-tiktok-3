# -*- coding: utf-8 -*-
import sys
import asyncio
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

import edge_tts
from core.stories.doraemon import get_30min_doraemon_mystery_story
from core.audio_engine import split_into_tts_chunks

s = get_30min_doraemon_mystery_story()
p2_text = s['parts'][1]['full_text']
chunks = split_into_tts_chunks(p2_text)
chunk0 = chunks[0]
print("Testing chunk 0 len:", len(chunk0.split()), "words")

async def test():
    try:
        comm = edge_tts.Communicate(chunk0, voice="vi-VN-NamMinhNeural", rate="-2%")
        out = Path("scratch/test_doraemon_chk0.mp3")
        await comm.save(str(out))
        print(f"SUCCESS! Output size: {out.stat().st_size} bytes")
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}")

asyncio.run(test())
