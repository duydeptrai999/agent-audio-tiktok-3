# -*- coding: utf-8 -*-
import sys
import os
import subprocess
import imageio_ffmpeg
import yt_dlp
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
bgm_dir = Path("TikTok_BGM_Audio")
bgm_dir.mkdir(exist_ok=True)

# Clean temp files
for p in bgm_dir.glob("temp_*"):
    try: p.unlink()
    except Exception: pass

remaining = [
    ("15 - Cau Xem Troi Toi Roi - Piano", "你看天黑了 钢琴 piano instrumental"),
    ("16 - Thoi Khong Sai Lech - Piano", "时空错位 钢琴 piano instrumental"),
    ("17 - Secret - Jay Chou Piano", "Jay chou secret piano instrumental")
]

for filename, query in remaining:
    mp3_target = bgm_dir / f"{filename}.mp3"
    if mp3_target.exists() and mp3_target.stat().st_size > 500000:
        print(f"Da co: {filename}")
        continue
    print(f"Downloading {filename}...")
    temp_file = str(bgm_dir / f"temp_{filename}.m4a")
    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": temp_file,
        "quiet": True,
        "noplaylist": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{query}"])
    
    # find actual downloaded file
    candidates = list(bgm_dir.glob(f"temp_{filename}*"))
    if not candidates:
        print(f"Khong tim thay file download cho {filename}")
        continue
    actual_file = str(candidates[0])
    print(f"Converting to MP3: {filename}...")
    cmd = [ffmpeg_exe, "-y", "-i", actual_file, "-vn", "-ab", "192k", str(mp3_target)]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if os.path.exists(actual_file):
        os.remove(actual_file)
    print(f"Hoan tat: {filename} ({mp3_target.stat().st_size} bytes)")

print("\n--- TAT CA BGM CON LAI DA TAI THANH CONG! ---")
