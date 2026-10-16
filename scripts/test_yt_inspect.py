# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import yt_dlp

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.youtube.com/watch?v=3NvvOVrm1uY"
ydl_opts = {"quiet": True}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    formats = info.get("formats", [])
    print(f"Title: {info.get('title')}")
    print(f"Total Duration: {info.get('duration')}s ({info.get('duration')//60} mins)")
    for f in formats:
        h = f.get("height")
        if f.get("vcodec") != "none" and h in [720, 1080]:
            size = (f.get("filesize") or f.get("filesize_approx") or 0) / (1024 * 1024)
            print(f"ID: {f.get('format_id')}, ext: {f.get('ext')}, {h}p, vcodec: {f.get('vcodec')[:8]}, size: {size:.1f} MB")
