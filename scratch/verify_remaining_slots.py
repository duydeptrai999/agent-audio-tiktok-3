# -*- coding: utf-8 -*-
import sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series
from core.stories.script_quality_gate import validate_story_series
from core.voice_profiles import get_voice_profile_for_genre

date_str = "2026-10-25"
series_list = get_daily_10_series(date_str)

remaining_slots = [s for s in series_list if s["slot_index"] in [7, 8, 9, 10]]

print(f"Kiểm tra 4 bộ audio còn lại cho ngày {date_str}:")
for s in remaining_slots:
    print("=" * 60)
    print(f"Slot {s['slot_index']}: {s['title']}")
    print(f"  Thể loại: {s['genre']}")
    prof = get_voice_profile_for_genre(s['genre'])
    print(f"  Voice Profile: {prof.display_name} ({prof.voice_name}) | Rate: {prof.rate} | Vol: {prof.volume}")
    
    validated = validate_story_series(s)
    passed = validated.get("quality_audit_passed", False)
    print(f"  Quality Gate: {'PASS ✅' if passed else 'FAIL ❌'}")
    
    total_words = 0
    for p in validated["parts"]:
        wc = len(p["text"].split())
        total_words += wc
        print(f"    - Tập {p['part_number']}: {wc} từ (Badge: {p['badge_label']})")
    print(f"  Tổng số từ: {total_words} từ")
