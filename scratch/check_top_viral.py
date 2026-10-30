import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/top_viral_deep_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total top viral deep analysis: {len(data)}")
for i, item in enumerate(data[:10]):
    print(f"#{i+1}: {item.get('title')} ({item.get('views'):,} views, {item.get('likes'):,} likes) - {item.get('channel')}")
    print(f"   Desc: {item.get('description_preview', '')[:200]}")
    print()
