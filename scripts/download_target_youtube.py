# -*- coding: utf-8 -*-
"""
scripts/download_target_youtube.py
Tải video YouTube chỉ định của user: https://www.youtube.com/watch?v=3NvvOVrm1uY
Lưu vào assets/footage/youtube_pool/
"""
import sys
import os
from pathlib import Path
import yt_dlp

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

root = Path(__file__).resolve().parent.parent
pool_dir = root / "assets" / "footage" / "youtube_pool"
pool_dir.mkdir(parents=True, exist_ok=True)

url = "https://www.youtube.com/watch?v=3NvvOVrm1uY"
target_filename = "baking_asmr_2hours_3NvvOVrm1uY.mp4"
target_path = pool_dir / target_filename

print(f"🎬 Bắt đầu tải video nền YouTube 2 tiếng từ link: {url}")
print(f"📁 Lưu tại: {target_path}")

ydl_opts = {
    # Ưu tiên 1080p mp4 (137) hoặc 720p mp4 (136) hoặc bestvideo[ext=mp4]
    'format': '137/bestvideo[height<=1080][ext=mp4]/136/bestvideo[height<=720]',
    'outtmpl': str(pool_dir / "baking_asmr_2hours_3NvvOVrm1uY.%(ext)s"),
    'quiet': False,
    'no_warnings': True,
    'nocheckcertificate': True
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("\n✅ Tải video thành công!")
        print(f"  Tiêu đề: {info.get('title')}")
        print(f"  Thời lượng: {info.get('duration')}s")
except Exception as e:
    print(f"❌ Lỗi khi tải video: {e}")
    sys.exit(1)
