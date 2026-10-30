# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.life_mother_in_law import get_30min_mother_in_law_story
from core.stories.script_quality_gate import validate_story_series

s = get_30min_mother_in_law_story()
print("Title:", s["title"])
lens = [len(p["full_text"].split()) for p in s["parts"]]
print("Part lengths:", lens, "Total words:", sum(lens))
res = validate_story_series(s)
print("Quality Gate Passed:", res.get("passed"))
print("Quality Gate Warnings:", res.get("warnings", []))
