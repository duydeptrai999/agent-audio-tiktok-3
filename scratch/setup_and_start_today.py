# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import json
from datetime import datetime
from core.stories.daily_story_factory import get_daily_10_series

target_date = "2026-10-29"
series_list = get_daily_10_series(target_date)

status = {
    "_meta": {
        "date": target_date,
        "last_published_timestamp": 0.0,
        "last_published_time_str": "",
        "last_series_completed_timestamp": 0.0
    }
}

for s in series_list:
    idx = s["slot_index"]
    key = s["key"]
    # Slots 1-4 (06:30, 08:20, 10:10, 12:00) đã qua khung giờ sáng
    is_morning_past = idx < 5
    status[key] = {
        "slot_index": idx,
        "title": s["title"],
        "part1": is_morning_past,
        "part2": is_morning_past,
        "part3": is_morning_past,
        "produced": is_morning_past
    }

status_file = ROOT / "data" / f"daily_schedule_status_{target_date}.json"
status_file.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"✅ Đã khởi tạo {status_file.name}:")
for k, v in status.items():
    if k != "_meta":
        state_str = "⏭️ ĐÃ QUA GIỜ SÁNG" if v["part1"] else "🎯 ACTIVE LÊN LỊCH CHIỀU TỐI NAY"
        print(f"  Slot {v['slot_index']:02d}: {v['title'][:45]}... [{state_str}]")

# Dọn dẹp lock cũ
for lock_p in [ROOT / "data" / ".autopilot.lock", ROOT / "data" / ".coccoc_publisher.lock"]:
    if lock_p.exists():
        try:
            lock_p.unlink(missing_ok=True)
            print(f"🧹 Đã xóa lock cũ: {lock_p.name}")
        except Exception as e:
            print(f"⚠️ Không thể xóa lock {lock_p.name}: {e}")
