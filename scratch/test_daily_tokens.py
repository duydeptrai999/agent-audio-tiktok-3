# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
series = get_daily_10_series(target_date='2026-10-25')
print(f"Generated {len(series)} series")
for s in series:
    token = s.get("consultation_token", "NONE")
    brief = s.get("knowledge_brief")
    bench = brief.get("relevant_cases", [{}])[0].get("title", "N/A") if brief else "N/A"
    print(f"  Slot {s['slot_index']:02d} ({s['genre']}): {s['title'][:35]}... -> Token: {token[:25]}... (Benchmark: {bench})")
