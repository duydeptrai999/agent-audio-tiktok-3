# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.script_quality_gate import audit_and_optimize_part_text
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part

for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        opt_text, warns = audit_and_optimize_part_text(p['full_text'], s['title'], p['part_number'])
        r = agent_auditor_evaluate_part(opt_text, s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']}: score={r['score']}, flaws={r['flaws']}")
print("Audit check done!")
