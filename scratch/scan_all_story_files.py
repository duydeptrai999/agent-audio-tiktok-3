import sys, os, glob, re
sys.path.insert(0, os.path.abspath('.'))
sys.stdout.reconfigure(encoding='utf-8')

story_files = sorted(glob.glob('core/stories/*_masterpiece.py'))
print(f"Checking {len(story_files)} masterpiece story files...")

for fpath in story_files:
    content = open(fpath, encoding='utf-8').read()
    quotes = re.findall(r"['\"“]([^'\"”\n]+)['\"”]", content)
    long_s = [sub.strip() for q in quotes for sub in re.split(r'[.!?…]+', q) if len(sub.strip().split()) > 16]
    if long_s:
        fname = os.path.basename(fpath)
        print(f"{fname}: {len(long_s)} long clauses (> 16 words)")
        for item in long_s[:2]:
            print(f"   -> [{len(item.split())}w] {item[:65]}...")
