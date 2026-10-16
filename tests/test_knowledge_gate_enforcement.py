# -*- coding: utf-8 -*-
"""
tests/test_knowledge_gate_enforcement.py
Kiểm thử tự động tính nghiêm ngặt của Cổng Kiểm Duyệt Tri Thức (Knowledge Gate).
Bảo đảm 100% không thể sinh kịch bản nếu không thông qua bước tra cứu tri thức!
"""

import sys
import unittest
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from core.knowledge_base import (
    get_knowledge_base,
    require_knowledge_consultation,
    verify_knowledge_gate,
    KnowledgeGateViolationError
)
from core.script_generator import get_script_engine
from core.narrative_synthesizer import get_masterpiece_narrative

class TestKnowledgeGateEnforcement(unittest.TestCase):

    def setUp(self):
        self.engine = get_script_engine()

    def test_gate_rejects_none_consultation(self):
        """Kịch bản không truyền consult_data phải bị ném ngoại lệ KnowledgeGateViolationError ngay lập tức"""
        with self.assertRaises(KnowledgeGateViolationError):
            verify_knowledge_gate(None)

    def test_gate_rejects_empty_dict(self):
        """Kịch bản truyền dict rỗng không có token phải bị ném ngoại lệ"""
        with self.assertRaises(KnowledgeGateViolationError):
            verify_knowledge_gate({})

    def test_gate_rejects_forged_token_without_cases(self):
        """Kịch bản có token giả mạo nhưng không có danh sách Case Study thật phải bị chặn"""
        with self.assertRaises(KnowledgeGateViolationError):
            verify_knowledge_gate({"consultation_token": "FAKE_TOKEN_123", "relevant_cases": []})

    def test_step2_blueprint_rejects_bypassed_consultation(self):
        """step2_build_blueprint phải ném lỗi nếu consult_data không hợp lệ"""
        with self.assertRaises(KnowledgeGateViolationError):
            self.engine.step2_build_blueprint(
                genre_key="TRONG_SINH",
                title="Test Bypass",
                premise="Test",
                consult_data={}
            )

    def test_step3_synthesize_rejects_bypassed_consultation(self):
        """step3_synthesize_script phải ném lỗi nếu consult_data không hợp lệ"""
        with self.assertRaises(KnowledgeGateViolationError):
            self.engine.step3_synthesize_script(
                genre_key="TRONG_SINH",
                title="Test Bypass",
                premise="Test",
                consult_data=None
            )

    def test_narrative_synthesizer_rejects_bypassed_consultation(self):
        """get_masterpiece_narrative phải ném lỗi nếu consult_data=None"""
        with self.assertRaises(KnowledgeGateViolationError):
            get_masterpiece_narrative(
                genre_key="TRONG_SINH",
                consult_data=None
            )

    def test_valid_consultation_passes_gate(self):
        """Khi tra cứu hợp lệ qua step1_consult_knowledge, token được cấp và vượt qua cổng an toàn"""
        consult_data = self.engine.step1_consult_knowledge(
            topic_title="Thiên Kim Trở Về",
            topic_summary="Trọng sinh vả mặt trà xanh và tra nam",
            genre_hint="TRONG_SINH"
        )
        self.assertIn("consultation_token", consult_data)
        self.assertTrue(consult_data["consultation_token"].startswith("TOKEN_KB_"))
        self.assertGreaterEqual(len(consult_data["relevant_cases"]), 1)
        self.assertTrue(verify_knowledge_gate(consult_data))

if __name__ == "__main__":
    unittest.main()
