# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_41_to_50_masterpieces import CYCLE_41_TO_50_STORIES
from scripts.run_agent_scriptwriting_cycles_41_to_50 import agent_auditor_evaluate_part

print("--- DETAILED AUDIT FOR CYCLES 41-50 ---")
for c in range(41, 51):
    s = CYCLE_41_TO_50_STORIES[c]()
    for p in s['parts']:
        r = agent_auditor_evaluate_part(p['full_text'], s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']} (Score: {r['score']}):")
            for fl in r['flaws']:
                print(f"   Flaw: {fl}")
            if "THOAI_DAI_DONG" in str(r['flaws']):
                quotes = re.findall(r"['\"“][^'\"”]+['\"”]", p['full_text'])
                for q in quotes:
                    if len(q.split()) > 18:
                        print(f"     Long Quote ({len(q.split())}w): {q}")
            if "CAU_QUA_DAI" in str(r['flaws']):
                sents = [st.strip() for st in re.split(r'[.!?]+', p['full_text']) if len(st.strip().split()) > 3]
                print(f"     Sent count: {len(sents)}, avg: {sum(len(x.split()) for x in sents)/len(sents):.1f}")
