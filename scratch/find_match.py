import sys, subprocess
from pathlib import Path
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image
import numpy as np
from core.ffmpeg_utils import get_ffmpeg_exe

ffmpeg = get_ffmpeg_exe()
s06_im = np.array(Image.open('scratch/s06_frame.jpg'))

for p in sorted(Path('assets/footage').glob('**/*.*')):
    if p.suffix.lower() == '.mp4' and 'slices' not in str(p) and p.stat().st_size > 10000000:
        tmp = Path('scratch/cand_frame.jpg')
        subprocess.run([ffmpeg, '-y', '-ss', '10', '-i', str(p), '-vframes', '1', str(tmp)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if tmp.exists():
            c_im = np.array(Image.open(tmp))
            if c_im.shape == s06_im.shape:
                diff = np.mean(np.abs(c_im.astype(float) - s06_im.astype(float)))
                print(f"Match: {p.name} ({p.parent.name}) diff={diff:.2f}")
            else:
                print(f"Cand: {p.name} shape={c_im.shape}")
