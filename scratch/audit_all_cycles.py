# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.cycles_31_to_40_masterpieces import CYCLE_31_TO_40_STORIES
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part as eval_21
from scripts.run_agent_scriptwriting_cycles_31_to_40 import agent_auditor_evaluate_part as eval_31

print("--- AUDITING CYCLES 21-30 ---")
for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        r = eval_21(p['full_text'], s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']}: score={r['score']}, flaws={r['flaws']}")
            import re
            sentences = re.split(r'[.!?]+', p['full_text'])
            for sent in sentences:
                clauses = re.split(r'[,:;—–\-]+', sent)
                for cl in clauses:
                    words = cl.strip().split()
                    if len(words) > 25:
                        print(f"   Clause ({len(words)}w): '{cl.strip()}'")

print("--- AUDITING CYCLES 31-40 ---")
for c in range(31, 41):
    s = CYCLE_31_TO_40_STORIES[c]()
    for p in s['parts']:
        r = eval_31(p['full_text'], s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']}: score={r['score']}, flaws={r['flaws']}")
