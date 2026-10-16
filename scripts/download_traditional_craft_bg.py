# -*- coding: utf-8 -*-
"""
scripts/download_traditional_craft_bg.py
Tải video thủ công mỹ nghệ / đồ truyền thống từ YouTube để làm Video Background cho hệ thống:
1. Video Gốm Thủ Công Truyền Thống: "How a Teapot is Made — ASMR Edition" (60 phút, 1080p 16:9)
2. Video Chạm Khắc Gỗ Thủ Công: "1 Hour of Wood Carving ASMR - No talking - Sounds of Wood" (58 phút, 1080p 16:9)

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

CANDIDATES = [
    {
        "url": "https://www.youtube.com/watch?v=AGVNlB400qI",
        "target_filename": "traditional_pottery_teapot_asmr_AGVNlB400qI.mp4",
        "description": "Nghệ nhân gốm chế tác ấm trà thủ công truyền thống (60 phút ASMR)"
    },
    {
        "url": "https://www.youtube.com/watch?v=JRAMK6nA9wM",
        "target_filename": "traditional_wood_carving_asmr_JRAMK6nA9wM.mp4",
        "description": "Nghệ nhân chạm khắc gỗ thủ công truyền thống (58 phút ASMR)"
    }
]

def download_and_register_video(item: dict) -> Path:
    url = item["url"]
    filename = item["target_filename"]
    desc = item["description"]
    out_path = POOL_DIR / filename

    print(f"\n=======================================================")
    print(f"🎬 Bắt đầu xử lý: {desc}")
    print(f"🔗 URL: {url}")
    print(f"📁 Đích đến: {out_path}")
    print(f"=======================================================")

    if out_path.exists() and out_path.stat().st_size > 50000000: # > 50MB
        print(f"✅ File đã tồn tại sẵn trong pool ({out_path.stat().st_size / (1024*1024):.1f} MB). Tiến hành đăng ký...")
        background_manager.register_source_video(
            video_path=out_path,
            url=url,
            title=desc,
            max_audios=10
        )
        return out_path

    ydl_opts = {
        'format': '137/bestvideo[height<=1080][ext=mp4]/136/bestvideo[height<=720]/bestvideo[ext=mp4]',
        'outtmpl': str(out_path),
        'quiet': False,
        'no_warnings': True,
        'nocheckcertificate': True,
        'socket_timeout': 30,
        'retries': 5
    }

    t0 = time.time()
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", desc)
            dur = info.get("duration", 0)

        if out_path.exists() and out_path.stat().st_size > 1000000:
            elapsed = time.time() - t0
            size_mb = out_path.stat().st_size / (1024 * 1024)
            print(f"✅ Tải thành công trong {elapsed:.1f}s!")
            print(f"   * Kích thước: {size_mb:.1f} MB")
            print(f"   * Thời lượng: {dur//60}m{dur%60:02d}s")

            # Đăng ký vào BackgroundVideoManager
            background_manager.register_source_video(
                video_path=out_path,
                url=url,
                title=title,
                max_audios=10
            )
            print(f"🎉 Đã đăng ký thành công vào Video Pool!")
            return out_path
        else:
            raise FileNotFoundError(f"File tải về không tồn tại hoặc rỗng: {out_path}")

    except Exception as e:
        print(f"❌ Lỗi khi tải video: {e}")
        raise

if __name__ == "__main__":
    POOL_DIR.mkdir(parents=True, exist_ok=True)
    success_list = []
    for cand in CANDIDATES:
        try:
            downloaded = download_and_register_video(cand)
            success_list.append(downloaded)
        except Exception as err:
            print(f"⚠️ Thất bại với {cand['url']}: {err}")

    print("\n" + "=" * 60)
    print(f"✨ HOÀN TẤT: Đã tải và đăng ký {len(success_list)}/{len(CANDIDATES)} video thủ công mỹ nghệ vào pool!")
    print("=" * 60)
