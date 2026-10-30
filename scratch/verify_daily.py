# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.daily_story_factory import get_daily_10_series

series = get_daily_10_series('2026-10-24')
print('=== DAILY 10 SERIES OVERVIEW (CODEX 8.1 REALISTIC SPOKEN) ===')
for i, s in enumerate(series):
    total_words = sum(len(p['text'].split()) for p in s['parts'])
    min_part = min(len(p['text'].split()) for p in s['parts'])
    slot = s.get('slot_index', i + 1)
    title = s['title']
    print(f"Slot {slot:02d}: {title[:48]:<48} | Words: {total_words:>5}w | Min: {min_part:>4}w")
