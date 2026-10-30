# -*- coding: utf-8 -*-
"""
core/voice_profiles.py
Hệ Thống Ma Trận 48 Giọng Đọc Điện Ảnh & Diễn Đọc Đa Nhân Vật Chuẩn Hollywood (Cinema Vocal Studio Master Pro 4.0).
Tối ưu hóa âm học chuyên sâu bằng kết hợp 5 tầng công nghệ:
  1. Voice gốc Edge-TTS chuẩn phát thanh (Nam Minh & Hoài My).
  2. Pitch & Rate Modulation trực tiếp từ Edge-TTS (số nguyên Hz).
  3. Rubberband Studio Pitch & Formant Shifting (Công nghệ Hollywood thay đổi tuổi tác & giới tính không vỡ tiếng).
  4. Chuỗi FFmpeg Broadcast EQ, Dynamic Multi-band Compression, De-Esser & Spatial Acoustic Room.
  5. Bộ bóc tách kịch bản Đa Vai Diễn (Multi-Role Voice Acting): Tự động đổi giọng cho Nhân vật & Lời dẫn.
  6. Bộ điều biến tâm trạng cảnh quay đa chiều (Multi-Mood Scene Acoustic Modulation).
"""

import re
from dataclasses import dataclass
from typing import Dict, Any, Optional, List, Tuple


@dataclass
class VoiceProfile:
    profile_id: str
    display_name: str
    genre_match: List[str]
    voice_name: str
    pitch: str                  # Pitch gốc Edge-TTS (vd: "-4Hz", "+1Hz")
    rate: str                   # Rate gốc Edge-TTS (vd: "+0%", "+3%")
    volume: str                 # Volume Edge-TTS (vd: "+0%", "+2%")
    tempo_multiplier: float     # Tốc độ đọc FFmpeg tổng
    description: str
    eq_settings: Dict[str, Any]
    compressor_settings: Dict[str, Any]
    special_effects: Optional[str] = None
    rubberband_pitch: Optional[float] = None  # Hệ số Rubberband Pitch (vd: 0.82 đến 1.25)


# ==============================================================================
# MA TRẬN 48 GIỌNG ĐỌC ĐIỆN ẢNH ĐỘC BẢN (48 UNIQUE CINEMA VOICE CAST)
# ==============================================================================
VOICE_PROFILES: Dict[str, VoiceProfile] = {
    # --------------------------------------------------------------------------
    # --- [NHÓM 1: NAM CHÍNH & DẪN CHUYỆN NAM - 14 GIỌNG ĐỘC BẢN] ---
    # --------------------------------------------------------------------------
    "DETECTIVE_COLD_MALE": VoiceProfile(
        profile_id="DETECTIVE_COLD_MALE",
        display_name="Nam Minh - Thám Tử Lạnh Lùng",
        genre_match=["HUYEN_NGHI", "TRINH_THAM", "PHAP_Y", "TOI_PHAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="-2%", volume="-14%", tempo_multiplier=1.0,
        rubberband_pitch=0.96,
        description="Trầm, đặc, uy nghiêm, bí ẩn, nhấn nhá đanh thép như trong phòng thẩm vấn hiện trường.",
        eq_settings={"warmth_freq": 110, "warmth_gain": 4.5, "scoop_freq": 800, "scoop_gain": -2.5, "clarity_freq": 3200, "clarity_gain": 3.8, "deess_freq": 6500, "deess_gain": -2.5},
        compressor_settings={"threshold": "-19dB", "ratio": 3.6, "attack": 10, "release": 70},
        special_effects="stereotools=mpan=-0.02"
    ),

    "HORROR_CREEPY_MALE": VoiceProfile(
        profile_id="HORROR_CREEPY_MALE",
        display_name="Nam Minh - Quái Đàm Âm U",
        genre_match=["KINH_DI", "QUAI_DAM", "CREEPYPASTA"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-4Hz", rate="-4%", volume="-14%", tempo_multiplier=1.0,
        rubberband_pitch=0.91,
        description="Lạnh buốt, ma mị, âm u, trầm sát màng nhĩ tạo cảm giác rợn gáy trong bóng tối.",
        eq_settings={"warmth_freq": 90, "warmth_gain": 5.0, "scoop_freq": 1000, "scoop_gain": -3.0, "clarity_freq": 2800, "clarity_gain": 2.5, "deess_freq": 6000, "deess_gain": -3.5},
        compressor_settings={"threshold": "-21dB", "ratio": 4.2, "attack": 15, "release": 90},
        special_effects="lowpass=f=6800"
    ),

    "SURVIVOR_GRITTY_MALE": VoiceProfile(
        profile_id="SURVIVOR_GRITTY_MALE",
        display_name="Nam Minh - Chiến Binh Sinh Tồn",
        genre_match=["MAT_THE", "BANG_GIA", "SINH_TON", "VO_HAN"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+1%", volume="-14%", tempo_multiplier=1.0,
        rubberband_pitch=0.98,
        description="Gấp gáp, nghẹt thở, sắt đá, cương quyết giữa bão tuyết và đếm ngược sinh tử.",
        eq_settings={"warmth_freq": 150, "warmth_gain": 4.0, "scoop_freq": 900, "scoop_gain": -2.0, "clarity_freq": 2600, "clarity_gain": 4.2, "deess_freq": 6500, "deess_gain": -2.0},
        compressor_settings={"threshold": "-16dB", "ratio": 4.5, "attack": 4, "release": 50}
    ),

    "CEO_AUTHORITY_MALE": VoiceProfile(
        profile_id="CEO_AUTHORITY_MALE",
        display_name="Nam Minh - Tổng Tài Quyền Lực",
        genre_match=["HAO_MON", "THUONG_CHIEN", "TAI_CHINH"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+1%", volume="+2%", tempo_multiplier=1.15,
        rubberband_pitch=0.95,
        description="Đĩnh đạc, trầm ổn, làm chủ cuộc chơi tài chính, chuẩn phong thái phòng họp 60 tầng.",
        eq_settings={"warmth_freq": 135, "warmth_gain": 4.2, "scoop_freq": 1000, "scoop_gain": -2.2, "clarity_freq": 3400, "clarity_gain": 3.6, "deess_freq": 6400, "deess_gain": -2.2},
        compressor_settings={"threshold": "-17dB", "ratio": 3.8, "attack": 7, "release": 60}
    ),

    "ACTION_INTENSE_MALE": VoiceProfile(
        profile_id="ACTION_INTENSE_MALE",
        display_name="Nam Minh - Chỉ Huy Thép",
        genre_match=["HANH_DONG", "CUU_HO", "BIEN_SAU", "HANG_DONG", "CAP_TREO"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+4%", volume="+2%", tempo_multiplier=1.20,
        rubberband_pitch=0.97,
        description="Mạnh mẽ, dồn dập, tiếng hô đanh thép hiệu triệu giữa cuồng phong và giàn khoan biển sâu.",
        eq_settings={"warmth_freq": 130, "warmth_gain": 4.5, "scoop_freq": 950, "scoop_gain": -2.2, "clarity_freq": 3100, "clarity_gain": 4.2, "deess_freq": 6500, "deess_gain": -2.2},
        compressor_settings={"threshold": "-15dB", "ratio": 4.8, "attack": 3, "release": 45}
    ),

    "YOUTH_HERO_MALE": VoiceProfile(
        profile_id="YOUTH_HERO_MALE",
        display_name="Nam Minh - Nam Sinh Nhiệt Huyết",
        genre_match=["HOC_DUONG_NAM", "THI_DAU_NAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="+1Hz", rate="+3%", volume="+1%", tempo_multiplier=1.14,
        rubberband_pitch=1.04,
        description="Trẻ trung, đầy sinh lực, thông minh kiên định, hào quang thủ khoa khoa học.",
        eq_settings={"warmth_freq": 170, "warmth_gain": 3.0, "scoop_freq": 1100, "scoop_gain": -1.8, "clarity_freq": 3500, "clarity_gain": 3.5, "deess_freq": 6600, "deess_gain": -2.0},
        compressor_settings={"threshold": "-18dB", "ratio": 3.2, "attack": 8, "release": 60}
    ),

    "COLD_SURGEON_MALE": VoiceProfile(
        profile_id="COLD_SURGEON_MALE",
        display_name="Nam Minh - Bác Sĩ Ngoại Khoa Vi Phẫu",
        genre_match=["Y_KHOA_NAM", "NGOAI_KHOA", "CAP_CUU"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="+0%", volume="+1%", tempo_multiplier=1.12,
        rubberband_pitch=0.94,
        description="Lạnh lùng, điềm tĩnh tuyệt đối trước lằn ranh sinh tử, dứt khoát như đường dao mổ vi phẫu.",
        eq_settings={"warmth_freq": 125, "warmth_gain": 4.0, "scoop_freq": 920, "scoop_gain": -2.2, "clarity_freq": 3300, "clarity_gain": 4.0, "deess_freq": 6500, "deess_gain": -2.6},
        compressor_settings={"threshold": "-18dB", "ratio": 3.6, "attack": 6, "release": 65}
    ),

    "OCEAN_NAVIGATOR_MALE": VoiceProfile(
        profile_id="OCEAN_NAVIGATOR_MALE",
        display_name="Nam Minh - Hoa Tiêu Viễn Dương",
        genre_match=["HANG_HAI", "TAU_CONTAINER", "BAO_BIEN"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="+2%", volume="+2%", tempo_multiplier=1.16,
        rubberband_pitch=0.93,
        description="Vang rền, dày ấm, uy lực chỉ huy con tàu container vượt qua tâm bão cấp mười bốn.",
        eq_settings={"warmth_freq": 115, "warmth_gain": 4.8, "scoop_freq": 850, "scoop_gain": -2.5, "clarity_freq": 3000, "clarity_gain": 4.2, "deess_freq": 6400, "deess_gain": -2.2},
        compressor_settings={"threshold": "-16dB", "ratio": 4.0, "attack": 5, "release": 55}
    ),

    "ARCTIC_RADAR_MALE": VoiceProfile(
        profile_id="ARCTIC_RADAR_MALE",
        display_name="Nam Minh - Kỹ Sư Trạm Radar Cực Bắc",
        genre_match=["KHI_TUONG", "CUC_BAC", "BANG_TUYET"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="+1%", volume="+1%", tempo_multiplier=1.13,
        rubberband_pitch=0.95,
        description="Rắn rỏi, buốt giá, chuẩn xác từng tọa độ radar trước trận bão từ âm năm mươi độ.",
        eq_settings={"warmth_freq": 130, "warmth_gain": 4.0, "scoop_freq": 980, "scoop_gain": -2.0, "clarity_freq": 3400, "clarity_gain": 3.8, "deess_freq": 6500, "deess_gain": -2.4},
        compressor_settings={"threshold": "-17dB", "ratio": 3.6, "attack": 7, "release": 60}
    ),

    "MIDNIGHT_STORYTELLER_MALE": VoiceProfile(
        profile_id="MIDNIGHT_STORYTELLER_MALE",
        display_name="Nam Minh - Người Kể Chuyện Đêm Khuya",
        genre_match=["PODCAST_DEM", "TAM_SU_NAM", "CHIEM_NGHIEM", "PODCAST"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-4Hz", rate="-5%", volume="+0%", tempo_multiplier=1.02,
        rubberband_pitch=0.92,
        description="Thì thầm truyền cảm, sâu lắng, ấm áp, vỗ về tâm can trong đêm tĩnh mịch.",
        eq_settings={"warmth_freq": 105, "warmth_gain": 5.0, "scoop_freq": 1100, "scoop_gain": -2.8, "clarity_freq": 2800, "clarity_gain": 2.5, "deess_freq": 6200, "deess_gain": -3.2},
        compressor_settings={"threshold": "-20dB", "ratio": 3.0, "attack": 15, "release": 90},
        special_effects="equalizer=f=80:t=q:w=1.0:g=3.0"
    ),

    "CYBER_FORENSIC_MALE": VoiceProfile(
        profile_id="CYBER_FORENSIC_MALE",
        display_name="Nam Minh - Chuyên Viên Điều Tra An Ninh Mạng",
        genre_match=["AN_NINH_MANG", "DEEPFAKE", "BTS_LAU", "BLOCKCHAIN", "CONG_NGHE_CAO"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+2%", volume="+1%", tempo_multiplier=1.16,
        rubberband_pitch=0.97,
        description="Trầm tĩnh, nhịp gãy gọn, phân tích logic sắc bén bóc trần bẫy Deepfake và trạm BTS lậu.",
        eq_settings={"warmth_freq": 130, "warmth_gain": 3.8, "scoop_freq": 1000, "scoop_gain": -2.0, "clarity_freq": 3400, "clarity_gain": 4.0, "deess_freq": 6500, "deess_gain": -2.2},
        compressor_settings={"threshold": "-17dB", "ratio": 3.6, "attack": 6, "release": 55}
    ),

    "ANTIQUE_APPRAISER_MALE": VoiceProfile(
        profile_id="ANTIQUE_APPRAISER_MALE",
        display_name="Nam Minh - Chuyên Gia Giám Định Cổ Vật",
        genre_match=["GIAM_DINH", "CO_VAT_NAM", "NGOC_QUY", "DO_CO"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="-2%", volume="+1%", tempo_multiplier=1.09,
        rubberband_pitch=0.93,
        description="Thong thả, đĩnh đạc, ấm áp chiều sâu lịch sử, từng lời khẳng định giá trị bảo vật nghìn năm.",
        eq_settings={"warmth_freq": 110, "warmth_gain": 4.5, "scoop_freq": 950, "scoop_gain": -2.4, "clarity_freq": 3000, "clarity_gain": 3.6, "deess_freq": 6300, "deess_gain": -2.5},
        compressor_settings={"threshold": "-18dB", "ratio": 3.4, "attack": 10, "release": 75}
    ),

    "FLIGHT_CONTROLLER_MALE": VoiceProfile(
        profile_id="FLIGHT_CONTROLLER_MALE",
        display_name="Nam Minh - Trực Ban Kiểm Soát Không Lưu",
        genre_match=["KHONG_LUU", "HANG_KHONG", "RADAR_BAY"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+4%", volume="+2%", tempo_multiplier=1.19,
        rubberband_pitch=0.96,
        description="Dứt khoát, chuẩn xác từng giây, giọng chuẩn tần số vô tuyến điều phối máy bay trong dông bão.",
        eq_settings={"warmth_freq": 140, "warmth_gain": 4.0, "scoop_freq": 900, "scoop_gain": -2.2, "clarity_freq": 3500, "clarity_gain": 4.2, "deess_freq": 6600, "deess_gain": -2.0},
        compressor_settings={"threshold": "-16dB", "ratio": 4.4, "attack": 4, "release": 45},
        special_effects="highpass=f=120,equalizer=f=2500:t=q:w=1.0:g=2.0"
    ),

    "BIOHAZARD_SCIENTIST_MALE": VoiceProfile(
        profile_id="BIOHAZARD_SCIENTIST_MALE",
        display_name="Nam Minh - Nhà Khoa Học Vi Sinh BSL-4",
        genre_match=["VI_SINH", "PHONG_THI_NGHIEM", "BSL4", "DICH_BENH"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="+1%", volume="+1%", tempo_multiplier=1.13,
        rubberband_pitch=0.94,
        description="Lạnh lùng, tập trung cao độ, đanh thép trong buồng áp lực âm cách ly mầm bệnh nguy hiểm.",
        eq_settings={"warmth_freq": 120, "warmth_gain": 4.2, "scoop_freq": 960, "scoop_gain": -2.5, "clarity_freq": 3200, "clarity_gain": 4.0, "deess_freq": 6400, "deess_gain": -2.6},
        compressor_settings={"threshold": "-17dB", "ratio": 3.8, "attack": 6, "release": 60}
    ),

    # --------------------------------------------------------------------------
    # --- [NHÓM 2: NHÂN VẬT ĐẶC THÙ NAM (CHARACTER ROLES) - 10 GIỌNG ĐỘC BẢN] ---
    # --------------------------------------------------------------------------
    "ELDER_PATRIARCH_MALE": VoiceProfile(
        profile_id="ELDER_PATRIARCH_MALE",
        display_name="Nam Minh - Trưởng Bối / Lão Gia Thâm Sâu",
        genre_match=["LAO_GIA", "TRUONG_BOI"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-5Hz", rate="-6%", volume="+0%", tempo_multiplier=1.02,
        rubberband_pitch=0.86,
        description="Giọng người già từng trải, khàn đặc, thâm sâu, mỗi lời thốt ra nặng tựa ngàn cân.",
        eq_settings={"warmth_freq": 100, "warmth_gain": 5.2, "scoop_freq": 900, "scoop_gain": -3.5, "clarity_freq": 2400, "clarity_gain": 3.0, "deess_freq": 5800, "deess_gain": -3.0},
        compressor_settings={"threshold": "-20dB", "ratio": 4.0, "attack": 15, "release": 85}
    ),

    "DARK_VILLAIN_MALE": VoiceProfile(
        profile_id="DARK_VILLAIN_MALE",
        display_name="Nam Minh - Kẻ Săn Mồi / Ác Nhân Gằn Giọng",
        genre_match=["PHAN_DIEN_NAM", "TRUM_CUOI"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-4Hz", rate="+1%", volume="+2%", tempo_multiplier=1.14,
        rubberband_pitch=0.90,
        description="Gằn giọng, nguy hiểm, tàn nhẫn, đe dọa trực diện với nụ cười lạnh rợn người.",
        eq_settings={"warmth_freq": 120, "warmth_gain": 4.8, "scoop_freq": 850, "scoop_gain": -2.8, "clarity_freq": 3300, "clarity_gain": 4.0, "deess_freq": 6300, "deess_gain": -2.5},
        compressor_settings={"threshold": "-16dB", "ratio": 4.5, "attack": 5, "release": 50}
    ),

    "GHOST_WHISPER_MALE": VoiceProfile(
        profile_id="GHOST_WHISPER_MALE",
        display_name="Nam Minh - Bóng Ma Tầng Hầm",
        genre_match=["OAN_LINH", "BONG_MA"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-6Hz", rate="-8%", volume="-1%", tempo_multiplier=0.98,
        rubberband_pitch=0.82,
        description="Rỉ rả như phát ra từ kẽ tường ẩm mốc hoặc máy ghi âm hỏng.",
        eq_settings={"warmth_freq": 85, "warmth_gain": 5.5, "scoop_freq": 1200, "scoop_gain": -4.0, "clarity_freq": 2200, "clarity_gain": 2.0, "deess_freq": 5500, "deess_gain": -4.0},
        compressor_settings={"threshold": "-22dB", "ratio": 5.0, "attack": 20, "release": 100},
        special_effects="lowpass=f=6000,echo=0.8:0.88:30:0.4"
    ),

    "NERDY_HACKER_MALE": VoiceProfile(
        profile_id="NERDY_HACKER_MALE",
        display_name="Nam Minh - Kỹ Sư Công Nghệ Thông Tin",
        genre_match=["CONG_NGHE", "HACKER"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-1Hz", rate="+5%", volume="+1%", tempo_multiplier=1.20,
        rubberband_pitch=1.02,
        description="Nhanh, gãy gọn, tập trung cao độ, chuẩn nhịp gõ bàn phím dữ liệu.",
        eq_settings={"warmth_freq": 140, "warmth_gain": 3.5, "scoop_freq": 1000, "scoop_gain": -2.0, "clarity_freq": 3600, "clarity_gain": 4.0, "deess_freq": 6600, "deess_gain": -2.0},
        compressor_settings={"threshold": "-16dB", "ratio": 3.5, "attack": 5, "release": 50}
    ),

    "WISE_OLD_SAGE_MALE": VoiceProfile(
        profile_id="WISE_OLD_SAGE_MALE",
        display_name="Nam Minh - Cụ Già Triết Nhân Cổ Đạo",
        genre_match=["CO_DAO", "AN_SI"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-5Hz", rate="-7%", volume="+0%", tempo_multiplier=0.99,
        rubberband_pitch=0.84,
        description="Thong thả, thâm trầm, đúc kết sự đời như cổ thụ nghìn năm đón nắng chiều.",
        eq_settings={"warmth_freq": 95, "warmth_gain": 5.0, "scoop_freq": 950, "scoop_gain": -3.2, "clarity_freq": 2500, "clarity_gain": 3.0, "deess_freq": 5900, "deess_gain": -3.0},
        compressor_settings={"threshold": "-20dB", "ratio": 3.8, "attack": 14, "release": 80}
    ),

    "SATIRIC_INTERNAL_MALE": VoiceProfile(
        profile_id="SATIRIC_INTERNAL_MALE",
        display_name="Nam Minh - Tiếng Lòng Nam Chính Trào Phúng",
        genre_match=["SA_DIEU_NAM", "HAI_HUOC_NAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="+1Hz", rate="+4%", volume="+1%", tempo_multiplier=1.18,
        rubberband_pitch=1.03,
        description="Hài hước, tếu táo, độc thoại dở khóc dở cười trước các tình huống oái oăm.",
        eq_settings={"warmth_freq": 160, "warmth_gain": 3.0, "scoop_freq": 1050, "scoop_gain": -1.8, "clarity_freq": 3600, "clarity_gain": 3.8, "deess_freq": 6700, "deess_gain": -2.0},
        compressor_settings={"threshold": "-17dB", "ratio": 3.0, "attack": 6, "release": 50}
    ),

    "DEEP_CAVE_DIVER_MALE": VoiceProfile(
        profile_id="DEEP_CAVE_DIVER_MALE",
        display_name="Nam Minh - Thợ Lặn Hang Động Sâu",
        genre_match=["THO_LAN", "CUU_HO_NGAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-4Hz", rate="-1%", volume="+1%", tempo_multiplier=1.10,
        rubberband_pitch=0.89,
        description="Trầm nặng, tiếng thở nghẹt qua buồng áp suất bình dưỡng khí sâu 80 mét.",
        eq_settings={"warmth_freq": 105, "warmth_gain": 4.6, "scoop_freq": 880, "scoop_gain": -2.6, "clarity_freq": 2900, "clarity_gain": 3.6, "deess_freq": 6200, "deess_gain": -2.8},
        compressor_settings={"threshold": "-18dB", "ratio": 4.2, "attack": 8, "release": 70},
        special_effects="equalizer=f=250:t=q:w=1.5:g=2.5"
    ),

    "CRIME_BOSS_CALM_MALE": VoiceProfile(
        profile_id="CRIME_BOSS_CALM_MALE",
        display_name="Nam Minh - Trùm Tài Phiệt Ngầm",
        genre_match=["TRUM_TAI_PHIET", "NGAM"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-3Hz", rate="-3%", volume="+2%", tempo_multiplier=1.09,
        rubberband_pitch=0.92,
        description="Điềm tĩnh đến rợn tóc gáy, giọng mượt như nhung nhưng giấu nanh vuốt sau từng câu chữ.",
        eq_settings={"warmth_freq": 115, "warmth_gain": 4.5, "scoop_freq": 900, "scoop_gain": -2.4, "clarity_freq": 3300, "clarity_gain": 3.8, "deess_freq": 6400, "deess_gain": -2.4},
        compressor_settings={"threshold": "-17dB", "ratio": 4.0, "attack": 8, "release": 65}
    ),

    "RESCUE_PILOT_MALE": VoiceProfile(
        profile_id="RESCUE_PILOT_MALE",
        display_name="Nam Minh - Phi Công Trực Thăng Cứu Nạn",
        genre_match=["PHI_CONG_CUU_HO", "TRUC_THANG", "SAT_LO"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-2Hz", rate="+5%", volume="+2%", tempo_multiplier=1.20,
        rubberband_pitch=0.95,
        description="Hơi thở dồn dập, gầm vang át tiếng cánh quạt trực thăng cứu hộ giữa tâm bão sạt lở.",
        eq_settings={"warmth_freq": 135, "warmth_gain": 4.6, "scoop_freq": 880, "scoop_gain": -2.4, "clarity_freq": 3300, "clarity_gain": 4.5, "deess_freq": 6500, "deess_gain": -2.2},
        compressor_settings={"threshold": "-15dB", "ratio": 4.8, "attack": 3, "release": 40}
    ),

    "BLACKSMITH_MASTER_MALE": VoiceProfile(
        profile_id="BLACKSMITH_MASTER_MALE",
        display_name="Nam Minh - Nghệ Nhân Rèn Kiếm Truyền Thống",
        genre_match=["LUYEN_KIM", "REN_KIEM", "THO_REN"],
        voice_name="vi-VN-NamMinhNeural",
        pitch="-5Hz", rate="-4%", volume="+2%", tempo_multiplier=1.07,
        rubberband_pitch=0.88,
        description="Khàn đục, vang rền, uy lực như tiếng búa nện trên đe thép nung đỏ nghìn độ.",
        eq_settings={"warmth_freq": 95, "warmth_gain": 5.5, "scoop_freq": 920, "scoop_gain": -3.0, "clarity_freq": 2600, "clarity_gain": 3.5, "deess_freq": 6000, "deess_gain": -2.8},
        compressor_settings={"threshold": "-17dB", "ratio": 4.2, "attack": 8, "release": 65}
    ),

    # --------------------------------------------------------------------------
    # --- [NHÓM 3: NỮ CHÍNH & DẪN CHUYỆN NỮ - 14 GIỌNG ĐỘC BẢN] ---
    # --------------------------------------------------------------------------
    "QUEEN_COLD_VENOM_FEMALE": VoiceProfile(
        profile_id="QUEEN_COLD_VENOM_FEMALE",
        display_name="Hoài My - Nữ Chủ Tự Sự Điềm Tĩnh",
        genre_match=["ME_CHONG", "GIA_DAU", "VA_MAT", "TRONG_SINH", "HOAN_DOI"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="+0%", volume="-16%", tempo_multiplier=1.0,
        rubberband_pitch=1.00,
        description="Điềm đạm, êm dịu, ấm áp, sâu sắc, giọng nhẹ nhàng không chói gắt.",
        eq_settings={"warmth_freq": 180, "warmth_gain": 3.8, "scoop_freq": 1150, "scoop_gain": -2.2, "clarity_freq": 3200, "clarity_gain": 2.2, "deess_freq": 6800, "deess_gain": -3.2},
        compressor_settings={"threshold": "-18dB", "ratio": 2.8, "attack": 8, "release": 65}
    ),

    "SATIRIC_SPARKLING_FEMALE": VoiceProfile(
        profile_id="SATIRIC_SPARKLING_FEMALE",
        display_name="Hoài My - Tiếng Lòng Tinh Quái",
        genre_match=["SA_DIEU", "HAI_HUOC", "TIENG_LONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+0Hz", rate="+2%", volume="-14%", tempo_multiplier=1.0,
        rubberband_pitch=1.04,
        description="Nhí nhảnh, nảy tiếng, tinh nghịch, lém lỉnh, gây cười giòn giã khi bóc phốt sếp.",
        eq_settings={"warmth_freq": 220, "warmth_gain": 2.2, "scoop_freq": 1300, "scoop_gain": -1.5, "clarity_freq": 3600, "clarity_gain": 3.0, "deess_freq": 7000, "deess_gain": -2.5},
        compressor_settings={"threshold": "-16dB", "ratio": 2.6, "attack": 5, "release": 45},
        special_effects="equalizer=f=8000:t=q:w=1.0:g=1.2"
    ),

    "IMPERIAL_SERENE_FEMALE": VoiceProfile(
        profile_id="IMPERIAL_SERENE_FEMALE",
        display_name="Hoài My - Thâm Cung Trầm Mặc",
        genre_match=["CUNG_DAU", "TRACH_DAU", "CO_PHONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="-1%", volume="-15%", tempo_multiplier=1.0,
        rubberband_pitch=0.96,
        description="Ung dung, thâm sâu, êm ái như tơ lụa nhưng ẩn chứa độc dược và trâm bạc thử độc.",
        eq_settings={"warmth_freq": 180, "warmth_gain": 3.6, "scoop_freq": 1150, "scoop_gain": -2.2, "clarity_freq": 3300, "clarity_gain": 2.5, "deess_freq": 6400, "deess_gain": -2.6},
        compressor_settings={"threshold": "-18dB", "ratio": 3.0, "attack": 9, "release": 65}
    ),

    "HEALING_SOUL_FEMALE": VoiceProfile(
        profile_id="HEALING_SOUL_FEMALE",
        display_name="Hoài My - Chữa Lành Êm Dịu",
        genre_match=["CHUA_LANH", "DOI_SONG", "HEALING", "NGUOC_TAM"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-2Hz", rate="-2%", volume="-18%", tempo_multiplier=1.0,
        rubberband_pitch=0.98,
        description="Thủ thỉ, ấm áp, sâu lắng, vỗ về tâm hồn người nghe trong đêm vắng.",
        eq_settings={"warmth_freq": 160, "warmth_gain": 4.2, "scoop_freq": 1200, "scoop_gain": -2.0, "clarity_freq": 2800, "clarity_gain": 2.0, "deess_freq": 6500, "deess_gain": -3.5},
        compressor_settings={"threshold": "-20dB", "ratio": 2.8, "attack": 12, "release": 80},
        special_effects="equalizer=f=7500:t=q:w=1.5:g=-2.0"
    ),

    "YOUTH_EMOTIONAL_FEMALE": VoiceProfile(
        profile_id="YOUTH_EMOTIONAL_FEMALE",
        display_name="Hoài My - Thanh Xuân Trong Sáng",
        genre_match=["THANH_XUAN", "CUU_ROI", "HOC_DUONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="+1%", volume="-15%", tempo_multiplier=1.0,
        rubberband_pitch=1.01,
        description="Trong trẻo, giàu cảm xúc, nhiệt huyết tuổi trẻ, tha thiết vươn lên bảo vệ công lý.",
        eq_settings={"warmth_freq": 200, "warmth_gain": 2.5, "scoop_freq": 1250, "scoop_gain": -1.8, "clarity_freq": 3400, "clarity_gain": 2.8, "deess_freq": 6600, "deess_gain": -2.8},
        compressor_settings={"threshold": "-18dB", "ratio": 2.8, "attack": 8, "release": 60}
    ),

    "HORROR_WHISPER_FEMALE": VoiceProfile(
        profile_id="HORROR_WHISPER_FEMALE",
        display_name="Hoài My - Thì Thào Lạnh Gáy",
        genre_match=["KINH_DI_NU", "QUAI_DAM_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-2Hz", rate="-4%", volume="-16%", tempo_multiplier=1.0,
        rubberband_pitch=0.94,
        description="Giọng nữ thì thào, lạnh ngắt, tạo cảm giác có người đang thở ngay sau gáy.",
        eq_settings={"warmth_freq": 160, "warmth_gain": 3.5, "scoop_freq": 1200, "scoop_gain": -2.0, "clarity_freq": 3200, "clarity_gain": 2.5, "deess_freq": 6200, "deess_gain": -3.0},
        compressor_settings={"threshold": "-20dB", "ratio": 3.8, "attack": 12, "release": 80},
        special_effects="lowpass=f=7000"
    ),

    "LITIGATOR_SHARP_FEMALE": VoiceProfile(
        profile_id="LITIGATOR_SHARP_FEMALE",
        display_name="Hoài My - Nữ Luật Sư Tranh Tụng Đanh Thép",
        genre_match=["PHAP_LY_NU", "TOA_AN", "KHE_UOC", "PHAP_LY"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+1Hz", rate="+3%", volume="+2%", tempo_multiplier=1.17,
        rubberband_pitch=1.02,
        description="Đanh thép, chuẩn xác từng điều khoản luật, sắc sảo bóc trần hợp đồng giả mạo trước vành móng ngựa.",
        eq_settings={"warmth_freq": 195, "warmth_gain": 3.0, "scoop_freq": 1150, "scoop_gain": -2.0, "clarity_freq": 4100, "clarity_gain": 4.4, "deess_freq": 6700, "deess_gain": -2.8},
        compressor_settings={"threshold": "-16dB", "ratio": 3.8, "attack": 5, "release": 50}
    ),

    "FORENSIC_AUDITOR_FEMALE": VoiceProfile(
        profile_id="FORENSIC_AUDITOR_FEMALE",
        display_name="Hoài My - Nữ Kiểm Toán Tử Huyệt Vốn",
        genre_match=["KIEM_TOAN", "TAI_CHINH_NU", "THI_TRUONG_VON"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+0Hz", rate="+1%", volume="+1%", tempo_multiplier=1.15,
        rubberband_pitch=0.99,
        description="Lạnh lùng, rành rọt, từng con số kiểm toán bóc trần dòng tiền bẩn và phong tỏa tài khoản tức thì.",
        eq_settings={"warmth_freq": 190, "warmth_gain": 3.2, "scoop_freq": 1100, "scoop_gain": -2.1, "clarity_freq": 3900, "clarity_gain": 4.0, "deess_freq": 6600, "deess_gain": -2.6},
        compressor_settings={"threshold": "-17dB", "ratio": 3.5, "attack": 6, "release": 55}
    ),

    "ANCIENT_ARCHIVIST_FEMALE": VoiceProfile(
        profile_id="ANCIENT_ARCHIVIST_FEMALE",
        display_name="Hoài My - Nữ Phục Chế Cổ Thư",
        genre_match=["PHUC_CHE", "CO_THU", "DI_THAO"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="-2%", volume="+0%", tempo_multiplier=1.08,
        rubberband_pitch=0.97,
        description="Trang nhã, êm đềm, thanh tao như mực nho trên giấy dó, nâng niu từng di vật lịch sử.",
        eq_settings={"warmth_freq": 175, "warmth_gain": 3.8, "scoop_freq": 1200, "scoop_gain": -2.2, "clarity_freq": 3200, "clarity_gain": 3.2, "deess_freq": 6400, "deess_gain": -2.8},
        compressor_settings={"threshold": "-19dB", "ratio": 3.0, "attack": 10, "release": 70}
    ),

    "CELEBRITY_DIVA_FEMALE": VoiceProfile(
        profile_id="CELEBRITY_DIVA_FEMALE",
        display_name="Hoài My - Nữ Minh Tinh Kiêu Kỳ",
        genre_match=["SHOWBIZ", "GIOI_GIAI_TRI", "MINH_TINH"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+2Hz", rate="+4%", volume="+2%", tempo_multiplier=1.18,
        rubberband_pitch=1.05,
        description="Sang chảnh, kiêu kỳ, thâm thúy, thần thái thảm đỏ thượng lưu bóc phốt trà xanh showbiz.",
        eq_settings={"warmth_freq": 220, "warmth_gain": 2.2, "scoop_freq": 1200, "scoop_gain": -1.8, "clarity_freq": 4400, "clarity_gain": 4.2, "deess_freq": 6900, "deess_gain": -2.5},
        compressor_settings={"threshold": "-16dB", "ratio": 3.4, "attack": 5, "release": 48}
    ),

    "INVESTIGATIVE_JOURNALIST_FEMALE": VoiceProfile(
        profile_id="INVESTIGATIVE_JOURNALIST_FEMALE",
        display_name="Hoài My - Nữ Phóng Viên Điều Tra Hiện Trường",
        genre_match=["DIEU_TRA_XA_HOI", "PHONG_SU", "BUON_NGUOI", "LUA_DAO_BIEN_GIOI", "CAM_BAY_XA_HOI"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+1Hz", rate="+3%", volume="+2%", tempo_multiplier=1.17,
        rubberband_pitch=1.01,
        description="Cương trực, sắc sảo, dấn thân, vạch trần bẫy việc nhẹ lương cao và sào huyệt lừa đảo công nghệ.",
        eq_settings={"warmth_freq": 200, "warmth_gain": 3.0, "scoop_freq": 1100, "scoop_gain": -2.0, "clarity_freq": 4200, "clarity_gain": 4.6, "deess_freq": 6700, "deess_gain": -2.6},
        compressor_settings={"threshold": "-16dB", "ratio": 3.8, "attack": 5, "release": 50}
    ),

    "MICHELIN_CHEF_FEMALE": VoiceProfile(
        profile_id="MICHELIN_CHEF_FEMALE",
        display_name="Hoài My - Bếp Trưởng Michelin Tinh Tế",
        genre_match=["AM_THUC", "MICHELIN", "BEP_TRUONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="+1%", volume="+1%", tempo_multiplier=1.14,
        rubberband_pitch=0.98,
        description="Sang trọng, chỉn chu, quyền uy và tinh tế từng sắc thái vị giác trong căn bếp năm sao.",
        eq_settings={"warmth_freq": 190, "warmth_gain": 3.4, "scoop_freq": 1200, "scoop_gain": -2.0, "clarity_freq": 3800, "clarity_gain": 3.8, "deess_freq": 6600, "deess_gain": -2.6},
        compressor_settings={"threshold": "-17dB", "ratio": 3.2, "attack": 7, "release": 60}
    ),

    "SPACE_COMM_FEMALE": VoiceProfile(
        profile_id="SPACE_COMM_FEMALE",
        display_name="Hoài My - Kỹ Sư Viễn Thông Vệ Tinh Quỹ Đạo",
        genre_match=["VIEN_THONG_KHONG_GIAN", "VE_TINH", "KHONG_GIAN"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+1Hz", rate="+0%", volume="+1%", tempo_multiplier=1.11,
        rubberband_pitch=1.02,
        description="Trong vắt, tĩnh tại, chuẩn nhịp sóng truyền thông tín hiệu vũ trụ không gian vô tận.",
        eq_settings={"warmth_freq": 210, "warmth_gain": 2.8, "scoop_freq": 1300, "scoop_gain": -1.8, "clarity_freq": 4100, "clarity_gain": 3.8, "deess_freq": 6800, "deess_gain": -2.4},
        compressor_settings={"threshold": "-18dB", "ratio": 3.0, "attack": 8, "release": 65},
        special_effects="equalizer=f=6000:t=q:w=1.2:g=2.0"
    ),

    "ANCIENT_POETESS_FEMALE": VoiceProfile(
        profile_id="ANCIENT_POETESS_FEMALE",
        display_name="Hoài My - Nữ Thi Sĩ Cung Cấm Trữ Tình",
        genre_match=["THI_TU_CUNG_DINH", "NGU_THIEN_NU", "CO_PHONG_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="-3%", volume="+0%", tempo_multiplier=1.07,
        rubberband_pitch=0.96,
        description="Dịu dàng, u hoài, âm vận êm như tiếng đàn tranh đêm trăng giữa chốn thâm cung.",
        eq_settings={"warmth_freq": 175, "warmth_gain": 3.8, "scoop_freq": 1200, "scoop_gain": -2.2, "clarity_freq": 3200, "clarity_gain": 3.2, "deess_freq": 6400, "deess_gain": -2.8},
        compressor_settings={"threshold": "-19dB", "ratio": 3.0, "attack": 10, "release": 70}
    ),

    # --------------------------------------------------------------------------
    # --- [NHÓM 4: NHÂN VẬT ĐẶC THÙ NỮ (CHARACTER ROLES) - 10 GIỌNG ĐỘC BẢN] ---
    # --------------------------------------------------------------------------
    "HARSH_MATRIARCH_FEMALE": VoiceProfile(
        profile_id="HARSH_MATRIARCH_FEMALE",
        display_name="Hoài My - Mẹ Chồng Cay Nghiệt The Thé",
        genre_match=["ME_CHONG_AC", "PHAN_DIEN_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+3Hz", rate="+4%", volume="+2%", tempo_multiplier=1.18,
        rubberband_pitch=1.12,
        description="The thé, chua ngoa, cao giọng đay nghiến khinh miệt từng từ.",
        eq_settings={"warmth_freq": 220, "warmth_gain": 1.5, "scoop_freq": 1000, "scoop_gain": -2.5, "clarity_freq": 4500, "clarity_gain": 5.0, "deess_freq": 7000, "deess_gain": -3.5},
        compressor_settings={"threshold": "-15dB", "ratio": 4.2, "attack": 4, "release": 45}
    ),

    "SWEET_TRAITOR_FEMALE": VoiceProfile(
        profile_id="SWEET_TRAITOR_FEMALE",
        display_name="Hoài My - Trà Xanh Ngọt Xớt",
        genre_match=["TRA_XANH", "BACH_LIEN_HOA"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+4Hz", rate="+3%", volume="+1%", tempo_multiplier=1.14,
        rubberband_pitch=1.10,
        description="Giả nai, ngọt ngào giả tạo, nũng nịu nhưng tâm địa thâm độc.",
        eq_settings={"warmth_freq": 260, "warmth_gain": 2.2, "scoop_freq": 1400, "scoop_gain": -1.5, "clarity_freq": 4400, "clarity_gain": 3.8, "deess_freq": 6800, "deess_gain": -2.2},
        compressor_settings={"threshold": "-16dB", "ratio": 3.0, "attack": 6, "release": 50}
    ),

    "SCARED_CHILD_FEMALE": VoiceProfile(
        profile_id="SCARED_CHILD_FEMALE",
        display_name="Hoài My - Bé Gái Cầu Cứu",
        genre_match=["TRE_EM", "BE_GAI"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+4Hz", rate="+2%", volume="+1%", tempo_multiplier=1.12,
        rubberband_pitch=1.20,
        description="Trong trẻo, non nớt, hoảng loạn sợ hãi kêu cứu khiến người nghe xót xa.",
        eq_settings={"warmth_freq": 280, "warmth_gain": 1.5, "scoop_freq": 1500, "scoop_gain": -1.0, "clarity_freq": 4000, "clarity_gain": 3.5, "deess_freq": 7200, "deess_gain": -2.0},
        compressor_settings={"threshold": "-17dB", "ratio": 2.8, "attack": 8, "release": 55}
    ),

    "COLD_DOCTOR_FEMALE": VoiceProfile(
        profile_id="COLD_DOCTOR_FEMALE",
        display_name="Hoài My - Bác Sĩ Ngoại Khoa Điềm Tĩnh",
        genre_match=["BAC_SI_NU", "CHUYEN_GIA_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-1Hz", rate="+1%", volume="+1%", tempo_multiplier=1.14,
        rubberband_pitch=0.97,
        description="Chính xác, gãy gọn, điềm đạm trước sinh tử, chuẩn y khoa.",
        eq_settings={"warmth_freq": 190, "warmth_gain": 3.2, "scoop_freq": 1150, "scoop_gain": -2.0, "clarity_freq": 3600, "clarity_gain": 3.8, "deess_freq": 6500, "deess_gain": -2.5},
        compressor_settings={"threshold": "-17dB", "ratio": 3.4, "attack": 7, "release": 60}
    ),

    "ANCIENT_EMPRESS_FEMALE": VoiceProfile(
        profile_id="ANCIENT_EMPRESS_FEMALE",
        display_name="Hoài My - Hoàng Thái Hậu Uy Quyền",
        genre_match=["THAI_HAU", "NU_VUONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-2Hz", rate="-3%", volume="+2%", tempo_multiplier=1.06,
        rubberband_pitch=0.92,
        description="Bề trên tối thượng, uy nghiêm ngút trời, thong thả mà rợn gáy.",
        eq_settings={"warmth_freq": 170, "warmth_gain": 4.0, "scoop_freq": 1100, "scoop_gain": -2.5, "clarity_freq": 3200, "clarity_gain": 3.5, "deess_freq": 6300, "deess_gain": -2.8},
        compressor_settings={"threshold": "-18dB", "ratio": 3.8, "attack": 10, "release": 70}
    ),

    "FEMALE_WARRIOR": VoiceProfile(
        profile_id="FEMALE_WARRIOR",
        display_name="Hoài My - Nữ Cơ Trưởng / Hoa Tiêu",
        genre_match=["CO_TRUONG_NU", "HOA_TIEU_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-2Hz", rate="+3%", volume="+2%", tempo_multiplier=1.16,
        rubberband_pitch=0.95,
        description="Bản lĩnh thép, bình tĩnh chỉ huy vượt bão biển và sự cố buồng lái.",
        eq_settings={"warmth_freq": 185, "warmth_gain": 3.5, "scoop_freq": 1100, "scoop_gain": -2.0, "clarity_freq": 3700, "clarity_gain": 4.0, "deess_freq": 6500, "deess_gain": -2.5},
        compressor_settings={"threshold": "-16dB", "ratio": 3.6, "attack": 6, "release": 55}
    ),

    "COMEDY_AUNTIE_FEMALE": VoiceProfile(
        profile_id="COMEDY_AUNTIE_FEMALE",
        display_name="Hoài My - Bà Bác Hàng Xóm Hóng Hớt",
        genre_match=["BA_HANG_XOM", "HAI_DOI_THUONG"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+2Hz", rate="+6%", volume="+2%", tempo_multiplier=1.22,
        rubberband_pitch=1.07,
        description="Nhanh mồm nhanh miệng, nhiều chuyện, buôn dưa lê tấu hài cực duyên.",
        eq_settings={"warmth_freq": 230, "warmth_gain": 2.0, "scoop_freq": 1200, "scoop_gain": -1.5, "clarity_freq": 4200, "clarity_gain": 4.2, "deess_freq": 6800, "deess_gain": -2.5},
        compressor_settings={"threshold": "-15dB", "ratio": 3.0, "attack": 5, "release": 45}
    ),

    "ANGELIC_NARRATOR_FEMALE": VoiceProfile(
        profile_id="ANGELIC_NARRATOR_FEMALE",
        display_name="Hoài My - Giọng Kể Mộng Mơ Truyền Cảm",
        genre_match=["CO_TICH", "MONG_MO"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+1Hz", rate="-1%", volume="+1%", tempo_multiplier=1.10,
        rubberband_pitch=1.03,
        description="Mượt mà, bay bổng, trong sáng, như dắt người nghe vào thế giới diệu kỳ.",
        eq_settings={"warmth_freq": 200, "warmth_gain": 3.0, "scoop_freq": 1250, "scoop_gain": -1.8, "clarity_freq": 4000, "clarity_gain": 3.5, "deess_freq": 6700, "deess_gain": -2.5},
        compressor_settings={"threshold": "-18dB", "ratio": 3.0, "attack": 10, "release": 70}
    ),

    "UNDERCOVER_AGENT_FEMALE": VoiceProfile(
        profile_id="UNDERCOVER_AGENT_FEMALE",
        display_name="Hoài My - Nữ Đặc Vụ Ngầm Trá Hình",
        genre_match=["DAC_VU_NU", "GIA_DANH", "DIEP_VIEN_NU"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="+0Hz", rate="+3%", volume="+2%", tempo_multiplier=1.17,
        rubberband_pitch=1.00,
        description="Biến ảo khôn lường, chuyển tông linh hoạt giữa mềm mỏng quyến rũ và quyết đoán tử thần.",
        eq_settings={"warmth_freq": 195, "warmth_gain": 3.2, "scoop_freq": 1100, "scoop_gain": -2.0, "clarity_freq": 4300, "clarity_gain": 4.5, "deess_freq": 6700, "deess_gain": -2.8},
        compressor_settings={"threshold": "-16dB", "ratio": 3.8, "attack": 5, "release": 48}
    ),

    "MYSTIC_SHAMAN_FEMALE": VoiceProfile(
        profile_id="MYSTIC_SHAMAN_FEMALE",
        display_name="Hoài My - Bà Thầy Sơn Cước Quái Đàm",
        genre_match=["SON_CUOC", "THAY_PHAP_NU", "BUA_CHU", "ME_TIN"],
        voice_name="vi-VN-HoaiMyNeural",
        pitch="-3Hz", rate="-5%", volume="+1%", tempo_multiplier=1.04,
        rubberband_pitch=0.91,
        description="Khàn đục, cổ quái, âm vực rợn người với tiếng niệm chú thì thầm giữa rừng thiêng nước độc.",
        eq_settings={"warmth_freq": 150, "warmth_gain": 4.5, "scoop_freq": 1150, "scoop_gain": -3.0, "clarity_freq": 3100, "clarity_gain": 3.0, "deess_freq": 6100, "deess_gain": -3.5},
        compressor_settings={"threshold": "-20dB", "ratio": 4.2, "attack": 15, "release": 85},
        special_effects="lowpass=f=6500,equalizer=f=180:t=q:w=1.5:g=3.0"
    ),
}


def normalize_genre_keyword(text: str) -> str:
    import unicodedata
    t = re.sub(r'([a-z\u00e0-\u017e])([A-Z\u0102\u00c2\u0110\u00ca\u00d4\u01a0\u01af])', r'\1 \2', text)
    t = unicodedata.normalize('NFD', t)
    t = re.sub(r'[\u0300-\u036f]', '', t)
    t = t.replace('đ', 'd').replace('Đ', 'D')
    t = re.sub(r'[^\w\s]', ' ', t)
    return re.sub(r'\s+', '_', t).upper().strip()


# ==============================================================================
# HÀM LỰA CHỌN VOICE PROFILE TỐI ƯU
# ==============================================================================
def get_voice_profile_for_genre(genre: str, preferred_gender: str = "auto") -> VoiceProfile:
    """
    Tự động lựa chọn Voice Profile điện ảnh tối ưu nhất cho thể loại được chỉ định.
    Hỗ trợ chuẩn hóa tiếng Việt không dấu, đối sánh token và 48 profiles âm học chuyên sâu.
    """
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

    # 2. Fallback theo từ khóa đặc thù chuẩn hóa tiếng Việt
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

    if any(k in g for k in ["CHUA_LANH", "HEALING", "NGUOC_TAM", "DOI_SONG", "TAM_SU", "CUU_ROI", "NHE_NHANG", "LANG_MAN", "HAO_MON"]):
        return VOICE_PROFILES["HEALING_SOUL_FEMALE"] if preferred_gender != "male" else VOICE_PROFILES["CEO_AUTHORITY_MALE"]

    if any(k in g for k in ["THANH_XUAN", "HOC_DUONG", "VUON_TRUONG", "TUOI_TRE", "NGOT_SUNG", "VUNG_TROM"]) or "THANHXUAN" in g:
        return VOICE_PROFILES["YOUTH_EMOTIONAL_FEMALE"] if preferred_gender != "male" else VOICE_PROFILES["YOUTH_HERO_MALE"]

    if any(k in g for k in ["ME_CHONG", "GIA_DAU", "VA_MAT", "TRONG_SINH", "LY_HON", "HOAN_DOI"]):
        return VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]

    if any(k in g for k in ["THUONG_CHIEN", "TONG_TAI", "TAI_CHINH", "DO_THI", "HOP_DONG"]):
        return VOICE_PROFILES["CEO_AUTHORITY_MALE"] if preferred_gender == "male" else VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]

    if any(k in g for k in ["PHAP_LY", "TOA_AN", "TRANH_TUNG", "KHE_UOC"]):
        return VOICE_PROFILES["LITIGATOR_SHARP_FEMALE"]

    if any(k in g for k in ["KIEM_TOAN", "THI_TRUONG_VON"]):
        return VOICE_PROFILES["FORENSIC_AUDITOR_FEMALE"]

    if any(k in g for k in ["HANG_HAI", "TAU_CONTAINER", "HOA_TIEU"]):
        return VOICE_PROFILES["OCEAN_NAVIGATOR_MALE"]

    if any(k in g for k in ["KHI_TUONG", "RADAR", "CUC_BAC"]):
        return VOICE_PROFILES["ARCTIC_RADAR_MALE"]

    if any(k in g for k in ["PODCAST", "DEM_KHUYA", "TAM_SU"]):
        return VOICE_PROFILES["MIDNIGHT_STORYTELLER_MALE"]

    if any(k in g for k in ["MANG", "DEEPFAKE", "BTS", "BLOCKCHAIN"]):
        return VOICE_PROFILES["CYBER_FORENSIC_MALE"]

    if any(k in g for k in ["CO_VAT", "DO_CO", "NGOC_QUY", "GIAM_DINH"]):
        return VOICE_PROFILES["ANTIQUE_APPRAISER_MALE"]

    if any(k in g for k in ["KHONG_LUU", "MAY_BAY", "HANG_KHONG"]):
        return VOICE_PROFILES["FLIGHT_CONTROLLER_MALE"]

    if any(k in g for k in ["VI_SINH", "LAB", "BSL4"]):
        return VOICE_PROFILES["BIOHAZARD_SCIENTIST_MALE"]

    if any(k in g for k in ["PHONG_SU", "BAO_CHI", "BUON_NGUOI", "XA_HOI"]):
        return VOICE_PROFILES["INVESTIGATIVE_JOURNALIST_FEMALE"]

    if any(k in g for k in ["AM_THUC", "NAU_AN", "CHEF"]):
        return VOICE_PROFILES["MICHELIN_CHEF_FEMALE"]

    if any(k in g for k in ["VE_TINH", "KHONG_GIAN", "VU_TRU"]):
        return VOICE_PROFILES["SPACE_COMM_FEMALE"]

    # Mặc định an toàn
    return VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"] if preferred_gender == "female" else VOICE_PROFILES["DETECTIVE_COLD_MALE"]


def detect_script_narrator_gender(text: str, genre: str = "") -> str:
    """
    Phân tích nội dung kịch bản thực tế & thể loại để xác định chính xác giới tính người kể chuyện ('female' hoặc 'male').
    Đảm bảo 100% kịch bản ngôi thứ nhất của nữ (váy cưới, mẹ chồng, làm dâu, mang thai, sinh con, nữ chính...) dùng Hoài My,
    và kịch bản trinh thám / kinh dị / quái đàm / mạt thế / nam chính dùng Nam Minh.
    """
    sample = (text or "")[:3500].lower()
    g = normalize_genre_keyword(genre or "")

    female_cues = [
        "váy cưới của tôi", "mẹ chồng tôi", "nhà chồng", "chồng tôi", "chồng cũ",
        "làm dâu", "nàng dâu", "con dâu", "bụng bầu", "mang thai", "tôi sinh",
        "viện sản", "em chồng", "chị dâu tôi", "vị hôn phu của tôi", "bạn trai tôi",
        "tôi là cô dâu", "gả thay", "thiên kim", "quý phi", "bổn cung", "thần thiếp",
        "hầu phủ", "tiểu thư", "tôi bưng khay trà", "thư ký", "nữ kế toán",
    ]
    male_cues = [
        "vợ tôi", "vợ cũ của tôi", "bạn gái tôi", "mẹ vợ tôi", "nhà vợ",
        "tôi là thám tử", "bác sĩ pháp y", "cảnh sát hình sự", "đội trưởng đội trọng án",
        "anh ơi", "chú em", "gã thanh niên như tôi",
    ]

    f_score = sum(2 for c in female_cues if c in sample)
    m_score = sum(2 for c in male_cues if c in sample)

    if any(k in g for k in ["SA_DIEU", "HAI_HUOC", "TIENG_LONG", "THANH_XUAN", "VUON_TRUONG",
                            "CUNG_DAU", "NU_QUYEN", "TRONG_SINH", "VA_MAT", "HAO_MON",
                            "NGON_TINH", "CHUA_LANH", "HEALING", "GIA_DAU", "ME_CHONG",
                            "LY_HON", "DOI_SONG", "ROMANCE"]):
        f_score += 3
    if any(k in g for k in ["TRINH_THAM", "KY_AN", "HUYEN_NGHI", "PHAP_Y", "QUAI_DAM",
                            "KINH_DI", "TRUYEN_MA", "HORROR", "MAT_THE", "SINH_TON", "DETECTIVE"]):
        m_score += 3

    return "male" if m_score > f_score else "female"


def select_voice_and_prosody_for_script(text: str, genre: str = "", explicit_voice: str = "") -> Dict[str, Any]:
    """
    Tự động chọn Giọng đọc (HoaiMyNeural / NamMinhNeural), Tốc độ đọc (Rate), Mood & VoiceProfile
    khớp 100% với nội dung kịch bản và thể loại (Codex 8.0):
    - Sa điêu / Tiếng lòng / Hài công sở: HoaiMyNeural, rate=+8% (nhịp lanh lẹ, dí dỏm, sắc sảo)
    - Gia đấu / Mẹ chồng / Vả mặt / Trọng sinh: HoaiMyNeural, rate=+7% (đanh thép, rõ ràng, dứt khoát)
    - Hào môn / Ngôn tình đô thị: HoaiMyNeural, rate=+6% (truyền cảm, cuốn hút)
    - Thanh xuân / Chữa lành / Cung đấu cổ phong: HoaiMyNeural, rate=+5% (ấm áp, sâu lắng, nhịp thở khoan thai)
    - Mạt thế / Sinh tồn: NamMinhNeural, rate=+6% (gấp gáp, kịch tính)
    - Trinh thám / Kỳ án / Pháp y: NamMinhNeural, rate=+5% (điềm tĩnh, sắc lạnh, phân tích)
    - Quy tắc quái đàm: NamMinhNeural, rate=+4% (bí ẩn, rợn ngợp)
    - Kinh dị đêm khuya / Truyện ma: NamMinhNeural, rate=+3% (trầm sâu, chậm rãi, lạnh gáy)
    """
    gender = detect_script_narrator_gender(text, genre)
    g = normalize_genre_keyword(genre or "")

    # Chọn profile đúng giới tính người kể chuyện trong kịch bản
    profile = get_voice_profile_for_genre(genre or "GIA_DAU", preferred_gender=gender)
    voice_name = "vi-VN-NamMinhNeural" if gender == "male" else "vi-VN-HoaiMyNeural"

    scene_mood = "normal"
    if gender == "female":
        if any(k in g for k in ["SA_DIEU", "HAI_HUOC", "TIENG_LONG", "CA_MAN"]):
            rate = "+8%"
            scene_mood = "normal"
        elif any(k in g for k in ["GIA_DAU", "ME_CHONG", "VA_MAT", "TRONG_SINH", "LY_HON"]):
            rate = "+7%"
            scene_mood = "climax"
        elif any(k in g for k in ["HAO_MON", "DO_THI", "HOP_DONG"]):
            rate = "+6%"
            scene_mood = "normal"
        elif any(k in g for k in ["CUNG_DAU", "CO_PHONG", "NU_QUYEN"]):
            rate = "+5%"
            scene_mood = "tense"
        else:
            # Thanh xuân, Chữa lành, Ngược tâm
            rate = "+5%"
            scene_mood = "normal"
    else:
        if any(k in g for k in ["MAT_THE", "SINH_TON", "BANG_GIA", "HANH_DONG"]):
            rate = "+6%"
            scene_mood = "tense"
        elif any(k in g for k in ["TRINH_THAM", "KY_AN", "HUYEN_NGHI", "PHAP_Y", "DETECTIVE"]):
            rate = "+5%"
            scene_mood = "tense"
        elif any(k in g for k in ["QUAI_DAM"]):
            rate = "+4%"
            scene_mood = "whisper"
        else:
            # Kinh dị đêm muộn, Truyện ma
            rate = "+3%"
            scene_mood = "whisper"

    return {
        "voice": voice_name,
        "rate": rate,
        "gender": gender,
        "scene_mood": scene_mood,
        "profile": profile,
    }


def build_genre_vocal_filter_chain(
    profile: VoiceProfile,
    voice_volume: float = 1.0,
    scene_mood: str = "normal",
    apply_rubberband: bool = False
) -> str:
    """
    Sinh chuỗi tham số -filter:a hoàn chỉnh của FFmpeg:
    Mặc định KHÔNG bóp méo pitch bằng rubberband trên giọng dẫn chuyện chính để giữ nguyên âm sắc người thật của Neural TTS,
    kết hợp Highpass, Warmth EQ, Scoop EQ, Clarity EQ, De-Esser, Compressor và Scene Mood.
    """
    eq = profile.eq_settings
    comp = profile.compressor_settings
    chain_parts = []

    # 1. Chỉ dùng Rubberband khi được yêu cầu tường minh (tránh méo tiếng robotic trên giọng dẫn chuyện)
    if apply_rubberband and profile.rubberband_pitch and abs(profile.rubberband_pitch - 1.0) > 0.01:
        chain_parts.append(f"rubberband=pitch={profile.rubberband_pitch:.3f}:tempo=1.0")

    # 2. Bộ lọc Studio Broadcast Mastering chuẩn
    chain_parts.extend([
        "highpass=f=75",
        f"equalizer=f={eq['warmth_freq']}:t=q:w=1.2:g={eq['warmth_gain']}",
        f"equalizer=f={eq['scoop_freq']}:t=q:w=1.5:g={eq['scoop_gain']}",
        f"equalizer=f={eq['clarity_freq']}:t=q:w=1.2:g={eq['clarity_gain']}",
        f"equalizer=f={eq['deess_freq']}:t=q:w=1.8:g={eq['deess_gain']}",
        f"acompressor=threshold={comp['threshold']}:ratio={comp['ratio']}:attack={comp['attack']}:release={comp['release']}",
    ])

    # 3. Điều biến âm học theo tâm trạng bối cảnh (Scene Mood Modulation)
    if scene_mood == "tense":
        chain_parts.append("equalizer=f=3600:t=q:w=1.2:g=1.5")
    elif scene_mood == "whisper":
        chain_parts.append("equalizer=f=130:t=q:w=1.0:g=2.0,lowpass=f=7500")
    elif scene_mood == "climax":
        chain_parts.append("equalizer=f=120:t=q:w=1.2:g=1.5,equalizer=f=4000:t=q:w=1.0:g=1.8")
    elif scene_mood == "vintage":
        chain_parts.append("highpass=f=150,lowpass=f=5500")

    # 4. Hiệu ứng môi trường không gian (nếu có)
    if profile.special_effects:
        chain_parts.append(profile.special_effects)

    chain_parts.append(f"volume={voice_volume}")
    return ",".join(chain_parts)


# ==============================================================================
# HỆ THỐNG DIỄN ĐỌC ĐA NHÂN VẬT (MULTI-ROLE VOICE ACTING PARSER)
# ==============================================================================
def parse_dialogue_roles(text: str, default_genre: str = "TRONG_SINH") -> List[Tuple[VoiceProfile, str]]:
    """
    Tự động phân tách kịch bản thành các phân đoạn:
    - Lời dẫn chuyện (Narrator): Dùng VoiceProfile chuẩn của thể loại.
    - Lời thoại nhân vật trong ngoặc kép: Tự động phát hiện vai diễn (Mẹ chồng, sếp, trẻ em, ác nhân, phóng viên...)
      để gán Voice Profile phù hợp.
    """
    default_narrator = get_voice_profile_for_genre(default_genre)
    pattern = r"(['\"“‘][^'\"”’]+['\"”’])"
    segments = re.split(pattern, text)

    results: List[Tuple[VoiceProfile, str]] = []
    prev_context = ""

    for seg in segments:
        s = seg.strip()
        if not s:
            continue

        # Nếu là lời thoại
        if (s.startswith(("'", '"', "“", "‘")) and s.endswith(("'", '"', "”", "’"))) or (len(s) > 2 and s[0] in "'\"“‘"):
            quote_content = s.strip("'\"“”‘’")
            context_lower = prev_context.lower()

            # Phân loại vai diễn dựa trên ngữ cảnh lời dẫn phía trước
            if any(k in context_lower for k in ["mẹ chồng", "bà mai", "mẹ anh", "bà nội", "bà cô", "bà hà"]):
                chosen_profile = VOICE_PROFILES["HARSH_MATRIARCH_FEMALE"]
            elif any(k in context_lower for k in ["trà xanh", "diệp nhi", "như yên", "tiểu tam", "ả tình nhân", "liễu như yên"]):
                chosen_profile = VOICE_PROFILES["SWEET_TRAITOR_FEMALE"]
            elif any(k in context_lower for k in ["bé gái", "đứa bé", "cháu bé", "con gái tôi", "tiểu bảo", "cô bé"]):
                chosen_profile = VOICE_PROFILES["SCARED_CHILD_FEMALE"]
            elif any(k in context_lower for k in ["tên trùm", "trang hạo", "tiêu trạch", "trịnh phong", "viktor", "kẻ cướp", "tên côn đồ", "mã khắc", "quản gia"]):
                chosen_profile = VOICE_PROFILES["DARK_VILLAIN_MALE"]
            elif any(k in context_lower for k in ["tổng tài", "chủ tịch", "giám đốc", "ông chủ", "cố bắc thần", "phó tổng"]):
                chosen_profile = VOICE_PROFILES["CEO_AUTHORITY_MALE"]
            elif any(k in context_lower for k in ["luật sư", "viện kiểm sát", "công tố viên"]):
                chosen_profile = VOICE_PROFILES["LITIGATOR_SHARP_FEMALE"] if any(w in context_lower for w in ["nữ", "chị", "cô"]) else VOICE_PROFILES["DETECTIVE_COLD_MALE"]
            elif any(k in context_lower for k in ["kiểm toán", "kế toán trưởng"]):
                chosen_profile = VOICE_PROFILES["FORENSIC_AUDITOR_FEMALE"]
            elif any(k in context_lower for k in ["thầy", "giáo sư", "bác sĩ", "chuyên gia"]):
                chosen_profile = VOICE_PROFILES["COLD_DOCTOR_FEMALE"] if any(w in context_lower for w in ["cô", "chị", "bà"]) else VOICE_PROFILES["COLD_SURGEON_MALE"]
            elif any(k in context_lower for k in ["ông cụ", "lão gia", "người già", "ông nội", "sư phụ"]):
                chosen_profile = VOICE_PROFILES["ELDER_PATRIARCH_MALE"]
            elif any(k in context_lower for k in ["thái hậu", "hoàng hậu", "quý phi"]):
                chosen_profile = VOICE_PROFILES["ANCIENT_EMPRESS_FEMALE"]
            elif any(k in context_lower for k in ["bà hàng xóm", "chị hàng xóm", "bác gái"]):
                chosen_profile = VOICE_PROFILES["COMEDY_AUNTIE_FEMALE"]
            elif any(k in context_lower for k in ["phóng viên", "nhà báo", "điều tra viên"]):
                chosen_profile = VOICE_PROFILES["INVESTIGATIVE_JOURNALIST_FEMALE"]
            elif any(k in context_lower for k in ["bếp trưởng", "đầu bếp", "nấu ăn"]):
                chosen_profile = VOICE_PROFILES["MICHELIN_CHEF_FEMALE"]
            elif any(k in context_lower for k in ["phi công", "trực thăng", "cứu nạn", "cứu hộ"]):
                chosen_profile = VOICE_PROFILES["RESCUE_PILOT_MALE"]
            elif any(k in context_lower for k in ["thợ rèn", "luyện kim", "thợ mỏ"]):
                chosen_profile = VOICE_PROFILES["BLACKSMITH_MASTER_MALE"]
            elif any(k in context_lower for k in ["hacker", "an ninh mạng", "công nghệ"]):
                chosen_profile = VOICE_PROFILES["CYBER_FORENSIC_MALE"]
            elif any(k in context_lower for k in ["giám định", "cổ vật", "đá quý"]):
                chosen_profile = VOICE_PROFILES["ANTIQUE_APPRAISER_MALE"]
            elif any(k in context_lower for k in ["không lưu", "đài chỉ huy"]):
                chosen_profile = VOICE_PROFILES["FLIGHT_CONTROLLER_MALE"]
            elif any(k in context_lower for k in ["vi sinh", "phòng áp lực"]):
                chosen_profile = VOICE_PROFILES["BIOHAZARD_SCIENTIST_MALE"]
            elif any(k in context_lower for k in ["vệ tinh", "trạm không gian"]):
                chosen_profile = VOICE_PROFILES["SPACE_COMM_FEMALE"]
            elif any(k in context_lower for k in ["thi sĩ", "ngâm thơ"]):
                chosen_profile = VOICE_PROFILES["ANCIENT_POETESS_FEMALE"]
            elif any(k in context_lower for k in ["đặc vụ", "trinh sát", "gián điệp"]):
                chosen_profile = VOICE_PROFILES["UNDERCOVER_AGENT_FEMALE"]
            elif any(k in context_lower for k in ["bà thầy", "pháp sư", "thầy cúng", "bùa chú"]):
                chosen_profile = VOICE_PROFILES["MYSTIC_SHAMAN_FEMALE"]
            else:
                # Ngược giới tính với narrator để tạo độ tương phản phong phú
                if "MALE" in default_narrator.profile_id:
                    chosen_profile = VOICE_PROFILES["QUEEN_COLD_VENOM_FEMALE"]
                else:
                    chosen_profile = VOICE_PROFILES["DETECTIVE_COLD_MALE"]

            results.append((chosen_profile, quote_content))
            prev_context = ""
        else:
            # Lời dẫn chuyện
            results.append((default_narrator, s))
            prev_context = s

    return results


def list_all_voice_profiles_summary() -> List[Dict[str, Any]]:
    """Trả về bảng danh mục toàn bộ 48 Voice Profiles phục vụ báo cáo và kiểm tra."""
    summary = []
    for pid, p in VOICE_PROFILES.items():
        summary.append({
            "profile_id": p.profile_id,
            "display_name": p.display_name,
            "genres": p.genre_match,
            "voice_name": p.voice_name,
            "pitch": p.pitch,
            "rate": p.rate,
            "rubberband_pitch": f"{p.rubberband_pitch:.2f}x" if p.rubberband_pitch else "1.00x",
            "tempo": f"{p.tempo_multiplier}x",
            "description": p.description
        })
    return summary
