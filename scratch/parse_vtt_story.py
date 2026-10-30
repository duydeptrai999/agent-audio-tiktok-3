import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/tiktok_study/NuIZnjtMXvY.vi.vtt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Clean VTT timestamps and formatting
lines = raw.split('\n')
clean_lines = []
for line in lines:
    line = line.strip()
    if not line or '-->' in line or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
        continue
    # remove inline timestamps <00:00:00.000> and <c> tags
    line = re.sub(r'<[^>]+>', '', line)
    clean_lines.append(line)

# De-duplicate consecutive repeated lines from auto-captions
deduped = []
for l in clean_lines:
    if not deduped or l != deduped[-1]:
        deduped.append(l)

full_transcript = " ".join(deduped)

print(f"Total length in characters: {len(full_transcript)}")
print(f"Total words approx: {len(full_transcript.split())}")

print("\n--- SAMPLE ACT 1 (Lines 0 to 1000 chars) ---")
print(full_transcript[:1200])

print("\n--- SAMPLE MID-POINT CLIMAX (Characters 4000 to 5200) ---")
print(full_transcript[4000:5200])

print("\n--- SAMPLE ENDING RESOLUTION (Characters 10000 to 11200) ---")
print(full_transcript[10000:11200])
