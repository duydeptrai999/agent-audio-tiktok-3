# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.sa_dieu_tieng_long_masterpiece import get_sa_dieu_tieng_long_masterpiece_story
from core.stories.script_quality_gate import validate_story_series

s = get_sa_dieu_tieng_long_masterpiece_story()
print("Title:", s["title"])
lens = [len(p["full_text"].split()) for p in s["parts"]]
print("Part lengths:", lens, "Total words:", sum(lens))
res = validate_story_series(s)
print("Quality Gate Passed:", res.get("passed"))
print("Quality Gate Warnings count:", len(res.get("warnings", [])))
if res.get("warnings"):
    for w in res.get("warnings")[:5]:
        print("  -", w)
