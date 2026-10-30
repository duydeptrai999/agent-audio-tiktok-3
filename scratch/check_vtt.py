import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = ['F3rG-3AsrSg.vi.vtt', 'NuIZnjtMXvY.vi.vtt', 'rsWEMsObGAU.vi.vtt', 'W0HlUFKGuYM.vi.vtt']
for f in files:
    path = os.path.join('data/tiktok_study', f)
    if os.path.exists(path):
        vid_id = f.replace('.vi.vtt', '')
        with open(path, 'r', encoding='utf-8') as vtt:
            content = vtt.read(1000).replace('\n', ' ')
        print(f"ID: {vid_id} -> {content[:300]}...\n")
