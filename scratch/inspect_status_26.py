import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('data/daily_schedule_status_2026-10-26.json', encoding='utf-8'))
for k, v in d.items():
    if isinstance(v, dict) and 'title' in v:
        print(f"{k}: {v.get('title')} | p1: {v.get('part1')} | p2: {v.get('part2')} | p3: {v.get('part3')}")
