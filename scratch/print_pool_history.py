import sys, json
sys.stdout.reconfigure(encoding="utf-8")
with open('data/background_video_pool.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for h in d.get('used_history', []):
    print(h)
