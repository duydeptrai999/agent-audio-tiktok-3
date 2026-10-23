import os
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.stories.daily_story_factory import get_daily_10_series

series_list = get_daily_10_series("2026-10-20")
for s in series_list:
    idx = s["slot_index"]
    title = s["title"]
    counts = [len(p["text"].split()) for p in s["parts"]]
    print(f"Slot {idx:02d}: {title[:40]}... -> Words: {counts}")
