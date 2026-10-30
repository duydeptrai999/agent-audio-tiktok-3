import sys

with open('core/video_audit_engine.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''        if not metrics["has_video"] or metrics["width"] < 1280 or metrics["height"] < 720:
            return False, (
                f"🚨 [AUDIT THẤT BẠI] Luồng hình ảnh không đạt chuẩn Full HD/HD "
                f"({metrics['width']}x{metrics['height']})."
            ), metrics'''

replacement = '''        # Hỗ trợ cả chuẩn ngang 16:9 (1920x1080 / 1280x720) và chuẩn dọc 9:16 TikTok (1080x1920 / 720x1280)
        is_hd_horizontal = metrics["width"] >= 1280 and metrics["height"] >= 720
        is_hd_vertical = metrics["width"] >= 720 and metrics["height"] >= 1280
        if not metrics["has_video"] or not (is_hd_horizontal or is_hd_vertical):
            return False, (
                f"🚨 [AUDIT THẤT BẠI] Luồng hình ảnh không đạt chuẩn Full HD/HD "
                f"({metrics['width']}x{metrics['height']}). Bắt buộc >= 1080x1920 (dọc) hoặc >= 1920x1080 (ngang)!"
            ), metrics'''

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open('core/video_audit_engine.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully patched video_audit_engine.py!")
else:
    print("Target not found!")
    # Check normalized
    t_lines = [l.strip() for l in target.splitlines()]
    print("First target line:", t_lines[0])
