# -*- coding: utf-8 -*-
with open("core/stories/script_quality_gate.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

target = """def check_sentence_length_and_rhythm(text: str) -> List[str]:"""

punchiness_func = """def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    \"\"\"
    Tối ưu hóa câu thoại dao găm: Cắt gọt và ngắt nhịp cho các câu thoại dài (> 16 từ).
    Tách các câu thoại dài dòng thành các nhịp thoại gãy gọn, nhấn nhá dưới 12 từ.
    \"\"\"
    pattern = r"['\"“]([^'\"”\\n]+)['\"”]"
    fixed_count = 0

    def _replacer(m):
        nonlocal fixed_count
        q = m.group(1).strip()
        words = q.split()
        if len(words) <= 16:
            return f"'{q}'"
        fixed_count += 1
        parts = re.split(r'([,;!?.…]+|\\s+(?:nhưng|bởi vì|cho nên|vậy mà|thế mà|trong khi|đồng thời)\\s+)', q)
        beats = []
        curr = []
        for p in parts:
            if not p:
                continue
            curr.append(p)
            if len((''.join(curr)).split()) >= 7:
                beats.append((''.join(curr)).strip(' ,;'))
                curr = []
        if curr:
            beats.append((''.join(curr)).strip(' ,;'))
        
        joined = "... ".join([b for b in beats if b])
        return f"'{joined}'"

    optimized_text = re.sub(pattern, _replacer, text)
    return optimized_text, fixed_count


def check_sentence_length_and_rhythm(text: str) -> List[str]:"""

assert target in text, "Target check_sentence_length_and_rhythm not found!"
text = text.replace(target, punchiness_func)

# Call inside audit_and_optimize_part_text
target_call = """    # 3.2. Cảnh báo độn chữ hóa đơn siêu thị (Grocery List Padding)
    grocery_patterns = ["tấn gạo", "tấn mì", "nồi lẩu tự sôi"]
    for g in grocery_patterns:
        if g in cleaned_text.lower():
            warnings.append(f"CẢNH BÁO: Phát hiện hóa đơn siêu thị '{g}', khuyến nghị mô tả thiết bị cơ học thay thế.")"""

call_addition = """    # 3.2. Cảnh báo độn chữ hóa đơn siêu thị (Grocery List Padding)
    grocery_patterns = ["tấn gạo", "tấn mì", "nồi lẩu tự sôi"]
    for g in grocery_patterns:
        if g in cleaned_text.lower():
            warnings.append(f"CẢNH BÁO: Phát hiện hóa đơn siêu thị '{g}', khuyến nghị mô tả thiết bị cơ học thay thế.")

    # 3.3. Tối ưu câu thoại dao găm (Punchy Dialogue dưới 12-16 từ)
    cleaned_text, diag_fixed = optimize_dialogue_punchiness(cleaned_text)
    if diag_fixed > 0:
        warnings.append(f"Đã tự động tối ưu ngắt nhịp dao găm cho {diag_fixed} câu thoại dài.")"""

assert target_call in text, "target_call not found!"
text = text.replace(target_call, call_addition)

with open("core/stories/script_quality_gate.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully added optimize_dialogue_punchiness to core/stories/script_quality_gate.py!")
