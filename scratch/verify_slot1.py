import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.stdout.reconfigure(encoding='utf-8')
from core.stories.daily_story_factory import get_daily_10_series

series = get_daily_10_series('2026-10-27')
s1 = series[0]
print("Title:", s1['title'])
print("Genre:", s1['genre'])
print("Voice:", s1['voice'])
print("Hour:", s1['hour'], "Minute:", s1['minute'])
for p in s1['parts']:
    w = len(p['text'].split())
    print(f"Part {p['part_number']}: {w} words | Snippet: {p['text'][:120]}...")
