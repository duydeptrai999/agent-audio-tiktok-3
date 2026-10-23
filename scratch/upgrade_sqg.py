# -*- coding: utf-8 -*-
from pathlib import Path

sqg_file = Path("core/stories/script_quality_gate.py")
content = sqg_file.read_text(encoding="utf-8")

old_block = """    codex_info = load_master_codex_rules()

    title = series_data.get("title", "")

    all_warnings = []

    logger.info(f"[ScriptQualityGate] Dang nap kinh nghiem va tham dinh: {title}")"""

new_block = """    codex_info = load_master_codex_rules()

    title = series_data.get("title", "")

    all_warnings = []

    logger.info(f"[ScriptQualityGate] Dang nap kinh nghiem va tham dinh: {title}")

    # BẮT BUỘC TRA CỨU TRI THỨC 100 KIỆT TÁC: Tự động tra cứu và cấp token nếu chưa có
    if not series_data.get("consultation_token"):
        try:
            from core.knowledge_base import require_knowledge_consultation
            brief = require_knowledge_consultation(
                topic_title=title,
                topic_summary=title,
                genre_hint=series_data.get("genre", "TRONG_SINH")
            )
            series_data["consultation_token"] = brief.get("consultation_token", "")
            series_data["knowledge_brief"] = brief
            logger.info(f"  [ScriptQualityGate] Da tra cuu Knowledge Base thanh cong, cap token: {series_data['consultation_token']}")
        except Exception as e:
            logger.warning(f"  [ScriptQualityGate] Khong the tra cuu Knowledge Base: {e}")"""

norm_content = content.replace("\r\n", "\n")
norm_old = old_block.replace("\r\n", "\n")
norm_new = new_block.replace("\r\n", "\n")

if norm_old in norm_content:
    norm_content = norm_content.replace(norm_old, norm_new)
    sqg_file.write_text(norm_content, encoding="utf-8")
    print("Successfully upgraded validate_story_series in core/stories/script_quality_gate.py with auto Knowledge Gate consultation!")
else:
    print("Warning: old_block not found in script_quality_gate.py")
