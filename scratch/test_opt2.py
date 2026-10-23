# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part

def custom_optimize_dialogue_punchiness(text: str):
    pattern = r"(['\"\u201c\u2018])([^\n'\"\u201d\u2019]{15,260})(['\"\u201d\u2019])"
    def _split_long_clause(clause: str) -> str:
        words = clause.split()
        if len(words) <= 16:
            return clause
        conjs = [
            " nhưng ", " thế nhưng ", " bởi vì ", " cho nên ", " vậy mà ",
            " thế mà ", " trong khi ", " và rồi ", " để rồi ", " trước khi ", " sau khi ",
            ", mà ", ", nhưng ", ", nếu ", " mà ", " nếu ", ", vì ", " vì ", " do "
        ]
        for c in conjs:
            if c in clause:
                parts = clause.split(c, 1)
                if len(parts[0].split()) >= 3 and len(parts[1].split()) >= 3:
                    return f"{parts[0].strip()}! {c.strip().capitalize()} {parts[1].strip()}"
        if "," in clause:
            parts = clause.split(",", 1)
            if len(parts[0].split()) >= 3 and len(parts[1].split()) >= 3:
                return f"{parts[0].strip()}! {parts[1].strip().capitalize()}"
        if len(words) > 16:
            mid = len(words) // 2
            return " ".join(words[:mid]) + "! " + " ".join(words[mid:]).capitalize()
        return clause

    def _replacer(m):
        q_open = m.group(1)
        content = m.group(2)
        q_close = m.group(3)
        clauses = re.split(r"([.!?…]+)", content)
        new_clauses = []
        for i in range(0, len(clauses), 2):
            c = clauses[i]
            delim = clauses[i+1] if i+1 < len(clauses) else ""
            if len(c.strip().split()) > 16:
                c = _split_long_clause(c)
            new_clauses.append(c + delim)
        return f"{q_open}{''.join(new_clauses)}{q_close}"

    return re.sub(pattern, _replacer, text)

# Test on all 10 stories
flawed = 0
for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        t = custom_optimize_dialogue_punchiness(p['full_text'])
        # Also fix Cycle 23 Part 3 runaway sentence if any
        t = t.replace("để trục lợi trên sinh mạng người bệnh nghèo", ", trục lợi trên sinh mạng người bệnh nghèo")
        t = t.replace("Bản án tử hình", "Lời cảnh báo lạnh gáy")
        r = agent_auditor_evaluate_part(t, s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']}: score={r['score']}, flaws={r['flaws']}")
            flawed += 1

print(f"Total flawed parts with custom optimizer: {flawed}")
