# -*- coding: utf-8 -*-
"""
scripts/download_chinese_asmr_bg.py
Hệ thống Tải & Đăng Ký Video Nền ASMR Trung Quốc (Douyin Style):
1. ASMR Chăm Sóc Da & Trang Điểm Chị Em Trung Quốc (Skincare Makeup ASMR)
2. ASMR Nấu Ăn Mỹ Vị Ẩm Thực Truyền Thống Trung Hoa (Chinese Traditional Cooking ASMR)
3. ASMR Làm Bánh Nghệ Thuật / Điểm Tâm Cổ Phong (Chinese Pastry Baking ASMR)
4. ASMR Thủ Công Mỹ Nghệ Di Sản Phi Vật Thể (Chinese Intangible Cultural Heritage Craft ASMR)

Tự động lưu vào assets/footage/youtube_pool/ và đăng ký vào BackgroundVideoManager.
"""

import sys
import os
import time
from pathlib import Path
import yt_dlp

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.background_manager import background_manager, POOL_DIR

CHINESE_ASMR_CANDIDATES = [
    {
        "url": "https://www.youtube.com/watch?v=AGVNlB400qI",
        "target_filename": "chinese_pottery_craft_asmr_AGVNlB400qI.mp4",
        "theme": "chinese_craft_heritage",
        "description": "Nghệ nhân gốm sứ cổ truyền chế tác ấm tử sa (60 phút ASMR không lời)"
    },
    {
        "url": "https://www.youtube.com/watch?v=JRAMK6nA9wM",
        "target_filename": "chinese_wood_carving_asmr_JRAMK6nA9wM.mp4",
        "theme": "chinese_craft_heritage",
        "description": "Nghệ nhân chạm khắc gỗ cổ phong truyền thống (58 phút ASMR không lời)"
    }
]

def search_and_download_chinese_asmr(theme: str = "chinese_beauty_asmr", max_duration_mins: int = 60) -> Path:
    """Tìm kiếm và tải video ASMR Trung Quốc theo theme trên YouTube/Douyin."""
    theme_queries = {
        "chinese_beauty_asmr": "chinese makeup skincare asmr satisfying douyin no music",
        "chinese_cooking_asmr": "chinese traditional cooking asmr satisfying street food no music",
        "chinese_pastry_baking": "traditional chinese pastry dim sum baking asmr no music",
        "chinese_craft_heritage": "chinese intangible cultural heritage traditional craft embroidery pottery wood asmr"
    }
    query = theme_queries.get(theme, theme_queries["chinese_beauty_asmr"])
    print(f"\n🔍 Đang tìm kiếm video ASMR Trung Quốc: '{query}'...")

    ydl_opts = {
        'format': '137/bestvideo[height<=1080][ext=mp4]/136/bestvideo[height<=720]/bestvideo[ext=mp4]',
        'outtmpl': str(POOL_DIR / f"{theme}_%(id)s.%(ext)s"),
        'default_search': f"ytsearch1:{query}",
        'quiet': False,
        'no_warnings': True,
        'nocheckcertificate': True,
        'socket_timeout': 30,
        'retries': 3
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=True)
            if "entries" in info and info["entries"]:
                entry = info["entries"][0]
                vid_id = entry.get("id")
                ext = entry.get("ext", "mp4")
                downloaded_file = POOL_DIR / f"{theme}_{vid_id}.{ext}"
                if downloaded_file.exists():
                    background_manager.register_source_video(
                        video_path=downloaded_file,
                        url=entry.get("webpage_url", ""),
                        title=entry.get("title", theme),
                        max_audios=10
                    )
                    print(f"🎉 Đã tải và đăng ký thành công video ASMR: {downloaded_file.name}")
                    return downloaded_file
    except Exception as e:
        print(f"⚠️ Không thể tải video trực tiếp qua search: {e}")
        # Dùng video có sẵn trong pool
        for f in POOL_DIR.glob("*.mp4"):
            if f.stat().st_size > 1000000:
                print(f"✅ Sử dụng video nền chất lượng cao sẵn có: {f.name}")
                return f
    return Path()

if __name__ == "__main__":
    print("=== TẢI & ĐĂNG KÝ VIDEO NỀN ASMR TRUNG QUỐC ===")
    for c in CHINESE_ASMR_CANDIDATES:
        out = POOL_DIR / c["target_filename"]
        if out.exists():
            print(f"✅ Đã có sẵn: {out.name}")
            background_manager.register_source_video(
                video_path=out,
                url=c["url"],
                title=c["description"],
                max_audios=10
            )
        else:
            print(f"⏳ File {out.name} chưa tồn tại.")
