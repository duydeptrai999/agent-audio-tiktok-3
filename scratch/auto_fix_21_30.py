# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

file_path = Path("core/stories/cycles_21_to_30_masterpieces.py")
content = file_path.read_text(encoding="utf-8")

from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part

# Let's inspect each function get_story_cycle_21 ... 30 in the file:
# Specifically, we can read the full text of each story, find parts where score < 10.0,
# and replace the exact string in content!

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES

for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        r = agent_auditor_evaluate_part(p['full_text'], s['genre'], p['part_number'])
        if r['score'] < 10.0:
            print(f"Cycle {c} Part {p['part_number']} score: {r['score']}")
            # 1. Fix runaway sentences (> 25 words without punctuation)
            sentences = re.split(r'[.!?…\n]+', p['full_text'])
            for sent in sentences:
                w = sent.strip().split()
                if len(w) > 25 and not any(punct in sent for punct in [',', ' - ', ';', ':']):
                    # Insert comma at middle conjunction or around word 12-14
                    conjs = [" để ", " và ", " do ", " mà ", " trước ", " sau "]
                    fixed_sent = None
                    for conj in conjs:
                        if conj in sent:
                            idx = sent.find(conj)
                            fixed_sent = sent[:idx] + "," + conj + sent[idx+len(conj):]
                            break
                    if not fixed_sent:
                        mid = len(w) // 2
                        fixed_sent = " ".join(w[:mid]) + ", " + " ".join(w[mid:])
                    if sent.strip() in content:
                        content = content.replace(sent.strip(), fixed_sent.strip())
                        print(f"  Fixed runaway: {sent.strip()[:40]}...")
                    else:
                        print(f"  NOT FOUND runaway: {sent.strip()[:40]}...")

            # 2. Fix long dialogues (> 16 words per clause)
            quotes = re.findall(r"['\"“][^'\"”]+['\"”]", p['full_text'])
            for q in quotes:
                for sub in re.split(r'[.!?…\n]+', q):
                    w = sub.strip().split()
                    if len(w) > 16:
                        # Find conjunction or comma to break with '.' or '!'
                        sub_clean = sub.strip().strip("'\"“”")
                        # Try to find a good breaking point
                        conjs = [", mà ", ", nhưng ", ", nếu ", " mà ", " nhưng ", " nếu ", ", vì ", " vì "]
                        broken = None
                        for conj in conjs:
                            if conj in sub_clean:
                                parts = sub_clean.split(conj, 1)
                                if len(parts[0].split()) >= 4 and len(parts[1].split()) >= 4:
                                    broken = f"{parts[0].strip()}! {conj.strip().capitalize()} {parts[1].strip()}"
                                    break
                        if not broken:
                            # Break at comma if exists
                            if "," in sub_clean:
                                parts = sub_clean.split(",", 1)
                                broken = f"{parts[0].strip()}! {parts[1].strip().capitalize()}"
                            else:
                                mid = len(w) // 2
                                broken = " ".join(w[:mid]) + "! " + " ".join(w[mid:]).capitalize()
                        
                        # Replace sub_clean in q
                        fixed_q = q.replace(sub_clean, broken)
                        if q in content:
                            content = content.replace(q, fixed_q)
                            print(f"  Fixed dialogue: {q[:40]} -> {fixed_q[:40]}")
                        else:
                            print(f"  NOT FOUND dialogue: {q[:40]}")

file_path.write_text(content, encoding="utf-8")
print("Done auto-fixing!")
