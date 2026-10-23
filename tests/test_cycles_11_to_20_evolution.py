# -*- coding: utf-8 -*-
"""
tests/test_cycles_11_to_20_evolution.py
Kiểm thử tự động cho Chuỗi Thực Nghiệm Tiến Hóa Vòng 11 - 20:
- Đảm bảo 10 kiệt tác mới đạt 10.0/10 điểm audit.
- Đảm bảo tính độc bản tuyệt đối (Jaccard < 30%, Hook overlap < 45%).
- Đảm bảo thoại dao găm < 14 từ và nhịp thở Edge-TTS chuẩn xác.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_11_to_20_masterpieces import CYCLE_11_TO_20_STORIES
from core.stories.script_quality_gate import (
    calculate_jaccard_similarity,
    calculate_hook_similarity,
    audit_and_optimize_part_text
)
from scripts.run_agent_scriptwriting_cycles_11_to_20 import agent_auditor_evaluate_part
from core.narrative_synthesizer import get_masterpiece_narrative
from core.knowledge_base import require_knowledge_consultation


class TestCycles11To20Evolution(unittest.TestCase):

    def test_all_10_new_stories_structure(self):
        """10 kiệt tác mới phải có đủ 3 phần, có tiêu đề, thể loại và giọng đọc."""
        for cycle_num, story_fn in CYCLE_11_TO_20_STORIES.items():
            story = story_fn()
            self.assertIn("title", story)
            self.assertIn("genre", story)
            self.assertIn("voice", story)
            self.assertEqual(len(story["parts"]), 3)
            for p in story["parts"]:
                self.assertIn("hook", p)
                self.assertIn("body", p)
                self.assertIn("cliffhanger", p)
                self.assertIn("full_text", p)

    def test_all_10_new_stories_score_perfect_audit(self):
        """Tất cả các tập trong 10 kiệt tác mới phải đạt 10.0/10 điểm audit."""
        for cycle_num, story_fn in CYCLE_11_TO_20_STORIES.items():
            story = story_fn()
            genre = story["genre"]
            for p in story["parts"]:
                p_text = p["full_text"]
                audit = agent_auditor_evaluate_part(p_text, genre, p["part_number"])
                self.assertEqual(
                    audit["score"],
                    10.0,
                    f"Cycle {cycle_num} Part {p['part_number']} failed with flaws: {audit['flaws']}"
                )
                self.assertEqual(len(audit["flaws"]), 0)

    def test_cross_distinctiveness_across_new_stories(self):
        """Chỉ số Jaccard < 30% và Hook Overlap < 45% giữa tất cả các cặp truyện mới."""
        stories = {k: fn() for k, fn in CYCLE_11_TO_20_STORIES.items()}
        keys = list(stories.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                k1, k2 = keys[i], keys[j]
                s1, s2 = stories[k1], stories[k2]
                t1 = " ".join(p["full_text"] for p in s1["parts"])
                t2 = " ".join(p["full_text"] for p in s2["parts"])
                h1 = s1["parts"][0]["hook"]
                h2 = s2["parts"][0]["hook"]

                j_sim = calculate_jaccard_similarity(t1, t2)
                h_sim = calculate_hook_similarity(h1, h2)

                self.assertLess(
                    j_sim,
                    0.30,
                    f"Jaccard similarity between Cycle {k1} and Cycle {k2} is {j_sim:.2%} (>= 30%)"
                )
                self.assertLess(
                    h_sim,
                    0.45,
                    f"Hook similarity between Cycle {k1} and Cycle {k2} is {h_sim:.2%} (>= 45%)"
                )

    def test_masterpiece_dispatcher_for_new_genres(self):
        """Kiểm tra dispatcher get_masterpiece_narrative nạp đúng 10 thể loại mới."""
        new_genres = [
            ("Y_KHOA", "vi-VN-NamMinhNeural"),
            ("HAI_TRINH", "vi-VN-NamMinhNeural"),
            ("CO_NGOAN", "vi-VN-NamMinhNeural"),
            ("RAP_CHIEU", "vi-VN-NamMinhNeural"),
            ("BAN_KHONG", "vi-VN-HoaiMyNeural"),
            ("MICHELIN", "vi-VN-HoaiMyNeural"),
            ("BANG_GIA", "vi-VN-NamMinhNeural"),
            ("OLYMPIC", "vi-VN-HoaiMyNeural"),
            ("THAI_Y", "vi-VN-HoaiMyNeural"),
            ("DU_LIEU_SO", "vi-VN-NamMinhNeural"),
        ]

        consult = require_knowledge_consultation(topic_title="Test Dispatch", genre_hint="Y_KHOA")

        for g_key, expected_voice in new_genres:
            res = get_masterpiece_narrative(genre_key=g_key, custom_title=f"Test {g_key}", consult_data=consult)
            self.assertEqual(len(res["parts"]), 3)
            self.assertEqual(res["voice"], expected_voice)


if __name__ == "__main__":
    unittest.main()
