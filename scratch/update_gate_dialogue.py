with open("core/stories/script_quality_gate.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

target = """def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    \"\"\"
    Tối ưu hóa câu thoại dao găm: Cắt gọt và ngắt nhịp cho các câu thoại dài (> 16 từ).
    Tách các câu thoại dài dòng thành các nhịp thoại gãy gọn, nhấn nhá dưới 12 từ.
    \"\"\"
    pattern = r"[\'\\"\u201c]([^\'\\"\u201d\\n]+)[\'\\"\u201d]"
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
    return optimized_text, fixed_count"""

replacement = """def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    \"\"\"
    Tối ưu hóa câu thoại dao găm: Cắt gọt và ngắt nhịp cho các câu thoại dài (> 14 từ).
    Tách các câu thoại dài dòng thành các nhịp thoại gãy gọn, nhấn nhá dưới 12-14 từ cho Edge-TTS.
    \"\"\"
    pattern = r"[\'\\\"\\u201c\\u2018]([^\\\'\\\"\\u201d\\u2019\\n]+)[\\\'\\\"\\u201d\\u2019]"
    fixed_count = 0

    def _split_long_clause(clause: str) -> str:
        words = clause.split()
        if len(words) <= 14:
            return clause
        conjs = [" nhưng ", " thế nhưng ", " bởi vì ", " cho nên ", " vậy mà ", " thế mà ", " trong khi ", " và rồi ", " để rồi ", " mà "]
        for c in conjs:
            if c in clause:
                parts = clause.split(c, 1)
                if len(parts[0].split()) >= 4 and len(parts[1].split()) >= 4:
                    left = _split_long_clause(parts[0].strip())
                    right = _split_long_clause(f"{c.strip()} {parts[1].strip()}")
                    return f"{left}... {right}"
        mid = len(words) // 2
        left = _split_long_clause(" ".join(words[:mid]))
        right = _split_long_clause(" ".join(words[mid:]))
        return f"{left}... {right}"

    def _replacer(m):
        nonlocal fixed_count
        content = m.group(1).strip()
        clauses = re.split(r'([.!?…]+)', content)
        new_clauses = []
        changed = False
        for i in range(0, len(clauses), 2):
            c = clauses[i]
            delim = clauses[i+1] if i+1 < len(clauses) else ""
            if len(c.strip().split()) > 14:
                c = _split_long_clause(c)
                changed = True
            new_clauses.append(c + delim)
        if changed:
            fixed_count += 1
            return f"'{''.join(new_clauses)}'"
        return m.group(0)

    optimized_text = re.sub(pattern, _replacer, text)
    return optimized_text, fixed_count"""

assert target in text, "Target not found in script_quality_gate.py"
text = text.replace(target, replacement)

with open("core/stories/script_quality_gate.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully upgraded optimize_dialogue_punchiness in core/stories/script_quality_gate.py!")
