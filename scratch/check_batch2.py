# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from core.stories.batch2_5_masterpieces import BATCH2_5_SERIES_DATA
for s in BATCH2_5_SERIES_DATA:
    lens = [len(p['text'].split()) for p in s['parts']]
    print(f"Title: {s['title']}")
    print(f"Genre: {s['genre']} | Parts: {lens} | Total: {sum(lens)} words\n")
