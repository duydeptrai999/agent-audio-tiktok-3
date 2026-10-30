# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.stories.daily_story_factory import get_daily_10_series
import json

series = get_daily_10_series("2026-10-28")
print(f"Total series for 2026-10-28: {len(series)}")
for s in series:
    idx = s.get("slot_index")
    key = s.get("key")
    t_str = s.get("start_time_str")
    title = s.get("title")
    voice = s.get("voice")
    genre = s.get("genre")
    print(f"Slot {idx:02d} ({t_str}): [{genre}] {title} ({voice})")

status_p = ROOT / "data" / "daily_schedule_status_2026-10-28.json"
print("\nStatus file exists:", status_p.exists())
if status_p.exists():
    print(status_p.read_text(encoding="utf-8"))
