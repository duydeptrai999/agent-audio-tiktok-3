# -*- coding: utf-8 -*-
with open("tests/test_script_evolution_and_quality_gate.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

# Add imports if needed
old_imports = """from core.stories.script_quality_gate import (
    load_master_codex_rules,
    require_preflight_experience,
    audit_and_optimize_part_text,
    validate_story_series,
    deduplicate_paragraphs,
    FORBIDDEN_PHRASES,
    CLICHE_OPENING_PATTERNS
)"""

new_imports = """from core.stories.script_quality_gate import (
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
)"""

assert old_imports in text, "old_imports not found in test file"
text = text.replace(old_imports, new_imports)

# Add new test methods
new_tests = """    def test_diverse_hook_archetypes_10_completeness(self):
        \"\"\"Bảo đảm Ma Trận 10 Trường Phái Mở Đầu có đầy đủ 10 Archetype và chiến thuật kép.\"\"\"
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
        \"\"\"Bảo đảm 10 Vũ Trụ Nhân Vật có tên nhân vật độc bản, không trùng lặp chéo.\"\"\"
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
        \"\"\"Bảo đảm có 10 Cơ chế lật kèo độc bản, không chỉ dựa vào công an/thuế.\"\"\"
        self.assertEqual(len(DIVERSE_RESOLUTIONS_10), 10)
        for r in DIVERSE_RESOLUTIONS_10:
            self.assertIn("resolution_id", r)
            self.assertIn("name", r)
            self.assertIn("mechanism", r)

    def test_jaccard_and_hook_similarity_algorithms(self):
        \"\"\"Kiểm thử thuật toán tính độ trùng lặp Jaccard và Hook Similarity.\"\"\"
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
        \"\"\"Bảo đảm Cổng Chống Đồng Hóa phát hiện và cảnh báo khi 2 truyện có cùng hook mở đầu.\"\"\"
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
        \"\"\"Kiểm tra cơ chế xoay vòng LRU trong consult_before_writing bảo đảm không lặp lại Hook Archetype.\"\"\"
        kb = get_knowledge_base()
        c1 = kb.consult_before_writing(genre_hint="TRONG_SINH", topic_title="Rotation Test 1")
        c2 = kb.consult_before_writing(genre_hint="TRONG_SINH", topic_title="Rotation Test 2")
        
        hook_1_id = c1["recommended_hook_archetype"]["archetype_id"]
        hook_2_id = c2["recommended_hook_archetype"]["archetype_id"]
        self.assertNotEqual(hook_1_id, hook_2_id, "Hai lượt gọi liên tiếp không được nhận cùng một Hook Archetype!")
"""

target_footer = """if __name__ == "__main__":
    unittest.main()"""

assert target_footer in text, "target_footer not found"
text = text.replace(target_footer, new_tests + "\n\n" + target_footer)

with open("tests/test_script_evolution_and_quality_gate.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully added new unit tests!")
