# -*- coding: utf-8 -*-
import sys
import io
import json
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.daily_story_factory import get_daily_10_series

series_list = get_daily_10_series("2026-10-25")
s4 = next(s for s in series_list if s["slot_index"] == 4)
s5 = next(s for s in series_list if s["slot_index"] == 5)

print("Slot 4 Title:", s4["title"])
print("Slot 4 Genre:", s4.get("genre"))
print("Slot 4 Voice:", s4.get("voice"))
print("Slot 4 Parts words:", [len(p["text"].split()) for p in s4["parts"]])

print("\nSlot 5 Title:", s5["title"])
print("Slot 5 Genre:", s5.get("genre"))
print("Slot 5 Voice:", s5.get("voice"))
print("Slot 5 Parts words:", [len(p["text"].split()) for p in s5["parts"]])
