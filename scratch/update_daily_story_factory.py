# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/stories/daily_story_factory.py")
text = fpath.read_text(encoding="utf-8")

old_code = '''def get_daily_10_series(target_date: str = "") -> List[Dict[str, Any]]:
    """
    Sinh danh sách 10 bộ truyện cho một ngày cụ thể (YYYY-MM-DD).
    Nạp toàn bộ văn bản 15.000+ từ chuẩn điện ảnh cho từng tập.
    Tự động lọc trùng lặp với quá khứ và blacklist.
    """'''

new_code = '''def get_daily_10_series(target_date: str = "") -> List[Dict[str, Any]]:
    """
    Sinh danh sách 10 bộ truyện cho một ngày cụ thể (YYYY-MM-DD).
    Nạp toàn bộ văn bản 15.000+ từ chuẩn điện ảnh cho từng tập.
    Tự động lọc trùng lặp với quá khứ và blacklist.
    BẮT BUỘC KIỂM TRA CỔNG KINH NGHIỆM 10 VÒNG (require_preflight_experience).
    """
    from core.stories.script_quality_gate import require_preflight_experience
    require_preflight_experience()'''

if old_code in text:
    text = text.replace(old_code, new_code)
    fpath.write_text(text, encoding="utf-8")
    print("Updated daily_story_factory.py successfully!")
else:
    print("Could not find old_code in daily_story_factory.py")
