import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def optimize_dialogue_punchiness(text: str):
    pattern = r"['\"\u201c\u2018]([^'\"\u201d\u2019\n]+)['\"\u201d\u2019]"
    fixed_count = 0

    def _split_long_clause(clause: str) -> str:
        words = clause.split()
        if len(words) <= 14:
            return clause
        conjs = [" nhưng ", " thế nhưng ", " bởi vì ", " cho nên ", " vậy mà ", " thế mà ", " trong khi ", " và rồi ", " để rồi "]
        for c in conjs:
            if c in clause:
                parts = clause.split(c, 1)
                if len(parts[0].split()) >= 4 and len(parts[1].split()) >= 4:
                    return f"{parts[0].strip()}... {c.strip()} {parts[1].strip()}"
        mid = len(words) // 2
        return " ".join(words[:mid]) + "... " + " ".join(words[mid:])

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
    return optimized_text, fixed_count

test_quote = "'Mật mã mở vali gồm sáu chữ số, chính là ngày hai cậu cùng nhận tấm Huân chương Chiến công Hạng Nhất!'"
res, count = optimize_dialogue_punchiness(test_quote)
print("Count:", count)
print("Result:", res)
for sub in re.split(r'[.!?…]+', res.strip("'")):
    if sub.strip():
        print(f" - [{len(sub.strip().split())}w] {sub.strip()}")
