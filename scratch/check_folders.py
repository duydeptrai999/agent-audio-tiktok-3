import sys
from pathlib import Path
sys.path.insert(0, '.')
from core.ffmpeg_utils import probe_media_file

for folder in ['raw_downloaded', 'youtube_pool', 'baking', 'cooking']:
    p_dir = Path('assets/footage') / folder
    print('===', folder, '===')
    if p_dir.exists():
        for p in p_dir.glob('*.mp4'):
            info = probe_media_file(p)
            w = info.get("width")
            h = info.get("height")
            d = info.get("duration", 0)
            sz = p.stat().st_size / 1024 / 1024
            print(f'  {p.name}: {w}x{h} ({d:.1f}s, {sz:.1f}MB)')
