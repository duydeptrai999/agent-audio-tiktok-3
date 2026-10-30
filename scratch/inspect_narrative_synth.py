# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('core/narrative_synthesizer.py', 'r', encoding='utf-8') as f:
    text = f.read()

genres = re.findall(r'"([A-Z_]+)":\s*\{', text)
print('Genres in narrative_synthesizer:', genres)

for g in genres:
    pos = text.find(f'"{g}":')
    preview = text[pos:pos+300]
    print(f"\n--- {g} preview ---")
    print(preview[:200])
