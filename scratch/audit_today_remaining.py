# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.stories.script_quality_gate import validate_story_series

sl = get_daily_10_series("2026-10-23")
for s in sl[4:]:
    print("=" * 60)
    print(f"Slot {s['slot_index']}: {s['title']} ({s['genre']})")
    for p in s["parts"]:
        words = len(p["text"].split())
        first_sentence = p["text"].split(".")[0][:120].strip()
        print(f"  Part {p['part_number']}: {words} words | Hook: {first_sentence}...")
