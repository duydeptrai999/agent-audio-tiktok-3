# -*- coding: utf-8 -*-
"""
tests/test_infinite_script_diversity.py
Kiểm thử toàn diện tính Độc bản & Chống Đồng hóa Tuyệt đối (Anti-Homogenization Master Gate):
- Quét toàn bộ 780 cặp kịch bản (Cycles 11 đến 50).
- Assert Title Similarity < 0.35 (100% không trùng lặp tiêu đề).
- Assert Hook Overlap < 0.30 (100% không trùng lặp câu mở đầu Part 1).
- Assert Jaccard Similarity < 0.25 (100% không trùng lặp từ vựng/mô-típ).
- Assert Độ đa dạng cơ chế lật kèo (Resolution Mechanisms >= 10 loại).
- Assert 100% Zero-Politics Guard (Không chứa từ ngữ chính trị/nhạy cảm).
"""

import re
import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.cycles_11_to_20_masterpieces import (
    get_story_cycle_11, get_story_cycle_12, get_story_cycle_13, get_story_cycle_14, get_story_cycle_15,
    get_story_cycle_16, get_story_cycle_17, get_story_cycle_18, get_story_cycle_19, get_story_cycle_20
)
from core.stories.cycles_21_to_30_masterpieces import (
    get_story_cycle_21, get_story_cycle_22, get_story_cycle_23, get_story_cycle_24, get_story_cycle_25,
    get_story_cycle_26, get_story_cycle_27, get_story_cycle_28, get_story_cycle_29, get_story_cycle_30
)
from core.stories.cycles_31_to_40_masterpieces import (
    get_story_cycle_31, get_story_cycle_32, get_story_cycle_33, get_story_cycle_34, get_story_cycle_35,
    get_story_cycle_36, get_story_cycle_37, get_story_cycle_38, get_story_cycle_39, get_story_cycle_40
)
from core.stories.cycles_41_to_50_masterpieces import (
    get_story_cycle_41, get_story_cycle_42, get_story_cycle_43, get_story_cycle_44, get_story_cycle_45,
    get_story_cycle_46, get_story_cycle_47, get_story_cycle_48, get_story_cycle_49, get_story_cycle_50
)
from core.stories.script_quality_gate import (
    calculate_title_similarity,
    calculate_hook_similarity,
    calculate_jaccard_similarity,
    detect_resolution_mechanism,
    detect_opening_syntax_archetype,
    extract_hook_snippet,
    extract_story_full_text
)


class TestInfiniteScriptDiversity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stories = []
        for i in range(11, 21):
            fn = globals()[f"get_story_cycle_{i}"]
            cls.stories.append((i, fn()))
        for i in range(21, 31):
            fn = globals()[f"get_story_cycle_{i}"]
            cls.stories.append((i, fn()))
        for i in range(31, 41):
            fn = globals()[f"get_story_cycle_{i}"]
            cls.stories.append((i, fn()))
        for i in range(41, 51):
            fn = globals()[f"get_story_cycle_{i}"]
            cls.stories.append((i, fn()))
        cls.total_pairs = len(cls.stories) * (len(cls.stories) - 1) // 2

    def test_total_stories_count(self):
        """Khẳng định đủ 40 bộ kịch bản kiệt tác và 780 cặp so sánh chéo."""
        self.assertEqual(len(self.stories), 40)
        self.assertEqual(self.total_pairs, 780)

    def test_zero_title_similarity_clash(self):
        """100% Không có bất kỳ cặp nào trùng tiêu đề >= 35%."""
        clashes = []
        for i in range(len(self.stories)):
            num1, s1 = self.stories[i]
            t1 = s1.get("title", "")
            for j in range(i + 1, len(self.stories)):
                num2, s2 = self.stories[j]
                t2 = s2.get("title", "")
                sim = calculate_title_similarity(t1, t2)
                if sim >= 0.35:
                    clashes.append((num1, num2, sim, t1, t2))
        msg = "\n".join([f"Cycle {c[0]} vs {c[1]}: {c[2]:.1%} ('{c[3]}' vs '{c[4]}')" for c in clashes])
        self.assertEqual(len(clashes), 0, f"Phát hiện trùng lặp tiêu đề:\n{msg}")

    def test_zero_hook_overlap_clash(self):
        """100% Không có bất kỳ cặp nào trùng mở đầu Hook Part 1 >= 30%."""
        clashes = []
        for i in range(len(self.stories)):
            num1, s1 = self.stories[i]
            h1 = extract_hook_snippet(s1)
            for j in range(i + 1, len(self.stories)):
                num2, s2 = self.stories[j]
                h2 = extract_hook_snippet(s2)
                sim = calculate_hook_similarity(h1, h2)
                if sim >= 0.30:
                    clashes.append((num1, num2, sim, h1, h2))
        msg = "\n".join([f"Cycle {c[0]} vs {c[1]}: {c[2]:.1%}\n  H1: {c[3]}\n  H2: {c[4]}" for c in clashes])
        self.assertEqual(len(clashes), 0, f"Phát hiện trùng lặp mở đầu:\n{msg}")

    def test_cross_cycle_jaccard_distinctiveness(self):
        """100% Không có bất kỳ cặp nào có Jaccard Similarity >= 25% trên toàn bộ 780 cặp."""
        clashes = []
        for i in range(len(self.stories)):
            num1, s1 = self.stories[i]
            txt1 = extract_story_full_text(s1)
            for j in range(i + 1, len(self.stories)):
                num2, s2 = self.stories[j]
                txt2 = extract_story_full_text(s2)
                sim = calculate_jaccard_similarity(txt1, txt2)
                if sim >= 0.25:
                    clashes.append((num1, num2, sim))
        msg = "\n".join([f"Cycle {c[0]} vs {c[1]}: {c[2]:.1%}" for c in clashes])
        self.assertEqual(len(clashes), 0, f"Phát hiện tương đồng từ vựng Jaccard >= 25%:\n{msg}")

    def test_resolution_mechanisms_variety(self):
        """Đảm bảo kho kịch bản sở hữu ít nhất 10+ cơ chế lật kèo độc bản khác nhau."""
        resolutions = set()
        for num, s in self.stories:
            full_text = extract_story_full_text(s)
            res = detect_resolution_mechanism(full_text)
            resolutions.add(res)
        self.assertGreaterEqual(len(resolutions), 10, f"Độ đa dạng lật kèo quá thấp: {len(resolutions)} loại")

    def test_opening_syntax_variety(self):
        """Đảm bảo các mở đầu luân chuyển đa dạng qua nhiều trường phái cú pháp."""
        syntax_types = set()
        for num, s in self.stories:
            hook = extract_hook_snippet(s)
            st = detect_opening_syntax_archetype(hook)
            syntax_types.add(st)
        self.assertGreaterEqual(len(syntax_types), 5, f"Cú pháp mở đầu quá đơn điệu: {len(syntax_types)} loại")

    def test_zero_politics_compliance(self):
        """Đảm bảo 100% các kịch bản không chứa bất kỳ từ nhạy cảm chính trị nào."""
        forbidden_politics = [
            "chính trị", "đảng phái", "nhà nước", "chính phủ", "bộ ngoại giao",
            "lãnh sự quán", "đại sứ quán", "quân đội", "chế độ", "biểu tình", "bầu cử"
        ]
        violations = []
        for num, s in self.stories:
            txt = extract_story_full_text(s).lower()
            for w in forbidden_politics:
                if re.search(r'\b' + re.escape(w) + r'\b', txt):
                    violations.append((num, w))
        self.assertEqual(len(violations), 0, f"Phát hiện vi phạm Zero Politics: {violations}")


if __name__ == "__main__":
    unittest.main()
