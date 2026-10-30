# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from core.stories.cung_dau_duoc_dien_masterpiece import get_cung_dau_duoc_dien_masterpiece_story
s = get_cung_dau_duoc_dien_masterpiece_story()
for p in s['parts']:
    print(f"Part {p['part_number']}: {len(p['text'].split())} words")
