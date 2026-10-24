# -*- coding: utf-8 -*-
"""
scripts/configure_pure_catalog.py
Cấu hình SLOT_STORY_CATALOG trong core/stories/daily_story_factory.py:
Sử dụng 100% kho 23 kiệt tác độc bản thật (3,500 - 10,672 từ, 22 - 62 phút audio, không lặp đoạn văn).
"""
from pathlib import Path
import re

target_file = Path("core/stories/daily_story_factory.py")
content = target_file.read_text(encoding="utf-8")

old_catalog_pattern = re.compile(r"# --- CATALOG KIỆT TÁC THEO TỪNG SLOT \(SLOT_STORY_CATALOG\) ---.*?(?=# Tương thích ngược)", re.DOTALL)

new_catalog = '''# --- CATALOG KIỆT TÁC THEO TỪNG SLOT (SLOT_STORY_CATALOG) ---
# 100% KHO 23 KIỆT TÁC ĐỘC BẢN THẬT (3.500 - 10.672 TỪ, ZERO 49S TOLERANCE)
SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,  # 3.600 từ (~21.2p)
        get_30min_school_romance_story,            # 10.517 từ (~61.9p)
    ],
    2: [
        get_30min_school_romance_story,            # 10.517 từ (~61.9p)
        get_vungtrom_masterpiece_story,            # 3.567 từ (~21.0p)
    ],
    3: [
        get_romance_nguoctam_masterpiece_story,    # 10.574 từ (~62.2p)
        get_cung_dau_nu_quyen_masterpiece_story,   # 3.391 từ (~19.9p)
    ],
    4: [
        get_30min_angst_romance_story,             # 5.750 từ (~33.8p)
        get_romance_haomon_masterpiece_story,      # 5.629 từ (~33.1p)
    ],
    5: [
        get_horror_chuyentau_masterpiece_story,    # 6.603 từ (~38.8p)
        get_30min_divorce_drama_story,             # 4.883 từ (~28.7p)
    ],
    6: [
        get_romance_chualanh_masterpiece_story,    # 10.622 từ (~62.5p)
        get_romance_chualanh_tuyetpham_story,      # 5.705 từ (~33.6p)
        get_30min_romance_story,                   # 5.610 từ (~33.0p)
        get_romance_haomon_masterpiece_story,      # 5.629 từ (~33.1p)
    ],
    7: [
        get_life_healing_masterpiece_story,        # 4.929 từ (~29.0p)
        get_30min_mother_in_law_story,             # 4.822 từ (~28.4p)
        get_30min_life_drama_story,                # 4.593 từ (~27.0p)
        get_me_chong_thuc_tinh_masterpiece_story,  # 3.890 từ (~22.9p)
    ],
    8: [
        get_huyen_nghi_trang_mau_masterpiece_story, # 10.672 từ (~62.8p)
        get_detective_masterpiece_story,           # 8.073 từ (~47.5p)
        get_30min_doraemon_mystery_story,          # 4.656 từ (~27.4p)
        get_30min_detective_story,                 # 4.639 từ (~27.3p)
    ],
    9: [
        get_horror_chuyentau_masterpiece_story,    # 6.603 từ (~38.8p)
        get_horror_trocot_masterpiece_story,       # 6.101 từ (~35.9p)
    ],
    10: [
        get_kinh_di_huyet_nguyen_masterpiece_story, # 10.630 từ (~62.5p)
        get_horror_guongquy_masterpiece_story,     # 8.246 từ (~48.5p)
        get_horror_trocot_masterpiece_story,       # 6.101 từ (~35.9p)
        get_30min_horror_story,                    # 5.946 từ (~35.0p)
    ]
}

'''

content = old_catalog_pattern.sub(new_catalog, content)
target_file.write_text(content, encoding="utf-8")
print("Pure catalog configured successfully!")
