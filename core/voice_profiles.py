# -*- coding: utf-8 -*-
"""
core/voice_profiles.py
Hệ Thống Ma Trận Đa Giọng Đọc Điện Ảnh Theo Thể Loại (Multi-Genre Cinema Voice Profiles Engine).
Tối ưu hóa âm học chuyên sâu từ Edge-TTS và FFmpeg Vocal Mastering:
- Mỗi thể loại sở hữu một hoặc nhiều Profile Giọng Đọc độc bản với:
  1. Voice gốc: vi-VN-NamMinhNeural hoặc vi-VN-HoaiMyNeural.
  2. Pitch Modulation (Cao độ âm thanh): Tinh chỉnh -4.5Hz đến +3.5Hz để biến hóa âm sắc nhân vật.
  3. Edge-TTS Rate: Tốc độ phát âm tự nhiên của AI.
  4. FFmpeg Vocal Studio Chain: EQ, Compressor, De-Esser, Reverb/Spatial riêng biệt cho từng thể loại.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List


@dataclass
class VoiceProfile:
    profile_id: str
    display_name: str
    genre_match: List[str]
    voice_name: str
    pitch: str           # Ví dụ: "-3Hz", "+1Hz", "+3Hz"
    rate: str            # Ví dụ: "+0%", "+3%", "-2%"
    volume: str          # Ví dụ: "+0%", "+2%"
    tempo_multiplier: float
    description: str
    eq_settings: Dict[str, Any]
    compressor_settings: Dict[str, Any]
    special_effects: Optional[str] = None


# MA TRẬN 10 VOICE PROFILES CHUYÊN SÂU THEO TỪNG THỂ LOẠI
VOICE_PROFILES: Dict[str, VoiceProfile] = {
    # 1. TRINH THÁM / KỲ ÁN / HUYỀN NGHI
    "DETECTIVE_COLD_MALE": VoiceProfile(
        profile_id="DETECTIVE_COLD_MALE",
        display_name="Nam Minh - Thám Tử Lạnh Lùng",
        genre_match=["HUYEN_NGHI", "TRINH_THAM", "PHAP_Y", "TOI_PHAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3.5Hz",
        rate="-2%",
        volume="+0%",
        tempo_multiplier=1.12,
        description="Trầm, đặc, uy nghiêm, bí ẩn, nhấn nhá đanh thép như trong phòng thẩm vấn hiện trường.",
        eq_settings={
            "warmth_freq": 110, "warmth_gain": 4.5,
            "scoop_freq": 800, "scoop_gain": -2.5,
            "clarity_freq": 3200, "clarity_gain": 3.8,
            "deess_freq": 6500, "deess_gain": -2.5
        },
        compressor_settings={"threshold": "-19dB", "ratio": 3.6, "attack": 10, "release": 70},
        special_effects="stereotools=mpan=-0.02"  # Giữ giọng trọng tâm vững chắc
    ),

    # 2. KINH DỊ / QUÁI ĐÀM / NGUY DỊ
    "HORROR_CREEPY_MALE": VoiceProfile(
        profile_id="HORROR_CREEPY_MALE",
        display_name="Nam Minh - Quái Đàm Âm U",
        genre_match=["KINH_DI", "QUAI_DAM", "CREEPYPASTA"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-4.5Hz",
        rate="-4%",
        volume="+0%",
        tempo_multiplier=1.08,
        description="Lạnh buốt, ma mị, âm u, trầm sát màng nhĩ tạo cảm giác rợn gáy trong hành lang bỏ hoang.",
        eq_settings={
            "warmth_freq": 90, "warmth_gain": 5.0,
            "scoop_freq": 1000, "scoop_gain": -3.0,
            "clarity_freq": 2800, "clarity_gain": 2.5,
            "deess_freq": 6000, "deess_gain": -3.5
        },
        compressor_settings={"threshold": "-21dB", "ratio": 4.2, "attack": 15, "release": 90},
        special_effects="lowpass=f=6800"  # Cắt bớt dải siêu cao để tạo màu âm tối u ám
    ),

    "HORROR_WHISPER_FEMALE": VoiceProfile(
        profile_id="HORROR_WHISPER_FEMALE",
        display_name="Hoài My - Thì Thào Lạnh Gáy",
        genre_match=["KINH_DI_NU", "QUAI_DAM_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-2.0Hz",
        rate="-3%",
        volume="+0%",
        tempo_multiplier=1.08,
        description="Giọng nữ thì thào, lạnh ngắt, tạo cảm giác có người đang thở ngay sau gáy.",
        eq_settings={
            "warmth_freq": 160, "warmth_gain": 3.5,
            "scoop_freq": 1200, "scoop_gain": -2.0,
            "clarity_freq": 3500, "clarity_gain": 3.0,
            "deess_freq": 6200, "deess_gain": -3.0
        },
        compressor_settings={"threshold": "-20dB", "ratio": 3.8, "attack": 12, "release": 80},
        special_effects="lowpass=f=7000"
    ),

    # 3. MẠT THẾ / BĂNG GIÁ / CỰC HẠN SINH TỒN
    "SURVIVOR_GRITTY_MALE": VoiceProfile(
        profile_id="SURVIVOR_GRITTY_MALE",
        display_name="Nam Minh - Chiến Binh Sinh Tồn",
        genre_match=["MAT_THE", "BANG_GIA", "SINH_TON", "VO_HAN"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-1.5Hz",
        rate="+3%",
        volume="+2%",
        tempo_multiplier=1.18,
        description="Gấp gáp, nghẹt thở, sắt đá, cương quyết giữa bão tuyết và đếm ngược sinh tử.",
        eq_settings={
            "warmth_freq": 150, "warmth_gain": 4.0,
            "scoop_freq": 900, "scoop_gain": -2.0,
            "clarity_freq": 2600, "clarity_gain": 4.2,
            "deess_freq": 6500, "deess_gain": -2.0
        },
        compressor_settings={"threshold": "-16dB", "ratio": 4.5, "attack": 4, "release": 50},
        special_effects=None
    ),

    # 4. MẸ CHỒNG / GIA ĐẤU / VẢ MẶT
    "QUEEN_COLD_VENOM_FEMALE": VoiceProfile(
        profile_id="QUEEN_COLD_VENOM_FEMALE",
        display_name="Hoài My - Nữ Chủ Bạo Lực Lạnh",
        genre_match=["ME_CHONG", "GIA_DAU", "VA_MAT", "TRONG_SINH"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+0.5Hz",
        rate="+2%",
        volume="+1%",
        tempo_multiplier=1.16,
        description="Sắc lẹm như dao găm, quý phái, bạo lực lạnh, từng câu nhát gừng vả mặt đối phương.",
        eq_settings={
            "warmth_freq": 200, "warmth_gain": 2.8,
            "scoop_freq": 1100, "scoop_gain": -2.0,
            "clarity_freq": 4200, "clarity_gain": 4.5,
            "deess_freq": 6800, "deess_gain": -3.0
        },
        compressor_settings={"threshold": "-17dB", "ratio": 3.5, "attack": 6, "release": 55},
        special_effects=None
    ),

    # 5. HÀO MÔN / THƯƠNG CHIẾN / TỔNG TÀI
    "CEO_AUTHORITY_MALE": VoiceProfile(
        profile_id="CEO_AUTHORITY_MALE",
        display_name="Nam Minh - Tổng Tài Quyền Lực",
        genre_match=["HAO_MON", "THUONG_CHIEN", "TAI_CHINH"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2.0Hz",
        rate="+1%",
        volume="+2%",
        tempo_multiplier=1.15,
        description="Đĩnh đạc, trầm ổn, làm chủ cuộc chơi tài chính, chuẩn phong thái phòng họp 60 tầng.",
        eq_settings={
            "warmth_freq": 135, "warmth_gain": 4.2,
            "scoop_freq": 1000, "scoop_gain": -2.2,
            "clarity_freq": 3400, "clarity_gain": 3.6,
            "deess_freq": 6400, "deess_gain": -2.2
        },
        compressor_settings={"threshold": "-17dB", "ratio": 3.8, "attack": 7, "release": 60},
        special_effects=None
    ),

    # 6. SA ĐIÊU / HÀI HƯỚC / TIẾNG LÒNG TRÀO PHÚNG
    "SATIRIC_SPARKLING_FEMALE": VoiceProfile(
        profile_id="SATIRIC_SPARKLING_FEMALE",
        display_name="Hoài My - Tiếng Lòng Tinh Quái",
        genre_match=["SA_DIEU", "HAI_HUOC", "TIENG_LONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+3.2Hz",
        rate="+5%",
        volume="+1%",
        tempo_multiplier=1.22,
        description="Nhí nhảnh, nảy tiếng, tinh nghịch, lém lỉnh, gây cười giòn giã trong các pha bóc phốt sếp.",
        eq_settings={
            "warmth_freq": 240, "warmth_gain": 2.0,
            "scoop_freq": 1300, "scoop_gain": -1.5,
            "clarity_freq": 4800, "clarity_gain": 4.0,
            "deess_freq": 7000, "deess_gain": -2.0
        },
        compressor_settings={"threshold": "-15dB", "ratio": 2.6, "attack": 5, "release": 45},
        special_effects="equalizer=f=8000:t=q:w=1.0:g=2.2"  # Air boost tạo độ bay bổng sáng rực
    ),

    # 7. CUNG ĐẤU / TRẠCH ĐẤU / DƯỢC ĐIỂN
    "IMPERIAL_SERENE_FEMALE": VoiceProfile(
        profile_id="IMPERIAL_SERENE_FEMALE",
        display_name="Hoài My - Thâm Cung Trầm Mặc",
        genre_match=["CUNG_DAU", "TRACH_DAU", "CO_PHONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1.2Hz",
        rate="-2%",
        volume="+0%",
        tempo_multiplier=1.10,
        description="Ung dung, thâm sâu, êm ái như tơ lụa nhưng ẩn chứa độc dược và trâm bạc thử độc.",
        eq_settings={
            "warmth_freq": 180, "warmth_gain": 3.6,
            "scoop_freq": 1150, "scoop_gain": -2.2,
            "clarity_freq": 3300, "clarity_gain": 3.4,
            "deess_freq": 6400, "deess_gain": -2.6
        },
        compressor_settings={"threshold": "-18dB", "ratio": 3.2, "attack": 9, "release": 65},
        special_effects=None
    ),

    # 8. CHỮA LÀNH / TÂM LÝ / CUỘC SỐNG
    "HEALING_SOUL_FEMALE": VoiceProfile(
        profile_id="HEALING_SOUL_FEMALE",
        display_name="Hoài My - Chữa Lành Êm Dịu",
        genre_match=["CHUA_LANH", "DOI_SONG", "HEALING", "NGUOC_TAM"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-0.5Hz",
        rate="-4%",
        volume="+0%",
        tempo_multiplier=1.05,
        description="Thủ thỉ, ấm áp, sâu lắng, vỗ về tâm hồn người nghe trong đêm vắng.",
        eq_settings={
            "warmth_freq": 160, "warmth_gain": 4.2,
            "scoop_freq": 1200, "scoop_gain": -2.0,
            "clarity_freq": 3000, "clarity_gain": 2.8,
            "deess_freq": 6500, "deess_gain": -3.0
        },
        compressor_settings={"threshold": "-20dB", "ratio": 3.0, "attack": 12, "release": 80},
        special_effects="equalizer=f=7500:t=q:w=1.5:g=-2.0"  # Giảm bớt dải chói để không mỏi tai nghe đêm
    ),

    # 9. THANH XUÂN / HỌC ĐƯỜNG / CỨU RỖI
    "YOUTH_EMOTIONAL_FEMALE": VoiceProfile(
        profile_id="YOUTH_EMOTIONAL_FEMALE",
        display_name="Hoài My - Thanh Xuân Trong Sáng",
        genre_match=["THANH_XUAN", "CUU_ROI", "HOC_DUONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+1.8Hz",
        rate="+2%",
        volume="+1%",
        tempo_multiplier=1.14,
        description="Trong trẻo, giàu cảm xúc, nhiệt huyết tuổi trẻ, tha thiết vươn lên bảo vệ công lý.",
        eq_settings={
            "warmth_freq": 210, "warmth_gain": 2.5,
            "scoop_freq": 1250, "scoop_gain": -1.8,
            "clarity_freq": 3800, "clarity_gain": 3.8,
            "deess_freq": 6600, "deess_gain": -2.4
        },
        compressor_settings={"threshold": "-18dB", "ratio": 3.2, "attack": 8, "release": 60},
        special_effects=None
    ),

    # 10. HÀNH ĐỘNG / CỨU HỘ BIỂN SÂU / CÁP TREO
    "ACTION_INTENSE_MALE": VoiceProfile(
        profile_id="ACTION_INTENSE_MALE",
        display_name="Nam Minh - Chỉ Huy Thép",
        genre_match=["HANH_DONG", "CUU_HO", "BIEN_SAU", "HANG_DONG", "CAP_TREO"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2.2Hz",
        rate="+4%",
        volume="+2%",
        tempo_multiplier=1.20,
        description="Mạnh mẽ, dồn dập, tiếng hô đanh thép hiệu triệu giữa cuồng phong và giàn khoan biển sâu.",
        eq_settings={
            "warmth_freq": 130, "warmth_gain": 4.5,
            "scoop_freq": 950, "scoop_gain": -2.2,
            "clarity_freq": 3100, "clarity_gain": 4.2,
            "deess_freq": 6500, "deess_gain": -2.2
        },
        compressor_settings={"threshold": "-15dB", "ratio": 4.8, "attack": 3, "release": 45},
        special_effects=None
    ),
}


def get_voice_profile_for_genre(genre: str, preferred_gender: str = "auto") -> VoiceProfile:
    """
    Tự động lựa chọn Voice Profile điện ảnh tối ưu nhất cho thể loại được chỉ định:
    - Nếu genre là HUYEN_NGHI -> DETECTIVE_COLD_MALE
    - Nếu genre là KINH_DI / QUAI_DAM -> HORROR_CREEPY_MALE hoặc HORROR_WHISPER_FEMALE
    - Nếu genre là SA_DIEU -> SATIRIC_SPARKLING_FEMALE
    - Nếu genre là ME_CHONG / VA_MAT -> QUEEN_COLD_VENOM_FEMALE
    - Nếu genre là MAT_THE / SINH_TON -> SURVIVOR_GRITTY_MALE
    - Nếu genre là CHUA_LANH / NGUOC_TAM -> HEALING_SOUL_FEMALE
    - Nếu genre là CUNG_DAU -> IMPERIAL_SERENE_FEMALE
    - Nếu genre là THANH_XUAN / CUU_ROI -> YOUTH_EMOTIONAL_FEMALE
    - Nếu genre là HANH_DONG -> ACTION_INTENSE_MALE
    - Mặc định: QUEEN_COLD_VENOM_FEMALE (Nữ) hoặc CEO_AUTHORITY_MALE (Nam).
    """
    g = genre.upper().strip()

    # Quét trực tiếp danh sách genre_match
    for pid, profile in VOICE_PROFILES.items():
        if preferred_gender != "auto":
            if preferred_gender == "male" and "MALE" not in pid:
                continue
            if preferred_gender == "female" and "FEMALE" not in pid:
                continue
        if g in profile.genre_match:
            return profile

    # Fallback mờ (Fuzzy matching)
    if any(k in g for k in ["KINH_DI", "MA", "QUAI_DAM", "CREEPY"]):
        return VOICE_PROFILES["HORROR_CREEPY_MALE"] if preferred_gender != "female" else VOICE_PROFILES["HORROR_WHISPER_FEMALE"]

    if any(k in g for k in ["TRINH_THAM", "HUYEN_NGHI", "DIEU_TRA", "PHAP_Y"]):
        return VOICE_PROFILES["DETECTIVE_COLD_MALE"]

    if any(k in g for k in ["SA_DIEU", "HAI", "TIENG_LONG"]):
        return VOICE_PROFILES["SATIRIC_SPARKLING_FEMALE"]

    if any(k in g for k in ["MAT_THE", "BANG_GIA", "SINH_TON", "VO_HAN"]):
        return VOICE_PROFILES["SURVIVOR_GRITTY_MALE"]

    if any(k in g for k in ["CUNG_DAU", "TRACH_DAU", "CO_PHONG"]):
        return VOICE_PROFILES["IMPERIAL_SERENE_FEMALE"]

    if any(k in g for k in ["CHUA_LANH", "HEALING", "NGUOC_TAM", "DOI_SONG"]):
        return VOICE_PROFILES["HEALING_SOUL_FEMALE"]

    if any(k in g for k in ["THANH_XUAN", "HOC_DUONG", "CUU_ROI"]):
        return VOICE_PROFILES["YOUTH_EMOTIONAL_FEMALE"]

    if any(k in g for k in ["HANH_DONG", "CUU_HO", "BIEN_SAU"]):
        return VOICE_PROFILES["ACTION_INTENSE_MALE"]

    if any(k in g for k in ["HAO_MON", "THUONG_CHIEN", "TONG_TAI"]):
        return VOICE_PROFILES["CEO_AUTHORITY_MALE"] if preferred_gender == "male" else VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]

    # Mặc định an toàn
    return VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"] if preferred_gender == "female" else VOICE_PROFILES["DETECTIVE_COLD_MALE"]


def build_genre_vocal_filter_chain(profile: VoiceProfile, voice_volume: float = 1.0) -> str:
    """
    Sinh chuỗi tham số -filter:a hoàn chỉnh của FFmpeg dựa trên VoiceProfile:
    Gồm Highpass, Warmth EQ, Scoop EQ, Clarity EQ, De-Esser, Compressor và Special Effects.
    """
    eq = profile.eq_settings
    comp = profile.compressor_settings

    chain_parts = [
        "highpass=f=75",
        f"equalizer=f={eq['warmth_freq']}:t=q:w=1.2:g={eq['warmth_gain']}",
        f"equalizer=f={eq['scoop_freq']}:t=q:w=1.5:g={eq['scoop_gain']}",
        f"equalizer=f={eq['clarity_freq']}:t=q:w=1.2:g={eq['clarity_gain']}",
        f"equalizer=f={eq['deess_freq']}:t=q:w=1.8:g={eq['deess_gain']}",
        f"acompressor=threshold={comp['threshold']}:ratio={comp['ratio']}:attack={comp['attack']}:release={comp['release']}",
    ]

    if profile.special_effects:
        chain_parts.append(profile.special_effects)

    chain_parts.append(f"volume={voice_volume}")
    return ",".join(chain_parts)


def list_all_voice_profiles_summary() -> List[Dict[str, Any]]:
    """Trả về bảng danh mục các Voice Profiles để phục vụ báo cáo và kiểm tra."""
    summary = []
    for pid, p in VOICE_PROFILES.items():
        summary.append({
            "profile_id": p.profile_id,
            "display_name": p.display_name,
            "genres": p.genre_match,
            "voice_name": p.voice_name,
            "pitch": p.pitch,
            "rate": p.rate,
            "tempo": f"{p.tempo_multiplier}x",
            "description": p.description
        })
    return summary
