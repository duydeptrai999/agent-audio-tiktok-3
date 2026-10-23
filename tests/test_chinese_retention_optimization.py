# -*- coding: utf-8 -*-
"""
tests/test_chinese_retention_optimization.py
Bộ Test Tự Động Kiểm Chứng Toàn Diện Hệ Thống Tối Ưu Hóa Retention & Yêu Cầu Mới:
1. Màn hình sạch (Clean Screen) & TikTok Auto-caption CC (ENABLE_SUBTITLES=False, TIKTOK_AUTO_CAPTION=True)
2. Tự động tạo/thêm Tuyển tập / Playlist (AUTO_ADD_TO_PLAYLIST=True)
3. Nhạc nền không lời Trung Quốc & Cinema Sidechain Ducking (release=750ms, threshold=0.079)
4. Video nền ASMR Trung Quốc (Làm đẹp, nấu ăn, làm bánh, thủ công mỹ nghệ)
5. Kịch bản độc lạ & Tên nhân vật Trung Quốc (Liễu Như Yên, Bạch Ngưng Băng, Cố Bắc Thần, Thẩm Tri Ý)
6. Tốc độ đọc tự nhiên 1.15x chống mỏi tai suốt 10 phút
"""

import os
import sys
import unittest
from pathlib import Path

# Đảm bảo import được module gốc
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

class TestChineseRetentionOptimization(unittest.TestCase):

    def test_config_settings(self):
        """Kiểm chứng các cấu hình trung tâm trong config/settings.py"""
        import config.settings as s
        
        # 1. Clean screen cho TikTok Auto-caption CC
        self.assertFalse(s.ENABLE_SUBTITLES, "ENABLE_SUBTITLES phải là False để nhường chỗ cho TikTok Auto-caption CC")
        self.assertTrue(s.TIKTOK_AUTO_CAPTION, "TIKTOK_AUTO_CAPTION phải là True")
        
        # 2. Playlist automation
        self.assertTrue(s.AUTO_ADD_TO_PLAYLIST, "AUTO_ADD_TO_PLAYLIST phải là True")
        
        # 3. Tempo & Words per minute
        self.assertAlmostEqual(s.VOICE_SPEED_MULTIPLIER, 1.15, places=2)
        self.assertGreaterEqual(s.EFFECTIVE_WORDS_PER_MINUTE, 200)
        self.assertGreaterEqual(s.SCRIPT_MIN_WORDS_PER_PART_10MIN, 2000)
        
        # 4. Cinema Ducking specs
        self.assertEqual(s.DUCKING_RELEASE_MS, 750, "Release phải là 750ms để triệt tiêu nấc cục")
        self.assertEqual(s.DUCKING_THRESHOLD, 0.079, "Threshold phải là 0.079")
        self.assertEqual(s.DUCKING_RATIO, 4.0, "Ratio phải là 4.0")
        self.assertEqual(s.DUCKING_KNEE, 2.5, "Knee phải là 2.5")
        
        # 5. Chinese theme preferences
        self.assertEqual(s.PREFERRED_BG_THEME, "chinese_asmr")
        self.assertEqual(s.PREFERRED_BGM_STYLE, "chinese_instrumental")

    def test_bgm_manager_chinese_tracks(self):
        """Kiểm chứng thư viện BGM không lời Trung Quốc & Cinema Ducking Filter"""
        from core.bgm_manager import (
            SAFE_BGM_PRESETS,
            get_safe_bgm_for_genre,
            get_cinema_ducking_filter
        )
        
        # Kiểm tra danh mục CHINESE_INSTRUMENTAL
        self.assertIn("CHINESE_INSTRUMENTAL", SAFE_BGM_PRESETS)
        chinese_tracks = SAFE_BGM_PRESETS["CHINESE_INSTRUMENTAL"]
        self.assertGreaterEqual(len(chinese_tracks), 4)
        
        # Kiểm tra get_safe_bgm_for_genre với từ khóa Trung Quốc
        bgm_path = get_safe_bgm_for_genre("CHINESE_CO_PHONG")
        self.assertTrue(bgm_path.exists(), f"Track BGM {bgm_path} phải tồn tại")
        
        # Kiểm tra filter cinema ducking
        filter_str = get_cinema_ducking_filter()
        self.assertIn("release=750", filter_str)
        self.assertIn("threshold=0.079", filter_str)
        self.assertIn("knee=2.5", filter_str)
        self.assertIn("ratio=4", filter_str)
        self.assertIn("loudnorm=I=-14", filter_str)

    def test_background_manager_chinese_asmr(self):
        """Kiểm chứng danh mục tìm kiếm Video Nền ASMR Trung Quốc"""
        from core.background_manager import DEFAULT_SEARCH_THEMES
        
        themes = [t["theme"] for t in DEFAULT_SEARCH_THEMES]
        self.assertIn("chinese_beauty_asmr", themes)
        self.assertIn("chinese_cooking_asmr", themes)
        self.assertIn("chinese_pastry_baking", themes)
        self.assertIn("chinese_craft_heritage", themes)
        
        # Kiểm tra query có chứa asmr và no music
        beauty_t = next(t for t in DEFAULT_SEARCH_THEMES if t["theme"] == "chinese_beauty_asmr")
        self.assertIn("chinese", beauty_t["query"].lower())
        self.assertIn("asmr", beauty_t["query"].lower())
        self.assertIn("no music", beauty_t["query"].lower())

    def test_ffmpeg_utils_clean_screen_and_ducking(self):
        """Kiểm chứng FFmpeg rendering hỗ trợ clean screen và cinema ducking"""
        import inspect
        from core.ffmpeg_utils import render_playable_video
        
        source = inspect.getsource(render_playable_video)
        self.assertIn("release={ducking_release}", source)
        self.assertIn("threshold={ducking_thresh}", source)
        self.assertIn("enable_subtitles", source)

    def test_tiktok_publisher_core_playlist_and_caption(self):
        """Kiểm chứng Playwright Publisher hỗ trợ Playlist và Auto-caption CC"""
        from scripts.tiktok_publisher_core import (
            enable_auto_captions_feature,
            add_to_playlist_feature,
            upload_and_publish_video
        )
        import inspect
        
        self.assertTrue(callable(enable_auto_captions_feature))
        self.assertTrue(callable(add_to_playlist_feature))
        
        sig = inspect.signature(upload_and_publish_video)
        self.assertIn("playlist_name", sig.parameters)
        self.assertIn("enable_auto_captions", sig.parameters)

    def test_chinese_prompts_and_characters(self):
        """Kiểm chứng hệ thống prompts chứa tên nhân vật Liễu Như Yên, Bạch Ngưng Băng và phong cách Trung Quốc"""
        from core.prompts import (
            BOSS_PROMPT,
            TREND_HUNTER_PROMPT,
            SCRIPTWRITER_PROMPT_SLEEP,
            MUSIC_PROMPT,
            PUBLISHER_PROMPT
        )
        
        # Trend Hunter có Liễu Như Yên & Bạch Ngưng Băng
        self.assertIn("Liễu Như Yên", TREND_HUNTER_PROMPT)
        self.assertIn("Bạch Ngưng Băng", TREND_HUNTER_PROMPT)
        self.assertIn("Cố Bắc Thần", TREND_HUNTER_PROMPT)
        self.assertIn("Thẩm Tri Ý", TREND_HUNTER_PROMPT)
        
        # Scriptwriter Sleep có Liễu Như Yên & Bạch Ngưng Băng
        self.assertIn("Liễu Như Yên", SCRIPTWRITER_PROMPT_SLEEP)
        self.assertIn("Bạch Ngưng Băng", SCRIPTWRITER_PROMPT_SLEEP)
        self.assertIn("ĐÔ THỊ HÀO MÔN", SCRIPTWRITER_PROMPT_SLEEP)
        
        # Boss Prompt có 80% Nữ giới và ASMR Trung Quốc
        self.assertIn("80% Nữ giới", BOSS_PROMPT)
        self.assertIn("ASMR Trung Quốc", BOSS_PROMPT)
        self.assertIn("Clean Screen", BOSS_PROMPT)
        
        # Music Prompt có Nhạc không lời Trung Quốc & Cinema Ducking 750ms
        self.assertIn("Trung Quốc", MUSIC_PROMPT)
        self.assertIn("750ms", MUSIC_PROMPT)
        
        # Publisher Prompt có Auto-caption CC & Tuyển tập Playlist
        self.assertIn("Auto-caption CC", PUBLISHER_PROMPT)
        self.assertIn("Danh sách phát", PUBLISHER_PROMPT)

    def test_narrative_master_library_chinese_scenes(self):
        """Kiểm chứng thư viện cảnh truyện độc bản Liễu Như Yên và Bạch Ngưng Băng"""
        from core.narrative_master_library import (
            LIEU_NHU_YEN_TIENG_LONG_P1_SCENES,
            BACH_NGUNG_BANG_TRONG_SINH_P1_SCENES
        )
        
        self.assertGreaterEqual(len(LIEU_NHU_YEN_TIENG_LONG_P1_SCENES), 5)
        self.assertGreaterEqual(len(BACH_NGUNG_BANG_TRONG_SINH_P1_SCENES), 5)
        
        # Kiểm tra nội dung có chứa đúng tên và xung đột độc lạ
        t1 = " ".join(LIEU_NHU_YEN_TIENG_LONG_P1_SCENES)
        self.assertIn("Liễu Như Yên", t1)
        self.assertIn("Cố Bắc Thần", t1)
        self.assertIn("Thẩm Tri Ý", t1)
        self.assertIn("tiếng lòng", t1.lower())
        
        t2 = " ".join(BACH_NGUNG_BANG_TRONG_SINH_P1_SCENES)
        self.assertIn("Bạch Ngưng Băng", t2)
        self.assertIn("đấu giá", t2.lower())
        self.assertIn("một trăm tỷ", t2.lower())

if __name__ == "__main__":
    unittest.main()
