# -*- coding: utf-8 -*-
"""
scripts/download_extra_viral_bgm.py
Tải các bản nhạc nền viral kinh điển trên TikTok VN:
1. Kiss The Rain - Yiruma (Piano kinh điển cho drama mẹ chồng / gia đình / tâm sự)
2. River Flows In You - Yiruma (Piano lofi nhẹ nhàng thư giãn)
3. Always With Me - Spirited Away (Piano Lofi chữa lành / thanh xuân)
"""
import os
import sys
import subprocess
import imageio_ffmpeg
from yt_dlp import YoutubeDL

sys.stdout.reconfigure(encoding='utf-8')

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUTPUT_DIR = "TikTok_BGM_Audio"
ASSETS_DIR = "assets/bgm"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

TRACKS = [
    {
        "filename": "18 - Kiss The Rain - Yiruma.mp3",
        "query": "ytsearch1:Kiss The Rain Yiruma piano original clean audio",
        "title": "Kiss The Rain - Yiruma"
    },
    {
        "filename": "19 - River Flows In You - Yiruma Lofi.mp3",
        "query": "ytsearch1:River Flows In You Yiruma lofi chill acoustic piano",
        "title": "River Flows In You - Yiruma Lofi"
    },
    {
        "filename": "20 - Always With Me - Spirited Away Piano.mp3",
        "query": "ytsearch1:Always With Me Spirited Away piano gentle relaxing clean",
        "title": "Always With Me - Spirited Away Piano"
    }
]

def download_and_convert(track):
    fn = track["filename"]
    out_path = os.path.join(OUTPUT_DIR, fn)
    asset_path = os.path.join(ASSETS_DIR, fn)
    
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100000:
        print(f"Already exists: {fn}")
        return True
        
    temp_template = os.path.join(OUTPUT_DIR, f"temp_{os.path.splitext(fn)[0]}.%(ext)s")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_template,
        'quiet': True,
        'no_warnings': True,
    }
    
    print(f"Searching and downloading: {track['title']}...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([track["query"]])
    except Exception as e:
        print(f"Error downloading {track['title']}: {e}")
        return False
        
    # Find downloaded temp file
    temp_file = None
    for f in os.listdir(OUTPUT_DIR):
        if f.startswith(f"temp_{os.path.splitext(fn)[0]}"):
            temp_file = os.path.join(OUTPUT_DIR, f)
            break
            
    if not temp_file or not os.path.exists(temp_file):
        print(f"Failed to find temp file for {fn}")
        return False
        
    # Convert to 192k MP3 using imageio_ffmpeg
    cmd = [
        FFMPEG_EXE, "-y", "-i", temp_file,
        "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k",
        out_path
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0 and os.path.exists(out_path):
        print(f"Successfully converted to {out_path} ({os.path.getsize(out_path)} bytes)")
        # Sync to assets/bgm
        import shutil
        shutil.copy2(out_path, asset_path)
        print(f"Synced to {asset_path}")
        # Remove temp file
        try:
            os.remove(temp_file)
        except:
            pass
        return True
    else:
        print(f"FFmpeg conversion failed for {fn}: {res.stderr.decode('utf-8', errors='ignore')}")
        return False

def main():
    success_count = 0
    for t in TRACKS:
        if download_and_convert(t):
            success_count += 1
    print(f"\nDone! Downloaded and integrated {success_count}/{len(TRACKS)} extra viral BGM tracks.")

if __name__ == "__main__":
    main()
