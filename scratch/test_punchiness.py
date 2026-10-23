import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def optimize_dialogue(text):
    pattern = r"['\"“]([^'\"”\n]+)['\"”]"
    fixed_count = 0
    def _replacer(m):
        nonlocal fixed_count
        q = m.group(1).strip()
        words = q.split()
        if len(words) <= 16:
            return f"'{q}'"
        fixed_count += 1
        parts = re.split(r'([,;!?.…]+|\s+(?:nhưng|bởi vì|cho nên|vậy mà|thế mà)\s+)', q)
        beats = []
        curr = []
        for p in parts:
            if not p: continue
            curr.append(p)
            if len((''.join(curr)).split()) >= 8:
                beats.append((''.join(curr)).strip(' ,;'))
                curr = []
        if curr:
            beats.append((''.join(curr)).strip(' ,;'))
        return "'" + "... ".join([b for b in beats if b]) + "'"
    return re.sub(pattern, _replacer, text), fixed_count

sample = "Bà Mai quát lớn: 'Đồ ăn cắp trơ trẽn, gia đình tao đón nhận một đứa nhà quê như mày vào cửa là ân huệ lớn nhất đời mày rồi, vậy mà mày dám cấu kết với người ngoài tuồn tài liệu bí mật của tập đoàn ra ngoài bán lấy tiền nuôi trai!'."
res, count = optimize_dialogue(sample)
print(f"Fixed: {count}")
print(f"Result: {res}")
