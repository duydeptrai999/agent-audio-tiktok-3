# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import subprocess
from core.ffmpeg_utils import get_ffmpeg_exe
from core.voice_profiles import get_voice_profile_for_genre, build_genre_vocal_filter_chain

ff = get_ffmpeg_exe()
in_file = ROOT / "scratch" / "test_pitch_hz.mp3"
if not in_file.exists():
    print("test file does not exist")
    exit()

for genre in ["HEALING", "KINH_DI", "TRINH_THAM", "SA_DIEU", "GIA_DAU"]:
    prof = get_voice_profile_for_genre(genre)
    vfilter = build_genre_vocal_filter_chain(prof, voice_volume=0.82)
    out_file = ROOT / "scratch" / f"test_{genre}.mp3"
    cmd = [ff, "-y", "-i", str(in_file), "-filter:a", vfilter, str(out_file)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[{genre}] SUCCESS! Out size: {out_file.stat().st_size} bytes")
    else:
        print(f"[{genre}] ERROR:\n{res.stderr[:200]}")
