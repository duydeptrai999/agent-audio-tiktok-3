# -*- coding: utf-8 -*-
from pathlib import Path

kb_file = Path("core/knowledge_base.py")
content = kb_file.read_text(encoding="utf-8")

if "\ndef format_brief_for_prompt(" not in content:
    content += """

def format_brief_for_prompt(brief: Dict[str, Any]) -> str:
    \"\"\"Module-level helper to format knowledge brief.\"\"\"
    return get_knowledge_base().format_brief_for_prompt(brief)
"""
    kb_file.write_text(content, encoding="utf-8")
    print("Added module-level format_brief_for_prompt to core/knowledge_base.py")
else:
    print("Already exists")
