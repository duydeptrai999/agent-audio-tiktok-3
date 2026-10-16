# -*- coding: utf-8 -*-
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.tiktok_publisher_core import upload_and_publish_video

part2_video = root / "assets" / "output" / "VID_20261013_173859_part2_final.mp4"
caption = (
    "[PHẦN 2] Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp. "
    "👉 Đã có Tập 1 trên kênh. Đón xem Tập 3 - Đại Kết Cục tiếp theo nhé! "
    "#audio #xuhuong #ngontinh #audiotruyen #kểchuyện #podcast #fyp #thanhxuan"
)

success = upload_and_publish_video(part2_video, caption, screenshot_prefix="part2")
if success:
    print("🎉 ĐÃ ĐĂNG THÀNH CÔNG PART 2 LÊN TIKTOK STUDIO!")
else:
    print("❌ ĐĂNG PART 2 THẤT BẠI!")
