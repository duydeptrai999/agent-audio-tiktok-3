import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/viral_full_100_cases.json', 'r', encoding='utf-8') as f:
    cases = json.load(f)

print(f"Total analyzed cases: {len(cases)}")

channels = Counter([c.get('channel', 'Unknown') for c in cases])
print("\n--- TOP CHANNELS ---")
for ch, count in channels.most_common(15):
    print(f"  {ch}: {count} videos")

print("\n--- SAMPLE 15 VIRAL CASES WITH HOOKS & THEMES ---")
for i, c in enumerate(cases[:15]):
    title = c.get('title', '')
    views = c.get('views', 0)
    hook = c.get('opening_hook', c.get('hook', ''))
    print(f"#{i+1:02d} | [{c.get('channel')}] | Views: {views:,}")
    print(f"     Title: {title}")
    if hook:
        print(f"     Hook: {hook[:120]}...")
    print()
