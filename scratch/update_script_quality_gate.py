# -*- coding: utf-8 -*-
import re

with open("core/stories/script_quality_gate.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

# Check imports & globals
insertion_point = "EXPERIENCE_FILE = EXPERIENCE_10_FILE if EXPERIENCE_10_FILE.exists() else EXPERIENCE_5_FILE\nREPORT_10_FILE = ROOT_DIR / \"docs\" / \"10_CYCLES_AGENT_SCRIPT_AUDIT_REPORT.md\""

new_globals = """EXPERIENCE_FILE = EXPERIENCE_10_FILE if EXPERIENCE_10_FILE.exists() else EXPERIENCE_5_FILE
REPORT_10_FILE = ROOT_DIR / "docs" / "10_CYCLES_AGENT_SCRIPT_AUDIT_REPORT.md"
SCRIPT_HISTORY_FILE = ROOT_DIR / "data" / "script_history.jsonl"

# Tập hợp stop words tiếng Việt dùng để tính toán chỉ số tương đồng từ vựng
VIETNAMESE_STOPWORDS = {
    "và", "của", "là", "có", "trong", "được", "cho", "với", "các", "những", 
    "một", "này", "đó", "đã", "đang", "sẽ", "khi", "thì", "mà", "nhưng", 
    "bởi", "vì", "nếu", "như", "lại", "đến", "từ", "ra", "vào", "lên", 
    "xuống", "về", "qua", "lấy", "làm", "thấy", "biết", "nói", "bảo", 
    "nghe", "nhìn", "đứng", "ngồi", "đi", "bước", "tay", "mắt", "tôi", 
    "anh", "cô", "bà", "ông", "hắn", "nó", "chúng", "người", "ta"
}"""

assert insertion_point in text, "insertion_point not found in script_quality_gate.py"
text = text.replace(insertion_point, new_globals)

# Now add cross-script distinctiveness functions before validate_story_series
functions_block = """def calculate_jaccard_similarity(text1: str, text2: str) -> float:
    \"\"\"Tính chỉ số tương đồng từ vựng Jaccard giữa 2 kịch bản (loại bỏ stopwords tiếng Việt).\"\"\"
    tokens1 = set(t for t in re.findall(r'\\b[a-zà-ỹ0-9_]+\\b', text1.lower()) if len(t) >= 2 and t not in VIETNAMESE_STOPWORDS)
    tokens2 = set(t for t in re.findall(r'\\b[a-zà-ỹ0-9_]+\\b', text2.lower()) if len(t) >= 2 and t not in VIETNAMESE_STOPWORDS)
    if not tokens1 or not tokens2:
        return 0.0
    return len(tokens1 & tokens2) / len(tokens1 | tokens2)


def calculate_hook_similarity(hook1: str, hook2: str) -> float:
    \"\"\"Tính độ trùng lặp của 25 từ đầu tiên giữa 2 phần mở đầu.\"\"\"
    words1 = [w.strip(".,!?:;\\\"'()[]") for w in hook1.lower().split()[:25] if w.strip(".,!?:;\\\"'()[]")]
    words2 = [w.strip(".,!?:;\\\"'()[]") for w in hook2.lower().split()[:25] if w.strip(".,!?:;\\\"'()[]")]
    if not words1 or not words2:
        return 0.0
    common = set(words1) & set(words2)
    return len(common) / max(len(set(words1)), len(set(words2)))


def extract_hook_snippet(story_dict: Dict[str, Any]) -> str:
    \"\"\"Trích xuất 30 từ đầu tiên của Part 1 làm hook mẫu để so sánh.\"\"\"
    parts = story_dict.get("parts", [])
    if not parts:
        return ""
    p1_text = parts[0].get("text", "") or parts[0].get("full_text", "") or parts[0].get("body", "")
    words = p1_text.strip().split()[:30]
    return " ".join(words)


def extract_story_full_text(story_dict: Dict[str, Any]) -> str:
    \"\"\"Trích xuất toàn bộ văn bản của bộ truyện.\"\"\"
    parts = story_dict.get("parts", [])
    full_pieces = []
    for p in parts:
        t = p.get("text", "") or p.get("full_text", "") or p.get("body", "")
        if t:
            full_pieces.append(t)
    return "\\n\\n".join(full_pieces)


def verify_cross_audio_distinctiveness(
    story_dict: Dict[str, Any],
    history_file: Optional[Path] = None,
    max_jaccard_threshold: float = 0.30,
    max_hook_overlap: float = 0.45
) -> Tuple[bool, List[str]]:
    \"\"\"
    Cổng Thẩm Định Chống Đồng Hóa Kịch Bản (Anti-Homogenization & Cross-Script Distinctiveness Gate):
    - Đảm bảo kịch bản mới ĐỘC BẢN HOÀN TOÀN, không na ná hay lặp lại mô-típ các audio trước.
    - So sánh với lịch sử 10 audio gần nhất trong script_history.jsonl:
      1. Hook Part 1 không được trùng cấu trúc quá 45% từ.
      2. Tương đồng từ vựng Jaccard không vượt quá 30% (ngăn chặn tái sử dụng stock phrases).
    - Tự động ghi lại footprint vào script_history.jsonl để bảo vệ các audio kế tiếp.
    \"\"\"
    import json
    from datetime import datetime

    warnings = []
    passed = True
    hist_path = history_file or SCRIPT_HISTORY_FILE
    current_title = story_dict.get("title", "Kịch bản chưa đặt tên")
    current_hook = extract_hook_snippet(story_dict)
    current_full_text = extract_story_full_text(story_dict)

    if not current_hook or not current_full_text:
        return True, warnings

    recent_records = []
    if hist_path.exists():
        try:
            with open(hist_path, "r", encoding="utf-8") as f:
                lines = [ln.strip() for ln in f if ln.strip()]
            for line in lines[-10:]:
                try:
                    recent_records.append(json.loads(line))
                except Exception:
                    pass
        except Exception as e:
            logger.warning(f"Không thể đọc script history: {e}")

    # So sánh với các bản ghi lịch sử
    for idx, rec in enumerate(reversed(recent_records), 1):
        prev_title = rec.get("title", "Audio trước")
        prev_hook = rec.get("hook_snippet", "")
        prev_full_sample = rec.get("full_sample", "")

        # 1. Kiểm tra Hook Overlap
        if prev_hook:
            h_sim = calculate_hook_similarity(current_hook, prev_hook)
            if h_sim >= max_hook_overlap:
                warn_msg = f"CẢNH BÁO TRÙNG LẶP HOOK: Mở đầu Part 1 trùng {h_sim*100:.1f}% từ với '{prev_title}'. Cần dùng Hook Archetype khác!"
                warnings.append(warn_msg)
                passed = False

        # 2. Kiểm tra Jaccard Vocabulary Similarity
        if prev_full_sample:
            j_sim = calculate_jaccard_similarity(current_full_text, prev_full_sample)
            if j_sim >= max_jaccard_threshold:
                warn_msg = f"CẢNH BÁO ĐỒNG HÓA TỪ VỰNG: Độ tương đồng từ vựng với '{prev_title}' là {j_sim*100:.1f}% (> {max_jaccard_threshold*100:.0f}%). Yêu cầu đổi bối cảnh nghề nghiệp!"
                warnings.append(warn_msg)
                passed = False

    # Ghi nhận kịch bản hiện tại vào script_history.jsonl
    hist_path.parent.mkdir(parents=True, exist_ok=True)
    new_record = {
        "timestamp": datetime.now().isoformat(),
        "title": current_title,
        "hook_snippet": current_hook,
        "full_sample": current_full_text[:3000],  # Lưu mẫu 3000 ký tự để so sánh
        "total_words": len(current_full_text.split())
    }
    try:
        with open(hist_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(new_record, ensure_ascii=False) + "\\n")
    except Exception as e:
        logger.warning(f"Không thể ghi script history: {e}")

    return passed, warnings
"""

old_validate = """def validate_story_series(series_data: Dict[str, Any]) -> Dict[str, Any]:
    \"\"\"
    Cổng kiểm duyệt chất lượng Master Script Quality Gate:
    - Bắt buộc đọc qua GEMINI.md và kinh nghiệm 5 vòng trước khi thẩm định.
    - Duyệt qua từng tập trong bộ truyện (Part 1, 2, 3).
    - Đảm bảo 100% tiêu đề khớp với nội dung và không vi phạm bất kỳ điều cấm nào.
    \"\"\"
    codex_info = load_master_codex_rules()
    title = series_data.get("title", "")
    all_warnings = []

    logger.info(f"[ScriptQualityGate] Dang nap kinh nghiem va tham dinh: {title}")

    validated_parts = []
    for part in series_data.get("parts", []):
        p_num = part.get("part_number", 1)
        raw_text = part.get("text", "") or part.get("full_text", "") or part.get("body", "")
        
        opt_text, warnings = audit_and_optimize_part_text(raw_text, title, p_num)
        if warnings:
            all_warnings.extend(warnings)

        part["text"] = opt_text
        part["full_text"] = opt_text
        part["body"] = opt_text
        validated_parts.append(part)

    series_data["parts"] = validated_parts
    series_data["quality_audit_passed"] = True
    series_data["quality_audit_warnings"] = all_warnings

    if all_warnings:
        logger.info(f"  Da toi uu hoa {len(all_warnings)} diem cho kich ban")
    else:
        logger.info(f"  Kich ban dat chuan Masterpiece ngay tu dau, sach sao ngu!")

    return series_data"""

new_validate = functions_block + "\n\n" + """def validate_story_series(series_data: Dict[str, Any]) -> Dict[str, Any]:
    \"\"\"
    Cổng kiểm duyệt chất lượng Master Script Quality Gate:
    - Bắt buộc đọc qua GEMINI.md và kinh nghiệm 10 vòng trước khi thẩm định.
    - Duyệt qua từng tập trong bộ truyện (Part 1, 2, 3).
    - Thẩm định chống đồng hóa & chống lặp mô-típ (Anti-Homogenization Check).
    - Đảm bảo 100% tiêu đề khớp với nội dung và không vi phạm bất kỳ điều cấm nào.
    \"\"\"
    codex_info = load_master_codex_rules()
    title = series_data.get("title", "")
    all_warnings = []

    logger.info(f"[ScriptQualityGate] Dang nap kinh nghiem va tham dinh: {title}")

    validated_parts = []
    for part in series_data.get("parts", []):
        p_num = part.get("part_number", 1)
        raw_text = part.get("text", "") or part.get("full_text", "") or part.get("body", "")
        
        opt_text, warnings = audit_and_optimize_part_text(raw_text, title, p_num)
        if warnings:
            all_warnings.extend(warnings)

        part["text"] = opt_text
        part["full_text"] = opt_text
        part["body"] = opt_text
        validated_parts.append(part)

    series_data["parts"] = validated_parts

    # Cổng thẩm định chống đồng hóa giữa các audio (Anti-Homogenization Gate)
    distinct_passed, distinct_warnings = verify_cross_audio_distinctiveness(series_data)
    if distinct_warnings:
        all_warnings.extend(distinct_warnings)

    series_data["quality_audit_passed"] = True
    series_data["distinctiveness_passed"] = distinct_passed
    series_data["quality_audit_warnings"] = all_warnings

    if all_warnings:
        logger.info(f"  Da toi uu hoa {len(all_warnings)} diem cho kich ban (Bao gom {len(distinct_warnings)} diem chong dong hoa)")
    else:
        logger.info(f"  Kich ban dat chuan Masterpiece doc ban ngay tu dau, sach sao ngu!")

    return series_data"""

assert old_validate in text, "old_validate not found in script_quality_gate.py"
text = text.replace(old_validate, new_validate)

with open("core/stories/script_quality_gate.py", "w", encoding="utf-8", newline="\r\n") as f:
    f.write(text)

print("Successfully updated core/stories/script_quality_gate.py with anti-homogenization gate!")
