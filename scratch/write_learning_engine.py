# -*- coding: utf-8 -*-
from pathlib import Path

content = """import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional
from config.settings import DATABASE_DIR
from core.state import VideoCategory
from core.llm_client import call_llm, clean_json_response
from core.harvester import TrendHarvester

logger = logging.getLogger("LearningEngine")
LEARNED_PATTERNS_FILE = DATABASE_DIR / "learned_patterns.json"

DEFAULT_LEARNED_KNOWLEDGE: Dict[str, Any] = {
    "version": "3.0",
    "last_updated": "2026-10-23T06:00:00Z",
    "total_insights_learned": 75,
    "evolution_cycles": 10,
    "tiktok_audio_mastery": {
        "visual_pillar": {
            "insight": "Khán giả nghe kịch truyền thanh trên TikTok tập trung thính giác, thị giác cần video ASMR không lời (làm bánh hoa văn mỹ nghệ, trang điểm ASMR Trung Quốc, làm gốm sứ/gỗ di sản) để mắt không bị xao nhãng và giữ chân > 75%.",
            "recommended_brolls": ["chinese_beauty_asmr", "chinese_cooking_asmr", "chinese_pastry_baking", "chinese_craft_heritage"]
        },
        "audio_pillar": {
            "insight": "Giọng đọc Edge-TTS (Hoài My / Nam Minh) là linh hồn của audio. Nhạc nền 100% không lời (Instrumental Only), áp dụng Cinema Ducking (threshold=0.079, ratio=4.0, release=750ms). Câu văn 8-16 từ ngắt nhịp dấu câu để AI lấy hơi tự nhiên, chốt câu bằng thanh trắc đanh thép.",
            "standards": {
                "voice_clarity": "100% Crisp Neural Speech nhịp 1.15x tự nhiên không mỏi tai",
                "bgm_type": "100% Instrumental Only (No Vocals)",
                "ducking_level": "-22dB to -26dB (Voice dominant)",
                "no_copyright": "100% Safe for TikTok Monetization"
            }
        },
        "narrative_pillar": {
            "insight": "Cấu trúc 3 Hồi chuẩn 30 Phút (3 Tập x 10 Phút): Tuyệt đối không dùng văn tả thời tiết, không tóm tắt tiểu sử (Zero-Biography), không độc thoại 'mình trọng sinh rồi sao', không lặp đoạn văn và không độn hóa đơn siêu thị. Mở đầu bằng Cơ Chế Kép Dual-Engine (Thoáng qua hoặc Hiện trường chi tiết).",
            "series_split_rule": "3 phần độc lập nối tiếp tự nhiên (không nói 'Ở tập 1', 'Đón xem tập 2'), chốt Comment Magnet phân cực 2 lựa chọn."
        }
    },
    "viral_hooks_library": {
        "STRATEGY_A_FLASH_FORWARD": [
            {
                "formula": "Lát cắt vật chứng rợn gáy thoáng qua (Forensic / Threatening Glimpse)",
                "template": "[Vật chứng / Âm thanh cơ học bất thường] + [Phát hiện sinh tử trong 15 từ] + [Cắt sang thời khắc định đoạt]",
                "example": "Mũi kim đồng hồ trên tay nạn nhân đứng khựng ở hai giờ mười bốn phút sáng, ngay dưới đáy móng tay gãy vụn của cô ấy là sợi len màu xanh cổ vịt - chiếc áo duy nhất tôi mặc trong ngày cưới.",
                "retention_impact": "Cực cao (+75% 3s retention)",
                "source": "10_cycles_master_codex"
            },
            {
                "formula": "Mép khế ước tài chính bạo lực lạnh (Cashflow Guillotine Hook)",
                "template": "[Đạo cụ xa xỉ] + [Mép văn bản bất ngờ lộ diện] + [Hành động kích hoạt phong tỏa dòng tiền]",
                "example": "Chiếc thìa mạ vàng vừa chạm vào đáy bát yến sáu mươi triệu, mép giấy bảo hiểm nhân thọ người thụ hưởng tên mẹ chồng đã lộ ra trước mắt tôi.",
                "retention_impact": "Đỉnh cao (+78% 3s retention)",
                "source": "10_cycles_master_codex"
            },
            {
                "formula": "Mũi kéo niêm phong & Tiếng còi xe thanh tra",
                "template": "[Động tác cắt đứt sợi chỉ niêm phong] + [Tiếng còi xe thanh tra kinh tế rú lên dồn dập]",
                "example": "Mũi kéo inox của tôi vừa bấm đứt sợi chỉ niêm phong trên tập hồ sơ ba mươi tỷ, tiếng còi xe thanh tra thuế đã rú lên dưới sảnh.",
                "retention_impact": "Rất cao (+72% 3s retention)",
                "source": "10_cycles_master_codex"
            }
        ],
        "STRATEGY_B_IN_MEDIA_RES": [
            {
                "formula": "Hiện trường đối đầu cửa bọc thép mạt thế (Bunker Defense Kick-off)",
                "template": "[Cửa thép đóng sập chốt cơ học] + [Tiếng đập cửa rầm rầm đòi mì gói] + [Lỗ hồng ngoại soi thấu búp bê cao su & xà beng]",
                "example": "Cánh cửa thép chống đạn ba lớp vừa đóng sập chốt cơ học, tiếng đập cửa rầm rầm đã vang lên kèm tiếng khóc the thé của ả em họ ngoài hành lang: 'Chị Lam ơi! Thằng bé sốt bốn mươi độ rồi, cho em xin mẩu nến và gói mì tôm thôi!'. Tôi không mở cửa. Tôi tựa lưng vào vách thép dày mười lăm phân, ngón tay đặt sẵn trên van xả khí cay áp suất cao.",
                "retention_impact": "Đỉnh cao (+82% 5s retention)",
                "source": "10_cycles_master_codex"
            },
            {
                "formula": "Tiếng lòng thực tập sinh bóc mẽ hợp đồng 500 tỷ (Satirical Subtext Kick-off)",
                "template": "[Ngòi bút máy cách chữ ký 1mm] + [Tiếng lòng lanh lảnh dội thẳng vào màng nhĩ sếp tổng bóc mẽ điều khoản ma]",
                "example": "Chiếc bút máy nạm kim cương của Lục Cảnh Hoài chỉ còn cách dòng chữ ký bản hợp đồng năm trăm tỷ đúng một milimét, thì một giọng nữ lanh lảnh bỗng dội thẳng vào màng nhĩ anh: 'Dừng bút lại đồ ngốc! Bản hợp đồng này ký xuống là mất trắng năm trăm tỷ, chưa kể chiếc cà vạt hoa hòe màu cánh sen chấm bi của sếp nhìn y hệt con công đang xòe đuôi!'.",
                "retention_impact": "Đỉnh cao (+85% 5s retention)",
                "source": "10_cycles_master_codex"
            },
            {
                "formula": "Đầu trâm bạc sủi bọt thâm cung (Palace Chemical Reaction Kick-off)",
                "template": "[Trâm bạc nhúng vào chén trà thanh nhiệt] + [Lớp men sủi bọt xám tro như bồ hóng] + [Nụ cười thâm độc ép uống]",
                "example": "Chiếc trâm bạc vừa nhúng vào chén trà hoa cúc của Thục phi, đầu trâm đã sủi lên một lớp bọt xám tro như bồ hóng. Thục phi vẫn mỉm cười dịu dàng nâng tách trà lên môi tôi: 'Uống đi con dâu, trà nguội mất ngon'.",
                "retention_impact": "Rất cao (+76% 5s retention)",
                "source": "10_cycles_master_codex"
            }
        ]
    },
    "viral_title_templates": {
        "DOUYIN_ZHIZU": [
            "Bát Yến Chưng Dưới Đáy Bản Khế Ước: Đòi Lại Căn Biệt Thự 50 Tỷ",
            "Thư Ký Giả Ngốc: Tiếng Lòng Chê Tổng Tài Khiến Cả Phòng Họp Cười Xỉu",
            "Bản Đồ Quy Hoạch Ngầm: Bẫy Đấu Giá Một Trăm Hai Mươi Tỷ",
            "Cánh Cửa Thép Lúc Âm Sáu Mươi Độ: Búp Bê Cao Su Giả Trẻ Con Sốt",
            "Chén Trà Hoa Cúc Thâm Cung: Con Dấu Ngự Y Dưới Lớp Men Gốm",
            "Hàng Ghế Số Bốn Rạp Chiếu Phim Đêm: Người Áo Mưa Đen",
            "Chiếc Thẻ Nhớ Trong Bút Dạ Quang: Bí Mật Bảng Danh Dự Học Đường",
            "Bản Khế Ước Niêm Phong Sáp Đỏ: Đại Hội Cổ Đông Ba Mươi Nghìn Tỷ"
        ]
    },
    "comment_magnets": {
        "DOUYIN_ZHIZU": [
            "Nếu ở vị trí của nữ chính, bạn sẽ chọn phong tỏa tài sản ngay tại bàn tiệc (Bình luận 1) hay tương kế tựu kế thu thập thêm chứng cứ (Bình luận 2)?",
            "Bạn nhận ra kẻ đứng sau mưu đồ tráo đổi từ chi tiết chiếc bút dạ quang hay bản kiểm toán? Để lại bình luận số 1 hoặc 2 nhé!",
            "Màn vả mặt này đã đủ hả dạ chưa? Bạn muốn thấy kẻ phản bội phải trả lời trước pháp luật như thế nào?"
        ]
    },
    "broll_synergies": {
        "chinese_pastry_baking": {
            "best_genre": "Gia Đấu, Mẹ Chồng Nàng Dâu, Trọng Sinh Hào Môn",
            "reason": "Các nét cắt bột làm bánh hoa cúc, hoa sen tinh xảo giữ mắt người xem mê mẩn, giúp thính giác hấp thụ 100% drama gia tộc nghẹt thở.",
            "synergy_score": 9.9
        },
        "chinese_beauty_asmr": {
            "best_genre": "Tiếng Lòng, Sa Điêu Hài Hước, Trà Xanh Liễu Như Yên",
            "reason": "Cảnh trang điểm cổ phong lụa là, chuốt mi tỉ mỉ tạo tương phản cực mạnh với lời bóc phốt trào phúng, kích nổ thời gian xem hết video.",
            "synergy_score": 9.8
        },
        "chinese_craft_heritage": {
            "best_genre": "Trinh Thám Kỳ Án, Đấu Trí Thương Trường, Mạt Thế Sinh Tồn",
            "reason": "Âm thanh đục đẽo gỗ, nung men gốm và rèn thép thủ công tạo cảm giác cơ học chân thực, bổ trợ tối đa cho các tình tiết phá án và xây hầm ngầm.",
            "synergy_score": 9.9
        }
    }
}


class ContinuousLearningEngine:
    def __init__(self):
        self.knowledge = self.load_knowledge()

    def load_knowledge(self) -> Dict[str, Any]:
        if LEARNED_PATTERNS_FILE.exists():
            try:
                with open(LEARNED_PATTERNS_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Lỗi đọc {LEARNED_PATTERNS_FILE}: {e}")
        return DEFAULT_LEARNED_KNOWLEDGE.copy()

    def save_knowledge(self):
        LEARNED_PATTERNS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LEARNED_PATTERNS_FILE, "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=2)
        logger.info("Đã lưu tri thức học được từ 10 Vòng Thực Nghiệm.")

    def get_best_hook_strategy(self, genre: str = "") -> Dict[str, Any]:
        """Lấy chiến thuật mở đầu tốt nhất dựa trên Dual-Engine Hook Architecture."""
        g = genre.upper()
        if any(k in g for k in ["TRINH_THAM", "GIA_DAU", "ME_CHONG", "KINH_DI"]):
            hooks = self.knowledge.get("viral_hooks_library", {}).get("STRATEGY_A_FLASH_FORWARD", [])
            return hooks[0] if hooks else {}
        else:
            hooks = self.knowledge.get("viral_hooks_library", {}).get("STRATEGY_B_IN_MEDIA_RES", [])
            return hooks[0] if hooks else {}
"""

Path('scratch/update_learning_engine.py').write_text(content.strip() + '\n', encoding='utf-8')
print("WROTE scratch/update_learning_engine.py")
