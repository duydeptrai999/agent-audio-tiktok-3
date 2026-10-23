# -*- coding: utf-8 -*-
"""
tests/test_multi_genre_voice_profiles.py
Kiểm thử tự động Hệ Thống Ma Trận 48 Giọng Đọc Điện Ảnh & Diễn Đọc Đa Nhân Vật Chuẩn Hollywood (Cinema Vocal Studio Master Pro 4.0):
- Đảm bảo mỗi thể loại và vai diễn sở hữu một Voice Profile chuyên sâu với pitch, rate, rubberband và EQ riêng biệt.
- Đảm bảo chuỗi FFmpeg Vocal Chain sinh ra hợp lệ và phân hóa rõ rệt.
- Kiểm tra tính năng tự động phân tách vai diễn (Multi-Role Voice Acting) với các nhân vật mới.
- Kiểm tra tính năng điều biến tâm trạng cảnh quay (Multi-Mood Scene Acoustic Modulation).
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
    list_all_voice_profiles_summary,
    parse_dialogue_roles
)
from core.audio_engine import get_vocal_chain_filter


class TestMultiGenreVoiceProfiles(unittest.TestCase):

    def test_voice_profiles_count(self):
        """Khẳng định hệ thống có ít nhất 40 Voice Profiles điện ảnh chuyên sâu (hiện có 48)."""
        self.assertGreaterEqual(len(VOICE_PROFILES), 40)
        self.assertEqual(len(VOICE_PROFILES), 48)

    def test_genre_profile_mapping(self):
        """Kiểm tra việc map đúng Voice Profile cho các thể loại trụ cột và vũ trụ mới."""
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
            "PHAP_LY": "LITIGATOR_SHARP_FEMALE",
            "KIEM_TOAN": "FORENSIC_AUDITOR_FEMALE",
            "HANG_HAI": "OCEAN_NAVIGATOR_MALE",
            "KHI_TUONG": "ARCTIC_RADAR_MALE",
            "PODCAST": "MIDNIGHT_STORYTELLER_MALE",
            "AN_NINH_MANG": "CYBER_FORENSIC_MALE",
            "GIAM_DINH": "ANTIQUE_APPRAISER_MALE",
            "KHONG_LUU": "FLIGHT_CONTROLLER_MALE",
            "VI_SINH": "BIOHAZARD_SCIENTIST_MALE",
            "DIEU_TRA_XA_HOI": "INVESTIGATIVE_JOURNALIST_FEMALE",
            "AM_THUC": "MICHELIN_CHEF_FEMALE",
            "VIEN_THONG_KHONG_GIAN": "SPACE_COMM_FEMALE",
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

        p_male_satiric = get_voice_profile_for_genre("SA_DIEU", preferred_gender="male")
        self.assertEqual(p_male_satiric.profile_id, "SATIRIC_INTERNAL_MALE")

    def test_pitch_and_rate_safety_bounds(self):
        """Đảm bảo các giá trị Pitch Modulation và Rate nằm trong ngưỡng an toàn."""
        for pid, p in VOICE_PROFILES.items():
            pitch_val = float(p.pitch.replace("Hz", ""))
            self.assertGreaterEqual(pitch_val, -6.0, f"{pid} pitch quá thấp: {pitch_val}")
            self.assertLessEqual(pitch_val, 6.0, f"{pid} pitch quá cao: {pitch_val}")

            rate_val = float(p.rate.replace("%", ""))
            self.assertGreaterEqual(rate_val, -12.0, f"{pid} rate quá chậm: {rate_val}")
            self.assertLessEqual(rate_val, 12.0, f"{pid} rate quá nhanh: {rate_val}")

            if p.rubberband_pitch:
                self.assertGreaterEqual(p.rubberband_pitch, 0.75, f"{pid} rubberband pitch quá thấp: {p.rubberband_pitch}")
                self.assertLessEqual(p.rubberband_pitch, 1.30, f"{pid} rubberband pitch quá cao: {p.rubberband_pitch}")

    def test_vocal_chain_filter_distinctiveness(self):
        """Đảm bảo chuỗi FFmpeg filter của các thể loại khác nhau là hoàn toàn phân hóa."""
        f_detective = get_vocal_chain_filter(genre="HUYEN_NGHI")
        f_horror = get_vocal_chain_filter(genre="KINH_DI")
        f_satiric = get_vocal_chain_filter(genre="SA_DIEU")
        f_healing = get_vocal_chain_filter(genre="CHUA_LANH")

        self.assertNotEqual(f_detective, f_horror)
        self.assertNotEqual(f_horror, f_satiric)
        self.assertNotEqual(f_satiric, f_healing)

        for f in [f_detective, f_horror, f_satiric, f_healing]:
            self.assertIn("highpass=f=75", f)
            self.assertIn("equalizer=", f)
            self.assertIn("acompressor=", f)

        # Quái đàm kinh dị có lowpass đặc thù
        self.assertIn("lowpass=", f_horror)
        # Sa điêu có air boost 8000Hz
        self.assertIn("8000", f_satiric)

    def test_scene_mood_modulation(self):
        """Kiểm tra tính năng điều biến tâm trạng bối cảnh (Scene Mood Modulation)."""
        f_normal = get_vocal_chain_filter(genre="HUYEN_NGHI", scene_mood="normal")
        f_tense = get_vocal_chain_filter(genre="HUYEN_NGHI", scene_mood="tense")
        f_whisper = get_vocal_chain_filter(genre="HUYEN_NGHI", scene_mood="whisper")
        f_climax = get_vocal_chain_filter(genre="HUYEN_NGHI", scene_mood="climax")
        f_vintage = get_vocal_chain_filter(genre="HUYEN_NGHI", scene_mood="vintage")

        self.assertIn("equalizer=f=3600:t=q:w=1.2:g=1.5", f_tense)
        self.assertIn("lowpass=f=7500", f_whisper)
        self.assertIn("equalizer=f=4000:t=q:w=1.0:g=1.8", f_climax)
        self.assertIn("highpass=f=150,lowpass=f=5500", f_vintage)

    def test_multi_role_dialogue_parser_extended(self):
        """Kiểm tra tính năng tự động bóc tách phân vai diễn đọc đa dạng nhân vật."""
        sample_text = (
            "Tôi bước vào phòng khách nhìn quanh. "
            "Bà Mai giơ tay chỉ trỏ: 'Ký đi con dâu, nhà họ Lục không nuôi người vô dụng!'. "
            "Nữ phóng viên điều tra giơ thẻ ngành bước tới: 'Tất cả hành vi tống tiền đã được ghi hình trực tiếp!'. "
            "Tôi mỉm cười gật đầu."
        )
        segments = parse_dialogue_roles(sample_text, default_genre="ME_CHONG")
        self.assertGreaterEqual(len(segments), 4)

        # Segment 0: Narrator (Hoài My - Nữ chủ)
        self.assertEqual(segments[0][0].profile_id, "QUEEN_COLD_VENOM_FEMALE")

        # Segment 1: Lời thoại của bà Mai -> Tự động nhận diện vai Mẹ chồng cay nghiệt the thé
        self.assertEqual(segments[1][0].profile_id, "HARSH_MATRIARCH_FEMALE")
        self.assertIn("Ký đi con dâu", segments[1][1])

        # Segment 3: Lời thoại của nữ phóng viên điều tra -> Tự động nhận diện INVESTIGATIVE_JOURNALIST_FEMALE
        self.assertEqual(segments[3][0].profile_id, "INVESTIGATIVE_JOURNALIST_FEMALE")
        self.assertIn("ghi hình trực tiếp", segments[3][1])

    def test_summary_list(self):
        """Kiểm tra danh mục báo cáo toàn bộ 48 Voice Profiles."""
        summary = list_all_voice_profiles_summary()
        self.assertEqual(len(summary), 48)
        for item in summary:
            self.assertIn("profile_id", item)
            self.assertIn("display_name", item)
            self.assertIn("pitch", item)
            self.assertIn("rate", item)
            self.assertIn("rubberband_pitch", item)


if __name__ == "__main__":
    unittest.main()
