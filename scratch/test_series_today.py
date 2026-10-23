# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.stories.script_quality_gate import validate_story_series

series_list = get_daily_10_series("2026-10-23")
print("Total series:", len(series_list))
for s in series_list:
    validated = validate_story_series(s)
    print(f"Slot {s['slot_index']} [{s['start_time_str']}]: {s['title']} | Parts: {len(s['parts'])}")
