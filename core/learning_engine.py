import os
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
    },
    "learned_history": []
}

class ContentLearningEngine:
    """
    Hệ thống Tự Học Hỏi & Tự Tiến Hóa Tri Thức Content Triệu View (Self-Learning Engine).
    Tự động quét internet, phân tích các mẫu viral, chưng cất tri thức thành quy tắc
    và nạp ngược lại cho các Agent trong Studio để liên tục nâng cao chất lượng & views.
    """

    def __init__(self):
        self.knowledge_file = LEARNED_PATTERNS_FILE
        self._ensure_knowledge_base()

    def _ensure_knowledge_base(self) -> None:
        """Đảm bảo file tri thức tồn tại và hợp lệ"""
        if not self.knowledge_file.exists():
            self.knowledge_file.parent.mkdir(parents=True, exist_ok=True)
            self.save_knowledge(DEFAULT_LEARNED_KNOWLEDGE)
        # Đồng bộ hóa tri thức từ các video TikTok thực tế đã thu thập
        self.sync_real_tiktok_studies()

    def sync_real_tiktok_studies(self) -> Dict[str, Any]:
        """
        Nạp toàn bộ dữ liệu nghiên cứu thực chiến từ 24 video TikTok/YouTube viral
        và 4 transcript chuyên sâu (Baking Storytime, Baking Mystery, Túi Mù Drama, Kỳ Án Có Thật).
        """
        knowledge = self.load_knowledge()
        study_file = Path("data/tiktok_study/real_script_analysis.json")
        cases_file = Path("data/real_tiktok_cases.json")
        
        real_cases = []
        if study_file.exists():
            try:
                with open(study_file, "r", encoding="utf-8") as f:
                    real_cases = json.load(f)
            except Exception as e:
                logger.warning(f"Không thể đọc {study_file}: {e}")
                
        raw_cases = []
        if cases_file.exists():
            try:
                with open(cases_file, "r", encoding="utf-8") as f:
                    raw_cases = json.load(f)
            except Exception as e:
                logger.warning(f"Không thể đọc {cases_file}: {e}")

        knowledge["real_tiktok_case_studies"] = {
            "total_scraped_videos": len(raw_cases),
            "deep_transcript_cases": len(real_cases),
            "archetypes": [
                {
                    "name": "Conan Deductive Mastery (Thám Tử Lừng Danh / Triệu Views)",
                    "broll": "craft",
                    "hook_style": "Catchphrase & Impossible Paradox: 'Sự thật chỉ có một' + câu đố án mạng phòng kín giật gân trong 5s đầu.",
                    "sample_hook": "'Sự thật chỉ có một, và hung thủ đang giấu mình sau một vỏ bọc không ai ngờ tới!' - Đúng hai giờ sáng, chiếc điện thoại bàn đã cắt dây từ 5 năm trước bỗng rung lên từng hồi đinh tai nhức óc!"
                },
                {
                    "name": "Doraemon Mystery & Time Sci-Fi (Kỳ Án Cỗ Máy Thời Gian & Cánh Cửa Thần Kỳ)",
                    "broll": "craft",
                    "hook_style": "Familiar Icon Shock: Đưa bảo bối Doraemon (Cỗ máy thời gian, Cánh cửa thần kỳ, Ngăn bàn học) vào kỳ án đấu trí nghẹt thở.",
                    "sample_hook": "'Nếu bước qua Cánh Cửa Thần Kỳ vào đúng 12 giờ đêm nay, bạn sẽ chứng kiến một vụ án mạng mà nạn nhân chính là bản thân mình 20 năm sau!' - Lời cảnh báo đẫm máu rơi ra từ ngăn bàn học cũ..."
                },
                {
                    "name": "Hào Môn 100B Drama (Tổng Tài Bạc Tỷ / Cưới Trước Yêu Sau)",
                    "broll": "baking",
                    "hook_style": "High-Stakes In-Media-Res Clash: Quát tháo dằn mặt, ném hợp đồng 100 tỷ ngay giây thứ 3.",
                    "sample_hook": "'Ký vào đây! Tôi cho cô 100 tỷ và sự tự do, cô chỉ là kẻ gả thay hèn kém thôi!' - Vị tổng tài tàn tật ném mạnh hợp đồng xuống bàn..."
                },
                {
                    "name": "Baking Storytime Drama (Nhã Bé Bắp / 787K views)",
                    "broll": "baking",
                    "hook_style": "In-Media-Res Dialogue: Nhảy thẳng vào giữa cuộc đối thoại tranh chấp, không chào hỏi rườm rà.",
                    "sample_hook": "Buổi lễ bắt đầu rồi kìa, khoan đã... Cô ta không phải là người của ngài đâu thưa hoàng tử..."
                },
                {
                    "name": "Baking Mystery Confession (Trang Trí Bánh & Chuyện Ma / 2.2M views)",
                    "broll": "baking",
                    "hook_style": "Listener Confession Hook: Kể lại trải nghiệm có thật của người theo dõi kênh.",
                    "sample_hook": "Hôm nay là câu chuyện của một bạn theo dõi kênh khá lâu kể lại. Câu chuyện xảy ra cách đây 4 năm khi xe đang chạy thì gặp trục trặc..."
                },
                {
                    "name": "First-Person Audio Drama (Túi Mù Audio / 1.08M views)",
                    "broll": "craft",
                    "hook_style": "High-Drama Sensory Monologue: Ngôi kể thứ nhất, giàu chi tiết giác quan, xung đột giai tầng / trả đũa.",
                    "sample_hook": "Tôi về nước. Chuyến bay 12 tiếng từ Florence đáp xuống sân bay Bắc Kinh. 7 năm đủ để một kẻ chiếm tổ chim khách ảo tưởng mình là Phượng Hoàng..."
                },
                {
                    "name": "Bedtime Healing Radio (Radio Truyện Đêm Khuya / 1.14M views)",
                    "broll": "nature",
                    "hook_style": "Sensory Whispering & Decompression: Giọng thì thầm êm ái, kéo dài nguyên âm, âm thanh mưa rơi.",
                    "sample_hook": "Đêm nay, hãy buông bỏ hết những mệt mỏi của ngày dài, hít thở thật sâu và cùng tôi bước vào không gian tĩnh lặng nhất..."
                }
            ],
            "audio_specs_measured": {
                "voice_peak_db": "-4.4 dB to -7.0 dB",
                "voice_mean_db": "-20.8 dB to -27.0 dB",
                "bgm_ducking_level": "-21.0 dB to -27.0 dB (Voice dominant)",
                "bgm_type": "100% Instrumental Only (Piano Lofi, Ambient, Dark Strings, NO vocals)"
            },
            "visual_specs": {
                "aspect_ratio": "16:9 Widescreen (1920x1080)",
                "dynamics": "Baking ASMR, Pottery/Wood Crafting, Rain/Cabin Nature loop",
                "purpose": "Giữ mắt người xem (oddly satisfying visual) để tai tập trung nghe trọn vẹn mạch truyện."
            }
        }
        
        self.save_knowledge(knowledge)
        return knowledge

    def load_knowledge(self) -> Dict[str, Any]:
        """Tải toàn bộ cơ sở tri thức đã học"""
        try:
            with open(self.knowledge_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Lỗi đọc tri thức ({e}), sử dụng mặc định.")
            return DEFAULT_LEARNED_KNOWLEDGE

    def save_knowledge(self, data: Dict[str, Any]) -> None:
        """Lưu trữ bền vững các tri thức mới học được"""
        self.knowledge_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.knowledge_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def learn_from_online_trends(self, limit: int = 5) -> Dict[str, Any]:
        """
        Chu trình tự động quét các bài viết/video hot trên internet, 
        dùng AI phân tích công thức thành công và cập nhật vào bộ não của Studio.
        """
        print("\n" + "=" * 65)
        print("🧠 [HỌC TẬP TỰ ĐỘNG] KHỞI ĐỘNG CHU TRÌNH TỰ TIẾN HÓA TRI THỨC")
        print("=" * 65)
        print(f" -> Quét dữ liệu xu hướng thực tế từ mạng xã hội (TikTok, Reddit, Quora, Life Stories)...")

        harvester = TrendHarvester()
        topics = harvester.harvest_all(total_budget_seconds=12.0)

        if not topics:
            print("[Học Tập Tự Động] Không thể cào dữ liệu mới, sử dụng kho dự phòng.")
            return self.load_knowledge()

        # Chọn ra các đề tài có điểm viral cao nhất để học
        sorted_topics = sorted(topics, key=lambda t: t.viral_score, reverse=True)[:limit]
        print(f" -> Đã chọn lọc {len(sorted_topics)} nội dung có chỉ số tương tác cao nhất để mổ xẻ phân tích.")

        knowledge = self.load_knowledge()
        new_insights_count = 0

        for idx, topic in enumerate(sorted_topics, 1):
            category = topic.category_match or "HIGH_IQ"
            print(f"\n [Bài học #{idx}] Phân tích mẫu: '{topic.title}' (Viral Score: {topic.viral_score:.1f} | Nguồn: {topic.source})")

            # Sử dụng LLM để giải mã lý do viral cho kênh Truyện Audio
            analysis_prompt = f"""Hãy đóng vai Chuyên gia Tối ưu Thuật toán TikTok / Douyin chuyên về DÒNG TRUYỆN AUDIO / KỂ CHUYỆN (Storytelling Audio).
Phân tích chủ đề sau và trích xuất công thức viral thành công cho một BỘ TRUYỆN AUDIO 30 PHÚT (3 HỒI):
Tiêu đề: {topic.title}
Tóm tắt: {topic.summary}
Nguồn: {topic.source}
Chỉ số: {topic.metrics}

Hãy trả về định dạng JSON:
{{
  "hook_formula": "Tên công thức hook (Climax First | Contrarian Shock | Curiosity Gap | Sensory Decompression | Confession Dilemma)",
  "hook_template": "Mẫu câu hook kể chuyện 0-3s mở đầu trừu tượng hóa có thể tái sử dụng",
  "viral_title_template": "Mẫu tiêu đề truyện audio hấp dẫn (tuyệt đối không ghi số phút)",
  "comment_trigger": "Câu hỏi phân cực ở cuối truyện tạo bão bình luận tranh cãi",
  "suggested_broll": "baking | craft | nature | mukbang",
  "why_it_works": "Lý giải ngắn gọn tại sao người nghe bị cuốn hút từ đầu đến cuối"
}}"""

            try:
                raw_res = call_llm(
                    prompt=analysis_prompt,
                    system_prompt="Bạn là Viện Trưởng Nghiên Cứu Thuật Toán Nội Dung Mạng Xã Hội."
                )
                data = clean_json_response(raw_res)

                hook_template = data.get("hook_template")
                title_template = data.get("viral_title_template")
                comment_trigger = data.get("comment_trigger")
                broll_theme = data.get("suggested_broll", "baking")

                if hook_template:
                    cat_key = "SLEEP_CHILL" if category == "SLEEP_CHILL" else "HIGH_IQ"
                    # Lưu vào kho hook
                    knowledge["viral_hooks_library"][cat_key].append({
                        "formula": data.get("hook_formula", "Discovered Hook"),
                        "template": hook_template,
                        "example": topic.title,
                        "retention_impact": "Được học từ bài viết triệu view",
                        "source": topic.source,
                        "learned_at": datetime.now().isoformat()
                    })

                    # Lưu vào kho title
                    if title_template and title_template not in knowledge["viral_title_templates"][cat_key]:
                        knowledge["viral_title_templates"][cat_key].append(title_template)

                    # Lưu vào kho comment magnets
                    if comment_trigger and comment_trigger not in knowledge["comment_magnets"][cat_key]:
                        knowledge["comment_magnets"][cat_key].append(comment_trigger)

                    new_insights_count += 1
                    print(f"    * 💡 Hook mới học được: [{data.get('hook_formula')}]: \"{hook_template[:70]}...\"")
                    print(f"    * 🎯 Title mẫu mới: \"{title_template}\"")
                    print(f"    * 💬 Comment Trigger mới: \"{comment_trigger}\"")
                    print(f"    * 🎬 B-Roll đề xuất: [{broll_theme}]")

            except Exception as e:
                print(f"    * Lỗi phân tích: {e}")

        # Cập nhật metadata tiến hóa
        knowledge["total_insights_learned"] += new_insights_count
        knowledge["evolution_cycles"] += 1
        knowledge["last_updated"] = datetime.now().isoformat()
        knowledge["learned_history"].append({
            "timestamp": datetime.now().isoformat(),
            "new_insights_added": new_insights_count,
            "top_topic": sorted_topics[0].title if sorted_topics else "N/A"
        })

        self.save_knowledge(knowledge)

        print("\n" + "=" * 65)
        print(f"✨ [TIẾN HÓA HOÀN TẤT] Đã nạp thành công {new_insights_count} bài học mới vào Studio!")
        print(f" -> Tổng số tri thức tích lũy: {knowledge['total_insights_learned']} insights")
        print(f" -> Chu kỳ tiến hóa: Chu kỳ #{knowledge['evolution_cycles']}")
        print("=" * 65)

        return knowledge

    def get_tactics_for_scriptwriter(self, category: VideoCategory, topic_title: str = "", topic_summary: str = "") -> Dict[str, Any]:
        """
        Cung cấp các công thức Hook, Title và CTA mới nhất vừa học được từ mạng,
        đồng thời bắt buộc đối soát và tra cứu Cơ sở dữ liệu 100 tác phẩm đoản văn kinh điển
        để Agent Biên Kịch nạp trực tiếp vào kịch bản mới.
        """
        knowledge = self.load_knowledge()
        cat_key = "SLEEP_CHILL" if category == VideoCategory.SLEEP_CHILL else "HIGH_IQ"

        hooks = knowledge.get("viral_hooks_library", {}).get(cat_key, [])
        titles = knowledge.get("viral_title_templates", {}).get(cat_key, [])
        ctas = knowledge.get("comment_magnets", {}).get(cat_key, [])

        # Lấy 2 hook gần nhất được học để ưu tiên áp dụng
        recent_hooks = hooks[-2:] if len(hooks) >= 2 else hooks
        recent_titles = titles[-2:] if len(titles) >= 2 else titles
        recent_ctas = ctas[-2:] if len(ctas) >= 2 else ctas

        # Trích xuất các Archetype từ nghiên cứu video TikTok triệu view thực tế
        all_archetypes = knowledge.get("real_tiktok_case_studies", {}).get("archetypes", [])
        if category == VideoCategory.SLEEP_CHILL:
            relevant_archetypes = [a for a in all_archetypes if "Radio" in a["name"] or "Bedtime" in a["name"] or a["broll"] == "nature"]
        else:
            relevant_archetypes = [a for a in all_archetypes if a["broll"] in ["baking", "craft"]]

        # Tra cứu Cơ sở tri thức 100 tác phẩm kinh điển
        from core.knowledge_base import get_knowledge_base
        kb = get_knowledge_base()
        masterclass_brief = kb.query_masterclass(
            topic_title=topic_title,
            topic_summary=topic_summary,
            category=category,
            top_k=3
        )
        prompt_instruction = kb.format_brief_for_prompt(masterclass_brief)

        return {
            "recommended_hooks": recent_hooks,
            "recommended_titles": recent_titles,
            "recommended_ctas": recent_ctas,
            "real_archetypes": relevant_archetypes,
            "total_learned": knowledge.get("total_insights_learned", 0),
            "masterclass_brief": masterclass_brief,
            "masterclass_prompt_instruction": prompt_instruction
        }

    def get_evolution_report(self) -> str:
        """Tạo báo cáo chi tiết về tiến trình tự hoàn thiện của Studio"""
        k = self.load_knowledge()
        report = []
        report.append(f"📊 BÁO CÁO TIẾN HÓA CỦA STUDIO (TỰ HỌC TỪ MẠNG XÃ HỘI):")
        report.append(f" - Phiên bản tri thức: {k.get('version', '2.0')}")
        report.append(f" - Số chu kỳ học tập đã thực hiện: {k.get('evolution_cycles', 0)}")
        report.append(f" - Tổng số tri thức/công thức viral đã tích lũy: {k.get('total_insights_learned', 0)}")
        report.append(f" - Số mẫu Hook High-IQ: {len(k.get('viral_hooks_library', {}).get('HIGH_IQ', []))}")
        report.append(f" - Số mẫu Hook Sleep-Chill: {len(k.get('viral_hooks_library', {}).get('SLEEP_CHILL', []))}")
        report.append(f" - Lần cập nhật gần nhất: {k.get('last_updated', 'N/A')}")
        return "\n".join(report)
