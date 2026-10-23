# -*- coding: utf-8 -*-
"""
core/daily_schedule_config.py
Cấu hình chuẩn hóa Lịch Trình Phát Sóng 10 Bộ Audio Mới Mỗi Ngày (24/7 Autopilot):
- 10 Khung giờ cố định rải đều cả ngày, tối ưu thuật toán TikTok.
- Mỗi bộ gồm 3 tập (Tập 1 -> 20p -> Tập 2 -> 20p -> Tập 3).
- Nghỉ tối thiểu 80 phút giữa 2 bộ khác nhau -> Tuyệt đối chống spam.
- Ban đêm (20h30, 22h30, 00h30) chuyên trị Kinh Dị, Quái Đàm, Trinh Thám Kỳ Án.
- Tự động dọn dẹp Zero-Footprint ngay sau khi xuất bản.
"""

from typing import List, Dict, Any

DAILY_10_SLOTS: List[Dict[str, Any]] = [
    {
        "slot_index": 1,
        "key": "slot_01_sadieu",
        "start_time_str": "06:30",
        "hour": 6,
        "minute": 30,
        "genre": "Sa Điêu Hài Hước",
        "sub_genre": "Độc Tâm / Tiếng Lòng / Hào Môn",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ROMANCE",
        "vibe": "Sáng sớm vui vẻ, sảng khoái, xả stress"
    },
    {
        "slot_index": 2,
        "key": "slot_02_thanhxuan",
        "start_time_str": "08:20",
        "hour": 8,
        "minute": 20,
        "genre": "Thanh Xuân Vườn Trường",
        "sub_genre": "Học Bá / Trùm Trường / Ngọt Sủng",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ROMANCE",
        "vibe": "Giữa sáng ngọt ngào, hoài niệm thanh xuân"
    },
    {
        "slot_index": 3,
        "key": "slot_03_cungdau",
        "start_time_str": "10:10",
        "hour": 10,
        "minute": 10,
        "genre": "Cung Đấu Nữ Quyền",
        "sub_genre": "Hoàng Hậu / Nữ Cường / Tự Chủ",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ANCIENT",
        "vibe": "Đón sóng trưa kịch tính, mưu lược"
    },
    {
        "slot_index": 4,
        "key": "slot_04_vamat",
        "start_time_str": "12:00",
        "hour": 12,
        "minute": 0,
        "genre": "Trọng Sinh Vả Mặt",
        "sub_genre": "Thiên Kim Thật / Hào Môn / Nghịch Tập",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ROMANCE",
        "vibe": "Giờ nghỉ trưa sảng khoái, lật ngược tình thế"
    },
    {
        "slot_index": 5,
        "key": "slot_05_matthe",
        "start_time_str": "13:50",
        "hour": 13,
        "minute": 50,
        "genre": "Mạt Thế Sinh Tồn",
        "sub_genre": "Hồng Thủy / Tích Trữ / Căn Cứ",
        "voice": "vi-VN-NamMinhNeural",
        "bgm_genre": "HORROR",
        "vibe": "Đầu giờ chiều hồi hộp, kích thích tư duy sinh tồn"
    },
    {
        "slot_index": 6,
        "key": "slot_06_haomon",
        "start_time_str": "15:40",
        "hour": 15,
        "minute": 40,
        "genre": "Hào Môn Đô Thị",
        "sub_genre": "Hợp Đồng Hôn Nhân / Giấu Nghề",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "ROMANCE",
        "vibe": "Giờ tan tầm kịch tính, ngọt ngào"
    },
    {
        "slot_index": 7,
        "key": "slot_07_giadau",
        "start_time_str": "17:30",
        "hour": 17,
        "minute": 30,
        "genre": "Gia Đấu Mẹ Chồng",
        "sub_genre": "Con Dâu Bản Lĩnh / Nữ Cường Khởi Nghiệp",
        "voice": "vi-VN-HoaiMyNeural",
        "bgm_genre": "GIA_DAU",
        "vibe": "Giờ cơm tối đồng cảm, vỗ tay tán thưởng"
    },
    {
        "slot_index": 8,
        "key": "slot_08_trinhtham",
        "start_time_str": "19:20",
        "hour": 19,
        "minute": 20,
        "genre": "Trinh Thám Kỳ Án",
        "sub_genre": "Đấu Trí Phòng Kín / Vết Bùn Trần Nhà",
        "voice": "vi-VN-NamMinhNeural",
        "bgm_genre": "DETECTIVE",
        "vibe": "Tối muộn bí ẩn, đấu trí nghẹt thở"
    },
    {
        "slot_index": 9,
        "key": "slot_09_quaidam",
        "start_time_str": "21:10",
        "hour": 21,
        "minute": 10,
        "genre": "Quy Tắc Quái Đàm",
        "sub_genre": "Vô Hạn Lưu / 8 Điều Cấm Kỵ Nửa Đêm",
        "voice": "vi-VN-NamMinhNeural",
        "bgm_genre": "HORROR",
        "vibe": "Đêm khuya lạnh gáy, quy tắc sinh tồn rùng rợn"
    },
    {
        "slot_index": 10,
        "key": "slot_10_kinhdi",
        "start_time_str": "23:00",
        "hour": 23,
        "minute": 0,
        "genre": "Kinh Dị Rùng Rợn",
        "sub_genre": "Chuyến Xe Buýt 404 / Truyện Ma Đêm Muộn",
        "voice": "vi-VN-NamMinhNeural",
        "bgm_genre": "HORROR",
        "vibe": "Đêm kinh dị cực độ, hoàn tất trọn vẹn trước 0h"
    }
]

# Các hằng số điều hành chuẩn
INTERVAL_PARTS_SECONDS = 20 * 60     # 20 phút (1200s) giữa các tập trong 1 bộ
MIN_SERIES_REST_SECONDS = 45 * 60    # 45 phút nghỉ giữa các bộ để hoàn tất trọn vẹn 10 bộ trước 0h đêm
PLANNED_SERIES_REST_SECONDS = 50 * 60 # Lịch tiêu chuẩn nghỉ 50 phút
