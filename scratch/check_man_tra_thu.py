import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.man_tra_thu_da_nhat_doi_toi_masterpiece import get_man_tra_thu_masterpiece_story
s = get_man_tra_thu_masterpiece_story()
print('Title:', s['title'])
print('Parts:', len(s['parts']))
for p in s['parts']:
    words = len(p['full_text'].split())
    print(f"Part {p['part_number']}: {words} words | Hook: {p.get('hook', '')[:80]}...")
