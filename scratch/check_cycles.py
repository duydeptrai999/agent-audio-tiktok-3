import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories import cycles_41_to_50_masterpieces as m
for attr in dir(m):
    if attr.startswith('get_story_'):
        s = getattr(m, attr)()
        lens = [len(p.get('text', '').split()) for p in s.get('parts', [])]
        print(f"{attr}: {s.get('title')} -> lens: {lens}, sum: {sum(lens)}")
