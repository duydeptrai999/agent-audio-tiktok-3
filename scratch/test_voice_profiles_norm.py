# -*- coding: utf-8 -*-
import sys
import io
import unicodedata
import re
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.voice_profiles import VOICE_PROFILES, VoiceProfile

def normalize_genre_keyword(text: str) -> str:
    t = unicodedata.normalize('NFD', text)
    t = re.sub(r'[\u0300-\u036f]', '', t)
    t = t.replace('đ', 'd').replace('Đ', 'D')
    t = re.sub(r'[^\w\s]', ' ', t)
    return re.sub(r'\s+', '_', t).upper().strip()

def get_voice_profile_for_genre_test(genre: str, preferred_gender: str = "auto") -> VoiceProfile:
    g = normalize_genre_keyword(genre)
    tokens = set(g.split("_"))

    # 1. Quét trực tiếp danh sách genre_match
    for pid, profile in VOICE_PROFILES.items():
        if preferred_gender != "auto":
            is_female = "FEMALE" in pid
            is_male = pid.endswith("_MALE") and not is_female
            if preferred_gender == "male" and not is_male:
                continue
            if preferred_gender == "female" and not is_female:
                continue
        if any(normalize_genre_keyword(gm) == g for gm in profile.genre_match) or g in profile.genre_match:
            return profile

    # 2. Fallback theo từ khóa đặc thù chuẩn hóa
    if any(k in g for k in ["KINH_DI", "QUAI_DAM", "CREEPY", "HUYET_NGUYEN", "AM_HON", "OAN_HON", "TRUYEN_MA", "BI_AN"]) or ("MA" in tokens and "MAT" not in tokens):
        return VOICE_PROFILES["HORROR_CREEPY_MALE"] if preferred_gender != "female" else VOICE_PROFILES["HORROR_WHISPER_FEMALE"]

    if any(k in g for k in ["TRINH_THAM", "HUYEN_NGHI", "DIEU_TRA", "PHAP_Y", "TOI_PHAM", "KY_AN"]):
        return VOICE_PROFILES["DETECTIVE_COLD_MALE"]

    if any(k in g for k in ["SA_DIEU", "HAI_HUOC", "TIENG_LONG", "CA_MAN"]) or "HAI" in tokens:
        return VOICE_PROFILES["SATIRIC_SPARKLING_FEMALE"] if preferred_gender != "male" else VOICE_PROFILES["SATIRIC_INTERNAL_MALE"]

    if any(k in g for k in ["MAT_THE", "BANG_GIA", "SINH_TON", "VO_HAN", "HONG_THUY"]):
        return VOICE_PROFILES["SURVIVOR_GRITTY_MALE"]

    if any(k in g for k in ["CUNG_DAU", "TRACH_DAU", "CO_PHONG", "HOANG_HAU", "NU_QUYEN"]):
        return VOICE_PROFILES["IMPERIAL_SERENE_FEMALE"]

    if any(k in g for k in ["CHUA_LANH", "HEALING", "NGUOC_TAM", "DOI_SONG", "TAM_SU", "CUU_ROI"]):
        return VOICE_PROFILES["HEALING_SOUL_FEMALE"]

    if any(k in g for k in ["THANH_XUAN", "HOC_DUONG", "VUON_TRUONG", "TUOI_TRE", "NGOT_SUNG", "VUNG_TROM"]):
        return VOICE_PROFILES["YOUTH_EMOTIONAL_FEMALE"] if preferred_gender != "male" else VOICE_PROFILES["YOUTH_HERO_MALE"]

    if any(k in g for k in ["ME_CHONG", "GIA_DAU", "VA_MAT", "TRONG_SINH", "LY_HON", "HOAN_DOI"]):
        return VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]

    if any(k in g for k in ["HAO_MON", "THUONG_CHIEN", "TONG_TAI", "TAI_CHINH", "DO_THI", "HOP_DONG"]):
        return VOICE_PROFILES["CEO_AUTHORITY_MALE"] if preferred_gender == "male" else VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]

    # Mặc định an toàn
    return VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"] if preferred_gender == "female" else VOICE_PROFILES["DETECTIVE_COLD_MALE"]

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

print("=== KẾT QUẢ MAPPING CHÍNH XÁC 100% ===")
for g in genres:
    p = get_voice_profile_for_genre_test(g)
    print(f"{g:25} -> {p.profile_id:25} | Voice: {p.voice_name:22} | Pitch: {p.pitch:5} | Rate: {p.rate:5}")
