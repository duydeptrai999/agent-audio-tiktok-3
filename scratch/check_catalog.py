import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.daily_story_factory import SLOT_STORY_CATALOG, get_published_titles_set, normalize_text

pub = get_published_titles_set()
for slot_idx, loaders in SLOT_STORY_CATALOG.items():
    print(f"\n--- SLOT {slot_idx} ({len(loaders)} stories) ---")
    for fn in loaders:
        s = fn()
        title = s.get('title')
        parts = s.get('parts', [])
        lens = [len(p.get('text', '').split()) for p in parts]
        is_pub = normalize_text(title) in pub
        print(f"  * {title} | Total words: {sum(lens)} (parts: {lens}) | Already published: {is_pub}")
