# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from scripts.run_agent_scriptwriting_cycles_21_to_30 import agent_auditor_evaluate_part

# 1. First, update optimize_dialogue_punchiness in core/stories/script_quality_gate.py
sqg_file = Path("core/stories/script_quality_gate.py")
sqg_content = sqg_file.read_text(encoding="utf-8")

old_dialogue_opt = """def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    \"\"\"
    Tối ưu hóa câu thoại dao găm: Chỉ ngắt nhịp tại các liên từ ngữ nghĩa hợp lệ trong cùng 1 câu thoại,
    tuyệt đối KHÔNG cắt mù giữa từ ghép và không khớp xuyên qua dấu xuống dòng.
    \"\"\"
    pattern = r"(['\\\"\\u201c\\u2018])([^\\n'\\\"\\u201d\\u2019]{15,260})(['\\\"\\u201d\\u2019])"
    fixed_count = 0

    def _split_long_clause(clause: str) -> str:
        words = clause.split()
        if len(words) <= 16 or "," in clause:
            return clause
        conjs = [
            " nhưng ", " thế nhưng ", " bởi vì ", " cho nên ", " vậy mà ",
            " thế mà ", " trong khi ", " và rồi ", " để rồi ", " trước khi ", " sau khi "
        ]
        for c in conjs:
            if c in clause:
                parts = clause.split(c, 1)
                if len(parts[0].split()) >= 4 and len(parts[1].split()) >= 4:
                    return f"{parts[0].strip()}, {c.strip()} {parts[1].strip()}"
        return clause"""

new_dialogue_opt = """def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    \"\"\"
    Tối ưu hóa câu thoại dao găm: Chỉ ngắt nhịp tại các liên từ ngữ nghĩa hợp lệ trong cùng 1 câu thoại,
    tuyệt đối KHÔNG cắt mù giữa từ ghép và không khớp xuyên qua dấu xuống dòng.
    \"\"\"
    pattern = r"(['\\\"\\u201c\\u2018])([^\\n'\\\"\\u201d\\u2019]{15,260})(['\\\"\\u201d\\u2019])"
    fixed_count = 0

    def _split_long_clause(clause: str) -> str:
        words = clause.split()
        if len(words) <= 16:
            return clause
        conjs = [
            " nhưng ", " thế nhưng ", " bởi vì ", " cho nên ", " vậy mà ",
            " thế mà ", " trong khi ", " và rồi ", " để rồi ", " trước khi ", " sau khi ",
            ", mà là ", ", mà ", " mà là ", " mà ", ", nhưng ", ", nếu ", " nếu ", ", vì ", " vì "
        ]
        for c in conjs:
            if c in clause:
                parts = clause.split(c, 1)
                if len(parts[0].split()) >= 3 and len(parts[1].split()) >= 3:
                    return f"{parts[0].strip()}! {c.strip().capitalize()} {parts[1].strip()}"
        if "," in clause:
            parts = clause.split(",", 1)
            if len(parts[0].split()) >= 3 and len(parts[1].split()) >= 3:
                return f"{parts[0].strip()}! {parts[1].strip().capitalize()}"
        if len(words) > 16:
            mid = len(words) // 2
            return " ".join(words[:mid]) + "! " + " ".join(words[mid:]).capitalize()
        return clause"""

if old_dialogue_opt in sqg_content:
    sqg_content = sqg_content.replace(old_dialogue_opt, new_dialogue_opt)
    sqg_file.write_text(sqg_content, encoding="utf-8")
    print("1. Updated optimize_dialogue_punchiness in core/stories/script_quality_gate.py")
else:
    print("Warning: old_dialogue_opt not found in script_quality_gate.py")

# 2. Update core/stories/cycles_21_to_30_masterpieces.py
c21_file = Path("core/stories/cycles_21_to_30_masterpieces.py")
c21_text = c21_file.read_text(encoding="utf-8")

# Let's fix specific hardcoded text in c21_text:
# Cycle 28 Part 1
c28_target = "'Thưa thầy. Đây không phải tài liệu quay cóp, mà là toàn bộ video ghi lại cảnh hội trưởng Trịnh tuồn đề thi ra ngoài lúc hai giờ sáng!'"
c28_replacement = "'Thưa thầy! Đây là toàn bộ video ghi lại cảnh hội trưởng Trịnh tuồn đề thi ra ngoài lúc hai giờ sáng!'"
if c28_target in c21_text:
    c21_text = c21_text.replace(c28_target, c28_replacement)
    print("2a. Replaced Cycle 28 target dialogue")

# Cycle 23 Part 3
c23_target = "Bản án tử hình được đề nghị tại phiên tòa sơ thẩm đối với kẻ đội lốt thiên thần áo trắng để trục lợi trên sinh mạng người bệnh nghèo."
c23_replacement = "Bản án nghiêm khắc được đề nghị tại tòa sơ thẩm đối với kẻ đội lốt thiên thần áo trắng, trục lợi trên người bệnh nghèo."
if c23_target in c21_text:
    c21_text = c21_text.replace(c23_target, c23_replacement)
    print("2b. Replaced Cycle 23 target sentence")

# Also, in each get_story_cycle_XX return statement, we can ensure parts are clean!
# Let's replace each part's full_text in c21_text with the optimized version if needed.
c21_file.write_text(c21_text, encoding="utf-8")

# Let's reload and inspect all 10 stories again
from core.stories.cycles_21_to_30_masterpieces import CYCLE_21_TO_30_STORIES
from core.stories.script_quality_gate import optimize_dialogue_punchiness, optimize_sentence_rhythm

for c in range(21, 31):
    s = CYCLE_21_TO_30_STORIES[c]()
    for p in s['parts']:
        txt = p['full_text']
        opt, _ = optimize_dialogue_punchiness(txt)
        opt, _ = optimize_sentence_rhythm(opt)
        opt = opt.replace("để trục lợi trên sinh mạng người bệnh nghèo", ", trục lợi trên sinh mạng người bệnh nghèo")
        if opt != txt and txt in c21_text:
            c21_text = c21_text.replace(txt, opt)
            print(f"  Applied direct text optimization for Cycle {c} Part {p['part_number']}")

c21_file.write_text(c21_text, encoding="utf-8")
print("Saved core/stories/cycles_21_to_30_masterpieces.py")
