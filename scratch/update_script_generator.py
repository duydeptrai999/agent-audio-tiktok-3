# -*- coding: utf-8 -*-
from pathlib import Path

fpath = Path("core/script_generator.py")
text = fpath.read_text(encoding="utf-8")

old_code = '''    def step1_consult_knowledge(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:
        """
        GIAI ĐOẠN 1: Bắt buộc tra cứu cơ sở tri thức trước khi viết.
        """
        logger.info(f"Đang tra cứu cơ sở tri thức cho đề tài: '{topic_title}' (genre: '{genre_hint}')...")'''

new_code = '''    def step1_consult_knowledge(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3,
        genre_hint: str = ""
    ) -> Dict[str, Any]:
        """
        GIAI ĐOẠN 1: Bắt buộc tra cứu cơ sở tri thức và kinh nghiệm 10 vòng trước khi viết.
        """
        from core.stories.script_quality_gate import require_preflight_experience
        require_preflight_experience()
        logger.info(f"Đang tra cứu cơ sở tri thức cho đề tài: '{topic_title}' (genre: '{genre_hint}')...")'''

if old_code in text:
    text = text.replace(old_code, new_code)
    fpath.write_text(text, encoding="utf-8")
    print("Updated step1_consult_knowledge in core/script_generator.py successfully!")
else:
    print("Could not find old_code in core/script_generator.py")
