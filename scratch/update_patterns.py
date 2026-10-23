# -*- coding: utf-8 -*-
from pathlib import Path

file_path = Path("core/stories/script_quality_gate.py")
content = file_path.read_text(encoding="utf-8")

old_patterns = """CLICHE_OPENING_PATTERNS = [
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Đúng\\s+\\d+\\s+giờ",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+hét",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+thét",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+xé",
    r"^Đúng\\s+\\d+\\s+giờ\\s+(sáng|tối)\\s+giữa\\s+đêm\\s+mưa",
    r"^Trời\\s+mưa\\s+như\\s+trút\\s+nước",
    r"^Nếu\\s+bạn\\s+vô\\s+tình",
    r"^Hôm\\s+nay\\s+tôi\\s+sẽ\\s+kể",
    r"^Chào\\s+các\\s+bạn",
]"""

new_patterns = """CLICHE_OPENING_PATTERNS = [
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Đúng\\s+\\d+\\s+giờ",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+hét",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+thét",
    r"^['\\"“][^'\\"”]+['\\"”]\\s*-\\s*Tiếng\\s+xé",
    r"^Đúng\\s+\\d+\\s+giờ\\s+(sáng|tối)\\s+giữa\\s+đêm\\s+mưa",
    r"^Trời\\s+mưa\\s+như\\s+trút\\s+nước",
    r"^Nếu\\s+bạn\\s+vô\\s+tình",
    r"^Hôm\\s+nay\\s+tôi\\s+sẽ\\s+kể",
    r"^Chào\\s+các\\s+bạn",
    r"^Tôi\\s+tên\\s+là",
    r"^Sinh\\s+ra\\s+trong\\s+một",
    r"^Đó\\s+là\\s+một\\s+ngày",
]"""

if old_patterns in content:
    content = content.replace(old_patterns, new_patterns)
    file_path.write_text(content, encoding="utf-8")
    print("Added new cliché patterns successfully.")
else:
    print("Old patterns not matched exactly.")
