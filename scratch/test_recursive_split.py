import re, sys
sys.stdout.reconfigure(encoding='utf-8')

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

long_q = "Tôi không thể nào ngờ rằng một người như cô lại có thể cấu kết với những kẻ ngoài kia để hãm hại toàn bộ gia tộc họ Hoàng mà tôi đã dày công xây dựng suốt bao nhiêu năm qua trên thương trường đầy sóng gió này!"
res = _split_long_clause(long_q)
print("Result:", res)
for sub in res.split("... "):
    print(f" - [{len(sub.strip().split())}w] {sub.strip()}")
