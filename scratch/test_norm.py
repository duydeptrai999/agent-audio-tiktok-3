# -*- coding: utf-8 -*-
import sys
import io
import unicodedata
import re
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

def strip_vietnamese_accents(text: str) -> str:
    text = unicodedata.normalize('NFD', text)
    text = re.sub(r'[\u0300-\u036f]', '', text)
    text = text.replace('đ', 'd').replace('Đ', 'D')
    return text.lower().strip()

genres = [
    ("Slot 1", "Sa Điêu Hài Hước", "vi-VN-HoaiMyNeural"),
    ("Slot 2", "Thanh Xuân Vườn Trường", "vi-VN-HoaiMyNeural"),
    ("Slot 3", "Cung Đấu Nữ Quyền", "vi-VN-HoaiMyNeural"),
    ("Slot 4", "Trọng Sinh Vả Mặt", "vi-VN-HoaiMyNeural"),
    ("Slot 5", "Mạt Thế Sinh Tồn", "vi-VN-NamMinhNeural"),
    ("Slot 6", "Hào Môn Đô Thị", "vi-VN-HoaiMyNeural"),
    ("Slot 7", "Gia Đấu Mẹ Chồng", "vi-VN-HoaiMyNeural"),
    ("Slot 8", "Trinh Thám Kỳ Án", "vi-VN-NamMinhNeural"),
    ("Slot 9", "Quy Tắc Quái Đàm", "vi-VN-NamMinhNeural"),
    ("Slot 10", "Kinh Dị Rùng Rợn", "vi-VN-NamMinhNeural")
]

for slot_num, g, expected_voice in genres:
    norm = strip_vietnamese_accents(g)
    print(f"{slot_num:8} | Genre: {g:24} -> Norm: {norm:24} | Voice: {expected_voice}")
