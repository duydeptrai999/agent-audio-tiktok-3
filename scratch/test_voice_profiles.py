# -*- coding: utf-8 -*-
import sys
import io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.voice_profiles import get_voice_profile_for_genre

genres = [
    "Sa Điêu Hài Hước",
    "Thanh Xuân Vườn Trường",
    "Cung Đấu Nữ Quyền",
    "Trọng Sinh Vả Mặt",
    "Mạt Thế Sinh Tồn",
    "Hào Môn Đô Thị",
    "Gia Đấu Mẹ Chồng",
    "Trinh Thám Kỳ Án",
    "Quy Tắc Quái Đàm",
    "Kinh Dị Rùng Rợn"
]

print("=== KIỂM TRA MAPPING VOICE PROFILES THEO THỂ LOẠI ===")
for g in genres:
    prof = get_voice_profile_for_genre(g)
    print(f"{g:25} -> {prof.profile_id:25} | Voice: {prof.voice_name:22} | Pitch: {prof.pitch:5} | Rate: {prof.rate:5} | Vol: {prof.volume:5}")
