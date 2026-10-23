# -*- coding: utf-8 -*-
from pathlib import Path

kb_file = Path("core/knowledge_base.py")
content = kb_file.read_text(encoding="utf-8")

helper_func = """

def format_brief_for_prompt(brief: Dict[str, Any]) -> str:
    \"\"\"Helper xuất chuỗi format từ knowledge brief.\"\"\"
    return get_knowledge_base().format_brief_for_prompt(brief)
"""

if "def format_brief_for_prompt(" not in content:
    content += helper_func
    kb_file.write_text(content, encoding="utf-8")
    print("Added format_brief_for_prompt helper to core/knowledge_base.py")
