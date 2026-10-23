import sys, os, re
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.detective_masterpiece import get_detective_masterpiece_story

s = get_detective_masterpiece_story()
for i, p in enumerate(s['parts']):
    text = p.get('full_text') or p.get('text', '')
    quotes = re.findall(r"['\"“]([^'\"”\n]+)['\"”]", text)
    long_s = [sub for q in quotes for sub in re.split(r'[.!?…]+', q) if len(sub.strip().split()) > 16]
    print(f"Part {i+1}: {len(quotes)} quotes, {len(long_s)} long clauses")
    for l in long_s[:2]:
        print("   ->", len(l.strip().split()), l.strip()[:60])
