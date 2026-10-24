# -*- coding: utf-8 -*-
"""
scripts/update_script_quality_gate.py
Bổ sung cổng kiểm duyệt thời lượng chuẩn 30 phút điện ảnh (Zero 49s Tolerance) vào script_quality_gate.py
"""
from pathlib import Path

target_file = Path("core/stories/script_quality_gate.py")
content = target_file.read_text(encoding="utf-8")

old_code = '''    series_data["quality_audit_passed"] = True

    series_data["distinctiveness_passed"] = distinct_passed'''

new_code = '''    # Cổng kiểm duyệt thời lượng chuẩn 30 phút điện ảnh (Zero 49s Tolerance)
    total_series_words = sum(len((p.get("full_text") or p.get("text") or "").split()) for p in validated_parts)
    min_part_words = min((len((p.get("full_text") or p.get("text") or "").split()) for p in validated_parts), default=0)

    if total_series_words < 2700 or min_part_words < 700:
        duration_err = f"LỖI THỜI LƯỢNG NGHIÊM TRỌNG (ZERO 49S TOLERANCE): Series chỉ có {total_series_words} từ (tập ngắn nhất {min_part_words} từ). Tiêu chuẩn bắt buộc là >= 2.700 từ (khuyến nghị >= 4.500 từ, ~25-35 phút audio). Cấm xuất bản kịch bản tóm tắt!"
        all_warnings.append(duration_err)
        series_data["quality_audit_passed"] = False
        logger.error(f"  [ScriptQualityGate] {duration_err}")
    else:
        series_data["quality_audit_passed"] = True

    series_data["distinctiveness_passed"] = distinct_passed'''

if old_code in content:
    content = content.replace(old_code, new_code)
    target_file.write_text(content, encoding="utf-8")
    print("Updated script_quality_gate.py successfully!")
else:
    print("Could not find old_code block!")
