# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.stories.daily_story_factory import get_daily_10_series

s5 = get_daily_10_series("2026-10-29")[4]
print("=== SLOT 5 (2026-10-29) ===")
print("Key:", s5["key"])
print("Prefix:", s5["prefix"])
print("Title:", s5["title"])
print("Genre:", s5.get("genre"), "| BGM Genre:", s5.get("bgm_genre"))
print("Voice:", s5.get("voice"))
print("Start time:", s5.get("start_time_str"))
for p in s5.get("parts", []):
    num = p["part_number"]
    badge = p.get("badge_label")
    w = len(p["text"].split())
    print(f"  Part {num}: {badge} ({w} words)")
