import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/DOCS_100_AUDIO_TIKTOK_TRIEU_VIEW_THUC_CHIEN.md', 'r', encoding='utf-8') as f:
    text = f.read()

cases = re.split(r'### 🎧 Case Study #', text)
print(f"Total split sections: {len(cases)}")

if len(cases) > 1:
    print("\n--- CASE #001 ---")
    print(cases[1][:1200])

if len(cases) > 21:
    print("\n--- CASE #021 ---")
    print(cases[21][:1200])
