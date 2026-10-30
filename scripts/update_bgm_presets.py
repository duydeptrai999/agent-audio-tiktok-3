# -*- coding: utf-8 -*-
from pathlib import Path

bgm_mgr_file = Path("core/bgm_manager.py")
text = bgm_mgr_file.read_text(encoding="utf-8")

old_part = """    # 1. Nhạc Cổ Phong / Douyin Instrumental / Da diết Á Đông
    "CHINESE_INSTRUMENTAL": [
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["fox_rain"],
    ],
    # 2. Gia Đấu Mẹ Chồng / Hào Môn Trà Xanh / Drama Kịch Tính
    "ME_CHONG": [
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["nguoi_yeu_bo_lo"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],
    # 3. Trọng Sinh Vả Mặt / Đấu Trí Cao Trào / Báo Thù
    "TRONG_SINH": [
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["cry_for_me"],
    ],
    # 4. Thanh Xuân Vườn Trường / Hào Môn Đô Thị / Lãng Mạn
    "ROMANCE": [
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fallin_flower"],
    ],
    # 5. Healing / Chữa Lành / ASMR
    "HEALING": [
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
    ],
    # 6. Hài Hước / Sa Điêu / Phản Sáo Lộ
    "FUNNY": [
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
    ],
    # 7. Huyền Nghi / Trinh Thám / Mạt Thế Sinh Tồn (100% An toàn bản quyền, không bị TikTok mute)
    "HUYEN_NGHI": [
        HORROR_TRACKS["sweet_dreams"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],"""

new_part = """    # 1. Nhạc Cổ Phong / Douyin Instrumental / Da diết Á Đông
    "CHINESE_INSTRUMENTAL": [
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],
        TIKTOK_TRACKS["the_truth_that_you_leave"],
        TIKTOK_TRACKS["cau_xem_troi_toi_roi"],
        TIKTOK_TRACKS["thoi_khong_sai_lech"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["fox_rain"],
    ],
    # 2. Gia Đấu Mẹ Chồng / Hào Môn Trà Xanh / Drama Kịch Tính
    "ME_CHONG": [
        TIKTOK_TRACKS["the_truth_that_you_leave"],
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],
        TIKTOK_TRACKS["cau_xem_troi_toi_roi"],
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["nguoi_yeu_bo_lo"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],
    # 3. Trọng Sinh Vả Mặt / Đấu Trí Cao Trào / Báo Thù
    "TRONG_SINH": [
        TIKTOK_TRACKS["the_truth_that_you_leave"],
        TIKTOK_TRACKS["thoi_khong_sai_lech"],
        TIKTOK_TRACKS["cause_i_love_you"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["cry_for_me"],
    ],
    # 4. Thanh Xuân Vườn Trường / Hào Môn Đô Thị / Lãng Mạn
    "ROMANCE": [
        TIKTOK_TRACKS["secret"],
        TIKTOK_TRACKS["the_truth_that_you_leave"],
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],
        TIKTOK_TRACKS["cau_xem_troi_toi_roi"],
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fallin_flower"],
    ],
    # 5. Healing / Chữa Lành / ASMR
    "HEALING": [
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],
        TIKTOK_TRACKS["the_truth_that_you_leave"],
        TIKTOK_TRACKS["cau_xem_troi_toi_roi"],
        TIKTOK_TRACKS["snowfall"],
        TIKTOK_TRACKS["nham_mat_thay_mua_he"],
        TIKTOK_TRACKS["fox_rain"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
        TIKTOK_TRACKS["da_lau_khong_gap"],
    ],
    # 6. Hài Hước / Sa Điêu / Phản Sáo Lộ
    "FUNNY": [
        TIKTOK_TRACKS["senorita"],
        TIKTOK_TRACKS["fallin_flower"],
        TIKTOK_TRACKS["thieu_nien_hoa_hong"],
        TIKTOK_TRACKS["fox_rain"],
    ],
    # 7. Huyền Nghi / Trinh Thám / Mạt Thế Sinh Tồn (100% An toàn bản quyền, không bị TikTok mute)
    "HUYEN_NGHI": [
        TIKTOK_TRACKS["snowfall"],
        TIKTOK_TRACKS["secret"],
        HORROR_TRACKS["sweet_dreams"],
        TIKTOK_TRACKS["cry_for_me"],
        TIKTOK_TRACKS["bong_la_roi"],
        TIKTOK_TRACKS["thu_qua_dong_sang"],
    ],"""

text_norm = text.replace("\r\n", "\n")
old_norm = old_part.replace("\r\n", "\n")
new_norm = new_part.replace("\r\n", "\n")

if old_norm in text_norm:
    text_norm = text_norm.replace(old_norm, new_norm)
    bgm_mgr_file.write_text(text_norm, encoding="utf-8")
    print("Cap nhat SAFE_BGM_PRESETS thanh cong!")
else:
    print("Khong tim thay old_part trong file!")
