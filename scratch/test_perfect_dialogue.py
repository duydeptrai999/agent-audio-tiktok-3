import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def optimize_dialogue_punchiness(text: str):
    pattern = r"['\"\u201c\u2018]([^'\"\u201d\u2019\n]+)['\"\u201d\u2019]"
    fixed_count = 0

    def _replacer(m):
        nonlocal fixed_count
        q = m.group(1).strip()
        words = q.split()
        if len(words) <= 15:
            return f"'{q}'"
        fixed_count += 1
        
        # Tách theo liên từ hoặc dấu câu
        parts = re.split(r'([,;!?.…:]+|\s+(?:nhưng|thế nhưng|bởi vì|cho nên|vậy mà|thế mà|trong khi|đồng thời|và rồi|ngay khi)\s+)', q)
        beats = []
        curr = []
        for p in parts:
            if not p:
                continue
            curr.append(p)
            if len((''.join(curr)).split()) >= 7:
                beats.append((''.join(curr)).strip(' ,;:'))
                curr = []
        if curr:
            beats.append((''.join(curr)).strip(' ,;:'))
            
        # Nếu vẫn còn beat dài > 16 từ do không có dấu câu, tự động chèn dấu ngắt nhịp giữa chừng
        final_beats = []
        for b in beats:
            b_words = b.split()
            if len(b_words) > 16:
                mid = len(b_words) // 2
                final_beats.append(" ".join(b_words[:mid]))
                final_beats.append(" ".join(b_words[mid:]))
            else:
                final_beats.append(b)
        
        joined = "... ".join([b for b in final_beats if b.strip()])
        return f"'{joined}'"

    optimized_text = re.sub(pattern, _replacer, text)
    return optimized_text, fixed_count

sample = "Hắn ta hét lên: 'Tôi không thể nào ngờ rằng một người như cô lại có thể cấu kết với những kẻ ngoài kia để hãm hại toàn bộ gia tộc họ Hoàng mà tôi đã dày công xây dựng suốt bao nhiêu năm qua!'."
res, count = optimize_dialogue_punchiness(sample)
print("Count:", count)
print("Result:", res)
for q in re.findall(r"'([^']+)'", res):
    print("Words in quote:", len(q.split()))
