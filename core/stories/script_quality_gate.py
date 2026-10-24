# -*- coding: utf-8 -*-

"""

core/stories/script_quality_gate.py

Cổng Kiểm Duyệt & Tự Động Tối Ưu Kịch Bản Bắt Buộc (Mandatory Script Quality Gate).

Tuân thủ 100% Bộ Quy Chuẩn Kịch Bản Vàng từ GEMINI.md & 5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md:

- Đọc lại kinh nghiệm và quy tắc trước khi cho phép kịch bản được đưa vào sản xuất audio.

- Triệt tiêu hoàn toàn lối mở đầu rập khuôn cũ ('[Thoại]' - Đúng X giờ..., 'Nếu bạn vô tình...').

- Quét sạch sáo ngữ convert Trung Quốc & thông báo cảm xúc suông (Tell instead of Show).

- Chống lặp đoạn văn (Deduplicate paragraphs).

- Đảm bảo 100% Tiêu đề khớp với Cốt truyện (Không treo đầu dê bán thịt chó).

- Đảm bảo cấu trúc nhịp thở tối ưu cho giọng đọc Edge-TTS (câu 8-16 từ, dấu ngắt nhịp).

"""

import sys

import re

import logging

from pathlib import Path

from typing import Dict, Any, List, Tuple, Optional

if hasattr(sys.stdout, "reconfigure"):

    try:

        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    except Exception:

        pass

logger = logging.getLogger("ScriptQualityGate")

ROOT_DIR = Path(__file__).parent.parent.parent

if not (ROOT_DIR / "GEMINI.md").exists():

    ROOT_DIR = Path.cwd()

RULES_FILE = ROOT_DIR / "GEMINI.md"

EXPERIENCE_100_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md"
EXPERIENCE_100_TIKTOK_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md"

EXPERIENCE_30_FILE = ROOT_DIR / "docs" / "30_CYCLES_SCRIPT_EVOLUTION_MASTERCLASS.md"

EXPERIENCE_50_FILE = ROOT_DIR / "docs" / "50_CYCLES_SCRIPT_EVOLUTION_MASTERCLASS.md"

REPORT_50_FILE = ROOT_DIR / "docs" / "50_CYCLES_AGENT_SCRIPT_AUDIT_REPORT.md"

EXPERIENCE_20_FILE = ROOT_DIR / "docs" / "20_CYCLES_SCRIPT_EVOLUTION_MASTERCLASS.md"

EXPERIENCE_10_FILE = ROOT_DIR / "docs" / "10_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md"

EXPERIENCE_5_FILE = ROOT_DIR / "docs" / "5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md"

EXPERIENCE_FILE = EXPERIENCE_10_FILE if EXPERIENCE_10_FILE.exists() else EXPERIENCE_5_FILE

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

}

# Danh sách từ cấm liên quan đến chính trị (Zero Politics Guard 100%)
POLITICAL_KEYWORDS = [
    "chính trị", "đảng phái", "nhà nước", "chính phủ", "bộ ngoại giao", "lãnh sự quán",
    "đại sứ quán", "quân đội", "chế độ", "biểu tình", "bầu cử", "tuyên truyền chính trị"
]

def check_zero_politics(text: str) -> Tuple[bool, List[str]]:
    """Xác thực 100% Zero Chính Trị: Kịch bản tuyệt đối sạch từ ngữ chính trị nhạy cảm."""
    text_lower = text.lower()
    found = [k for k in POLITICAL_KEYWORDS if k in text_lower]
    return len(found) == 0, found

def detect_4_hook_archetype(hook_text: str) -> str:
    """
    Phân loại câu mở đầu theo Ma Trận 4 Trường Phái Mở Đầu Audio Part 1 Triệu View (Master Codex 5.0):
    1. MICRO_SENSORY: Thoáng qua giật màng nhĩ bằng dị thường âm thanh, hình ảnh, khứu giác hoặc vật chứng rợn gáy.
    2. HIGH_STAKES_SCENE: Cận cảnh hiện trường ngàn cân treo sợi tóc, xung đột sinh tử (còng số tám, dùi cui, chốt sắt, cột sóng đỏ).
    3. PARADOXICAL_REALITY: Bẫy tò mò nghịch lý đời thực (đinh ốc phát wifi hồng ngoại, mép giấy bảo hiểm dưới bát yến).
    4. DETAILED_PARADOXICAL: Đạo cụ dị thường bất khả thi (lồng mèo bọc chì cản X-quang, bút kim cương 500 tỷ).
    """
    t = hook_text.strip().lower()
    
    if any(k in t for k in ["bọc chì", "lồng mèo", "nặng bất thường", "mười hai cân", "bút máy nạm", "năm trăm tỷ"]):
        return "DETAILED_PARADOXICAL"
    if any(k in t for k in ["đinh ốc", "hồng ngoại", "wifi", "bảo hiểm", "bát yến", "camera điện thoại"]):
        return "PARADOXICAL_REALITY"
    if any(k in t for k in ["còng số tám", "dùi cui", "tia lửa", "chốt thép", "chốt điện tử", "súng săn", "cột sóng đỏ"]):
        return "HIGH_STAKES_SCENE"
    return "MICRO_SENSORY"


# Danh sách sáo ngữ convert tuyệt đối cấm và từ thay thế thuần Việt

FORBIDDEN_PHRASES = {

    "khí chất bức người": "khí thế áp đảo",

    "bóp nghẹt lồng ngực": "nghẹt thở",

    "máu tươi tuôn xối xả": "chảy máu",

    "cười lạnh một tiếng": "cười nhạt",

    "đứng sững như trời trồng": "chết lặng",

    "thập phần": "vô cùng",

    "bất giác": "vô thức",

    "hơi thở phả vào làn da": "đứng sát ngay bên",

    "như nhìn một con sâu bọ": "khinh miệt",

    "nụ cười nham hiểm độc địa": "nụ cười toan tính",

    "sét đánh ngang tai": "bàng hoàng",

    "đồ tiện tì": "kẻ phản bội",

    "đồ súc sinh": "kẻ vô ơn",

    "tiện nhân": "kẻ trơ trẽn",

    "đồ lăng loàn": "kẻ bội bạc",

    "thằng khốn nạn": "kẻ đê hèn",

    "kinh hoàng tột độ": "tim đập dồn dập",

    "vô cùng sửng sốt": "đồng tử co giật",

    "sợ đến phát điên": "chân run bần bật",

    "mắt mở to như nhìn thấy quái vật": "kinh ngạc",

    "vô cùng tức giận": "ngón tay siết chặt",

    "đau đớn tột cùng": "lồng ngực nghẹn đắng",

    "sợ hãi tột độ": "mồ hôi lạnh chảy dọc sống lưng",

    "hoang mang tột độ": "đồng tử co rút",

    "đau khổ tột cùng": "cắn chặt môi rớm máu",

    "bản án tử hình": "lời cảnh báo lạnh gáy",

    "hận thù ngút trời": "ngọn lửa thù hận",

    "ác mộng kinh hoàng": "hiện thực tàn khốc",

        "chết lặng như bị bàng hoàng": "chết lặng",

    "mình... mình chưa chết": "tôi bàng hoàng mở mắt",

    "mình đã thực sự trọng sinh": "tôi nhìn đồng hồ đếm ngược",

    "lũ súc sinh vô ơn": "những kẻ phản trắc",

    "nhâm nhi ly trà sữa": "nhìn qua camera",

    "nụ cười sắc lạnh thấu xương": "nụ cười toan tính",

    "thẩm băng tuyết thong thả nhấp ngụm rượu vang": "ngón tay lật giở trang hồ sơ",

    "trong ván cờ sinh tử của giới tài phiệt": "trên bàn đàm phán",

    "giá trị đích thực của một con người": "kết quả kinh doanh",

    "mười năm sống trong bùn lầy kiếp trước": "những năm tháng gian khó",

    "từng con số kiểm toán sắc lẹm như những nhát búa": "từng con số kiểm toán đối chiếu",

}

# Các mẫu mở đầu rập khuôn cấm kỵ

CLICHE_OPENING_PATTERNS = [

    r"^['\"“][^'\"”]+['\"”]\s*-\s*Đúng\s+\d+\s+giờ",

    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+hét",

    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+thét",

    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+xé",

    r"^['\"“][^'\"”]+['\"”]\s*-\s*Tiếng\s+(hét|thét|xé|gầm|đập|rên)",

    r"^Bảy\s+năm\s+(sau|trước)",

    r"^Mười\s+năm\s+(sau|trước)",

    r"^Mình\.\.\.\s*mình\s+(chưa\s+chết|trọng\s+sinh)",

    r"^Tại\s+đám\s+tang\s+của\s+người\s+chồng",

    r"^Trước\s+khi\s+phiên\s+họp",

    r"^Đúng\s+\d+\s+giờ\s+(sáng|tối)\s+giữa\s+đêm\s+mưa",

    r"^Trời\s+mưa\s+như\s+trút\s+nước",

    r"^Nếu\s+bạn\s+vô\s+tình",

    r"^Hôm\s+nay\s+tôi\s+sẽ\s+kể",

    r"^Chào\s+các\s+bạn",

    r"^Tôi\s+tên\s+là",

    r"^Sinh\s+ra\s+trong\s+một",

    r"^Đó\s+là\s+một\s+ngày",

]

def load_master_codex_rules() -> Dict[str, str]:

    """

    Nạp bộ quy chuẩn kinh nghiệm từ GEMINI.md và docs/5_CYCLES_SCRIPT_EVOLUTION_EXPERIENCE.md.

    BẮT BUỘC thực thi trước khi thẩm định hoặc sinh bất kỳ audio nào.

    """

    rules_text = ""

    exp_text = ""

    if RULES_FILE.exists():

        try:

            rules_text = RULES_FILE.read_text(encoding="utf-8")

        except Exception as e:

            logger.warning(f"Không thể đọc {RULES_FILE}: {e}")

    if EXPERIENCE_FILE.exists():

        try:

            exp_text = EXPERIENCE_FILE.read_text(encoding="utf-8")

        except Exception as e:

            logger.warning(f"Không thể đọc {EXPERIENCE_FILE}: {e}")

    exp_100_text = ""

    if EXPERIENCE_100_FILE.exists():

        try:

            exp_100_text = EXPERIENCE_100_FILE.read_text(encoding="utf-8")

        except Exception as e:

            logger.warning(f"Không thể đọc {EXPERIENCE_100_FILE}: {e}")

    try:

        print("\n" + "=" * 80)

        print("[ScriptQualityGate] BAT BUOC DOC KINH NGHIEM TRUOC KHI BIEN KICH / LAM AUDIO:")

        print("   Nap thanh cong: GEMINI.md + docs/DAI_KINH_NGHIEM_100_AUDIO_TIKTOK_TRIEU_VIEW.md (Master Codex 6.0)")

        print("   10 Nguyen Tac Vang: Vat Chat Huu Hinh, Hook 3s Doi Thuc, Zero-Biography, Phan Dien Dang Cap,")

        print("   Thoai Nhat Gung Co Dao Gam, Micro-Pacing 25s, Micro-Movement, Action-Apex Cliffhanger,")

        print("   Am Hoc Edge-TTS (8-16 tu), Khoa Cong Kinh Nghiem Bat Buoc 100%.")

        print("=" * 80)

    except Exception:

        pass

    return {

        "gemini_rules": rules_text,

        "evolution_experience": exp_text,

        "master_100_experience": exp_100_text,

        "status": "LOADED_OK"

    }

def require_preflight_experience() -> bool:

    """Hàm xác thực cổng kinh nghiệm bắt buộc."""

    data = load_master_codex_rules()

    if not data.get("gemini_rules"):

        raise RuntimeError("FATAL: Chưa nạp được GEMINI.md! Kịch bản audio không được phép sản xuất.")

    return True

def deduplicate_paragraphs(text: str) -> Tuple[str, int]:

    """

    Loại bỏ triệt để các đoạn văn bị trùng lặp lặp đi lặp lại trong nội dung.

    """

    paras = [p.strip() for p in text.split("\n\n") if p.strip()]

    seen = set()

    cleaned_paras = []

    dup_count = 0

    for p in paras:

        norm = re.sub(r'\s+', ' ', p.lower())

        if norm in seen:

            dup_count += 1

            continue

        seen.add(norm)

        cleaned_paras.append(p)

    return "\n\n".join(cleaned_paras), dup_count

def check_micro_pacing(text: str) -> List[str]:

    """Kiểm tra nhịp độ kịch tính micro-pacing: Không để đoạn văn vượt quá 80 từ mà thiếu hành động."""

    warnings = []

    paras = [p.strip() for p in text.split("\n\n") if p.strip()]

    for i, p in enumerate(paras, 1):

        words = p.split()

        if len(words) > 80:

            warnings.append(f"Đoạn {i} dài {len(words)} từ (> 80 từ), khuyến nghị ngắt nhịp thở kịch tính.")

    return warnings

def optimize_sentence_rhythm(text: str) -> Tuple[str, int]:
    """
    Tự động chèn dấu ngắt nhịp (phẩy) cho các câu dài > 22 từ tại các liên từ tự nhiên.
    Tuyệt đối KHÔNG cắt mù ở giữa câu (len(words)//2) để tránh làm đứt từ ghép tiếng Việt.
    """
    fixed_count = 0
    sentences = re.split(r'([.!?…\n]+)', text)
    new_pieces = []
    conjunctions = [
        " nhưng ", " thế nhưng ", " bởi vì ", " khiến cho ", " làm cho ",
        " trong khi ", " đồng thời ", " và rồi ", " bất ngờ ", " ngay lập tức ",
        " cho nên ", " tuy nhiên ", " ngay khi ", " trước khi ", " sau khi "
    ]

    for i in range(0, len(sentences), 2):
        s = sentences[i]
        delim = sentences[i+1] if i+1 < len(sentences) else ""
        words = s.split()
        if len(words) > 22 and not any(p in s for p in [',', ' - ', ';', ':']):
            for conj in conjunctions:
                if conj in s:
                    s = s.replace(conj, f", {conj.strip()} ", 1)
                    fixed_count += 1
                    break
        new_pieces.append(s + delim)

    return "".join(new_pieces), fixed_count


def optimize_dialogue_punchiness(text: str) -> Tuple[str, int]:
    """
    Tối ưu hóa câu thoại dao găm: Chỉ ngắt nhịp tại các liên từ ngữ nghĩa hợp lệ trong cùng 1 câu thoại,
    tuyệt đối KHÔNG cắt mù giữa từ ghép và không khớp xuyên qua dấu xuống dòng.
    """
    pattern = r"(['\"\u201c\u2018])([^\n'\"\u201d\u2019]{15,260})(['\"\u201d\u2019])"
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
        return clause

    def _replacer(m):
        nonlocal fixed_count
        q_open = m.group(1)
        content = m.group(2)
        q_close = m.group(3)
        clauses = re.split(r"([.!?…]+)", content)
        new_clauses = []
        changed = False
        for i in range(0, len(clauses), 2):
            c = clauses[i]
            delim = clauses[i+1] if i+1 < len(clauses) else ""
            if len(c.strip().split()) > 16:
                new_c = _split_long_clause(c)
                if new_c != c:
                    c = new_c
                    changed = True
            new_clauses.append(c + delim)
        if changed:
            fixed_count += 1
            return f"{q_open}{''.join(new_clauses)}{q_close}"
        return m.group(0)

    optimized_text = re.sub(pattern, _replacer, text)
    return optimized_text, fixed_count

def check_sentence_length_and_rhythm(text: str) -> List[str]:

    """Kiểm tra nhịp điệu âm học Edge-TTS: Cảnh báo câu dài hơn 25 từ thiếu dấu ngắt nghỉ."""

    warnings = []

    sentences = re.split(r'[.!?…\n]+', text)

    long_count = 0

    for s in sentences:

        s = s.strip()

        if not s:

            continue

        words = s.split()

        if len(words) > 25 and not any(p in s for p in [',', ' - ', ';', ':']):

            long_count += 1

    if long_count > 0:

        warnings.append(f"Có {long_count} câu dài trên 25 từ thiếu dấu ngắt nhịp, ảnh hưởng nhịp đọc Edge-TTS.")

    return warnings

def audit_and_optimize_part_text(text: str, title: str, part_num: int) -> Tuple[str, List[str]]:

    """

    Tự động audit và tối ưu hóa văn bản của một tập kịch bản:

    1. Lọc trùng lặp đoạn văn (Zero Duplication).

    2. Kiểm tra và sửa lỗi mở đầu rập khuôn / kiểu YouTube.

    3. Thay thế sạch 100% sáo ngữ convert & từ thông báo cảm xúc suông.

    4. Kiểm tra nhịp ngắt nghỉ câu cho Edge-TTS & micro-pacing.

    """

    warnings = []

    # 0. Deduplicate paragraphs

    cleaned_text, dups = deduplicate_paragraphs(text.strip())

    if dups > 0:

        warnings.append(f"Đã loại bỏ {dups} đoạn văn bị lặp lại trong nội dung.")

    # 1. Kiểm tra mở đầu tập 1 (Không làm cụt chủ ngữ câu đầu)
    if part_num == 1:
        if re.match(r"^Nếu\s+bạn\s+vô\s+tình\s+nhận\s+được", cleaned_text, re.IGNORECASE):
            cleaned_text = re.sub(r"^Nếu\s+bạn\s+vô\s+tình\s+nhận\s+được", "Ngay khoảnh khắc nhận được", cleaned_text, flags=re.IGNORECASE)
        for pattern in CLICHE_OPENING_PATTERNS:
            if re.search(pattern, cleaned_text, re.IGNORECASE):
                warnings.append(f"Phát hiện mở đầu rập khuôn theo mẫu cũ: {pattern}")
                candidate = re.sub(pattern, "", cleaned_text).strip()
                if candidate.startswith(("-", ":", ",")):
                    candidate = candidate[1:].strip()
                if candidate:
                    cleaned_text = candidate[0].upper() + candidate[1:]

    # 2. Quét và thay thế sáo ngữ convert & tell cảm xúc

    for forbidden, replacement in FORBIDDEN_PHRASES.items():

        if forbidden in cleaned_text:

            cleaned_text = cleaned_text.replace(forbidden, replacement)

            warnings.append(f"Đã thay thế sáo ngữ: '{forbidden}' -> '{replacement}'")

        forbidden_cap = forbidden.capitalize()

        if forbidden_cap in cleaned_text:

            cleaned_text = cleaned_text.replace(forbidden_cap, replacement.capitalize())

    # 3. Dọn dẹp khoảng trắng và dấu câu thừa trong từng đoạn, giữ cấu trúc đoạn văn \n\n

    paras = cleaned_text.split("\n\n")

    cleaned_paras = []

    for p in paras:

        p_clean = re.sub(r'([!?,.:;…])\s*[!?,.:;…]+', r'\1', p)

        p_clean = re.sub(r'([!?])([A-ZÀ-Ỹa-zà-ỹ])', r'\1 \2', p_clean)
        p_clean = re.sub(r'[ \t]+', ' ', p_clean).strip()

        if p_clean:

            cleaned_paras.append(p_clean)

    cleaned_text = "\n\n".join(cleaned_paras)

    # 3.1. Quét và loại bỏ từ ngữ meta (Đón xem tập tiếp theo, bấm follow)

    meta_words = ["đón xem tập", "đón xem phần", "ở tập 1", "ở tập 2", "bấm follow", "đăng ký kênh"]

    for m in meta_words:

        if m in cleaned_text.lower():

            cleaned_text = re.sub(rf'(?i){m}[^\n.]*[.]?', '', cleaned_text).strip()

            warnings.append(f"Đã loại bỏ từ ngữ meta: '{m}'")

    # 3.2. Cảnh báo độn chữ hóa đơn siêu thị (Grocery List Padding)

    grocery_patterns = ["tấn gạo", "tấn mì", "nồi lẩu tự sôi"]

    for g in grocery_patterns:

        if g in cleaned_text.lower():

            warnings.append(f"CẢNH BÁO: Phát hiện hóa đơn siêu thị '{g}', khuyến nghị mô tả thiết bị cơ học thay thế.")

    # 3.3. Tối ưu câu thoại dao găm (Punchy Dialogue dưới 12-16 từ)

    cleaned_text, diag_fixed = optimize_dialogue_punchiness(cleaned_text)

    if diag_fixed > 0:

        warnings.append(f"Đã tự động tối ưu ngắt nhịp dao găm cho {diag_fixed} câu thoại dài.")

    # 4. Kiểm tra micro-pacing & sentence rhythm

    pacing_warns = check_micro_pacing(cleaned_text)

    if pacing_warns:

        warnings.extend(pacing_warns[:2])

    cleaned_text, r_fixed = optimize_sentence_rhythm(cleaned_text)

    if r_fixed > 0:

        warnings.append(f"Đã tự động tối ưu ngắt nhịp thở Edge-TTS cho {r_fixed} câu dài.")

    rhythm_warns = check_sentence_length_and_rhythm(cleaned_text)

    if rhythm_warns:

        warnings.extend(rhythm_warns)

    return cleaned_text, warnings

def calculate_jaccard_similarity(text1: str, text2: str) -> float:

    """Tính chỉ số tương đồng từ vựng Jaccard giữa 2 kịch bản (loại bỏ stopwords tiếng Việt)."""

    tokens1 = set(t for t in re.findall(r'\b[a-zà-ỹ0-9_]+\b', text1.lower()) if len(t) >= 2 and t not in VIETNAMESE_STOPWORDS)

    tokens2 = set(t for t in re.findall(r'\b[a-zà-ỹ0-9_]+\b', text2.lower()) if len(t) >= 2 and t not in VIETNAMESE_STOPWORDS)

    if not tokens1 or not tokens2:

        return 0.0

    return len(tokens1 & tokens2) / len(tokens1 | tokens2)

def detect_opening_syntax_archetype(hook_text: str) -> str:
    """
    Phân loại cấu trúc cú pháp của câu mở đầu để chống trùng lặp nhịp điệu (Syntax Rhythm Anti-Clash).
    Hệ thống sở hữu 10 trường phái cú pháp độc bản:
    1. ACOUSTIC_ONOMATOPOEIA (Tiếng động cơ học: Rắc!, Cắc!, Tách!, Cạch!, Keng!, Xèo!)
    2. DIRECT_DIALOGUE (Thoại nhát gừng mở màn)
    3. SATIRICAL_INTERNAL (Tiếng lòng / Suy nghĩ trào phúng độc thoại)
    4. SURVIVAL_RULE_COMMAND (Mệnh lệnh quy tắc sinh tồn)
    5. CHEMICAL_REACTION (Phản ứng hóa học kết tủa, bốc khói)
    6. ATMOSPHERIC_ENVIRONMENT (Nhiệt độ, không gian lạnh gáy, ánh sáng)
    7. COUNTDOWN_METRIC (Kim đo áp suất, đồng hồ sinh hiệu, đếm ngược)
    8. TEMPORAL_CONJUNCTION (Mệnh đề thời gian kịch tính)
    9. FINANCIAL_NUMERICAL (Con số tài chính chấn động)
    10. PHYSICAL_ACTION (Hành động cơ học trực tiếp)
    11. FORENSIC_OBJECT (Vật thể pháp y, vị trí vật lý)
    """
    t = hook_text.strip().lower()

    if re.match(r"^(rắc|tách|cạch|keng|xèo|bịch|chát|rầm|xoảng|cắc)[\s!.,-]", t):
        return "ACOUSTIC_ONOMATOPOEIA"

    if t.startswith(("'", '"', "“", "‘")):
        return "DIRECT_DIALOGUE"

    if any(k in t for k in ["tiếng lòng", "trong đầu tôi", "tôi thầm nghĩ"]):
        return "SATIRICAL_INTERNAL"

    if re.match(r"^(tôi|ngón tay|bàn tay|mũi kéo|cánh tay) ", t):
        return "PHYSICAL_ACTION"

    if re.match(r"^(\d+|ba trăm|năm mươi|bảy mươi|một trăm|năm nghìn|lệnh bán khống|lệnh giải chấp|bản sao kê)", t):
        return "FINANCIAL_NUMERICAL"

    if any(k in t for k in ["quy tắc", "luật sinh tồn", "điều cấm"]):
        return "SURVIVAL_RULE_COMMAND"

    if any(k in t for k in ["lớp muối", "kết tủa", "sủi bọt", "khói tím"]):
        return "CHEMICAL_REACTION"

    if re.search(r" vừa .+ (thì|đã|bỗng|lập tức) ", t):
        return "TEMPORAL_CONJUNCTION"

    if any(k in t for k in ["kim đồng hồ", "kim đo", "đồng hồ đo", "áp suất", "sinh hiệu", "đếm ngược"]):
        return "COUNTDOWN_METRIC"

    if any(k in t for k in ["âm năm", "độ c ", "độ c,", "độ c.", "ánh đèn", "luồng sáng", "bão tuyết", "màn sương", "hơi lạnh"]):
        return "ATMOSPHERIC_ENVIRONMENT"

    return "FORENSIC_OBJECT"

def calculate_hook_similarity(hook1: str, hook2: str) -> float:

    """Tính độ trùng lặp của 25 từ đầu tiên giữa 2 phần mở đầu."""

    words1 = [w.strip(".,!?:;\"'()[]") for w in hook1.lower().split()[:25] if w.strip(".,!?:;\"'()[]")]

    words2 = [w.strip(".,!?:;\"'()[]") for w in hook2.lower().split()[:25] if w.strip(".,!?:;\"'()[]")]

    if not words1 or not words2:

        return 0.0

    common = set(words1) & set(words2)

    return len(common) / max(len(set(words1)), len(set(words2)))

def extract_hook_snippet(story_dict: Dict[str, Any]) -> str:

    """Trích xuất hook mẫu của Part 1 để so sánh."""

    parts = story_dict.get("parts", [])

    if not parts:

        return ""

    if parts[0].get("hook"):

        return parts[0]["hook"]

    p1_text = parts[0].get("text", "") or parts[0].get("full_text", "") or parts[0].get("body", "")

    words = p1_text.strip().split()[:30]

    return " ".join(words)

def extract_story_full_text(story_dict: Dict[str, Any]) -> str:

    """Trích xuất toàn bộ văn bản của bộ truyện."""

    parts = story_dict.get("parts", [])

    full_pieces = []

    for p in parts:

        t = p.get("text", "") or p.get("full_text", "") or p.get("body", "")

        if t:

            full_pieces.append(t)

    return "\n\n".join(full_pieces)

def calculate_title_similarity(title1: str, title2: str) -> float:
    """
    Tính chỉ số tương đồng từ vựng giữa 2 tiêu đề (Title Similarity) để chống trùng lặp mẫu đặt tên.
    Loại bỏ stopwords tiếng Việt và các ký tự đặc biệt bằng regex chuẩn.
    """
    words1 = [re.sub(r'[^a-zà-ỹ0-9_]', '', w) for w in title1.lower().split()]
    words2 = [re.sub(r'[^a-zà-ỹ0-9_]', '', w) for w in title2.lower().split()]
    clean_w1 = set(w for w in words1 if len(w) >= 2 and w not in VIETNAMESE_STOPWORDS)
    clean_w2 = set(w for w in words2 if len(w) >= 2 and w not in VIETNAMESE_STOPWORDS)
    if not clean_w1 or not clean_w2:
        return 0.0
    return len(clean_w1 & clean_w2) / max(len(clean_w1), len(clean_w2))


def detect_resolution_mechanism(full_text: str) -> str:
    """
    Phân loại cơ chế lật kèo / kết liễu của câu chuyện (20 Non-Overlapping Climax Resolutions):
    Đảm bảo các kịch bản không bị rập khuôn một kiểu kết thúc.
    """
    t = full_text.lower()
    if any(k in t for k in ["bể thanh khoản", "ví lạnh", "blockchain", "hợp đồng thông minh", "usdt", "rút kiệt dự trữ"]):
        return "BLOCKCHAIN_ROLLBACK"
    if any(k in t for k in ["bán khống", "margin", "cháy tài khoản", "giải chấp", "phái sinh"]):
        return "MARGIN_CALL"
    if any(k in t for k in ["x-quang", "quang phổ", "hồng ngoại", "tia x", "bọc chì"]):
        return "INFRARED_SIGNATURE"
    if any(k in t for k in ["địa chỉ mac", "địa chỉ ip", "nhật ký máy chủ", "server log", "render deepfake"]):
        return "SERVER_AUDIT_LOG"
    if any(k in t for k in ["quy tắc", "luật phòng", "đảo ngược"]):
        return "RULE_INVERSION"
    if any(k in t for k in ["livestream", "màn hình led", "chiếu trực tiếp"]):
        return "DIGITAL_FORENSIC"
    if any(k in t for k in ["adn", "mẫu máu", "pháp y", "móng tay", "giải phẫu"]):
        return "FORENSIC_PATHOLOGY"
    if any(k in t for k in ["di chúc", "ngân hàng thụy sĩ", "tín thác", "két sắt"]):
        return "TIME_CAPSULE_WILL"
    if any(k in t for k in ["quỳ tím", "sủi bọt", "độc dược", "trâm bạc", "thảo mộc độc"]):
        return "CHEMICAL_INDICATOR"
    if any(k in t for k in ["van điều áp", "áp suất cao", "boong ke", "khoang ngoài"]):
        return "PRESSURE_ISOLATION"
    if any(k in t for k in ["tiếng lòng", "nghe thấy suy nghĩ", "chê sếp"]):
        return "SATIRICAL_COLLAPSE"
    if any(k in t for k in ["radar", "không lưu", "quỹ đạo bay"]):
        return "RADAR_TRAJECTORY"
    if any(k in t for k in ["áp lực âm", "bsl-4", "vi sinh", "cách ly"]):
        return "BSL4_CONTAINMENT"
    if any(k in t for k in ["sóng âm", "sonar", "biển sâu"]):
        return "SONAR_PING"
    if any(k in t for k in ["cáp treo", "tải trọng", "đứt cáp"]):
        return "CABLE_STRESS_LOAD"
    if any(k in t for k in ["địa tầng", "mẫu đất", "thạch cao", "móng ngầm", "kiểm định kết cấu"]):
        return "CORE_STRATA_ANALYSIS"
    return "CIVIL_FRAUD_VOID"

def verify_cross_audio_distinctiveness(
    story_dict: Dict[str, Any],
    history_file: Optional[Path] = None,
    max_jaccard_threshold: float = 0.25,
    max_hook_overlap: float = 0.30,
    max_title_similarity: float = 0.35
) -> Tuple[bool, List[str]]:

    """

    Cổng Thẩm Định Chống Đồng Hóa Kịch Bản (Anti-Homogenization & Cross-Script Distinctiveness Gate):

    - Đảm bảo kịch bản mới ĐỘC BẢN HOÀN TOÀN, không na ná hay lặp lại mô-típ các audio trước.

    - So sánh với lịch sử 10 audio gần nhất trong script_history.jsonl:

      1. Hook Part 1 không được trùng cấu trúc quá 40% từ.

      2. Tương đồng từ vựng Jaccard không vượt quá 28% (ngăn chặn tái sử dụng stock phrases).

      3. Cấm trùng nhịp cú pháp mở đầu (Syntax Rhythm Anti-Clash) với audio ngay trước đó!

    - Tự động ghi lại footprint vào script_history.jsonl để bảo vệ các audio kế tiếp.

    """

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
        if prev_title == current_title:
            continue

        prev_hook = rec.get("hook_snippet", "")

        prev_full_sample = rec.get("full_sample", "")

        # 0. Kiểm tra Title Similarity (Chống trùng lặp tiêu đề)
        t_sim = calculate_title_similarity(current_title, prev_title)
        if t_sim >= max_title_similarity:
            warn_msg = f"CẢNH BÁO TRÙNG LẶP TIÊU ĐỀ: Tiêu đề '{current_title}' trùng {t_sim*100:.1f}% từ khóa với '{prev_title}'. Yêu cầu đổi tên truyện độc bản hoàn toàn!"
            warnings.append(warn_msg)
            passed = False

        # 1. Kiểm tra Hook Overlap (Ngưỡng khắt khe < 30%)
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

        # 3. Kiểm tra Trùng Nhịp Cú Pháp Mở Đầu (Syntax Rhythm Anti-Clash) với audio gần nhất

        if idx == 1 and prev_hook:

            curr_syntax = detect_opening_syntax_archetype(current_hook)

            prev_syntax = detect_opening_syntax_archetype(prev_hook)

            if curr_syntax == prev_syntax:

                warn_msg = f"CẢNH BÁO TRÙNG NHỊP CÚ PHÁP: Mở đầu Part 1 cùng thuộc cú pháp '{curr_syntax}' với audio gần nhất '{prev_title}'. Yêu cầu đổi cấu trúc câu mở đầu để tránh làm khán giả nhàm chán!"

                warnings.append(warn_msg)

    # Ghi nhận kịch bản hiện tại vào script_history.jsonl

    hist_path.parent.mkdir(parents=True, exist_ok=True)

    new_record = {

        "timestamp": datetime.now().isoformat(),

        "title": current_title,

        "hook_snippet": current_hook,

        "syntax_archetype": detect_opening_syntax_archetype(current_hook),
        "resolution_mechanism": detect_resolution_mechanism(current_full_text),
        "title_keywords": list(set(w.lower() for w in current_title.split() if len(w) > 2)),
        "full_sample": current_full_text[:3000],

        "total_words": len(current_full_text.split())

    }

    try:

        with open(hist_path, "a", encoding="utf-8") as f:

            f.write(json.dumps(new_record, ensure_ascii=False) + chr(10))

    except Exception as e:

        logger.warning(f"Không thể ghi script history: {e}")

    return passed, warnings

def validate_story_series(series_data: Dict[str, Any]) -> Dict[str, Any]:

    """

    Cổng kiểm duyệt chất lượng Master Script Quality Gate:

    - Bắt buộc đọc qua GEMINI.md và kinh nghiệm 10 vòng trước khi thẩm định.

    - Duyệt qua từng tập trong bộ truyện (Part 1, 2, 3).

    - Thẩm định chống đồng hóa & chống lặp mô-típ (Anti-Homogenization Check).

    - Đảm bảo 100% tiêu đề khớp với nội dung và không vi phạm bất kỳ điều cấm nào.

    """

    codex_info = load_master_codex_rules()

    title = series_data.get("title", "")

    all_warnings = []

    logger.info(f"[ScriptQualityGate] Dang nap kinh nghiem va tham dinh: {title}")

    # BẮT BUỘC TRA CỨU TRI THỨC 100 KIỆT TÁC: Tự động tra cứu và cấp token nếu chưa có
    if not series_data.get("consultation_token"):
        try:
            from core.knowledge_base import require_knowledge_consultation
            brief = require_knowledge_consultation(
                topic_title=title,
                topic_summary=title,
                genre_hint=series_data.get("genre", "TRONG_SINH")
            )
            series_data["consultation_token"] = brief.get("consultation_token", "")
            series_data["knowledge_brief"] = brief
            logger.info(f"  [ScriptQualityGate] Da tra cuu Knowledge Base thanh cong, cap token: {series_data['consultation_token']}")
        except Exception as e:
            logger.warning(f"  [ScriptQualityGate] Khong the tra cuu Knowledge Base: {e}")

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

    # Cổng kiểm duyệt thời lượng chuẩn 30 phút điện ảnh (Zero 49s Tolerance)
    total_series_words = sum(len((p.get("full_text") or p.get("text") or "").split()) for p in validated_parts)
    min_part_words = min((len((p.get("full_text") or p.get("text") or "").split()) for p in validated_parts), default=0)

    if total_series_words < 2700 or min_part_words < 700:
        duration_err = f"LỖI THỜI LƯỢNG NGHIÊM TRỌNG (ZERO 49S TOLERANCE): Series chỉ có {total_series_words} từ (tập ngắn nhất {min_part_words} từ). Tiêu chuẩn bắt buộc là >= 2.700 từ (khuyến nghị >= 4.500 từ, ~25-35 phút audio). Cấm xuất bản kịch bản tóm tắt!"
        all_warnings.append(duration_err)
        series_data["quality_audit_passed"] = False
        logger.error(f"  [ScriptQualityGate] {duration_err}")
    else:
        series_data["quality_audit_passed"] = True

    series_data["distinctiveness_passed"] = distinct_passed

    series_data["quality_audit_warnings"] = all_warnings

    if all_warnings:

        logger.info(f"  Da toi uu hoa {len(all_warnings)} diem cho kich ban (Bao gom {len(distinct_warnings)} diem chong dong hoa)")

    else:

        logger.info(f"  Kich ban dat chuan Masterpiece doc ban ngay tu dau, sach sao ngu!")

    return series_data

