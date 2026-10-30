# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import json
from core.stories.daily_story_factory import get_daily_10_series

series_list = get_daily_10_series("2026-10-28")
status = {
    "_meta": {
        "date": "2026-10-28",
        "last_published_timestamp": 0.0,
        "last_published_time_str": "",
        "last_series_completed_timestamp": 0.0
    }
}

for s in series_list:
    idx = s["slot_index"]
    key = s["key"]
    is_daytime = idx < 8
    status[key] = {
        "slot_index": idx,
        "title": s["title"],
        "part1": is_daytime,
        "part2": is_daytime,
        "part3": is_daytime,
        "produced": is_daytime
    }

status_file = ROOT / "data" / "daily_schedule_status_2026-10-28.json"
status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
print("Successfully initialized", status_file.name)
for k, v in status.items():
    if k != "_meta":
        print(f"Slot {v['slot_index']:02d}: {v['title'][:40]}... -> active: {not v['part1']}")
