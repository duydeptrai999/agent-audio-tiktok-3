import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
sys.stdout.reconfigure(encoding='utf-8')

from core.stories.daily_story_factory import SLOT_STORY_CATALOG

print(f"Total slots in catalog: {len(SLOT_STORY_CATALOG)}")
for slot, loaders in SLOT_STORY_CATALOG.items():
    print(f"\nSlot {slot:02d}: {len(loaders)} story loaders available")
    for fn in loaders:
        try:
            story = fn()
            parts = story.get('parts', [])
            words = [len(p.get('full_text', '').split()) for p in parts]
            title = story.get('title', 'Unknown')
            total = sum(words)
            min_w = min(words) if words else 0
            status = "PASS" if min_w >= 1200 and total >= 4000 else "WARN"
            print(f"   [{status}] {title[:45]} | Parts: {len(parts)} | Total: {total}w (Min Part: {min_w}w)")
        except Exception as e:
            print(f"   [ERROR] in {fn.__name__}: {e}")
