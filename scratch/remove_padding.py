from pathlib import Path

p = Path("core/narrative_synthesizer.py")
content = p.read_text(encoding="utf-8")

old_func = """def ensure_part_word_count_and_uniqueness(paragraphs: List[str], genre_key: str, target_words: int = 3500) -> str:
    \"\"\"
    Đảm bảo 100% đoạn văn là duy nhất và tổng số từ đạt chuẩn >= 3,460 từ.
    \"\"\"
    # 1. Deduplicate while preserving order
    unique_paras: List[str] = []
    seen = set()
    for p in paragraphs:
        cleaned = p.strip()
        if cleaned and cleaned not in seen:
            unique_paras.append(cleaned)
            seen.add(cleaned)
            
    # 2. If short of target_words, generate unique padding paragraphs
    cur_words = sum(len(p.split()) for p in unique_paras)
    if cur_words < target_words:
        needed_paras = generate_unique_prose_padding(genre_key, target_words, unique_paras)
        unique_paras.extend(needed_paras)
        
    return "\\n\\n".join(unique_paras)"""

new_func = """def ensure_part_word_count_and_uniqueness(paragraphs: List[str], genre_key: str, target_words: int = 3500) -> str:
    \"\"\"
    Đảm bảo 100% đoạn văn là duy nhất và KHÔNG BAO GIỜ độn chữ cơ học (Zero Synthetic Padding).
    Chất lượng kịch tính, nhịp thở và xúc cảm chân thật là ưu tiên tuyệt đối.
    \"\"\"
    unique_paras: List[str] = []
    seen = set()
    for p in paragraphs:
        cleaned = p.strip()
        if cleaned and cleaned not in seen:
            unique_paras.append(cleaned)
            seen.add(cleaned)
            
    # Triệt tiêu hoàn toàn padding ma trận vô hồn để kịch bản không bị 'giả tạo/độ nhạt'
    return "\\n\\n".join(unique_paras)"""

norm_content = content.replace("\r\n", "\n")
norm_old = old_func.replace("\r\n", "\n")
norm_new = new_func.replace("\r\n", "\n")

if norm_old in norm_content:
    updated = norm_content.replace(norm_old, norm_new, 1)
    p.write_text(updated, encoding="utf-8")
    print("REMOVED SYNTHETIC PADDING FROM NARRATIVE SYNTHESIZER!")
else:
    print("OLD FUNC NOT FOUND")
