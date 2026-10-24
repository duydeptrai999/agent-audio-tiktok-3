# -*- coding: utf-8 -*-
"""
scripts/fix_slot1_slot2_separation.py
Đảm bảo Slot 1 và Slot 2 độc lập 100%, không bao giờ trùng lặp nhau.
"""
from pathlib import Path
import re

target_file = Path("core/stories/daily_story_factory.py")
content = target_file.read_text(encoding="utf-8")

old_s1_s2 = '''SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,  # 3.600 từ (~21.2p)
        get_30min_school_romance_story,            # 10.517 từ (~61.9p)
    ],
    2: [
        get_30min_school_romance_story,            # 10.517 từ (~61.9p)
        get_vungtrom_masterpiece_story,            # 3.567 từ (~21.0p)
    ],'''

new_s1_s2 = '''SLOT_STORY_CATALOG = {
    1: [
        get_sa_dieu_tieng_long_masterpiece_story,  # 3.600 từ (~21.2p) Sa điêu / Tiếng lòng
        get_life_drama_story,                      # 4.593 từ (~27.0p) Đời sống hài hước sâu cay
    ],
    2: [
        get_30min_school_romance_story,            # 10.517 từ (~61.9p) Thanh xuân vườn trường
        get_vungtrom_masterpiece_story,            # 3.567 từ (~21.0p) Vụng trộm ngọt ngào
    ],'''

if old_s1_s2 in content:
    content = content.replace(old_s1_s2, new_s1_s2)
    target_file.write_text(content, encoding="utf-8")
    print("Separated Slot 1 and Slot 2 successfully!")
else:
    print("Could not find old_s1_s2 block!")
