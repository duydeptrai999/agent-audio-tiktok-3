import sys, os, re
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.detective_masterpiece import get_detective_masterpiece_story
from core.stories.script_quality_gate import audit_and_optimize_part_text

s = get_detective_masterpiece_story()
p2_raw = s['parts'][1].get('full_text') or s['parts'][1].get('text', '')

cleaned, warns = audit_and_optimize_part_text(p2_raw, "Test", 2)
quotes = re.findall(r"['\"“]([^'\"”\n]+)['\"”]", cleaned)
long_s = [sub.strip() for q in quotes for sub in re.split(r'[.!?…]+', q) if len(sub.strip().split()) > 16]
print("Warns count:", len(warns))
for w in warns:
    if "dao găm" in w:
        print(" ->", w)
print(f"Remaining long sentences in cleaned: {len(long_s)}")
for item in long_s:
    print(f"  [{len(item.split())}w] {item}")
