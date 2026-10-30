import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/analyzed_full_100_audios.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total analyzed: {len(data)}")
if len(data) > 0:
    print("Keys in item 0:", list(data[0].keys()))
    print("\nFirst 5 items:")
    for i, item in enumerate(data[:5]):
        print(f"#{i+1}: {item.get('title')}")
        print(f"   Views: {item.get('views')}, Likes: {item.get('likes')}, Channel: {item.get('channel')}")
        print(f"   Hook: {item.get('hook', '')[:100]}")
        print(f"   Why Viral: {item.get('why_viral', item.get('analysis', ''))[:150]}")
        print()
