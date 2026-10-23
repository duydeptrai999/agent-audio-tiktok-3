# -*- coding: utf-8 -*-
"""
tests/test_script_evolution_and_quality_gate.py
Kiểm thử tự động việc tuân thủ 100% Bộ Quy Chuẩn 10 Vòng Thực Nghiệm & Cổng Đọc Kinh Nghiệm Bắt Buộc.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from core.stories.script_quality_gate import (
    load_master_codex_rules,
    require_preflight_experience,
    audit_and_optimize_part_text,
    validate_story_series,
    deduplicate_paragraphs,
    calculate_jaccard_similarity,
    calculate_hook_similarity,
    verify_cross_audio_distinctiveness,
    FORBIDDEN_PHRASES,
    CLICHE_OPENING_PATTERNS
)
from core.knowledge_base import (
    DIVERSE_HOOK_ARCHETYPES_10,
    CHARACTER_UNIVERSES_10,
    DIVERSE_RESOLUTIONS_10,
    get_knowledge_base
)
from core.stories.daily_story_factory import SLOT_STORY_LOADERS

class TestScriptEvolutionAndQualityGate(unittest.TestCase):

    def test_preflight_experience_loads_both_files(self):
        """Bảo đảm cả GEMINI.md và docs/10_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md đều được nạp đầy đủ."""
        res = load_master_codex_rules()
        self.assertEqual(res["status"], "LOADED_OK")
        self.assertTrue(len(res["gemini_rules"]) > 100)
        self.assertTrue(len(res["evolution_experience"]) > 100)
        self.assertTrue(require_preflight_experience())

    def test_deduplicate_paragraphs(self):
        """Bảo đảm loại bỏ các đoạn văn bị sao chép lặp lại nhiều lần."""
        text = "Đoạn văn thứ nhất.\n\nĐoạn văn thứ nhất.\n\nĐoạn văn thứ hai."
        cleaned, dups = deduplicate_paragraphs(text)
        self.assertEqual(dups, 1)
        self.assertIn("Đoạn văn thứ nhất.", cleaned)
        self.assertIn("Đoạn văn thứ hai.", cleaned)
        self.assertEqual(len(cleaned.split("\n\n")), 2)

    def test_paragraph_newlines_preserved(self):
        """Bảo đảm audit_and_optimize_part_text giữ nguyên cấu trúc đoạn văn phân tách bằng \\n\\n."""
        text = "Đoạn văn số một mở màn xung đột.\n\nĐoạn văn số hai đối thoại sắc bén.\n\nĐoạn văn số ba chốt hạ cliffhanger."
        cleaned, warns = audit_and_optimize_part_text(text, title="Test", part_num=1)
        self.assertEqual(len(cleaned.split("\n\n")), 3)

    def test_forbidden_phrases_replaced(self):
        """Bảo đảm quét sạch 100% sáo ngữ convert và tell cảm xúc."""
        bad_sample = "Cô ta vô cùng tức giận, cười lạnh một tiếng rồi nhìn tôi như nhìn một con sâu bọ. Cả người đứng sững như trời trồng."
        cleaned, warns = audit_and_optimize_part_text(bad_sample, title="Test", part_num=1)
        
        self.assertNotIn("vô cùng tức giận", cleaned)
        self.assertNotIn("cười lạnh một tiếng", cleaned)
        self.assertNotIn("như nhìn một con sâu bọ", cleaned)
        self.assertNotIn("đứng sững như trời trồng", cleaned)
        self.assertTrue(len(warns) >= 4)

    def test_cliche_openings_stripped(self):
        """Bảo đảm gỡ bỏ hoàn toàn các mẫu mở đầu rập khuôn cũ ('Nếu bạn vô tình...', 'Tiếng thét...')."""
        cliche_sample = "Nếu bạn vô tình nhận được tấm vé xem phim lúc 0 giờ, hãy cẩn thận."
        cleaned, warns = audit_and_optimize_part_text(cliche_sample, title="Test", part_num=1)
        self.assertFalse(cleaned.startswith("Nếu bạn vô tình"))

    def test_meta_words_stripped(self):
        """Bảo đảm gỡ bỏ từ ngữ meta như 'Đón xem tập tiếp theo'."""
        sample_meta = "Cô quay người bước đi kiêu hãnh. Đón xem tập tiếp theo để chứng kiến màn vả mặt!"
        cleaned, warns = audit_and_optimize_part_text(sample_meta, title="Test", part_num=1)
        self.assertNotIn("Đón xem tập tiếp theo", cleaned)

    def test_grocery_list_warning(self):
        """Bảo đảm phát hiện và cảnh báo độn chữ hóa đơn siêu thị (tấn gạo, tấn mì)."""
        sample_grocery = "Cô đặt mua năm mươi tấn gạo và một trăm nồi lẩu tự sôi cay nồng để tích trữ."
        cleaned, warns = audit_and_optimize_part_text(sample_grocery, title="Test", part_num=1)
        self.assertTrue(any("hóa đơn siêu thị" in w for w in warns))

    def test_validate_story_series_end_to_end(self):
        """Kiểm tra toàn bộ chuỗi validate_story_series trên cấu trúc dữ liệu thực tế."""
        sample_series = {
            "title": "Bản Di Chúc Bí Ẩn",
            "parts": [
                {
                    "part_number": 1,
                    "text": "Chiếc bút máy mạ vàng vừa chạm vào bản di chúc, tôi giơ chiếc bật lửa Zippo lên.",
                }
            ]
        }
        res = validate_story_series(sample_series)
        self.assertTrue(res["quality_audit_passed"])
        self.assertEqual(len(res["parts"]), 1)

    def test_daily_story_factory_zero_duplicates_across_all_10_slots(self):
        """Kiểm chứng toàn bộ 10 slots trong daily_story_factory đạt 100% không trùng lặp đoạn văn."""
        for slot, loader in SLOT_STORY_LOADERS.items():
            story = loader()
            for p in story.get("parts", []):
                text = p.get("full_text", "") or p.get("text", "")
                paras = [x.strip() for x in text.split("\n\n") if len(x.strip()) > 50]
                dups = len(paras) - len(set(paras))
                self.assertEqual(
                    dups, 0,
                    f"Phát hiện {dups} đoạn văn trùng lặp trong Slot {slot} - {p.get('badge_label')}"
                )


    def test_diverse_hook_archetypes_10_completeness(self):
        """Bảo đảm Ma Trận 10 Trường Phái Mở Đầu có đầy đủ 10 Archetype và chiến thuật kép."""
        self.assertEqual(len(DIVERSE_HOOK_ARCHETYPES_10), 10)
        for h in DIVERSE_HOOK_ARCHETYPES_10:
            self.assertIn("archetype_id", h)
            self.assertIn("name", h)
            self.assertIn("sensory_anchor", h)
            self.assertIn("strategy_a_flash", h)
            self.assertIn("strategy_b_detailed", h)
            self.assertIn("best_for", h)
            self.assertTrue(len(h["strategy_a_flash"]) > 10)
            self.assertTrue(len(h["strategy_b_detailed"]) > 20)

    def test_character_universes_10_uniqueness(self):
        """Bảo đảm 10 Vũ Trụ Nhân Vật có tên nhân vật độc bản, không trùng lặp chéo."""
        self.assertEqual(len(CHARACTER_UNIVERSES_10), 10)
        all_prots = []
        for u in CHARACTER_UNIVERSES_10:
            self.assertIn("universe_id", u)
            self.assertIn("domain", u)
            self.assertIn("protagonist_names", u)
            all_prots.extend(u["protagonist_names"])
        # Kiểm tra không có tên nhân vật chính bị trùng lặp giữa các universe
        self.assertEqual(len(all_prots), len(set(all_prots)), "Phát hiện tên nhân vật chính trùng lặp giữa các Universe!")

    def test_diverse_resolutions_10_completeness(self):
        """Bảo đảm có 10 Cơ chế lật kèo độc bản, không chỉ dựa vào công an/thuế."""
        self.assertEqual(len(DIVERSE_RESOLUTIONS_10), 10)
        for r in DIVERSE_RESOLUTIONS_10:
            self.assertIn("resolution_id", r)
            self.assertIn("name", r)
            self.assertIn("mechanism", r)

    def test_jaccard_and_hook_similarity_algorithms(self):
        """Kiểm thử thuật toán tính độ trùng lặp Jaccard và Hook Similarity."""
        text_a = "Chiếc thìa mạ vàng chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm lộ ra."
        text_b = "Chiếc thìa mạ vàng chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ."
        text_c = "Cánh cửa thép ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm vang lên."

        # Hook similarity
        hook_sim_high = calculate_hook_similarity(text_a, text_b)
        hook_sim_low = calculate_hook_similarity(text_a, text_c)
        self.assertTrue(hook_sim_high > 0.60)
        self.assertTrue(hook_sim_low < 0.20)

        # Jaccard similarity
        j_high = calculate_jaccard_similarity(text_a, text_b)
        j_low = calculate_jaccard_similarity(text_a, text_c)
        self.assertTrue(j_high > 0.50)
        self.assertTrue(j_low < 0.20)

    def test_verify_cross_audio_distinctiveness_rejects_duplicate_hook(self):
        """Bảo đảm Cổng Chống Đồng Hóa phát hiện và cảnh báo khi 2 truyện có cùng hook mở đầu."""
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            temp_history = Path(tmpdir) / "test_history.jsonl"
            story_1 = {
                "title": "Chuyện Thứ Nhất",
                "parts": [{"part_number": 1, "text": "Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, sợi len màu xanh lộ ra."}]
            }
            # Lần 1: Thêm story 1 vào history
            passed1, warns1 = verify_cross_audio_distinctiveness(story_1, history_file=temp_history)
            self.assertTrue(passed1)

            # Lần 2: Submit story 2 với hook giống hệt story 1
            story_2 = {
                "title": "Chuyện Thứ Hai Na Ná",
                "parts": [{"part_number": 1, "text": "Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, sợi len màu xanh lộ ra."}]
            }
            passed2, warns2 = verify_cross_audio_distinctiveness(story_2, history_file=temp_history)
            self.assertFalse(passed2)
            self.assertTrue(any("CẢNH BÁO TRÙNG LẶP HOOK" in w for w in warns2))

    def test_kb_consultation_dynamic_lru_rotation(self):
        """Kiểm tra cơ chế xoay vòng LRU trong consult_before_writing bảo đảm không lặp lại Hook Archetype."""
        kb = get_knowledge_base()
        c1 = kb.consult_before_writing(genre_hint="TRONG_SINH", topic_title="Rotation Test 1")
        c2 = kb.consult_before_writing(genre_hint="TRONG_SINH", topic_title="Rotation Test 2")
        
        hook_1_id = c1["recommended_hook_archetype"]["archetype_id"]
        hook_2_id = c2["recommended_hook_archetype"]["archetype_id"]
        self.assertNotEqual(hook_1_id, hook_2_id, "Hai lượt gọi liên tiếp không được nhận cùng một Hook Archetype!")


if __name__ == "__main__":
    unittest.main()
