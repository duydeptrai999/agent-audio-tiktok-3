# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")
import json
from pathlib import Path
from core.daily_schedule_config import DAILY_10_SLOTS
from core.stories.daily_story_factory import get_daily_10_series

print("=== DANH SÁCH 10 SLOTS HẰNG NGÀY ===")
for s in DAILY_10_SLOTS:
    print(f"Slot {s['slot_index']}: {s['start_time_str']} - [{s['genre']}] - {s.get('vibe', '')}")

today = "2026-10-24"
tomorrow = "2026-10-25"

print(f"\n=== DANH SÁCH TRUYỆN HÔM NAY ({today}) ===")
series_today = get_daily_10_series(today)
for s in series_today:
    print(f"Slot {s['slot_index']}: [{s['genre']}] {s['title']}")

print(f"\n=== DANH SÁCH TRUYỆN NGÀY MAI ({tomorrow}) ===")
series_tomorrow = get_daily_10_series(tomorrow)
for s in series_tomorrow:
    print(f"Slot {s['slot_index']}: [{s['genre']}] {s['title']}")

# Kiểm tra status files
status_file_today = Path(f"data/daily_schedule_status_{today}.json")
status_file_tomorrow = Path(f"data/daily_schedule_status_{tomorrow}.json")
print(f"\nStatus today exists: {status_file_today.exists()}")
print(f"Status tomorrow exists: {status_file_tomorrow.exists()}")
