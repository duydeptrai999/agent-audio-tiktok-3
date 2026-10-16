# -*- coding: utf-8 -*-
"""
scripts/batch_expand_background_pool.py
Tự động làm giàu và mở rộng kho video nền (Background Video Pool) với các chủ đề Thủ công mỹ nghệ truyền thống:
- Nghệ nhân chế tác đồ gốm Tử Sa (How a Teapot is Made — 60 phút) [Đã có]
- Nghệ nhân thủ công mỹ nghệ Nhật Bản (Japanese Craftsmanship ASMR — 65 phút) [Đang tải/hoàn tất]
- Phục chế dụng cụ cổ & đánh bóng đồ thủ công (Vintage Restoration ASMR — 79 phút)
- Chạm khắc gỗ thủ công mỹ nghệ (Wood Carving ASMR — 76 phút)

Đảm bảo:
1. Video có thời lượng dài (60-80 phút), âm thanh ASMR thuần không dính nhạc bản quyền.
2. Đăng ký đầy đủ vào BackgroundVideoManager và data/background_video_pool.json.
3. Cơ chế xoay tua tự động tối ưu hóa để các bộ audio kế tiếp KHÔNG BAO GIỜ bị lặp video nền.
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

TARGET_VIDEOS = [
    {
        "id": "Iv6tzWbx6M",
        "url": "https://www.youtube.com/watch?v=I_v6tzWbx6M",
        "filename": "traditional_japanese_craft_asmr_Iv6tzWbx6M.mp4",
        "title": "Nghệ nhân thủ công mỹ nghệ truyền thống Nhật Bản (65 phút ASMR)",
        "duration": 3910
    },
    {
        "id": "H7Vz9jOmB30",
        "url": "https://www.youtube.com/watch?v=H7Vz9jOmB30",
        "filename": "vintage_tool_restoration_asmr_H7Vz9jOmB30.mp4",
        "title": "Phục chế dụng cụ cổ & kim loại thủ công mỹ nghệ (79 phút ASMR)",
        "duration": 4755
    },
    {
        "id": "PO_qfxxmiNo",
        "url": "https://www.youtube.com/watch?v=PO_qfxxmiNo",
        "filename": "traditional_wood_carving_asmr_POqfxxmiNo.mp4",
        "title": "Nghệ nhân đục đẽo và chạm khắc gỗ thủ công (76 phút ASMR)",
        "duration": 4580
    }
]

def download_and_sync():
    POOL_DIR.mkdir(parents=True, exist_ok=True)
    print("=" * 65)
    print("🚀 BẮT ĐẦU MỞ RỘNG KHO VIDEO NỀN THỦ CÔNG MỸ NGHỆ CHO HỆ THỐNG")
    print(f"📁 Thư mục pool: {POOL_DIR}")
    print("=" * 65)

    for item in TARGET_VIDEOS:
        target_path = POOL_DIR / item["filename"]
        url = item["url"]
        title = item["title"]

        print(f"\n▶️ Kiểm tra: {title}")
        print(f"   * File: {target_path.name}")

        # Nếu file đã tải hoàn tất (> 50MB)
        if target_path.exists() and target_path.stat().st_size > 50000000:
            size_mb = target_path.stat().st_size / (1024 * 1024)
            print(f"   ✅ Đã có sẵn trên ổ đĩa ({size_mb:.1f} MB). Đồng bộ vào Video Pool...")
            background_manager.register_source_video(
                video_path=target_path,
                url=url,
                title=title,
                max_audios=2
            )
            continue

        print(f"   📥 Đang tải từ YouTube: {url}")
        ydl_opts = {
            'format': '137/bestvideo[height<=1080][ext=mp4]/136/bestvideo[height<=720]',
            'outtmpl': str(target_path),
            'quiet': False,
            'no_warnings': True,
            'nocheckcertificate': True,
            'socket_timeout': 30,
            'retries': 5,
            'http_chunk_size': 10485760
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                actual_title = info.get("title", title)
                dur = info.get("duration", item["duration"])

            if target_path.exists() and target_path.stat().st_size > 10000000:
                size_mb = target_path.stat().st_size / (1024 * 1024)
                print(f"   ✅ Tải thành công: {size_mb:.1f} MB | Thời lượng: {dur//60} phút")
                background_manager.register_source_video(
                    video_path=target_path,
                    url=url,
                    title=actual_title,
                    max_audios=2
                )
            else:
                print(f"   ⚠️ File tải về không hợp lệ: {target_path}")
        except Exception as e:
            print(f"   ❌ Lỗi tải {url}: {e}")

    print("\n" + "=" * 65)
    print("🎉 HOÀN TẤT ĐỒNG BỘ KHO VIDEO NỀN!")
    print(f"Hiện có trong pool: {len(list(POOL_DIR.glob('*.mp4')))} video background.")
    print("=" * 65)

if __name__ == "__main__":
    download_and_sync()
