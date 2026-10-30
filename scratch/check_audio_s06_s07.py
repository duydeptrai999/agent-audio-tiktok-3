import sys
from pathlib import Path
sys.path.insert(0, '.')
from core.ffmpeg_utils import probe_media_file

print("=== Check s07 audio ===")
for p in Path('assets/audio').glob('*20261027_s07*'):
    print(p.name, p.stat().st_size)

print("=== Check s06 audio ===")
for p in Path('assets/audio').glob('*20261027_s06*'):
    print(p.name, p.stat().st_size)
