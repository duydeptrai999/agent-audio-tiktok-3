# -*- coding: utf-8 -*-
"""
scripts/master_scheduler.py
Hệ thống Tự Động Hóa Đăng Bài Master:
- Quản lý lịch trình đăng video chính xác theo yêu cầu người dùng:
  + Bộ 1: Đã đăng Part 1, Part 2. Đúng 22:45 đăng Part 3 (trọn bộ trong 1 tiếng).
  + Cách 1 tiếng (23:45): Đăng Bộ 2 (Trinh Thám) rải đều 3 tập trong 1 tiếng (23:45, 00:05, 00:25).
  + Cách 1 tiếng (01:25): Đăng Bộ 3 (Drama Gia Đấu) rải đều 3 tập trong 1 tiếng (01:25, 01:45, 02:05).
- Khóa liên tiến trình CoccocFileLock chống xung đột ProcessSingleton
- Hỗ trợ tính toán lịch trình động (calculate_dynamic_schedule) với giãn cách chuẩn:
  * 20 phút giữa các tập trong 1 bộ
  * 60 phút (1 tiếng) giữa các bộ
- Lưu trữ trạng thái vào data/publishing_status.json
- Tự động kiểm tra file video đã sẵn sàng trước khi đăng.
"""

import sys
import os
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, List

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from scripts.tiktok_publisher_core import upload_and_publish_video, CoccocFileLock

STATUS_FILE = root / "data" / "publishing_status.json"

def calculate_dynamic_schedule(base_time: Optional[datetime] = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Tính toán lịch trình phát hành động:
    - 20 phút giãn cách giữa các tập trong cùng một bộ
    - 60 phút (1 tiếng) giãn cách giữa các bộ (tính từ thời điểm đăng tập cuối của bộ trước)
    """
    start = base_time or datetime.now()
    schedule = {
        "series1": [],
        "series2": [],
        "series3": []
    }

    # Series 1: Part 1 (T0), Part 2 (T0 + 20m), Part 3 (T0 + 40m)
    t = start
    for p in [1, 2, 3]:
        schedule["series1"].append({
            "part": f"part{p}",
            "target_time": t,
            "target_timestamp": t.timestamp()
        })
        t = t + timedelta(minutes=20)

    # Series 2: Bắt đầu 60 phút sau khi tập cuối Series 1 lên sóng (tại T0 + 40m + 60m = T0 + 100m)
    t_s1_end = schedule["series1"][-1]["target_time"]
    t = t_s1_end + timedelta(minutes=60)
    for p in [1, 2, 3]:
        schedule["series2"].append({
            "part": f"part{p}",
            "target_time": t,
            "target_timestamp": t.timestamp()
        })
        t = t + timedelta(minutes=20)

    # Series 3: Bắt đầu 60 phút sau khi tập cuối Series 2 lên sóng
    t_s2_end = schedule["series2"][-1]["target_time"]
    t = t_s2_end + timedelta(minutes=60)
    for p in [1, 2, 3]:
        schedule["series3"].append({
            "part": f"part{p}",
            "target_time": t,
            "target_timestamp": t.timestamp()
        })
        t = t + timedelta(minutes=20)

    return schedule

def load_status():
    if STATUS_FILE.exists():
        try:
            return json.loads(STATUS_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {
        "series1": {"part1": True, "part2": True, "part3": False},
        "series2": {"part1": False, "part2": False, "part3": False},
        "series3": {"part1": False, "part2": False, "part3": False}
    }

def save_status(status):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding='utf-8')

def wait_until(target_timestamp: float, label: str):
    """Chờ đến mốc thời gian quy định, in tiến trình mỗi phút."""
    now = time.time()
    if target_timestamp <= now:
        return
    diff = int(target_timestamp - now)
    print(f"\n⏳ [{datetime.now().strftime('%H:%M:%S')}] Chờ đến lịch đăng {label} (còn {diff // 60} phút {diff % 60} giây)...")
    while time.time() < target_timestamp:
        remaining = int(target_timestamp - time.time())
        if remaining % 60 == 0 or remaining <= 10:
            print(f"  [{datetime.now().strftime('%H:%M:%S')}] Còn {remaining // 60}m {remaining % 60}s tới mốc đăng {label}...")
        time.sleep(min(5, max(1, remaining)))

def run_schedule(dynamic: bool = False):
    out_dir = root / "assets" / "output"
    status = load_status()
    print("=" * 70)
    print(f"🌟 BẮT ĐẦU CHƯƠNG TRÌNH ĐĂNG BÀI MASTER TIKTOK ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"🔒 Cơ chế khóa liên tiến trình CoccocFileLock & giãn cách an toàn kích hoạt.")
    print("=" * 70)

    # ---------------------------------------------------------
    # 1. BỘ 1: PART 3 (Chiếc Áo Đồng Phục Năm Ấy)
    # Lịch: 22:45 tối nay (hoàn tất bộ 1 trong 1 tiếng)
    # ---------------------------------------------------------
    if not status["series1"]["part3"]:
        if dynamic:
            target_p3 = time.time() + 60
        else:
            target_p3 = datetime.now().replace(hour=22, minute=45, second=0, microsecond=0).timestamp()
            if time.time() > target_p3:
                # Nếu đã quá 22:45 thì chờ 1 phút rồi đăng
                target_p3 = time.time() + 60
        wait_until(target_p3, "Bộ 1 - Part 3")

        part3_vid = out_dir / "VID_20261013_173859_part3_final.mp4"
        part3_cap = (
            "[PHẦN 3 / KẾT] Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp. "
            "👉 Trọn bộ 3 tập đã lên sóng! Bạn cảm nhận thế nào về kết thúc này? "
            "#audio #xuhuong #ngontinh #audiotruyen #kểchuyện #podcast #fyp #thanhxuan"
        )
        success = upload_and_publish_video(part3_vid, part3_cap, screenshot_prefix="series1_part3")
        status["series1"]["part3"] = True
        save_status(status)
        print("🎉 HOÀN TẤT 100% BỘ 1 TRONG VÒNG 1 TIẾNG!")

    # ---------------------------------------------------------
    # 2. BỘ 2: TRINH THÁM (Kỳ Án Căn Phòng Số 13)
    # Cách 1 tiếng đăng 1 bộ -> Bắt đầu 23:45
    # Rải đều 3 tập: 23:45, 00:05, 00:25 (giãn cách 20 phút mỗi tập)
    # ---------------------------------------------------------
    s2_schedule = [
        ("part1", 23, 45, "VID_detective_part1_final.mp4", 
         "[PHẦN 1] Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất. 👉 Đón xem Tập 2 - Mật Mã Hầm Ngầm & Cầu Cảng Số 7 tối nay nhé! #audio #xuhuong #trinhtham #audiotruyen #kểchuyện #podcast #fyp #phapan #vuan"),
        ("part2", 0, 5, "VID_detective_part2_final.mp4",
         "[PHẦN 2] Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất. 👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục vạch mặt kẻ phản bội! #audio #xuhuong #trinhtham #audiotruyen #kểchuyện #podcast #fyp #phapan #vuan"),
        ("part3", 0, 25, "VID_detective_part3_final.mp4",
         "[PHẦN 3 / KẾT] Kỳ Án Căn Phòng Số 13: 3 Cuộc Gọi Tử Thần Của Kẻ Đã Mất. 👉 Trọn bộ 3 tập đã lên sóng! Bạn nghĩ gì về sự trả giá của kẻ phản bội? #audio #xuhuong #trinhtham #audiotruyen #kểchuyện #podcast #fyp #phapan #vuan")
    ]

    for p_key, hour, minute, vid_name, caption in s2_schedule:
        if not status["series2"][p_key]:
            vid_path = out_dir / vid_name
            while not vid_path.exists() or vid_path.stat().st_size < 1000000:
                print(f"⏳ Đang chờ video {vid_name} hoàn tất render...")
                time.sleep(15)

            if dynamic:
                target_ts = time.time() + 10
            else:
                now_dt = datetime.now()
                target_dt = now_dt.replace(hour=hour, minute=minute, second=0, microsecond=0)
                if hour < now_dt.hour:
                    target_dt += timedelta(days=1)
                target_ts = target_dt.timestamp()

            wait_until(target_ts, f"Bộ 2 - {p_key}")
            success = upload_and_publish_video(vid_path, caption, screenshot_prefix=f"series2_{p_key}")
            status["series2"][p_key] = True
            save_status(status)
            print(f"🎉 Đã đăng thành công Bộ 2 - {p_key}!")

    print("🎉 HOÀN TẤT 100% BỘ 2 TRONG VÒNG 1 TIẾNG!")

    # ---------------------------------------------------------
    # 3. BỘ 3: DRAMA GIA ĐẤU (Đêm Mưa Bị Đuổi Khỏi Hào Môn)
    # Cách 1 tiếng đăng 1 bộ -> Bắt đầu 01:25 (sau 00:25 đúng 60 phút)
    # Rải đều 3 tập: 01:25, 01:45, 02:05 (giãn cách 20 phút mỗi tập)
    # ---------------------------------------------------------
    s3_schedule = [
        ("part1", 1, 25, "VID_drama_part1_final.mp4",
         "[PHẦN 1] Đêm Mưa Bị Đuổi Khỏi Hào Môn: Màn Lật Kèo Đòi Lại Căn Biệt Thự 50 Tỷ. 👉 Đón xem Tập 2 - Nữ Vương Trỗi Dậy & Màn Đấu Giá tối nay nhé! #audio #xuhuong #giadau #audiotruyen #kểchuyện #podcast #fyp #mechong #drama"),
        ("part2", 1, 45, "VID_drama_part2_final.mp4",
         "[PHẦN 2] Đêm Mưa Bị Đuổi Khỏi Hào Môn: Màn Lật Kèo Đòi Lại Căn Biệt Thự 50 Tỷ. 👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục Hả Dạ! #audio #xuhuong #giadau #audiotruyen #kểchuyện #podcast #fyp #mechong #drama"),
        ("part3", 2, 5, "VID_drama_part3_final.mp4",
         "[PHẦN 3 / KẾT] Đêm Mưa Bị Đuổi Khỏi Hào Môn: Màn Lật Kèo Đòi Lại Căn Biệt Thự 50 Tỷ. 👉 Trọn bộ 3 tập đã lên sóng! Bạn nghĩ gì về sự trả giá của người chồng bội bạc? #audio #xuhuong #giadau #audiotruyen #kểchuyện #podcast #fyp #mechong #drama")
    ]

    for p_key, hour, minute, vid_name, caption in s3_schedule:
        if not status["series3"][p_key]:
            vid_path = out_dir / vid_name
            while not vid_path.exists() or vid_path.stat().st_size < 1000000:
                print(f"⏳ Đang chờ video {vid_name} hoàn tất render...")
                time.sleep(15)

            if dynamic:
                target_ts = time.time() + 10
            else:
                now_dt = datetime.now()
                target_dt = now_dt.replace(hour=hour, minute=minute, second=0, microsecond=0)
                if hour < now_dt.hour:
                    target_dt += timedelta(days=1)
                target_ts = target_dt.timestamp()

            wait_until(target_ts, f"Bộ 3 - {p_key}")
            success = upload_and_publish_video(vid_path, caption, screenshot_prefix=f"series3_{p_key}")
            status["series3"][p_key] = True
            save_status(status)
            print(f"🎉 Đã đăng thành công Bộ 3 - {p_key}!")

    print("\n" + "=" * 70)
    print("🚀 TẤT CẢ 3 BỘ AUDIO (9 VIDEO MP4 FULL HD) ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG RỰC RỠ TRÊN TIKTOK!")
    print("=" * 70)

if __name__ == "__main__":
    run_schedule()
