# -*- coding: utf-8 -*-
with open('core/anti_repost_guard.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """PAST_SERIES_BLACKLIST = [
    "mạt thế kỷ băng hà",
    "nàng dâu thức tỉnh",
    "kỳ án biệt thự trăng máu",
    "huyết nguyện lúc nửa đêm",
    "gặp lại người năm ấy",
    "đại ca học đường khó dỗ dành",
    "vụng trộm yêu thầm",
    "bản hợp đồng hôn nhân 100 tỷ",
    "khi hoa sơn tra tàn lụi",
    "chiếc áo đồng phục năm ấy",
    "ánh sáng nơi tận cùng đêm tối",
    "nghịch lý fermi",
    "chuyến du hành vào bầu trời đêm",
    "đóa sen lửa nở rộ"
]"""

replacement = """PAST_SERIES_BLACKLIST = [
    "mạt thế kỷ băng hà",
    "nàng dâu thức tỉnh",
    "gặp lại người năm ấy",
    "đại ca học đường khó dỗ dành",
    "nghịch lý fermi",
    "chuyến du hành vào bầu trời đêm",
    "đóa sen lửa nở rộ"
]"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open('core/anti_repost_guard.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated core/anti_repost_guard.py")
else:
    print("TARGET NOT FOUND in core/anti_repost_guard.py")
