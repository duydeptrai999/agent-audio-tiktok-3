# -*- coding: utf-8 -*-
"""
scripts/fix_autopilot_target_speed.py
Cập nhật daily_24h_master_autopilot.py:
Thay thế target_speed=1.50 thành target_speed=1.08 (chuẩn điện ảnh tự nhiên ấm áp, không méo giọng, không ép tốc độ).
"""
from pathlib import Path

target_file = Path("scripts/daily_24h_master_autopilot.py")
content = target_file.read_text(encoding="utf-8")

content = content.replace("target_speed=1.50", "target_speed=1.08")
content = content.replace("_15x.mp3", "_cinema.mp3")

target_file.write_text(content, encoding="utf-8")
print("Fixed target_speed in daily_24h_master_autopilot.py!")
