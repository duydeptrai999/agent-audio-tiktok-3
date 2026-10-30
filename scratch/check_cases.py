import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/viral_full_100_cases.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total cases: {len(data)}")
for i, item in enumerate(data[:50]):
    ch = item.get('channel', 'Unknown')
    v = item.get('views', 0)
    lk = item.get('likes', 0)
    title = item.get('title', '')
    print(f"{i+1:02d}. [{ch}] ({v:,} views | {lk:,} likes) {title}")
