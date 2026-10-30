# -*- coding: utf-8 -*-
from pathlib import Path

gate = Path("core/stories/script_quality_gate.py")
text = gate.read_text(encoding="utf-8")

old_code = """    for part in series_data.get("parts", []):"""
new_code = """    raw_parts = series_data.get("parts", [])
    if isinstance(raw_parts, dict):
        raw_parts = [{"part_number": idx + 1, "text": val} for idx, (k, val) in enumerate(raw_parts.items())]
    for part in raw_parts:"""

text_norm = text.replace("\r\n", "\n")
old_norm = old_code.replace("\r\n", "\n")
new_norm = new_code.replace("\r\n", "\n")

if old_norm in text_norm:
    text_norm = text_norm.replace(old_norm, new_norm)
    gate.write_text(text_norm, encoding="utf-8")
    print("Fixed parts dict handling in script_quality_gate!")
else:
    print("Could not find old_norm in file")
