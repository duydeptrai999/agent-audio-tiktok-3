import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('core/stories/*.py') + ['core/narrative_master_library.py']):
    text = open(f, encoding='utf-8', errors='ignore').read()
    quotes = re.findall(r"['\"“]([^'\"”\n]+)['\"”]", text)
    long_q = [q for q in quotes if len(q.split()) > 20]
    if long_q:
        print(f"{f}: {len(long_q)} long dialogues (> 20 words)")
        for q in long_q[:2]:
            print(f"   -> [{len(q.split())} words] {q[:80]}...")
