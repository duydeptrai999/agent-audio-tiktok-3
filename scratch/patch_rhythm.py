from pathlib import Path

p = Path("core/stories/script_quality_gate.py")
content = p.read_text(encoding="utf-8")

rhythm_logic = """def optimize_sentence_rhythm(text: str) -> Tuple[str, int]:
    \"\"\"
    Tự động chèn dấu ngắt nhịp (phẩy, gạch ngang) cho các câu dài > 22 từ tại các liên từ tự nhiên.
    Giúp Edge-TTS lấy hơi và nhấn nhá kịch tính.
    \"\"\"
    fixed_count = 0
    sentences = re.split(r'([.!?…\\n]+)', text)
    new_pieces = []
    
    conjunctions = [
        " nhưng ", " thế nhưng ", " bởi vì ", " khiến cho ", " làm cho ", 
        " trong khi ", " đồng thời ", " và rồi ", " bất ngờ ", " ngay lập tức "
    ]
    
    for i in range(0, len(sentences), 2):
        s = sentences[i]
        delim = sentences[i+1] if i+1 < len(sentences) else ""
        words = s.split()
        if len(words) > 22 and not any(p in s for p in [',', ' - ', ';', ':']):
            replaced = False
            for conj in conjunctions:
                if conj in s:
                    s = s.replace(conj, f\",{conj.lstrip()}\", 1)
                    replaced = True
                    fixed_count += 1
                    break
            if not replaced and len(words) > 25:
                mid_idx = len(words) // 2
                words[mid_idx] = words[mid_idx] + ","
                s = " ".join(words)
                fixed_count += 1
        new_pieces.append(s + delim)
        
    return "".join(new_pieces), fixed_count
"""

# Insert before check_sentence_length_and_rhythm
if "def optimize_sentence_rhythm" not in content:
    content = content.replace("def check_sentence_length_and_rhythm", rhythm_logic + "\n\ndef check_sentence_length_and_rhythm")

# In audit_and_optimize_part_text, call optimize_sentence_rhythm
old_call = """    rhythm_warns = check_sentence_length_and_rhythm(cleaned_text)
    if rhythm_warns:
        warnings.extend(rhythm_warns)"""

new_call = """    cleaned_text, r_fixed = optimize_sentence_rhythm(cleaned_text)
    if r_fixed > 0:
        warnings.append(f"Đã tự động tối ưu ngắt nhịp thở Edge-TTS cho {r_fixed} câu dài.")

    rhythm_warns = check_sentence_length_and_rhythm(cleaned_text)
    if rhythm_warns:
        warnings.extend(rhythm_warns)"""

if old_call in content:
    content = content.replace(old_call, new_call)

p.write_text(content, encoding="utf-8")
print("OPTIMIZED RHYTHM IN SCRIPT QUALITY GATE!")
