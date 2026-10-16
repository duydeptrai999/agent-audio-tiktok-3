# -*- coding: utf-8 -*-
"""
core/knowledge_base.py
Cơ Sở Dữ Liệu Tri Thức Biên Kịch Chuyên Sâu (Chinese Short Story Knowledge Base Engine)
Tổng hợp, lập chỉ mục và cung cấp API truy vấn thông minh từ 100 tác phẩm đoản văn kinh điển
thuộc 10 nhóm thể loại hàng đầu (Zhihu 盐选, Douyin 短剧, Fanqie, Jinjiang, Qidian).

Mục tiêu cốt lõi:
Mỗi khi hệ thống tạo ra một kịch bản mới, Agent Biên Kịch bắt buộc phải tra cứu Cơ sở dữ liệu này
để chọn lọc case study tương đồng nhất, áp dụng 10 Định Luật Vàng, Mô hình 4 Tầng Bất đối xứng Thông tin,
6 Mẫu Hook Mở màn, Ma trận Điểm Sảng, Hệ thống 4 Tầng Phản diện và Cắt điểm rơi Cliffhanger nghẹt thở.
"""

import os
import re
import json
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path

from core.state import VideoCategory
from data.stories_study.genre1_nguoc_tam import STORIES_GENRE_1
from data.stories_study.genre2_trong_sinh import STORIES_GENRE_2
from data.stories_study.genre3_huyen_nghi import STORIES_GENRE_3
from data.stories_study.genre4_me_chong import STORIES_GENRE_4
from data.stories_study.genre5_hao_mon import STORIES_GENRE_5
from data.stories_study.genre6_kinh_di import STORIES_GENRE_6
from data.stories_study.genre7_sa_dieu import STORIES_GENRE_7
from data.stories_study.genre8_cung_dau import STORIES_GENRE_8
from data.stories_study.genre9_cuu_roi import STORIES_GENRE_9
from data.stories_study.genre10_vo_han import STORIES_GENRE_10

logger = logging.getLogger("KnowledgeBase")
root_dir = Path(__file__).resolve().parent.parent

# ==============================================================================
# 1. HỆ THỐNG 10 ĐỊNH LUẬT VÀNG BIÊN KỊCH ĐOẢN VĂN VIRAL
# ==============================================================================
GOLDEN_RULES_10 = [
    {
        "rule_id": 1,
        "name": "In Medias Res (Golden Retention Hook 5 Giây)",
        "principle": "Cấm tuyệt đối đọc lý lịch tuổi tác hoặc tả thời tiết (Zero-Biography). 15 từ đầu tiên phải ném ngay câu thoại áp chế, hiện trường rùng mình hoặc nghịch lý biến cố.",
        "formula": "Hook = [Xung đột cực độ] + [Người thân phản trắc / Biến cố sinh tử] + [Nghịch lý nhận thức]"
    },
    {
        "rule_id": 2,
        "name": "Nén Áp Suất & Giải Phóng Cảm Xúc (Suppression & Catharsis)",
        "principle": "Khoái cảm sảng văn tỷ lệ thuận với độ nén ức chế. Cứ 300 từ có một vi-xung đột làm đối phương lấn tới, nhân vật chính nén lại rồi bùng nổ khi phản diện đắc ý nhất.",
        "formula": "Tập 1 nén áp lực -> Tập 2 bế tắc đường cùng -> Tập 3 vỡ òa trừng phạt triệt để"
    },
    {
        "rule_id": 3,
        "name": "Khẩu Súng Của Chekhov (Cỏ Rắn Vệt Tro - 草蛇灰线)",
        "principle": "Mọi vật phẩm, thói quen, chi tiết xuất hiện ở Hồi 1 (chiếc bánh bao, chiếc USB, thói quen dị ứng, đồng hồ chết) đều phải trở thành chìa khóa đoạt mạng ở Hồi 3.",
        "formula": "Chi tiết vô hại Hồi 1 -> Vật chứng quyết định Hồi 3"
    },
    {
        "rule_id": 4,
        "name": "Tương Phản Nhân Vật Cực Đoan (Extreme Archetype Contrast)",
        "principle": "Đặt hai hình tượng đối lập cạnh nhau: Tổng tài lạnh lùng vs Vợ thực dụng coi hôn nhân là công việc; Mẹ chồng gia quy vs Dâu kiểm toán viên sắc sảo; Mèo quýt béo ú vs Trùm xã hội đen.",
        "formula": "Sự va chạm giữa hai thế giới quan trái ngược tạo ra xung đột và tiếng cười tự nhiên"
    },
    {
        "rule_id": 5,
        "name": "Phản Sáo Lộ & Nghịch Chuyển Kỳ Vọng (Subverting Tropes)",
        "principle": "Khi khán giả nghĩ câu chuyện đi theo lối mòn A (khóc lóc tha thứ), kịch bản lập tức rẽ sang hướng B (rút dao rạch mặt, bỏ đi làm giàu, tuyệt đối không quay đầu).",
        "formula": "Dẫn dắt theo lối mòn cũ -> Bẻ ngoặt 180 độ ở giây phút quyết định"
    },
    {
        "rule_id": 6,
        "name": "Tiết Tấu Câu Ngắn Cho Tốc Độ Đọc 1.5x (Punchy Cadence)",
        "principle": "Tốc độ đọc 1.5x (346 từ/phút) đòi hỏi câu văn 10-20 từ. Dùng nhiều dấu phẩy ',', ba chấm '...', gạch ngang ' - ' để giọng đọc AI nhấn nhá truyền cảm.",
        "formula": "Câu ngắn gãy gọn + Điểm rơi dấu câu nhịp thở"
    },
    {
        "rule_id": 7,
        "name": "Show, Don't Tell (Hành Động Hóa Trạng Thái)",
        "principle": "Tuyệt đối không tóm tắt sự kiện khô khan. Miêu tả chi tiết bàn tay siết chặt, nhịp thở dồn dập, chiếc nhẫn cưới trượt rơi vào ly rượu vang.",
        "formula": "Hành động cụ thể + Chi tiết giác quan = Cảm xúc sống động"
    },
    {
        "rule_id": 8,
        "name": "Đảo Chiều Đa Tầng (Multi-Layered Plot Twist)",
        "principle": "Twist tầng 1 (Vả mặt bề mặt) -> Twist tầng 2 (Bóc trần âm mưu ngầm) -> Twist tầng 3 (Động cơ sâu xa / Dư âm lương tâm suốt đời).",
        "formula": "3 tầng lật kèo liên hoàn tạo dư chấn tâm lý mạnh mẽ"
    },
    {
        "rule_id": 9,
        "name": "Trả Thù Bằng Sự Nghiệp & Sự Tự Do (Sober Autonomy)",
        "principle": "Phụ nữ hiện đại không tranh giành đàn ông. Họ hả dạ nhất khi nhân vật chính độc lập tài chính, sự nghiệp thăng hoa và coi kẻ phản bội như rác rưởi.",
        "formula": "Tự do tài chính + Lạnh lùng buông bỏ = Sảng khoái tối thượng"
    },
    {
        "rule_id": 10,
        "name": "Cliffhanger Điểm Rơi Nghẹt Thở Cuối Tập 1 & 2 (卡点)",
        "principle": "Không bao giờ dừng tập khi câu chuyện đã giải quyết xong; dừng lại đúng 0.5 giây trước khi bí mật động trời được phơi bày hoặc ngay khi đối phương ra đòn hiểm.",
        "formula": "Cắt đúng đỉnh cao trào chưa giải quyết để kéo người nghe sang tập tiếp theo"
    }
]

# ==============================================================================
# 2. MÔ HÌNH 4 TẦNG BẤT ĐỐI XỨNG THÔNG TIN (INFORMATION ASYMMETRY ECONOMICS)
# ==============================================================================
INFORMATION_ASYMMETRY_MODEL = {
    "layers": {
        "fact_layer": "Sự thật khách quan: Biến cố thực tế diễn ra trong cốt truyện.",
        "narrator_layer": "Lời người kể chuyện: Có thể là Unreliable Narrator đánh lừa độc giả.",
        "character_layer": "Góc nhìn nhân vật: Tầm nhìn hạn chế của từng nhân vật trong bối cảnh.",
        "audience_layer": "Góc nhìn khán giả: Nhận thức được định hình qua dữ kiện nhận được."
    },
    "dynamics": {
        "audience_gt_character": "Khán giả biết > Nhân vật biết -> Tạo cảm giác Lo âu & Nghẹt thở ('Đừng mở cánh cửa đó!').",
        "character_gt_audience": "Nhân vật biết > Khán giả biết -> Tạo cảm giác Tò mò & Động cơ bí ẩn ('Tại sao lại quỳ trước người giao hàng?').",
        "narrator_gt_audience": "Người kể chuyện lừa Khán giả -> Tạo cảm giác Kinh ngạc cực độ (Mind-blowing Twist)."
    }
}

# ==============================================================================
# 3. HỆ THỐNG 6 MẪU MỞ MÀN HOOK VÀNG 3-5 GIÂY (GOLDEN HOOKS)
# ==============================================================================
OPENING_HOOK_TEMPLATES_6 = [
    {
        "type": "Xung đột tiền trí (Conflict Frontloaded)",
        "desc": "Mở đầu ngay bằng một cái tát, một vụ kiện tụng hoặc câu quát tháo dằn mặt.",
        "example": "'Mẹ chồng hắt thẳng bát canh gà nóng bỏng vào mặt tôi: Đồ gà mái không biết đẻ trứng, mau ký vào đơn ly hôn rồi cút ra khỏi nhà!'",
        "best_for": ["ME_CHONG", "TRONG_SINH", "NGUOC_TAM"]
    },
    {
        "type": "Nghiền ép thân phận (Identity Inversion / Crushing)",
        "desc": "Hiển thị sự coi thường của đối phương, ngay lập tức báo hiệu thân phận bí mật vượt trội.",
        "example": "'Quản lý hất chiếc thẻ nhân viên rách nát vào ngực tôi: Nơi này tối thiểu chi tiêu 100 triệu, người nghèo như cậu không có tư cách bước vào!' - Mười giây sau, chiếc Maybach của chủ tịch tập đoàn phanh rít trước sảnh...",
        "best_for": ["HAO_MON", "TRONG_SINH", "SA_DIEU"]
    },
    {
        "type": "Nghịch cảnh cực hạn (Extreme Dilemma / Crisis)",
        "desc": "Đẩy nhân vật vào tình huống sinh tử nghẹt thở hoặc phá sản, ung thư giai đoạn cuối.",
        "example": "'Cầm kết quả ung thư giai đoạn cuối trên tay, tôi bước vào nhà thì thấy chồng đang vui vẻ ký hợp đồng mua căn biệt thự 50 tỷ tặng sinh nhật thư ký riêng.'",
        "best_for": ["NGUOC_TAM", "ME_CHONG", "CUU_ROI"]
    },
    {
        "type": "Đảo tự nghịch lý (Retrograde Suspense / Paradox)",
        "desc": "Đưa ra một câu đố bất khả thi hoặc lời cảnh báo rùng mình trong 5s đầu.",
        "example": "'Đúng hai giờ sáng giữa đêm mưa bão, chiếc điện thoại bàn đã cắt dây từ 5 năm trước bỗng reo vang từng hồi đinh tai nhức óc!'",
        "best_for": ["HUYEN_NGHI", "KINH_DI", "VO_HAN"]
    },
    {
        "type": "Ngọt sủng độc tôn (Sweet & Doting Hook)",
        "desc": "Khoảnh khắc che chở thiên vị độc nhất vô nhị trước ánh mắt ngỡ ngàng của đám đông.",
        "example": "'Trước mặt toàn thể giới thượng lưu, vị tổng tài nổi tiếng lạnh lùng tàn nhẫn bỗng quỳ một gối, cẩn thận buộc lại dây giày cho cô gái gả thay.'",
        "best_for": ["HAO_MON", "CUU_ROI"]
    },
    {
        "type": "Trọng sinh thức tỉnh tức thì (Instant Rebirth / Awakening)",
        "desc": "Mở mắt ra ngay tại khoảnh khắc định mệnh của kiếp trước, lập tức hành động thay đổi số phận.",
        "example": "'Mở mắt ra trong đêm tân hôn ngập sắc đỏ, việc đầu tiên tôi làm không phải chờ phu quân vén khăn voan, mà là với lấy bình trà gốm đập vỡ góc phòng để ép mình tỉnh táo!'",
        "best_for": ["TRONG_SINH", "CUNG_DAU", "VO_HAN"]
    }
]

# ==============================================================================
# 4. MA TRẬN 5 LOẠI ĐIỂM SẢNG (SATISFACTION MATRIX)
# ==============================================================================
SATISFACTION_MATRIX_5 = {
    "identity_crushing": {
        "name": "Nghiền ép thân phận",
        "formula": "Bị sỉ nhục -> Nhẫn nhịn -> Lộ thân phận thật -> Toàn trường quỳ gối xin tha",
        "weight": 0.35
    },
    "face_slapping_revenge": {
        "name": "Vả mặt báo thù",
        "formula": "Phản diện đắc chí -> Bẫy sập -> Chứng cứ công khai đanh thép -> Phản diện thân bại danh liệt",
        "weight": 0.40
    },
    "counterattack_turnaround": {
        "name": "Nghịch tập lật kèo",
        "formula": "Rơi vào tuyệt cảnh -> Kích hoạt bài tẩy / Trí tuệ chiến thuật -> Lật ngược thế cờ",
        "weight": 0.15
    },
    "emotional_explosion": {
        "name": "Cảm xúc bùng nổ / Thiên vị độc sủng",
        "formula": "Bị cô lập -> Người quyền lực nhất đứng ra che chở vô điều kiện -> Hóa giải hiểu lầm",
        "weight": 0.10
    },
    "mystery_unveiling": {
        "name": "Giải mã chân tướng kinh hoàng",
        "formula": "Manh mối Chekhov -> Suy luận sắc bén -> Bóc trần kẻ thủ ác ngụy trang thánh thiện",
        "weight": 0.20
    }
}

# ==============================================================================
# 5. HỆ THỐNG 4 TẦNG PHẢN DIỆN (4-TIER VILLAIN SYSTEM)
# ==============================================================================
VILLAIN_SYSTEM_4 = [
    {"tier": 1, "role": "Pháo hôi (Cannon Fodder)", "timing": "Tập 1 (0-15%)", "purpose": "Sỉ nhục nhân vật chính để làm ngòi nổ, bị vả mặt nhanh chóng để tạo đà hưng phấn."},
    {"tier": 2, "role": "Trung phản diện (Mid-level)", "timing": "Tập 2 (15-60%)", "purpose": "Kẻ ngáng đường có thực lực, giở thủ đoạn dơ bẩn dồn nhân vật chính vào thế khó."},
    {"tier": 3, "role": "Đại phản diện (Ultimate Boss)", "timing": "Tập 3 (60-90%)", "purpose": "Trùm cuối có quyền thế khổng lồ, cuộc đấu trí sinh tử trực diện."},
    {"tier": 4, "role": "Ẩn tàng phản diện (Hidden Betrayer)", "timing": "Tập 3 (Cao trào)", "purpose": "Người thân tín nhất phản trắc, phải có ít nhất 3 phục bút từ Tập 1 để tạo cảm giác rùng mình (细思极恐)."}
]


class ChineseStoryKnowledgeBase:
    """
    Cơ sở dữ liệu tri thức biên kịch chứa 100 tác phẩm đoản văn kinh điển
    và hệ thống tra cứu thông minh hỗ trợ Agent 2 (Biên kịch).
    """

    def __init__(self):
        self._all_stories: List[Dict[str, Any]] = []
        self._genre_map: Dict[str, List[Dict[str, Any]]] = {}
        self._load_and_index()

    def _load_and_index(self) -> None:
        """Nạp toàn bộ 100 tác phẩm từ 10 modules và lập chỉ mục"""
        genre_collections = [
            ("NGUOC_TAM", STORIES_GENRE_1),
            ("TRONG_SINH", STORIES_GENRE_2),
            ("HUYEN_NGHI", STORIES_GENRE_3),
            ("ME_CHONG", STORIES_GENRE_4),
            ("HAO_MON", STORIES_GENRE_5),
            ("KINH_DI", STORIES_GENRE_6),
            ("SA_DIEU", STORIES_GENRE_7),
            ("CUNG_DAU", STORIES_GENRE_8),
            ("CUU_ROI", STORIES_GENRE_9),
            ("VO_HAN", STORIES_GENRE_10),
        ]

        self._all_stories = []
        for genre_key, stories_list in genre_collections:
            self._genre_map[genre_key] = stories_list
            for s in stories_list:
                s_copy = dict(s)
                s_copy["genre_key"] = genre_key
                self._all_stories.append(s_copy)

        logger.info(f"Đã lập chỉ mục thành công {len(self._all_stories)} tác phẩm trong Knowledge Base.")

    @property
    def total_stories(self) -> int:
        return len(self._all_stories)

    def get_all_stories(self) -> List[Dict[str, Any]]:
        return self._all_stories

    def get_golden_rules(self) -> List[Dict[str, Any]]:
        return GOLDEN_RULES_10

    def query_masterclass(
        self,
        topic_title: str = "",
        topic_summary: str = "",
        category: Optional[VideoCategory] = None,
        top_k: int = 3
    ) -> Dict[str, Any]:
        """
        Tra cứu cơ sở dữ liệu để tìm ra các case study và bài học tương đồng nhất.
        Được gọi bắt buộc trước mỗi lần biên kịch sinh kịch bản mới.
        """
        text_corpus = f"{topic_title} {topic_summary}".lower()
        
        # 1. Định hướng nhóm thể loại ưu tiên
        target_genre_keys = []
        if any(w in text_corpus for w in ["ngược", "hỏa táng", "bạch nguyệt quang", "thế thân", "bỏ lỡ", "tàn tâm"]):
            target_genre_keys.append("NGUOC_TAM")
        if any(w in text_corpus for w in ["trọng sinh", "vả mặt", "thiên kim", "sống lại", "thức tỉnh", "sảng văn"]):
            target_genre_keys.append("TRONG_SINH")
        if any(w in text_corpus for w in ["án mạng", "camera", "phòng kín", "thám tử", "sát nhân", "công an", "pháp y", "manh mối", "50 mét"]):
            target_genre_keys.append("HUYEN_NGHI")
        if any(w in text_corpus for w in ["mẹ chồng", "nàng dâu", "sính lễ", "nhà chồng", "ly hôn", "ngoại tình", "tiểu tam", "em trai chồng", "ma đệ ma", "cực phẩm"]):
            target_genre_keys.append("ME_CHONG")
        if any(w in text_corpus for w in ["hợp đồng", "tổng tài", "100 tỷ", "hào môn", "gả thay", "thái tử", "giả nghèo", "cưới trước yêu sau"]):
            target_genre_keys.append("HAO_MON")
        if any(w in text_corpus for w in ["quy tắc", "quái đàm", "kinh dị", "bệnh viện đêm", "ký túc xá", "ma-nơ-canh", "sinh tồn"]):
            target_genre_keys.append("KINH_DI")
        if any(w in text_corpus for w in ["tiếng lòng", "đọc suy nghĩ", "mèo", "tấu hài", "sa điêu", "hài hước", "nhầm tin nhắn", "phản sáo lộ"]):
            target_genre_keys.append("SA_DIEU")
        if any(w in text_corpus for w in ["cung đấu", "hoàng hậu", "thám hoa", "thứ nữ", "khoa cử", "vương phi", "trạch đấu"]):
            target_genre_keys.append("CUNG_DAU")
        if any(w in text_corpus for w in ["chữa lành", "thanh xuân", "học bá", "khiếm thính", "bức thư", "hộp thời gian", "bác trương", "cứu rỗi"]):
            target_genre_keys.append("CUU_ROI")
        if any(w in text_corpus for w in ["mạt thế", "bão tuyết", "kỷ băng hà", "tích trữ", "vô hạn lưu", "zombie", "thần chết", "axit"]):
            target_genre_keys.append("VO_HAN")

        # Fallback theo Category nếu không tìm thấy từ khóa
        if not target_genre_keys:
            if category == VideoCategory.HIGH_IQ:
                target_genre_keys = ["HUYEN_NGHI", "VO_HAN", "KINH_DI"]
            else:
                target_genre_keys = ["HAO_MON", "ME_CHONG", "NGUOC_TAM", "CUU_ROI"]

        # 2. Chấm điểm tương đồng cho các tác phẩm trong các nhóm ưu tiên
        scored_stories = []
        for s in self._all_stories:
            score = 0
            if s["genre_key"] in target_genre_keys:
                score += 10
            
            # Khớp từ khóa cụ thể trong tên và premise
            search_blob = f"{s['title_vn']} {s['premise']} {s['genre']}".lower()
            tokens = [t for t in re.split(r"\W+", text_corpus) if len(t) >= 2]
            for token in tokens:
                if token in search_blob:
                    score += 2

            scored_stories.append((score, s))

        # Sắp xếp giảm dần theo điểm
        scored_stories.sort(key=lambda x: x[0], reverse=True)
        top_cases = [item[1] for item in scored_stories[:top_k]]

        # 3. Tạo bản tóm tắt chỉ dẫn biên kịch (Scriptwriting Guidance Brief)
        brief_cases = []
        for c in top_cases:
            brief_cases.append({
                "id": c["id"],
                "title": f"《{c['title_vn']}》({c['title_cn']})",
                "author": c["author_platform"],
                "genre": c["genre"],
                "premise": c["premise"],
                "character_setup": c["characters"],
                "sample_hook_5s": c["golden_hook"],
                "plot_twist_essence": c["plot_twist"],
                "key_takeaways": c["core_lessons"]
            })

        # Chọn template hook tương thích nhất
        matched_hook_template = OPENING_HOOK_TEMPLATES_6[0]
        for ht in OPENING_HOOK_TEMPLATES_6:
            if any(gk in ht["best_for"] for gk in target_genre_keys):
                matched_hook_template = ht
                break

        return {
            "status": "CONSULTED_SUCCESS",
            "total_knowledge_pool": self.total_stories,
            "target_genres": target_genre_keys,
            "relevant_cases": brief_cases,
            "golden_rules": GOLDEN_RULES_10,
            "recommended_hook_template": matched_hook_template,
            "satisfaction_matrix": SATISFACTION_MATRIX_5,
            "villain_system": VILLAIN_SYSTEM_4,
            "information_asymmetry": INFORMATION_ASYMMETRY_MODEL,
            "voice_pacing_standard": {
                "reading_speed_multiplier": 1.5,
                "words_per_minute": 346,
                "min_words_per_part": 3460,
                "target_total_words_30min": 10380,
                "sentence_length": "10-20 words per sentence",
                "punctuation_density": "High (commas, ellipses, dashes for breathing pauses)"
            }
        }

    def consult_before_writing(
        self,
        category: Optional[VideoCategory] = None,
        topic_title: str = "",
        topic_summary: str = "",
        top_k: int = 3
    ) -> Dict[str, Any]:
        """
        Hàm bắt buộc gọi trước khi biên soạn bất kỳ kịch bản nào.
        Thực hiện tra cứu, lập kế hoạch chỉ dẫn và lưu vết audit log vào data/knowledge_consultations.jsonl.
        """
        brief = self.query_masterclass(
            topic_title=topic_title,
            topic_summary=topic_summary,
            category=category,
            top_k=top_k
        )

        # Ghi log lịch sử tra cứu (Audit Trail)
        consult_log_path = root_dir / "data" / "knowledge_consultations.jsonl"
        consult_log_path.parent.mkdir(parents=True, exist_ok=True)

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "query_title": topic_title,
            "target_genres": brief.get("target_genres", []),
            "matched_cases": [c["title"] for c in brief.get("relevant_cases", [])],
            "status": "VERIFIED_BEFORE_WRITING"
        }

        try:
            with open(consult_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        except Exception as e:
            logger.warning(f"Không thể ghi log consultation: {e}")

        return brief

    def format_brief_for_prompt(self, brief: Dict[str, Any]) -> str:
        """
        Định dạng bản tóm tắt tri thức thành chuỗi văn bản nạp trực tiếp vào Prompt của LLM
        để bảo đảm LLM phải soi chiếu vào kinh nghiệm này trước khi viết.
        """
        lines = []
        lines.append("=" * 65)
        lines.append("📚 [BỘ CƠ SỞ TRI THỨC 100 KỊCH BẢN KINH ĐIỂN ĐÃ ĐƯỢC TRA CỨU]:")
        lines.append("Hệ thống đã tự động đối soát kho tàng 100 tác phẩm đoản văn triệu view và chọn lọc các Case Study tinh hoa nhất để làm hình mẫu:")
        
        for idx, c in enumerate(brief.get("relevant_cases", []), 1):
            lines.append(f"\n--- CASE STUDY THAM CHIẾU #{idx}: {c['title']} ---")
            lines.append(f" * Nguồn & Tác giả: {c['author']} | Thể loại: {c['genre']}")
            lines.append(f" * Tiền đề nghịch lý: {c['premise']}")
            lines.append(f" * Tạo hình nhân vật mẫu:\n{c['character_setup']}")
            lines.append(f" * Hook mở màn 5s mẫu: {c['sample_hook_5s']}")
            lines.append(f" * Màn bẻ lái Plot Twist mẫu: {c['plot_twist_essence']}")
            lines.append(f" * Tinh hoa cần áp dụng:\n{c['key_takeaways']}")

        lines.append("\n🎯 10 ĐỊNH LUẬT VÀNG BẮT BUỘC ÁP DỤNG:")
        for r in brief.get("golden_rules", [])[:5]:
            lines.append(f" - [Định luật {r['rule_id']} - {r['name']}]: {r['principle']}")

        lines.append("\n⚡ NGHỆ THUẬT NGẮT NHỊP CHO GIỌNG ĐỌC AI TỐC ĐỘ 1.5X:")
        lines.append(" - Câu văn gãy gọn 10-20 từ. Sử dụng nhiều dấu phẩy ',', dấu ba chấm '...', gạch ngang ' - ' để tạo khoảng lặng kịch tính.")
        lines.append(" - Tổng 3 tập bắt buộc >= 10,380 từ (mỗi tập >= 3,460 từ) cho thời lượng tròn 30 phút audio.")
        lines.append("=" * 65)

        return "\n".join(lines)


# Singleton instance để tái sử dụng toàn hệ thống
_GLOBAL_KNOWLEDGE_BASE: Optional[ChineseStoryKnowledgeBase] = None

def get_knowledge_base() -> ChineseStoryKnowledgeBase:
    global _GLOBAL_KNOWLEDGE_BASE
    if _GLOBAL_KNOWLEDGE_BASE is None:
        _GLOBAL_KNOWLEDGE_BASE = ChineseStoryKnowledgeBase()
    return _GLOBAL_KNOWLEDGE_BASE

def require_knowledge_consultation(
    category: Optional[VideoCategory] = None,
    topic_title: str = "",
    topic_summary: str = "",
    top_k: int = 3
) -> Dict[str, Any]:
    """Hàm tiện ích toàn cục bắt buộc gọi trước khi tạo bất kỳ kịch bản nào"""
    kb = get_knowledge_base()
    return kb.consult_before_writing(category=category, topic_title=topic_title, topic_summary=topic_summary, top_k=top_k)
