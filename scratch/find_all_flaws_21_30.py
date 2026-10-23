# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part

for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        r = agent_auditor_evaluate_part(p['full_text'], s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"=== Cycle {c} Part {p['part_number']} (Score: {r['score']}) ===")
            for fl in r['flaws']:
                print(f"  Flaw: {fl}")
            # print long dialogues
            quotes = re.findall(r"['\"“][^'\"”]+['\"”]", p['full_text'])
            for q in quotes:
                for sub in re.split(r'[.!?…\n]+', q):
                    w = sub.strip().split()
                    if len(w) > 16:
                        print(f"    Long dialogue ({len(w)}w): {q}")
            # print runaway sentences
            sentences = re.split(r'[.!?…\n]+', p['full_text'])
            runaway = [sent for sent in sentences if len(sent.split()) > 25 and not any(punct in sent for punct in [',', ' - ', ';', ':'])]
            for sent in runaway:
                print(f"    Runaway sent ({len(sent.split())}w): {sent.strip()}")
