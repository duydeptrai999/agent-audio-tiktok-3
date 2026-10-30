# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import core.stories.daily_story_factory as dsf

print("Scanning all functions in dsf.SLOT_STORY_CATALOG with full text extraction:")
for slot, funcs in dsf.SLOT_STORY_CATALOG.items():
    print(f"\n--- SLOT {slot} ---")
    for fn in funcs:
        try:
            s = fn()
            parts = s.get("parts", [])
            lens = []
            if isinstance(parts, list) and parts:
                for p in parts:
                    txt = p.get("full_text") or p.get("text") or p.get("body") or ""
                    lens.append(len(txt.split()))
            elif isinstance(parts, dict):
                lens = [len(parts.get(f"part{i}", "").split()) for i in (1, 2, 3)]
            else:
                lens = [len(s.get(f"part{i}", "").split()) for i in (1, 2, 3)]
            print(f"  * Title: {s.get('title')}")
            print(f"    Genre: {s.get('genre')} | Parts: {lens} | Total: {sum(lens)} words")
        except Exception as e:
            print(f"  * Error loading {fn}: {e}")
