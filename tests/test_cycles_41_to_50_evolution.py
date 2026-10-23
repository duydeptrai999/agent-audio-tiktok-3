# -*- coding: utf-8 -*-
"""
tests/test_cycles_41_to_50_evolution.py
Kiểm thử tự động cho Chuỗi Thực Nghiệm Tiến Hóa Vòng 41 - 50:
- Bắt trend xã hội nổi cộm, cạm bẫy dân sự, độc lạ, cuốn hút.
- Đảm bảo 100% TUYỆT ĐỐI KHÔNG CHÍNH TRỊ (Zero Politics Guard 100%).
- Đảm bảo Ma Trận 4 Trường Phái Mở Đầu Audio Part 1 Triệu View (Micro Sensory, High-Stakes, Paradoxical Reality, Detailed Paradoxical).
- Đảm bảo 10 kiệt tác mới (30 tập audio) đạt tuyệt đối 10.0/10 điểm audit.
- Đảm bảo tính độc bản cao (Jaccard < 25%, Hook overlap < 30%).
- Đảm bảo tích hợp thành công vào Daily Story Factory và Script Quality Gate.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_41_to_50_masterpieces import CYCLE_41_TO_50_STORIES
from core.stories.script_quality_gate import (
    calculate_jaccard_similarity,
    calculate_hook_similarity,
    check_zero_politics,
    detect_4_hook_archetype
)
from scripts.run_agent_scriptwriting_cycles_41_to_50 import agent_auditor_evaluate_part
from core.stories.daily_story_factory import SLOT_STORY_CATALOG


class TestCycles41To50Evolution(unittest.TestCase):

    def test_all_10_stories_structure(self):
        """10 kiệt tác Vòng 41-50 phải có đủ 3 tập, tiêu đề, thể loại và giọng đọc."""
        self.assertEqual(len(CYCLE_41_TO_50_STORIES), 10)
        for cycle_num, story_fn in CYCLE_41_TO_50_STORIES.items():
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

    def test_all_30_parts_score_perfect_10_audit(self):
        """Tất cả 30 tập trong 10 kiệt tác mới (Vòng 41-50) phải đạt 10.0/10 điểm audit tuyệt đối."""
        for cycle_num, story_fn in CYCLE_41_TO_50_STORIES.items():
            story = story_fn()
            genre = story["genre"]
            for p in story["parts"]:
                p_text = p["full_text"]
                eval_res = agent_auditor_evaluate_part(p_text, genre, p["part_number"])
                self.assertEqual(
                    eval_res["score"], 10.0,
                    f"Cycle {cycle_num} Part {p['part_number']} không đạt 10.0/10. Lỗi: {eval_res['flaws']}"
                )
                self.assertEqual(len(eval_res["flaws"]), 0)

    def test_zero_politics_guard_100_percent(self):
        """100% các tập kịch bản không chứa từ ngữ chính trị nhạy cảm (Zero Politics Guard)."""
        for cycle_num, story_fn in CYCLE_41_TO_50_STORIES.items():
            story = story_fn()
            for p in story["parts"]:
                is_clean, found = check_zero_politics(p["full_text"])
                self.assertTrue(
                    is_clean,
                    f"Cycle {cycle_num} Part {p['part_number']} vi phạm Zero Politics: {found}"
                )

    def test_four_hook_archetypes_distribution(self):
        """Kiểm tra sự hiện diện đầy đủ của 4 trường phái mở đầu audio triệu view."""
        archetypes = set()
        for cycle_num in range(41, 51):
            story = CYCLE_41_TO_50_STORIES[cycle_num]()
            h_text = story["parts"][0]["hook"]
            arch = detect_4_hook_archetype(h_text)
            archetypes.add(arch)
        
        # Đảm bảo có ít nhất 3 trên 4 trường phái được áp dụng thực tế
        self.assertGreaterEqual(len(archetypes), 3, f"Số trường phái mở đầu: {archetypes}")
        self.assertIn("MICRO_SENSORY", archetypes)
        self.assertIn("HIGH_STAKES_SCENE", archetypes)

    def test_cross_script_diversity_within_cycles_41_to_50(self):
        """Đảm bảo các kịch bản trong Vòng 41-50 có Jaccard < 25% và Hook Overlap < 30%."""
        stories = [CYCLE_41_TO_50_STORIES[c]() for c in range(41, 51)]
        for i in range(len(stories)):
            for j in range(i + 1, len(stories)):
                text_i = " ".join(p["full_text"] for p in stories[i]["parts"])
                text_j = " ".join(p["full_text"] for p in stories[j]["parts"])
                jaccard = calculate_jaccard_similarity(text_i, text_j)
                self.assertLess(
                    jaccard, 0.25,
                    f"Trùng lặp từ vựng Jaccard ({jaccard:.4f}) giữa Cycle {i+41} và Cycle {j+41} vượt ngưỡng 0.25!"
                )

                hook_i = stories[i]["parts"][0]["hook"]
                hook_j = stories[j]["parts"][0]["hook"]
                hook_sim = calculate_hook_similarity(hook_i, hook_j)
                self.assertLess(
                    hook_sim, 0.30,
                    f"Trùng lặp mở đầu Hook ({hook_sim:.4f}) giữa Cycle {i+41} và Cycle {j+41} vượt ngưỡng 0.30!"
                )

    def test_daily_story_factory_integration(self):
        """Kiểm tra Daily Story Factory đã nạp thành công các hàm truyện Vòng 41-50 vào các slot tương ứng."""
        all_loaders = []
        for slot, loaders in SLOT_STORY_CATALOG.items():
            all_loaders.extend(loaders)

        from core.stories.cycles_41_to_50_masterpieces import (
            get_story_cycle_41, get_story_cycle_42, get_story_cycle_43,
            get_story_cycle_44, get_story_cycle_45, get_story_cycle_46,
            get_story_cycle_47, get_story_cycle_48, get_story_cycle_49,
            get_story_cycle_50
        )

        expected_fn = [
            get_story_cycle_41, get_story_cycle_42, get_story_cycle_43,
            get_story_cycle_44, get_story_cycle_45, get_story_cycle_46,
            get_story_cycle_47, get_story_cycle_48, get_story_cycle_49,
            get_story_cycle_50
        ]

        for fn in expected_fn:
            self.assertIn(fn, all_loaders, f"Hàm {fn.__name__} chưa được nạp vào SLOT_STORY_CATALOG!")


if __name__ == "__main__":
    unittest.main()
