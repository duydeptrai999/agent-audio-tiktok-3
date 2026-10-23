# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.cycles_31_to_40_masterpieces import CYCLE_31_TO_40_STORIES
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part as eval_21
from scripts.run_agent_scriptwriting_cycles_31_to_40 import agent_auditor_evaluate_part as eval_31

# Check Cycle 21 Part 3
s21 = CYCLE_21_TO_30_STORIES[21]()
p21_3 = s21['parts'][2]
res21 = eval_21(p21_3['full_text'], s21['genre'], 3)
print(f"Cycle 21 Part 3: score={res21['score']}, flaws={res21['flaws']}")

import re
sentences = re.split(r'[.!?]+', p21_3['full_text'])
for sent in sentences:
    clauses = re.split(r'[,:;—–\-]+', sent)
    for c in clauses:
        words = c.strip().split()
        if len(words) > 25:
            print(f"Long clause in C21P3 ({len(words)} words): '{c.strip()}'")

# Check Cycle 35 Part 1
s35 = CYCLE_31_TO_40_STORIES[35]()
p35_1 = s35['parts'][0]
res35 = eval_31(p35_1['full_text'], s35['genre'], 1)
print(f"Cycle 35 Part 1: score={res35['score']}, flaws={res35['flaws']}")

sents35 = [s.strip() for s in re.split(r'[.!?]+', p35_1['full_text']) if s.strip()]
print(f"C35P1 sent count: {len(sents35)}, avg length: {sum(len(s.split()) for s in sents35)/len(sents35):.2f}")
for s in sents35:
    if len(s.split()) > 20:
        print(f"  Long Sent ({len(s.split())} words): '{s}'")
