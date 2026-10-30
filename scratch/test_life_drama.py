# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.life_drama import get_30min_life_drama_story
from core.stories.script_quality_gate import validate_story_series

s = get_30min_life_drama_story()
print("Title:", s["title"])
lens = [len(p["full_text"].split()) for p in s["parts"]]
print("Part lengths:", lens, "Total words:", sum(lens))
res = validate_story_series(s)
print("Quality Gate Passed:", res.get("passed"))
print("Quality Gate Warnings count:", len(res.get("warnings", [])))
if res.get("warnings"):
    for w in res.get("warnings")[:5]:
        print("  -", w)
