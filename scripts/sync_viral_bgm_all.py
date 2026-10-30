# -*- coding: utf-8 -*-
import sys
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tiktok_dir = root / "TikTok_BGM_Audio"
assets_bgm_dir = root / "assets" / "bgm"
assets_bgm_dir.mkdir(parents=True, exist_ok=True)

# 1. Copy newly downloaded BGM to assets/bgm
for mp3_file in tiktok_dir.glob("*.mp3"):
    dest = assets_bgm_dir / mp3_file.name
    if not dest.exists() or dest.stat().st_size != mp3_file.stat().st_size:
        print(f"Copying {mp3_file.name} to assets/bgm...")
        shutil.copy2(mp3_file, dest)

print("Da dong bo toan bo BGM sang assets/bgm!")

# 2. Update core/bgm_manager.py
bgm_mgr_file = root / "core" / "bgm_manager.py"
content = bgm_mgr_file.read_text(encoding="utf-8")

old_dict = '''TIKTOK_TRACKS = {
    "senorita": TIKTOK_BGM_DIR / "01 - Senorita (Instrumental) - 16+ Romance.mp3",
    "thu_qua_dong_sang": TIKTOK_BGM_DIR / "02 - Thu Qua Dong Sang Ha Nho (Instrumental) - Sad Romance.mp3",
    "cause_i_love_you": TIKTOK_BGM_DIR / "03 - Cause I Love You (Instrumental) - Dramatic Romance.mp3",
    "fox_rain": TIKTOK_BGM_DIR / "04 - Fox Rain Acoustic - Romance BGM.mp3",
    "da_lau_khong_gap": TIKTOK_BGM_DIR / "05 - Da Lau Khong Gap - Ben Nhau Tron Doi OST.mp3",
    "fallin_flower": TIKTOK_BGM_DIR / "06 - Fallin Flower.mp3",
    "cry_for_me": TIKTOK_BGM_DIR / "07 - Cry For Me.mp3",
    "bong_la_roi": TIKTOK_BGM_DIR / "08 - Bong La Roi.mp3",
    "nguoi_yeu_bo_lo": TIKTOK_BGM_DIR / "09 - Nguoi Yeu Bo Lo.mp3",
    "nham_mat_thay_mua_he": TIKTOK_BGM_DIR / "10 - Nham Mat Thay Mua He.mp3",
    "thieu_nien_hoa_hong": TIKTOK_BGM_DIR / "11 - Thieu Nien Hoa Hong.mp3",
}'''

new_dict = '''TIKTOK_TRACKS = {
    "senorita": TIKTOK_BGM_DIR / "01 - Senorita (Instrumental) - 16+ Romance.mp3",
    "thu_qua_dong_sang": TIKTOK_BGM_DIR / "02 - Thu Qua Dong Sang Ha Nho (Instrumental) - Sad Romance.mp3",
    "cause_i_love_you": TIKTOK_BGM_DIR / "03 - Cause I Love You (Instrumental) - Dramatic Romance.mp3",
    "fox_rain": TIKTOK_BGM_DIR / "04 - Fox Rain Acoustic - Romance BGM.mp3",
    "da_lau_khong_gap": TIKTOK_BGM_DIR / "05 - Da Lau Khong Gap - Ben Nhau Tron Doi OST.mp3",
    "fallin_flower": TIKTOK_BGM_DIR / "06 - Fallin Flower.mp3",
    "cry_for_me": TIKTOK_BGM_DIR / "07 - Cry For Me.mp3",
    "bong_la_roi": TIKTOK_BGM_DIR / "08 - Bong La Roi.mp3",
    "nguoi_yeu_bo_lo": TIKTOK_BGM_DIR / "09 - Nguoi Yeu Bo Lo.mp3",
    "nham_mat_thay_mua_he": TIKTOK_BGM_DIR / "10 - Nham Mat Thay Mua He.mp3",
    "thieu_nien_hoa_hong": TIKTOK_BGM_DIR / "11 - Thieu Nien Hoa Hong.mp3",
    "the_truth_that_you_leave": TIKTOK_BGM_DIR / "12 - The Truth That You Leave - Pianoboy.mp3",
    "thanh_nam_hoa_da_no": TIKTOK_BGM_DIR / "13 - Thanh Nam Hoa Da No - Piano.mp3",
    "snowfall": TIKTOK_BGM_DIR / "14 - Snowfall - Oneheart Ambient.mp3",
    "cau_xem_troi_toi_roi": TIKTOK_BGM_DIR / "15 - Cau Xem Troi Toi Roi - Piano.mp3",
    "thoi_khong_sai_lech": TIKTOK_BGM_DIR / "16 - Thoi Khong Sai Lech - Piano.mp3",
    "secret": TIKTOK_BGM_DIR / "17 - Secret - Jay Chou Piano.mp3",
}'''

if old_dict in content:
    content = content.replace(old_dict, new_dict)
    bgm_mgr_file.write_text(content, encoding="utf-8")
    print("Da cap nhat core/bgm_manager.py!")
else:
    # Try normalizing newlines
    content_norm = content.replace("\r\n", "\n")
    old_norm = old_dict.replace("\r\n", "\n")
    new_norm = new_dict.replace("\r\n", "\n")
    if old_norm in content_norm:
        content_norm = content_norm.replace(old_norm, new_norm)
        bgm_mgr_file.write_text(content_norm, encoding="utf-8")
        print("Da cap nhat core/bgm_manager.py (normalized)!")
    else:
        print("Khong tim thay old_dict trong core/bgm_manager.py")
