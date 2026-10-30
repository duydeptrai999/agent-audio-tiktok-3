# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import get_story_cycle_22
from core.stories.cycles_31_to_40_masterpieces import get_story_cycle_32, get_story_cycle_36, get_story_cycle_40
from core.anti_repost_guard import PAST_SERIES_BLACKLIST, normalize_text

for fn, name in [(get_story_cycle_22, "cycle_22"), (get_story_cycle_32, "cycle_32"), (get_story_cycle_36, "cycle_36"), (get_story_cycle_40, "cycle_40")]:
    s = fn()
    t = s.get("title", "")
    words = sum(len(p.get("text", "").split()) for p in s.get("parts", []))
    norm = normalize_text(t)
    blacklisted = any(bl in norm for bl in PAST_SERIES_BLACKLIST)
    print(f"[{name}] {t} | Words: {words} | Blacklisted: {blacklisted}")
