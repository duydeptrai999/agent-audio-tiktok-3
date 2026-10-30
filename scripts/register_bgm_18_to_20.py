# -*- coding: utf-8 -*-
import sys

TARGET = "core/bgm_manager.py"
with open(TARGET, "r", encoding="utf-8") as f:
    text = f.read()

old_tiktok_tracks = '''    "thoi_khong_sai_lech": TIKTOK_BGM_DIR / "16 - Thoi Khong Sai Lech - Piano.mp3",
    "secret": TIKTOK_BGM_DIR / "17 - Secret - Jay Chou Piano.mp3",
}'''

new_tiktok_tracks = '''    "thoi_khong_sai_lech": TIKTOK_BGM_DIR / "16 - Thoi Khong Sai Lech - Piano.mp3",
    "secret": TIKTOK_BGM_DIR / "17 - Secret - Jay Chou Piano.mp3",
    "kiss_the_rain": TIKTOK_BGM_DIR / "18 - Kiss The Rain - Yiruma.mp3",
    "river_flows_in_you": TIKTOK_BGM_DIR / "19 - River Flows In You - Yiruma Lofi.mp3",
    "always_with_me": TIKTOK_BGM_DIR / "20 - Always With Me - Spirited Away Piano.mp3",
}'''

if old_tiktok_tracks in text:
    text = text.replace(old_tiktok_tracks, new_tiktok_tracks)
    print("Added tracks 18-20 to TIKTOK_TRACKS")
else:
    print("Could not find old_tiktok_tracks!")

# Add to ME_CHONG preset
old_me_chong = '''    "ME_CHONG": [
        TIKTOK_TRACKS["the_truth_that_you_leave"],'''

new_me_chong = '''    "ME_CHONG": [
        TIKTOK_TRACKS["kiss_the_rain"],
        TIKTOK_TRACKS["the_truth_that_you_leave"],'''

if old_me_chong in text:
    text = text.replace(old_me_chong, new_me_chong)
    print("Added kiss_the_rain to ME_CHONG preset")

# Add to HEALING / CHUALANH / ROMANCE
old_chualanh = '''    "CHUALANH": [
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],'''

new_chualanh = '''    "CHUALANH": [
        TIKTOK_TRACKS["river_flows_in_you"],
        TIKTOK_TRACKS["always_with_me"],
        TIKTOK_TRACKS["thanh_nam_hoa_da_no"],'''

if old_chualanh in text:
    text = text.replace(old_chualanh, new_chualanh)
    print("Added river_flows_in_you and always_with_me to CHUALANH preset")

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(text)
print("Updated core/bgm_manager.py successfully!")
