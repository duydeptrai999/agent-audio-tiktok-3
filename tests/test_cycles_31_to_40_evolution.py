# -*- coding: utf-8 -*-
"""
tests/test_cycles_31_to_40_evolution.py
Kiểm thử tự động cho Chuỗi Thực Nghiệm Tiến Hóa Vòng 31 - 40:
- Đảm bảo 10 kiệt tác mới (30 tập audio) đạt tuyệt đối 10.0/10 điểm audit.
- Đảm bảo tính độc bản siêu khắt khe (Jaccard < 25%, Hook overlap < 30%).
- Đảm bảo đối chiếu liên chu kỳ với Vòng 21-30 (20 bộ truyện không trùng lặp).
- Đảm bảo chống trùng nhịp cú pháp mở đầu (Consecutive Syntax Rhythm Anti-Clash = 0).
- Đảm bảo cân bằng 50/50 Chiến thuật Mở đầu Kép (5 Strategy A / 5 Strategy B).
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.cycles_31_to_40_masterpieces import CYCLE_31_TO_40_STORIES
from core.stories.script_quality_gate import (
    calculate_jaccard_similarity,
    calculate_hook_similarity,
    detect_opening_syntax_archetype
)
from scripts.run_agent_scriptwriting_cycles_31_to_40 import agent_auditor_evaluate_part


class TestCycles31To40Evolution(unittest.TestCase):

    def test_all_10_new_stories_structure(self):
        """10 kiệt tác Vòng 31-40 phải có đủ 3 phần, tiêu đề, thể loại và giọng đọc."""
        for cycle_num, story_fn in CYCLE_31_TO_40_STORIES.items():
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
        """Tất cả 30 tập trong 10 kiệt tác mới (Vòng 31-40) phải đạt 10.0/10 điểm audit."""
        for cycle_num, story_fn in CYCLE_31_TO_40_STORIES.items():
            story = story_fn()
            genre = story["genre"]
            for p in story["parts"]:
                p_text = p["full_text"]
                eval_res = agent_auditor_evaluate_part(p_text, genre, p["part_number"])
                self.assertEqual(
                    eval_res["score"], 10.0,
                    f"Cycle {cycle_num} Part {p['part_number']} failed score: {eval_res['flaws']}"
                )

    def test_dual_engine_hook_strategies_balance(self):
        """Kiểm tra tỷ lệ cân bằng 50/50 giữa 2 chiến thuật mở đầu kép: 5 Thoáng qua (<= 25 từ) và 5 Cận cảnh (> 25 từ)."""
        flash_count = 0
        detailed_count = 0
        for cycle_num in range(31, 41):
            story = CYCLE_31_TO_40_STORIES[cycle_num]()
            hook_words = len(story["parts"][0]["hook"].split())
            if hook_words <= 25:
                flash_count += 1
            else:
                detailed_count += 1
        self.assertEqual(flash_count, 5, f"Chiến thuật A phải có đúng 5 kịch bản (thực tế: {flash_count})")
        self.assertEqual(detailed_count, 5, f"Chiến thuật B phải có đúng 5 kịch bản (thực tế: {detailed_count})")

    def test_cross_script_diversity_within_cycles_31_to_40(self):
        """Đảm bảo các kịch bản trong Vòng 31-40 có Jaccard < 25% và Hook Overlap < 30%."""
        stories = [CYCLE_31_TO_40_STORIES[c]() for c in range(31, 41)]
        for i in range(len(stories)):
            for j in range(i + 1, len(stories)):
                text_i = " ".join(p["full_text"] for p in stories[i]["parts"])
                text_j = " ".join(p["full_text"] for p in stories[j]["parts"])
                jaccard = calculate_jaccard_similarity(text_i, text_j)
                self.assertLess(
                    jaccard, 0.25,
                    f"Jaccard similarity quá cao giữa Vòng {i+31} và Vòng {j+31}: {jaccard:.2%}"
                )

                hook_i = stories[i]["parts"][0]["hook"]
                hook_j = stories[j]["parts"][0]["hook"]
                hook_sim = calculate_hook_similarity(hook_i, hook_j)
                self.assertLess(
                    hook_sim, 0.30,
                    f"Hook similarity quá cao giữa Vòng {i+31} và Vòng {j+31}: {hook_sim:.2%}"
                )

    def test_consecutive_syntax_rhythm_anti_clash_31_to_40(self):
        """Đảm bảo không có 2 audio liên tiếp nào từ Vòng 30 đến Vòng 40 dùng chung một cú pháp câu mở đầu."""
        s30 = CYCLE_21_TO_30_STORIES[30]()
        stories_31_40 = [CYCLE_31_TO_40_STORIES[c]() for c in range(31, 41)]
        all_checked = [s30] + stories_31_40
        syntaxes = [detect_opening_syntax_archetype(s["parts"][0]["hook"]) for s in all_checked]
        for idx in range(len(syntaxes) - 1):
            curr_s = syntaxes[idx]
            next_s = syntaxes[idx + 1]
            self.assertNotEqual(
                curr_s, next_s,
                f"Audio {idx+30} và Audio {idx+31} bị trùng nhịp cú pháp câu mở đầu '{curr_s}'!"
            )

    def test_full_20_cycles_cross_distinctiveness_matrix(self):
        """Đảm bảo toàn bộ 20 kiệt tác (Vòng 21 đến 40 - 190 cặp đối chiếu) đều có Jaccard < 28% và Hook < 40%."""
        all_20_stories = (
            [CYCLE_21_TO_30_STORIES[c]() for c in range(21, 31)] +
            [CYCLE_31_TO_40_STORIES[c]() for c in range(31, 41)]
        )
        for i in range(len(all_20_stories)):
            for j in range(i + 1, len(all_20_stories)):
                t1 = " ".join(p["full_text"] for p in all_20_stories[i]["parts"])
                t2 = " ".join(p["full_text"] for p in all_20_stories[j]["parts"])
                j_sim = calculate_jaccard_similarity(t1, t2)
                self.assertLess(
                    j_sim, 0.28,
                    f"Vòng {i+21} và Vòng {j+21} vượt ngưỡng Jaccard 28%: {j_sim:.2%}"
                )

                h1 = all_20_stories[i]["parts"][0]["hook"]
                h2 = all_20_stories[j]["parts"][0]["hook"]
                h_sim = calculate_hook_similarity(h1, h2)
                self.assertLess(
                    h_sim, 0.40,
                    f"Vòng {i+21} và Vòng {j+21} vượt ngưỡng Hook 40%: {h_sim:.2%}"
                )


if __name__ == "__main__":
    unittest.main()
