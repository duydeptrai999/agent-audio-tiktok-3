# -*- coding: utf-8 -*-
"""
tests/test_multi_genre_voice_profiles.py
Kiểm thử tự động Hệ Thống Ma Trận Đa Giọng Đọc Điện Ảnh Theo Thể Loại (Multi-Genre Voice Profiles):
- Đảm bảo mỗi thể loại sở hữu một Voice Profile chuyên sâu với pitch, rate và EQ tối ưu riêng biệt.
- Đảm bảo chuỗi FFmpeg Vocal Chain sinh ra hợp lệ và phân hóa rõ rệt giữa các thể loại.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.voice_profiles import (
    VOICE_PROFILES,
    get_voice_profile_for_genre,
    build_genre_vocal_filter_chain,
    list_all_voice_profiles_summary
)
from core.audio_engine import get_vocal_chain_filter


class TestMultiGenreVoiceProfiles(unittest.TestCase):

    def test_voice_profiles_count(self):
        """Khẳng định hệ thống có ít nhất 10 Voice Profiles chuyên sâu."""
        self.assertGreaterEqual(len(VOICE_PROFILES), 10)

    def test_genre_profile_mapping(self):
        """Kiểm tra việc map đúng Voice Profile cho 10 thể loại trụ cột."""
        expected_mappings = {
            "HUYEN_NGHI": "DETECTIVE_COLD_MALE",
            "TRINH_THAM": "DETECTIVE_COLD_MALE",
            "KINH_DI": "HORROR_CREEPY_MALE",
            "QUAI_DAM": "HORROR_CREEPY_MALE",
            "MAT_THE": "SURVIVOR_GRITTY_MALE",
            "BANG_GIA": "SURVIVOR_GRITTY_MALE",
            "ME_CHONG": "QUEEN_COLD_VENOM_FEMALE",
            "GIA_DAU": "QUEEN_COLD_VENOM_FEMALE",
            "HAO_MON": "CEO_AUTHORITY_MALE",
            "SA_DIEU": "SATIRIC_SPARKLING_FEMALE",
            "HAI_HUOC": "SATIRIC_SPARKLING_FEMALE",
            "CUNG_DAU": "IMPERIAL_SERENE_FEMALE",
            "CHUA_LANH": "HEALING_SOUL_FEMALE",
            "THANH_XUAN": "YOUTH_EMOTIONAL_FEMALE",
            "HANH_DONG": "ACTION_INTENSE_MALE",
        }
        for genre, expected_pid in expected_mappings.items():
            profile = get_voice_profile_for_genre(genre)
            self.assertEqual(profile.profile_id, expected_pid, f"Thể loại {genre} map sai sang {profile.profile_id}")

    def test_gender_preference_override(self):
        """Kiểm tra tính năng ưu tiên giới tính giọng đọc (male / female)."""
        p_female_horror = get_voice_profile_for_genre("KINH_DI", preferred_gender="female")
        self.assertEqual(p_female_horror.profile_id, "HORROR_WHISPER_FEMALE")

        p_male_detective = get_voice_profile_for_genre("HUYEN_NGHI", preferred_gender="male")
        self.assertEqual(p_male_detective.profile_id, "DETECTIVE_COLD_MALE")

    def test_pitch_and_rate_safety_bounds(self):
        """Đảm bảo các giá trị Pitch Modulation và Rate nằm trong ngưỡng tự nhiên, không làm vỡ âm."""
        for pid, p in VOICE_PROFILES.items():
            pitch_val = float(p.pitch.replace("Hz", ""))
            self.assertGreaterEqual(pitch_val, -5.0, f"{pid} pitch quá thấp: {pitch_val}")
            self.assertLessEqual(pitch_val, 5.0, f"{pid} pitch quá cao: {pitch_val}")

            rate_val = float(p.rate.replace("%", ""))
            self.assertGreaterEqual(rate_val, -10.0, f"{pid} rate quá chậm: {rate_val}")
            self.assertLessEqual(rate_val, 10.0, f"{pid} rate quá nhanh: {rate_val}")

    def test_vocal_chain_filter_distinctiveness(self):
        """Đảm bảo chuỗi FFmpeg filter của các thể loại khác nhau là hoàn toàn phân hóa."""
        f_detective = get_vocal_chain_filter(genre="HUYEN_NGHI")
        f_horror = get_vocal_chain_filter(genre="KINH_DI")
        f_satiric = get_vocal_chain_filter(genre="SA_DIEU")
        f_healing = get_vocal_chain_filter(genre="CHUA_LANH")

        # Khẳng định các chuỗi filter không trùng nhau
        self.assertNotEqual(f_detective, f_horror)
        self.assertNotEqual(f_horror, f_satiric)
        self.assertNotEqual(f_satiric, f_healing)

        # Kiểm tra các thành phần kỹ thuật thiết yếu
        for f in [f_detective, f_horror, f_satiric, f_healing]:
            self.assertIn("highpass=f=75", f)
            self.assertIn("equalizer=", f)
            self.assertIn("acompressor=", f)

        # Quái đàm kinh dị có lowpass đặc thù
        self.assertIn("lowpass=", f_horror)
        # Sa điêu có air boost 8000Hz
        self.assertIn("8000", f_satiric)

    def test_summary_list(self):
        """Kiểm tra báo cáo danh mục voice profiles."""
        summary = list_all_voice_profiles_summary()
        self.assertGreaterEqual(len(summary), 10)
        for item in summary:
            self.assertIn("profile_id", item)
            self.assertIn("display_name", item)
            self.assertIn("pitch", item)
            self.assertIn("rate", item)


if __name__ == "__main__":
    unittest.main()
