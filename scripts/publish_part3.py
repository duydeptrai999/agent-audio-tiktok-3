# -*- coding: utf-8 -*-
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.tiktok_publisher_core import upload_and_publish_video

part3_video = root / "assets" / "output" / "VID_20261013_173859_part3_final.mp4"
caption = (
    "[PHẦN 3 / KẾT] Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp. "
    "👉 Trọn bộ 3 tập đã lên sóng! Bạn cảm nhận thế nào về kết thúc này? "
    "#audio #xuhuong #ngontinh #audiotruyen #kểchuyện #podcast #fyp #thanhxuan"
)

success = upload_and_publish_video(part3_video, caption, screenshot_prefix="part3")
if success:
    print("🎉 ĐÃ ĐĂNG THÀNH CÔNG PART 3 LÊN TIKTOK STUDIO!")
else:
    print("❌ ĐĂNG PART 3 THẤT BẠI!")
