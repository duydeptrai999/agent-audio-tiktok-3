# -*- coding: utf-8 -*-
"""
tests/test_cycles_21_to_30_evolution.py
Kiểm thử tự động cho Chuỗi Thực Nghiệm Tiến Hóa Vòng 21 - 30:
- Đảm bảo 10 kiệt tác mới đạt 10.0/10 điểm audit.
- Đảm bảo tính độc bản tuyệt đối (Jaccard < 30%, Hook overlap < 45%).
- Đảm bảo thoại dao găm < 14 từ và nhịp thở Edge-TTS chuẩn xác.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.script_quality_gate import (
    calculate_jaccard_similarity,
    calculate_hook_similarity,
    audit_and_optimize_part_text
)
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part
from core.knowledge_base import require_knowledge_consultation


class TestCycles21To30Evolution(unittest.TestCase):

    def test_all_10_new_stories_structure(self):
        """10 kiệt tác mới phải có đủ 3 phần, có tiêu đề, thể loại và giọng đọc."""
        for cycle_num, story_fn in CYCLE_21_TO_30_STORIES.items():
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
        for cycle_num, story_fn in CYCLE_21_TO_30_STORIES.items():
            story = story_fn()
            genre = story["genre"]
            for p in story["parts"]:
                p_text = p["full_text"]
                eval_res = agent_auditor_evaluate_part(p_text, genre, p["part_number"])
                self.assertEqual(eval_res["score"], 10.0, f"Cycle {cycle_num} Part {p['part_number']} failed score: {eval_res['flaws']}")

    def test_dual_engine_hook_strategies(self):
        """Kiểm tra tỷ lệ cân bằng giữa 2 chiến thuật mở đầu kép: 5 Thoáng qua và 5 Cận cảnh."""
        flash_count = 0
        detailed_count = 0
        for cycle_num in range(21, 31):
            story = CYCLE_21_TO_30_STORIES[cycle_num]()
            hook_words = len(story["parts"][0]["hook"].split())
            if hook_words <= 26:
                flash_count += 1
            else:
                detailed_count += 1
        self.assertEqual(flash_count, 5, f"Chiến thuật A phải có đúng 5 kịch bản (thực tế: {flash_count})")
        self.assertEqual(detailed_count, 5, f"Chiến thuật B phải có đúng 5 kịch bản (thực tế: {detailed_count})")

    def test_cross_script_diversity_between_cycles_21_to_30(self):
        """Đảm bảo các kịch bản liên tiếp trong Vòng 21-30 không vượt ngưỡng tương đồng (Jaccard < 30%, Hook < 45%)."""
        stories = [CYCLE_21_TO_30_STORIES[c]() for c in range(21, 31)]
        for i in range(len(stories)):
            for j in range(i + 1, len(stories)):
                text_i = stories[i]["parts"][0]["full_text"]
                text_j = stories[j]["parts"][0]["full_text"]
                jaccard = calculate_jaccard_similarity(text_i, text_j)
                self.assertLess(jaccard, 0.30, f"Jaccard similarity quá cao giữa Vòng {i+21} và Vòng {j+21}: {jaccard:.2%}")

                hook_i = stories[i]["parts"][0]["hook"]
                hook_j = stories[j]["parts"][0]["hook"]
                hook_sim = calculate_hook_similarity(hook_i, hook_j)
                self.assertLess(hook_sim, 0.45, f"Hook similarity quá cao giữa Vòng {i+21} và Vòng {j+21}: {hook_sim:.2%}")


    def test_consecutive_syntax_rhythm_anti_clash(self):
        """Đảm bảo không có 2 audio liên tiếp nào trong Vòng 21-30 dùng chung một cú pháp câu mở đầu."""
        from core.stories.script_quality_gate import detect_opening_syntax_archetype
        stories = [CYCLE_21_TO_30_STORIES[c]() for c in range(21, 31)]
        syntaxes = [detect_opening_syntax_archetype(s["parts"][0]["hook"]) for s in stories]
        for idx in range(len(syntaxes) - 1):
            curr_s = syntaxes[idx]
            next_s = syntaxes[idx + 1]
            self.assertNotEqual(
                curr_s, next_s,
                f"Audio {idx+21} và Audio {idx+22} bị trùng nhịp cú pháp câu mở đầu '{curr_s}'! Bắt buộc luân chuyển cú pháp."
            )


if __name__ == "__main__":
    unittest.main()
