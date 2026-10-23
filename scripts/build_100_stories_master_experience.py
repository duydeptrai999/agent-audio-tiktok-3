# -*- coding: utf-8 -*-
"""
scripts/build_100_stories_master_experience.py
Chương trình biên soạn Đại Điển Tri Thức & Kinh Nghiệm Biên Kịch 100 Bộ Đoản Văn Trung Quốc Kinh Điển.
Tạo tài liệu: docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md
"""

import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

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

OUT_FILE = ROOT_DIR / "docs" / "DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md"
CWD_OUT_FILE = Path.cwd() / "docs" / "DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md"

GENRE_METADATA = [
    {
        "genre_id": 1,
        "name_vn": "Ngược Luyến Tàn Tâm & Hỏa Táng Tràng Truy Thê",
        "name_cn": "虐恋残心 · 追妻火葬场",
        "platform": "Zhihu 盐选, Jinjiang (晋江文学城)",
        "core_emotion": "Đau xót dằn vặt, hối hận muộn màng, giải thoát bi tráng",
        "stories": STORIES_GENRE_1
    },
    {
        "genre_id": 2,
        "name_vn": "Trọng Sinh Vả Mặt & Nữ Cường Kinh Thương",
        "name_cn": "重生逆袭 · 绝地打脸",
        "platform": "Fanqie (番茄小说), Douyin 短剧, Zhihu",
        "core_emotion": "Sảng khoái tột độ, báo thù dứt khoát, tự do tài chính",
        "stories": STORIES_GENRE_2
    },
    {
        "genre_id": 3,
        "name_vn": "Huyền Nghi Trinh Thám & Pháp Y Tâm Lý",
        "name_cn": "悬疑推理 · 法医破案",
        "platform": "Zhihu 盐选 (Chuyên mục Phá Án), Douyin",
        "core_emotion": "Nghẹt thở, rùng mình lạnh gáy (细思极恐), công lý phục hồi",
        "stories": STORIES_GENRE_3
    },
    {
        "genre_id": 4,
        "name_vn": "Mẹ Chồng Nàng Dâu & Gia Đấu Bạo Lực Lạnh",
        "name_cn": "婆媳博弈 · 家族宅斗",
        "platform": "Douyin 短剧, Kuaishou, Zhihu",
        "core_emotion": "Ức chế bùng nổ, cắt dòng tiền, vạch mặt kẻ ăn bám",
        "stories": STORIES_GENRE_4
    },
    {
        "genre_id": 5,
        "name_vn": "Hào Môn Tổng Tài & Hợp Đồng Hôn Nhân Giả",
        "name_cn": "豪门总裁 · 契约隐婚",
        "platform": "Douyin 短剧, Fanqie, Jinjiang",
        "core_emotion": "Đối lập thân phận, nghiền ép địa vị, ngọt ngào bá đạo",
        "stories": STORIES_GENRE_5
    },
    {
        "genre_id": 6,
        "name_vn": "Kinh Dị Đô Thị & Quy Tắc Quái Đàm",
        "name_cn": "中式恐怖 · 规则怪谈",
        "platform": "Zhihu 盐选, Bilibili, Douyin",
        "core_emotion": "Hoang mang tâm lý, sinh tồn nghẹt thở, giải mã hiện trường",
        "stories": STORIES_GENRE_6
    },
    {
        "genre_id": 7,
        "name_vn": "Sa Điêu Hài Hước & Tiếng Lòng Thần Dụ",
        "name_cn": "沙雕搞笑 · 读心术吃瓜",
        "platform": "Fanqie, Douyin, Zhihu",
        "core_emotion": "Cười ra nước mắt, lật tẩy trà xanh bằng trò hề, hả hê trào phúng",
        "stories": STORIES_GENRE_7
    },
    {
        "genre_id": 8,
        "name_vn": "Cung Đấu Trạch Đấu & Bãi Công Tự Chủ",
        "name_cn": "宫廷宅斗 · 弃妇自强",
        "platform": "Jinjiang, Zhihu, Douyin",
        "core_emotion": "Tâm cơ thâm trầm, liên minh nữ giới, vượt qua giam cầm cung cấm",
        "stories": STORIES_GENRE_8
    },
    {
        "genre_id": 9,
        "name_vn": "Thanh Xuân Cứu Rỗi & Chữa Lành Tổn Thương",
        "name_cn": "救赎治愈 · 青春逆袭",
        "platform": "Zhihu, Jinjiang, Lofter",
        "core_emotion": "Ấm áp sưởi ấm, vượt qua bóng tối, ánh sáng chân thành",
        "stories": STORIES_GENRE_9
    },
    {
        "genre_id": 10,
        "name_vn": "Vô Hạn Lưu & Cực Hạn Sinh Tồn Mạt Thế",
        "name_cn": "无限流 · 末世基建极寒",
        "platform": "Qidian (起点), Fanqie, Douyin",
        "core_emotion": "Kỹ thuật sinh tồn, cô lập áp suất, pháo đài bất khả xâm phạm",
        "stories": STORIES_GENRE_10
    }
]

def generate_master_markdown():
    lines = [
        "# ĐẠI ĐIỂN TRI THỨC & KINH NGHIỆM BIÊN KỊCH 100 BỘ ĐOẢN VĂN TRUNG QUỐC KINH ĐIỂN",
        "",
        "> **Sổ Tay Bách Khoa Toàn Thư Về Biên Kịch Kịch Bản Đoản Văn & Audio Drama TikTok Triệu View.**",
        "> *Nguồn dữ liệu thực chiến: Tổng hợp và mổ xẻ chuyên sâu 100 tác phẩm đoản văn kinh điển nổi tiếng nhất từ Zhihu 盐选专栏, Douyin 短剧, Fanqie (番茄小说), Jinjiang (晋江文学城) và Qidian (起点中文网).*",
        "> *Được thiết kế làm kim chỉ nam bất biến cho toàn bộ Hệ thống Agent và Động cơ Biên Kịch Antigravity TikTok Studio.*",
        "",
        "---",
        "",
        "## PHẦN I: TỔNG LUẬN PHƯƠNG PHÁP LUẬN BIÊN KỊCH ĐOẢN VĂN VIRAL (ZHIHU & DOUYIN)",
        "",
        "### 1. Triết Lý Cốt Lõi: '12 Chữ Vàng' Của Đoản Văn Giữ Chân Người Nghe",
        "> **'Ba giây một cái móc (Hook), năm giây một đảo chiều (Twist), tập nào cũng có điểm sảng (Shuangdian)!'**",
        "",
        "- **Quy tắc 1.5 - 3 Giây Đầu**: Quyết định sinh tử của video. Thính giả lướt qua màn hình cực nhanh. Nếu 15 từ đầu tiên không chứa xung đột cực hạn, nghịch lý hành động hoặc vật chứng rợn gáy, tỷ lệ vuốt bỏ (Swipe Away) đạt trên 85%.",
        "- **Công Thức Sảng Điểm Định Lượng (The Shuangdian Neuro-Equation)**:",
        "",
        "$$\\text{Mức Độ Sảng} = (\\text{Độ Ức Chế Tột Cùng} \\times \\text{Độ Trì Hoãn Thỏa Mãn}) \\times \\text{Tốc Độ & Cường Độ Phản Đòn}$$",
        "",
        "- **Chu Trình 4 Giai Đoạn Áp Chế - Bộc Phát**:",
        "  1. `ÁP CHẾ (压抑 - Yayi)`: Tạo bất công phi lý, hạ thấp nhân vị, tước đoạt danh dự của NV chính (nạp đầy phẫn nộ cho khán giả).",
        "  2. `TÍCH TỤ / KÉO NÉN (蓄势 - Xushi)`: NV chính không manh động, ẩn nhẫn mài dao, giăng bẫy âm thầm (kỳ vọng đòn trừng phạt).",
        "  3. `BỘC PHÁT VẢ MẶT (爆发打脸 - Bofa Dalian)`: Lật mở sự thật ngay tại đỉnh cao đắc thắng của phản diện (giải phóng Dopamine cực hạn).",
        "  4. `THANH TOÁN TRIỆT ĐỂ (清算 - Qingsuan)`: Phản diện mất hết tiền tài, danh dự, địa vị; cầu xin trong tuyệt vọng (tuyệt đối không tha thứ rẻ rúng).",
        "",
        "### 2. Mô Hình Nhịp Độ 1 Phút / 1 Tập Chuẩn Điện Ảnh (Micro-Pacing Model)",
        "```mermaid",
        "flowchart LR",
        "    A[\"00s - 03s: Hook 3 Giây\n(Va chạm vật lý / Nghịch lý)\"] --> B[\"03s - 15s: Nén Ức Chế\n(Phản diện áp chế tột cùng)\"]",
        "    B --> C[\"15s - 45s: Biến Số & Lật Kèo\n(Rút bài tẩy / Bóc trần tử huyệt)\"]",
        "    C --> D[\"45s - 55s: Điểm Sảng Bùng Nổ\n(Vả mặt sòng phẳng / Sụp đổ)\"]",
        "    D --> E[\"55s - 60s: Cliffhanger Cắt Đỉnh\n(Mở ra hiểm nguy lớn hơn)\"]",
        "```",
        "",
        "### 3. Bảng Phân Bổ Âm Thanh & Nhịp Thở Audio Drama (Sound Design Pacing)",
        "| Thời Gian | Chức Năng Âm Thanh / Kịch Bản | Mục Tiêu Giữ Chân (Retention) | Kỹ Thuật Sound Design |",
        "| :--- | :--- | :--- | :--- |",
        "| **00:00 - 00:03** | **GOLDEN HOOK:** Lời thoại gây sốc / Mâu thuẫn đạo đức tột độ | Ngăn người dùng lướt đi (Stop-scrolling) | Tiếng tát vang dội, tiếng máy thở tít dài, tiếng đập bàn, âm bass drop đột ngột |",
        "| **00:03 - 00:15** | **ESCALATION:** Phản diện dồn ép, nhân vật chính rơi vào tuyệt lộ | Tạo cảm xúc phẫn nộ / tò mò tột đỉnh | Nhạc nền căng thẳng (Violin dồn dập, tiếng đồng hồ đếm ngược) |",
        "| **00:15 - 00:25** | **PRE-TWIST:** Một biến số lạ xuất hiện, hé lộ tia hy vọng | Kích hoạt tò mò trí tuệ | Nhạc nền im bặt đột ngột (Audio Pause / Negative Space) |",
        "| **00:25 - 00:30** | **CLIFFHANGER / MINI-PUNCH:** Câu nói lật đổ cục diện hoặc tiếng mở cửa | Buộc người nghe phải nghe tiếp tập sau | Tiếng hiệu ứng Whoosh + Câu thoại bỏ lửng then chốt |",
        "",
        "### 4. Bộ 5 Mô Thức 'Hook 3 Giây' Triệu View (Golden Hook Templates)",
        "1. **Hook Nghịch Luân Lý / Khiêu Khích Đạo Đức**: *'Ngày tôi sinh non trong phòng cấp cứu, chồng tôi đang ký giấy đồng ý hiến thận của tôi cho người yêu cũ của anh ta.'*",
        "2. **Hook Đếm Ngược Tử Thần**: *'Bác sĩ nói tôi chỉ còn sống được ba mươi ngày, và việc đầu tiên tôi làm là rút năm mươi tỷ tiền tiết kiệm.'*",
        "3. **Hook Phản So Sai Thân Phận Cực Đoan**: *'Mẹ chồng tống tôi ra khỏi biệt thự với hai trăm nghìn đồng dằn túi, bà không hề biết tập đoàn mà con trai bà đang làm thuê mang chính tên lót của tôi.'*",
        "4. **Hook Quái Đàm / Cấm Kỵ Quy Tắc**: *'Nếu bạn thức giấc lúc ba giờ sáng và thấy mẹ bạn đang đứng gõ cửa phòng tắm... Đừng mở cửa! Mẹ bạn đã mất ba năm trước rồi.'*",
        "5. **Hook Thẳng Tay Vả Mặt (Direct Slap Hook)**: *'Cầm năm mươi tỷ này và cút khỏi con trai tôi? Bác gái à, công ty của con trai bác tháng trước vừa vay của tôi một trăm tỷ đấy!'*",
        "",
        "### 5. Thiết Kế Nhân Vật Phản Diện 3 Chiều (Chống Bẫy Não Tàn)",
        "```",
        "           [LỚP NGOÀI: MẶT NẠ ĐẠO ĐỨC & TRÍ TUỆ]",
        "   - Lịch thiệp, được xã hội công nhận, lời nói luôn nhân danh lợi ích chung.",
        "   - Thấu hiểu luật pháp, dùng kẽ hở quy định để triệt hạ đối thủ.",
        "                         ↓",
        "           [LỚP GIỮA: ĐỘNG CƠ HỢP LÝ HÓA (JUSTIFICATION)]",
        "   - 'Ta không ác, ta chỉ đang giành lại những gì thế giới nợ ta.'",
        "   - Xuất thân chấn thương tâm lý, nghèo đói cùng cực hoặc bị áp bức thời niên thiếu.",
        "                         ↓",
        "           [LỚP LÕI: TỬ HUYỆT BẢO THỦ & KIÊU NGẠO]",
        "   - Không tin trên đời có người vô tư không tham lam.",
        "   - Đánh giá thấp nhân tính và tình yêu thương chân thành.",
        "```",
        "",
        "---",
        "",
        "## PHẦN II: MỔ XẺ CHI TIẾT 100 TÁC PHẨM ĐOẢN VĂN KINH ĐIỂN THEO 10 THỂ LOẠI",
        ""
    ]

    total_count = 0

    for g in GENRE_METADATA:
        gid = g["genre_id"]
        nvn = g["name_vn"]
        ncn = g["name_cn"]
        plat = g["platform"]
        emo = g["core_emotion"]
        stories = g["stories"]

        lines.extend([
            f"### 📂 THỂ LOẠI {gid:02d}: {nvn.upper()} ({ncn})",
            f"- **Nền tảng tiêu biểu**: {plat}",
            f"- **Trục cảm xúc chủ đạo**: *{emo}*",
            f"- **Số lượng tác phẩm nghiên cứu**: {len(stories)} tác phẩm nổi tiếng.",
            "",
            "---",
            ""
        ])

        for s in stories:
            total_count += 1
            sid = s["id"]
            tvn = s["title_vn"]
            tcn = s["title_cn"]
            author = s["author_platform"]
            sub_genre = s["genre"]
            premise = s["premise"]
            characters = s["characters"].strip()
            hook = s["golden_hook"].strip()
            acts = s["acts_and_pacing"].strip()
            twist = s["plot_twist"].strip()
            lessons = s["core_lessons"].strip()

            lines.extend([
                f"#### 📜 [{sid:03d}/100] 《{tvn}》 ({tcn})",
                f"- **Tác giả & Nền tảng**: `{author}`",
                f"- **Phân loại**: *{sub_genre}*",
                f"- **Bối cảnh & Tiền đề kịch tính (Premise)**: {premise}",
                "",
                "**1. Thiết Lập & Xây Dựng Nhân Vật (Character Archetypes & Dynamics):**",
                f"{characters}",
                "",
                "**2. Mở Đầu Audio 3 Giây Giữ Chân (The 3-Second Retention Hook):**",
                f"> ⚡ *{hook}*",
                "",
                "**3. Cấu Trúc 3 Hồi & Nhịp Độ Micro-Pacing (Acts & Pacing):**",
                f"{acts}",
                "",
                "**4. Cú Twist Đa Tầng & Điểm Sảng Bùng Nổ (Satisfaction Peak & Plot Twist):**",
                f"💥 **Điểm bẻ lái cốt lõi**: {twist}",
                "",
                "**5. Tinh Hoa Đúc Kết & Bài Học Biên Kịch Audio TikTok (Master Scriptwriting Takeaways):**",
                f"{lessons}",
                "",
                "> [!TIP]",
                f"> **Ứng dụng thực chiến của bộ {sid:03d}**: Khi sản xuất audio cho thể loại này, luôn neo đạo cụ vật lý chính vào phân đoạn mở màn và sử dụng đòn lật kèo logic, triệt tiêu hoàn toàn sáo ngữ kể lể.",
                "",
                "---",
                ""
            ])

    lines.extend([
        "## PHẦN III: MA TRẬN 5 CÔNG THỨC ĐIỂM SẢNG (SHUANGDIAN FORMULAS) ĐÚC KẾT TỪ 100 BỘ",
        "",
        "Qua việc mổ xẻ 100 tác phẩm kinh điển, hệ thống Agent đúc kết 5 công thức tạo điểm sảng mãnh liệt nhất:",
        "",
        "### 1. Công Thức Nghiền Ép Thân Phận (Identity Crushing)",
        "- **Cơ chế**: Nhân vật chính ẩn giấu danh tính (kỹ sư trưởng, người thừa kế, chủ tịch giấu mặt, bác sĩ hàng đầu) bị những kẻ thiển cận sỉ nhục, coi như rác rưởi. Đến cao trào, danh tính thực sự được công bố bởi một nhân vật có quyền lực tối cao khiến toàn trường chết lặng.",
        "- **Áp dụng Audio**: Thoại của đối phương đang lớn tiếng bỗng ngưng bặt giữa chừng khi nhìn thấy con dấu hoặc tấm thẻ đen.",
        "",
        "### 2. Công Thức Bẫy Ngược & Gậy Ông Đập Lưng Ông (Rule Inversion Trap)",
        "- **Cơ chế**: Kẻ phản diện nghĩ mình đã bày ra một cái bẫy hoàn hảo (cài ma túy, đánh cắp hồ sơ, đổ thuốc độc). Nhưng nhân vật chính đã đoán trước 3 bước, dùng chính chiếc bẫy đó để tống đối phương vào vòng lao lý.",
        "- **Áp dụng Audio**: Tiếng phát loa đoạn ghi âm bí mật hoặc kết quả xét nghiệm hóa học ngay tại hội nghị cổ đông.",
        "",
        "### 3. Công Thức Bạo Lực Lạnh & Cắt Đứt Dòng Tiền (Cold Violence Cashflow Guillotine)",
        "- **Cơ chế**: Không chửi bới, không xô xát thể xác. Nhân vật chính chỉ mỉm cười nhẹ nhàng ký lệnh thu hồi khoản vay, phong tỏa cổ phần hoặc kích hoạt điều khoản hợp đồng tín thác Thụy Sĩ, khiến kẻ phản trắc phá sản sau 1 đêm.",
        "- **Áp dụng Audio**: Tiếng gõ bàn phím Enter, tiếng tin nhắn ngân hàng báo số dư về 0.",
        "",
        "### 4. Công Thức Buông Bỏ Lạnh Lùng & Hỏa Táng Tràng (Sober Rejection Catharsis)",
        "- **Cơ chế**: Sau khi bị đối xử tệ bạc, nhân vật chính dứt khoát quay lưng làm lại cuộc đời. Đến khi kẻ phản bội nhận ra sai lầm và quỳ gối xin tha thứ, nhân vật chính không thèm nhìn lại dù chỉ một lần.",
        "- **Áp dụng Audio**: Câu thoại dao găm lạnh lùng 5-8 từ chốt hạ: *'Xin lỗi, chúng ta đã không còn liên quan'*, tiếng giày cao gót bước đi dứt khoát.",
        "",
        "### 5. Công Thức Tự Thú Tâm Lý Do Tiếng Lòng (Satirical Subtext Exposure)",
        "- **Cơ chế**: Sự tương phản giữa vẻ mặt đạo mạo và suy nghĩ bẩn bỉu bên trong bị phơi bày qua tiếng lòng, khiến kẻ thù hoảng sợ tự bộc lộ hành vi phạm tội.",
        "- **Áp dụng Audio**: Sử dụng 2 hiệu ứng giọng: Giọng đọc chính kịch trầm tĩnh đan xen với giọng thì thầm châm biếm sâu cay.",
        "",
        "---",
        "",
        "## PHẦN IV: BỘ TIÊU CHUẨN VĨNH VIỄN NẠP VÀO HỆ THỐNG AGENT",
        "",
        "1. **Bắt Buộc Tra Cứu Trước Khi Viết**: Bất kỳ audio nào được Agent tạo ra đều phải đối chiếu ít nhất 3 Case Study trong Đại Điển 100 Bộ Truyện này.",
        "2. **Zero Homogenization**: Mỗi câu chuyện phải có đạo cụ độc bản, nghề nghiệp chuyên sâu và cơ chế lật kèo logic.",
        "3. **Acoustic Cadence Standard**: Từng câu thoại được mài giũa dưới 12 từ, có dấu ngắt hơi để giọng đọc Edge-TTS đạt độ truyền cảm điện ảnh tối đa.",
        "",
        "---",
        "*Biên soạn bởi Hệ Thống Committee 10 Agents - Antigravity TikTok Studio.*",
        "*Bản quyền tri thức thuộc về Hệ thống Sản xuất Audio Drama Triệu View.*"
    ])

    content = "\n".join(lines)
    OUT_FILE.write_text(content, encoding="utf-8")
    if CWD_OUT_FILE != OUT_FILE:
        CWD_OUT_FILE.write_text(content, encoding="utf-8")
    print(f"SUCCESS: Generated {OUT_FILE} and {CWD_OUT_FILE} with {total_count} stories ({len(content)} characters).")

if __name__ == "__main__":
    generate_master_markdown()
