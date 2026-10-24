# -*- coding: utf-8 -*-
"""
scripts/update_video_audit_engine.py
Nâng cấp rào chắn VideoAuditEngine:
Khóa cứng MIN_DURATION_SECONDS = 300.0 (tối thiểu 5 phút / tập) và MIN_VIDEO_SIZE_BYTES = 10MB.
Chặn đứng vĩnh viễn 100% video ngắn dưới 5 phút, bảo vệ tuyệt đối chuẩn 30 phút điện ảnh.
"""
from pathlib import Path

target_file = Path("core/video_audit_engine.py")
content = target_file.read_text(encoding="utf-8")

old_block = '''    MIN_VIDEO_SIZE_BYTES = 3 * 1024 * 1024    # Tối thiểu 3 MB
    MIN_DURATION_SECONDS = 30.0               # Tối thiểu 30s (đáp ứng chuẩn short-form & audio drama)'''

new_block = '''    MIN_VIDEO_SIZE_BYTES = 10 * 1024 * 1024   # Tối thiểu 10 MB (chuẩn video dài 1080p)
    MIN_DURATION_SECONDS = 300.0              # Tối thiểu 300s (5 phút/tập, chuẩn 8-12 phút điện ảnh)'''

if old_block in content:
    content = content.replace(old_block, new_block)
    target_file.write_text(content, encoding="utf-8")
    print("Updated VideoAuditEngine thresholds successfully!")
else:
    print("Could not find old_block in VideoAuditEngine!")
