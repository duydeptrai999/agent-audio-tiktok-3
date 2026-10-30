# -*- coding: utf-8 -*-
"""
tests/test_master_codex_7_evolution.py
Kiểm thử toàn diện Bộ Quy Chuẩn Master Codex 7.0 & Hệ Thống Team Agent Sau Khảo Sát 100 Audio:
1. Thẩm định thời lượng 30 phút điện ảnh: 10/10 slot đều đạt >= 3.500 từ (tập >= 1.000 từ).
2. Chặn đứng tuyệt đối kịch bản cộc lốc (< 1.200 từ) hoặc video 45s.
3. Chặn đứng 100% cơ khí dị hợm (máy đo sóng hạ âm, lồng mèo bọc chì, máy phân tích FFT).
4. Xác thực 10 subagents đều đồng bộ Master Codex 7.0.
5. Xác thực 100% không trùng lặp câu chuyện giữa các khung giờ trong cùng ngày.
"""

import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from core.stories.daily_story_factory import get_daily_10_series, SLOT_STORY_CATALOG
from core.stories.script_quality_gate import validate_story_series
from core.narrative_synthesizer import get_masterpiece_narrative
from core.knowledge_base import require_knowledge_consultation

class TestMasterCodex7Evolution(unittest.TestCase):

    def test_daily_10_series_duration_and_word_counts(self):
        """Kiểm tra toàn bộ 10 slot của ngày hôm nay đều đạt chuẩn thời lượng >= 3.500 từ."""
        series_list = get_daily_10_series("2026-10-24")
        self.assertEqual(len(series_list), 10, f"Phải có đúng 10 slot, hiện có {len(series_list)}")
        
        titles = set()
        for s in series_list:
            parts = s.get("parts", [])
            self.assertEqual(len(parts), 3, f"Slot {s['slot_index']} phải có đúng 3 tập")
            word_counts = [len((p.get("full_text") or p.get("text") or "").split()) for p in parts]
            total_words = sum(word_counts)
            
            # Độ dài mỗi tập tối thiểu 1.000 từ, tổng series tối thiểu 3.500 từ
            self.assertGreaterEqual(total_words, 3500, f"Slot {s['slot_index']} ({s['title']}) chỉ có {total_words} từ (< 3500 từ)!")
            self.assertGreaterEqual(min(word_counts), 1000, f"Slot {s['slot_index']} có tập chỉ có {min(word_counts)} từ (< 1000 từ)!")
            
            # Tiêu đề phải độc bản trong ngày
            self.assertNotIn(s["title"], titles, f"Trùng tiêu đề trong ngày: {s['title']}")
            titles.add(s["title"])

    def test_quality_gate_rejects_stubs_and_jargon(self):
        """Cổng thẩm định phải từ chối kịch bản ngắn (< 1200 từ) hoặc dính cơ khí dị hợm."""
        stub_story = {
            "title": "Kịch Bản Test Ngắn 150 Từ",
            "genre": "TRONG_SINH",
            "parts": [
                {"part_number": 1, "text": "Đây là kịch bản rất ngắn chỉ có vài chục từ để test lỗi kỹ thuật nghiêm trọng."},
                {"part_number": 2, "text": "Phần hai cũng cộc lốc không đủ tiêu chuẩn ba mươi phút điện ảnh."},
                {"part_number": 3, "text": "Phần ba kết thúc lãng xẹt."}
            ]
        }
        validated_stub = validate_story_series(stub_story)
        self.assertFalse(validated_stub.get("quality_audit_passed"), "Quality gate phải đánh trượt kịch bản ngắn cộc lốc!")
        
        jargon_story = {
            "title": "Kịch Bản Cơ Khí Dị Hợm",
            "genre": "GIA_DAU",
            "parts": [
                {"part_number": 1, "text": "Tôi cầm máy phân tích phổ fft và máy đo sóng hạ âm 18hz quét sàn nhà " * 80},
                {"part_number": 2, "text": "Lồng mèo bọc chì cản tia x-quang giấu dưới gầm giường " * 80},
                {"part_number": 3, "text": "Buồng áp lực âm bsl-4 được kích hoạt để cô lập kẻ địch " * 80}
            ]
        }
        validated_jargon = validate_story_series(jargon_story)
        self.assertFalse(validated_jargon.get("quality_audit_passed"), "Quality gate phải đánh trượt kịch bản cơ khí dị hợm!")

    def test_teamwork_subagents_synchronized(self):
        """Kiểm tra 10 subagents đều có file BRIEFING.md đồng bộ Master Codex 7.0."""
        teamwork_dir = ROOT / ".agents" / "teamwork"
        expected_subagents = [
            "subagent_1_data_auditor", "subagent_2_retention_diagnostician",
            "subagent_3_audience_specialist", "subagent_4_tts_engineer",
            "subagent_5_bgm_specialist", "subagent_6_visual_curator",
            "subagent_7_subtitle_designer", "subagent_8_script_master",
            "subagent_9_playlist_architect", "subagent_10_master_strategist"
        ]
        for sa in expected_subagents:
            briefing = teamwork_dir / sa / "BRIEFING.md"
            self.assertTrue(briefing.exists(), f"Thiếu BRIEFING.md cho {sa}")
            text = briefing.read_text(encoding="utf-8")
            self.assertTrue(
                "MASTER CODEX 7.0" in text or "MASTER CODEX 8.0" in text or "MASTER CODEX 8.5" in text,
                f"{sa} chưa đồng bộ MASTER CODEX"
            )

    def test_masterpiece_narrative_synthesizer_clean(self):
        """Kiểm tra narrative synthesizer trả về kiệt tác chuẩn > 3.500 từ và không chứa từ cấm."""
        consult = require_knowledge_consultation(topic_title="Màn Trả Thù Đã Nhất", topic_summary="Gia đấu mẹ chồng", genre_hint="GIA_DAU")
        story = get_masterpiece_narrative("GIA_DAU", consult_data=consult)
        parts = story.get("parts", [])
        total_w = sum(len((p.get("full_text") or p.get("text") or "").split()) for p in parts)
        self.assertGreaterEqual(total_w, 4500, f"Truyện gia đấu phải đạt >= 4500 từ, thực tế: {total_w}")
        
        # Kiểm tra không chứa từ cơ khí dị hợm
        full_text = " ".join(p.get("text", "") for p in parts).lower()
        self.assertNotIn("máy phân tích phổ fft", full_text)
        self.assertNotIn("sóng hạ âm 18", full_text)
        self.assertNotIn("lồng mèo bọc chì", full_text)

if __name__ == "__main__":
    unittest.main()
