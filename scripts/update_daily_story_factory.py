# -*- coding: utf-8 -*-
"""
scripts/update_daily_story_factory.py
Cập nhật daily_story_factory.py:
1. Nạp 100% kho kiệt tác dài chuẩn điện ảnh (25-60 phút) vào SLOT_STORY_CATALOG.
2. Nâng ngưỡng kiểm duyệt tối thiểu: min(lens) >= 800 từ và sum(lens) >= 2700 từ (chặn đứng hoàn toàn video 49s).
"""
from pathlib import Path
import re

target_file = Path("core/stories/daily_story_factory.py")
content = target_file.read_text(encoding="utf-8")

# Thay thế SLOT_STORY_CATALOG
old_catalog_pattern = re.compile(r"# --- CATALOG KIỆT TÁC THEO TỪNG SLOT \(SLOT_STORY_CATALOG\) ---.*?(?=# Tương thích ngược)", re.DOTALL)

new_catalog = '''# --- CATALOG KIỆT TÁC THEO TỪNG SLOT (SLOT_STORY_CATALOG) ---
# 100% KIỆT TÁC DÀI CHUẨN ĐIỆN ẢNH (>= 25 - 60 PHÚT AUDIO, ZERO 49S TOLERANCE)
SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,
        get_gaplai_masterpiece_story,
        get_khododanh_masterpiece_story,
    ],
    2: [
        get_gaplai_masterpiece_story,
        get_khododanh_masterpiece_story,
        get_30min_school_romance_story,
        get_vungtrom_masterpiece_story,
    ],
    3: [
        get_cung_dau_nu_quyen_masterpiece_story,
        get_romance_nguoctam_masterpiece_story,
    ],
    4: [
        get_30min_angst_romance_story,
        get_trong_sinh_hoa_sen_lua_masterpiece_story,
        get_romance_haomon_masterpiece_story,
    ],
    5: [
        get_mat_the_sinh_ton_masterpiece_story,
        get_horror_chuyentau_masterpiece_story,
    ],
    6: [
        get_romance_chualanh_masterpiece_story,
        get_romance_nguoctam_masterpiece_story,
        get_romance_chualanh_tuyetpham_story,
        get_romance_haomon_masterpiece_story,
        get_30min_romance_story,
        get_30min_divorce_drama_story,
    ],
    7: [
        get_life_healing_masterpiece_story,
        get_family_drama_masterpiece_story,
        get_30min_mother_in_law_story,
        get_30min_life_drama_story,
        get_me_chong_thuc_tinh_masterpiece_story,
    ],
    8: [
        get_huyen_nghi_trang_mau_masterpiece_story,
        get_detective_masterpiece_story,
        get_30min_doraemon_mystery_story,
        get_30min_detective_story,
    ],
    9: [
        get_horror_chuyentau_masterpiece_story,
        get_horror_trocot_masterpiece_story,
    ],
    10: [
        get_kinh_di_huyet_nguyen_masterpiece_story,
        get_horror_trocot_masterpiece_story,
        get_horror_guongquy_masterpiece_story,
        get_30min_horror_story,
    ]
}

'''

content = old_catalog_pattern.sub(new_catalog, content)

# Cập nhật ngưỡng độ dài trong vòng lặp chọn truyện
content = content.replace("if not lens or min(lens) >= 140:", "if lens and min(lens) >= 800 and sum(lens) >= 2700:")

target_file.write_text(content, encoding="utf-8")
print("Updated daily_story_factory.py successfully!")
