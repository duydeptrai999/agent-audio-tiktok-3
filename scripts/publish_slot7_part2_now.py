# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
import json
import time
from pathlib import Path
from datetime import datetime

from scripts.tiktok_publisher_core import upload_and_publish_video

def main():
    target_date = "2026-10-24"
    status_file = Path(f"data/daily_schedule_status_{target_date}.json")
    if not status_file.exists():
        print(f"❌ Không tìm thấy file status: {status_file}")
        return

    with open(status_file, "r", encoding="utf-8") as f:
        status = json.load(f)

    s_key = "20261024_slot_07_giadau"
    prefix = "VID_20261024_s07_slot_07_giadau"
    s_info = status.get(s_key, {})

    print("=" * 80)
    print(f"🚀 [TIKTOK PUBLISHER] TIẾN HÀNH ĐĂNG KIỆT TÁC SLOT 7 - TẬP 2")
    print(f"Tiêu đề: {s_info.get('title')}")
    print("=" * 80)

    p_num = 2
    p_key = f"part{p_num}"
    if s_info.get(p_key, False):
        print(f"✅ {p_key} đã được đăng trước đó!")
        return

    video_path = Path(f"assets/output/{prefix}_part{p_num}_final.mp4")
    thumb_path = Path(f"assets/thumbnails/{prefix}_part{p_num}_thumb.jpg")
    
    if not video_path.exists():
        print(f"❌ Video không tồn tại: {video_path}")
        return

    caption = (
        f"[TẬP 2] Màn Trả Thù Đã Nhất Đời Tôi: Bát Canh Sau Sinh Của Mẹ Chồng Và Căn Chung Cư Đứng Tên Tôi. "
        f"Mẹ chồng đòi đuổi tôi ra khỏi nhà để rước con gái bà về ở, nhưng bà không ngờ tôi lẳng lặng rút hợp đồng mua bán nhà ra đối chất! "
        f"Liệu bà có chịu nhượng bộ không? Hãy bình luận dự đoán của bạn nhé! 👉 Đón xem tập 3 - Đại kết cục sẽ lên sóng ngay! "
        f"#audio #xuhuong #audiotruyen #kểchuyện #podcast #fyp #tamtrang #giađấumẹchồng"
    )

    playlist_name = "[TRỌN BỘ] Màn Trả Thù Đã Nhất Đời Tôi"[:30]

    print(f"\n📹 Bắt đầu upload: {video_path.name} ({video_path.stat().st_size / 1024 / 1024:.2f} MB)")
    print(f"📝 Caption: {caption[:100]}...")

    success = upload_and_publish_video(
        video_path=video_path,
        caption=caption,
        screenshot_prefix=f"{s_key}_{p_key}",
        thumbnail_path=thumb_path if thumb_path.exists() else None,
        playlist_name=playlist_name,
        enable_auto_captions=False
    )

    if success:
        status[s_key][p_key] = True
        status["_meta"]["last_published_timestamp"] = time.time()
        status["_meta"]["last_published_time_str"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(status_file, "w", encoding="utf-8") as f:
            json.dump(status, f, indent=2, ensure_ascii=False)
        print(f"\n🎉 [THÀNH CÔNG] ĐÃ ĐĂNG TẬP 2 LÊN TIKTOK STUDIO THÀNH CÔNG!")
    else:
        print(f"\n❌ [THẤT BẠI] Quá trình đăng Tập 2 gặp sự cố.")

if __name__ == "__main__":
    main()
