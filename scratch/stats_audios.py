import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/analyzed_full_100_audios.json', 'r', encoding='utf-8') as f:
    full_audios = json.load(f)

with open('data/tiktok_study/viral_full_100_cases.json', 'r', encoding='utf-8') as f:
    raw_cases = json.load(f)

with open('data/tiktok_study/top_viral_deep_analysis.json', 'r', encoding='utf-8') as f:
    deep_cases = json.load(f)

print(f"Loaded: full_audios={len(full_audios)}, raw_cases={len(raw_cases)}, deep_cases={len(deep_cases)}")

# Let's inspect durations and view distributions
durations_min = [x.get('duration_minutes', 0) for x in full_audios if x.get('duration_minutes')]
views = [x.get('views', 0) for x in full_audios if x.get('views')]

print(f"Duration stats (mins): min={min(durations_min):.1f}, max={max(durations_min):.1f}, avg={sum(durations_min)/len(durations_min):.1f}")
print(f"Views stats: min={min(views):,}, max={max(views):,}, avg={sum(views)/len(views):,.0f}")

# Group into buckets:
genres = {}
for a in full_audios:
    g = a.get('genre', 'UNKNOWN')
    genres[g] = genres.get(g, 0) + 1

print("\nGenre distribution:")
for g, count in sorted(genres.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {g}: {count} audios")
