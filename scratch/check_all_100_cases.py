import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/DOCS_100_AUDIO_TIKTOK_TRIEU_VIEW_THUC_CHIEN.md', 'r', encoding='utf-8') as f:
    text = f.read()

cases = re.findall(r'### 🎧 Case Study #(\d+): \*\*(.*?)\*\*', text)
print(f"Total cases found: {len(cases)}")
for num, title in cases[:20]:
    print(f"#{num}: {title}")

print("\n... and check the last 10 cases:")
for num, title in cases[-10:]:
    print(f"#{num}: {title}")
