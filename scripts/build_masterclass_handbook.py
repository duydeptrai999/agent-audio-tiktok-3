# -*- coding: utf-8 -*-
"""
Script: scripts/build_masterclass_handbook.py
Purpose: Aggregate all 100 Chinese short story case studies from data/stories_study/
and generate the comprehensive master handbook docs/CAM_NANG_100_KICH_BAN_TRUYEN_NGAN_TRUNG_QUOC.md
as well as update data/learned_patterns.json with the acquired storytelling patterns.
"""

import sys
import os
import json
from pathlib import Path

# Add project root to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

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

GENRE_GROUPS = [
    ("I. NGƯỢC LUYẾN TÀN TÂM & HỎA TÁNG TRÀNG TRUY THÊ", STORIES_GENRE_1),
    ("II. TRỌNG SINH BÁO THÙ & VẢ MẶT SẢNG VĂN", STORIES_GENRE_2),
    ("III. HUYỀN NGHI, TRINH THÁM & HIGH-IQ ÁN MẠNG", STORIES_GENRE_3),
    ("IV. MẸ CHỒNG NÀNG DÂU, GIA ĐÌNH CỰC PHẨM & HIỆN THỰC HÔN NHÂN", STORIES_GENRE_4),
    ("V. HÀO MÔN TỔNG TÀI, KHẾ ƯỚC HÔN NHÂN & CƯỚI TRƯỚC YÊU SAU", STORIES_GENRE_5),
    ("VI. KINH DỊ ĐÔ THỊ, QUY TẮC QUÁI ĐÀM & SINH TỒN", STORIES_GENRE_6),
    ("VII. SA ĐIÊU HÀI HƯỚC, PHẢN SÁO LỘ & ĐỌC SUY NGHĨ", STORIES_GENRE_7),
    ("VIII. CUNG ĐẤU, TRẠCH ĐẤU & NỮ QUYỀN CỔ ĐẠI", STORIES_GENRE_8),
    ("IX. CỨU RỖI, CHỮA LÀNH & THANH XUÂN HỌC ĐƯỜNG", STORIES_GENRE_9),
    ("X. VÔ HẠN LƯU, MẠT THẾ SINH TỒN & KHOA HUYỄN ĐÔ THỊ", STORIES_GENRE_10)
]

def build_markdown():
    lines = []
    lines.append("# CẨM NANG TINH HOA 100 KỊCH BẢN TRUYỆN NGẮN TRUNG QUỐC (ZHIHU - DOUYIN - FANQIE - JINJIANG) VÀ NGHỆ THUẬT BIÊN KỊCH VIRAL ĐỈNH CAO")
    lines.append("## Đúc Kết Toàn Diện Từ 100 Tác Phẩm Nổi Tiếng & Phương Pháp Luận Cho Hệ Thống Sản Xuất Audio/Video Storytelling 30 Phút")
    lines.append("")
    lines.append("> [!IMPORTANT]")
    lines.append("> **Mục tiêu tài liệu:** Tổng hợp và đúc kết kinh nghiệm biên kịch từ 100 bộ truyện ngắn / đoản văn kinh điển và thịnh hành nhất của Trung Quốc trên các nền tảng Zhihu (Muối Tuyển 盐选), Douyin, Fanqie, Jinjiang và Qidian. Mỗi tác phẩm được phân tích chuyên sâu về bối cảnh, nhân vật, cú hook 5 giây, cấu trúc 3 hồi, điểm xoay chuyển (plot twist) và bài học biên kịch thực chiến để nâng cấp xưởng sản xuất video/audio storytelling tự động.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## MỤC LỤC TỔNG QUAN")
    lines.append("1. **PHẦN I: 10 ĐỊNH LUẬT VÀNG CỦA KỊCH BẢN ĐOẢN VĂN VIRAL TRUNG QUỐC**")
    lines.append("2. **PHẦN II: CHI TIẾT 100 BỘ TRUYỆN NGẮN KINH ĐIỂN & ĐÚC KẾT KINH NGHIỆM BIÊN KỊCH**")
    for group_name, _ in GENRE_GROUPS:
        lines.append(f"   - {group_name}")
    lines.append("3. **PHẦN III: BỘ QUY CHUẨN KỊCH BẢN CHO HỆ THỐNG AUDIO/VIDEO 30 PHÚT (TỐC ĐỘ ĐỌC 1.5X CHUẨN GEMINI.MD)**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN I: 10 ĐỊNH LUẬT VÀNG CỦA KỊCH BẢN ĐOẢN VĂN VIRAL TRUNG QUỐC")
    lines.append("")
    lines.append("Qua việc rà soát và mổ xẻ cấu trúc tự sự của hơn 100 tác phẩm đoản văn triệu view tại Trung Quốc, chúng tôi đúc kết 10 nguyên lý tối cao quyết định sự bùng nổ của một câu chuyện ngắn:")
    lines.append("")
    lines.append("### 1. Định Luật Mở Màn 'In Medias Res' (Golden Retention Hook 5 Giây)")
    lines.append("- **Bản chất:** Tuyệt đối không bắt đầu bằng lời giới thiệu tuổi tác, lai lịch nhân vật hay tả thời tiết (Zero-Biography). Bắt đầu trực tiếp tại tâm chấn của một biến cố nghịch lý hoặc một câu thoại áp chế.")
    lines.append("- **Công thức toán học:** `Hook = [Xung đột cực độ] + [Người thân phản trắc / Biến cố sinh tử] + [Nghịch lý nhận thức]`.")
    lines.append("- **Ví dụ:** Thay vì *'Tôi là Thẩm Mạn, năm nay 25 tuổi và là vợ của tổng tài Lục Diễm'*, kịch bản mở màn: *'Cầm ly rượu vang đỏ chuẩn bị hắt vào mặt nữ chính theo kịch bản ngược văn, tôi bỗng dừng lại khi nhìn thấy số dư tài khoản 500 nghìn tỷ của mình'*.")
    lines.append("")
    lines.append("### 2. Định Luật Nén Áp Suất & Giải Phóng Cảm Xúc (Suppression & Catharsis)")
    lines.append("- **Cơ chế lò xo:** Khán giả chỉ cảm thấy 'sướng' (sảng văn) khi mức độ ức chế (suppression) trước đó được nén đủ sâu.")
    lines.append("- **Quy tắc 300 từ:** Cứ mỗi 300 từ phải có một vi-xung đột (micro-conflict) làm đối phương lấn tới và nhân vật chính nén lại một bậc.")
    lines.append("- **Thời điểm xả van:** Không xả van nửa vời; thời điểm bùng nổ phải là lúc phản diện đang đắc thắng và ngạo mạn nhất.")
    lines.append("")
    lines.append("### 3. Định Luật Khẩu Súng Của Chekhov (Chekhov's Gun - 草蛇灰线)")
    lines.append("- **Bản chất:** Mọi chi tiết, đồ vật, thói quen xuất hiện tưởng chừng vô hại ở Hồi 1 đều phải trở thành 'chốt hạ đoạt mạng' ở Hồi 3.")
    lines.append("- **Ví dụ:** Vết son trên áo, chiếc bánh bao hoa hồng, thói quen dị ứng đậu phộng, một chiếc usb cũ hay một biên lai chuyển tiền.")
    lines.append("")
    lines.append("### 4. Định Luật Tương Phản Nhân Vật Cực Đoan (Extreme Archetype Contrast)")
    lines.append("- Đặt hai nhân vật có sự tương phản mãnh liệt bên cạnh nhau:")
    lines.append("  * Vị tổng tài lạnh lùng tàn nhẫn vs Cô vợ thực dụng chỉ quan tâm đến lương tháng.")
    lines.append("  * Nàng dâu có bằng kiểm toán và luật sư vs Bà mẹ chồng dùng gia quy hủ bại.")
    lines.append("  * Chú mèo quýt béo ú kêu 'meo meo' vs Tiếng lòng của một ông trùm giang hồ.")
    lines.append("")
    lines.append("### 5. Định Luật Phản Sáo Lộ & Nghịch Chuyển Kỳ Vọng (Subverting Tropes)")
    lines.append("- Khi khán giả nghĩ câu chuyện sẽ đi theo lối mòn A (ngược đãi khóc lóc $\\rightarrow$ tha thứ), kịch bản đột ngột rẽ sang hướng B (rút đoản đao rạch mặt $\\rightarrow$ bỏ đi làm giàu $\\rightarrow$ không bao giờ quay đầu).")
    lines.append("- Sự ngỡ ngàng (surprise) là chất kích thích dopamine mạnh nhất giữ chân người nghe.")
    lines.append("")
    lines.append("### 6. Định Luật Tiết Tấu Câu Ngắn (Punchy Pacing & Cadence)")
    lines.append("- Ở tốc độ nghe 1.5x (346 từ/phút), câu văn dài 35-50 từ sẽ làm người nghe nghẹt thở.")
    lines.append("- Mỗi câu chỉ dài 10 - 20 từ. Dùng dấu phẩy `,` ngắt nhịp thở và dấu ba chấm `...` tạo khoảng lặng kịch tính trước các từ khóa quan trọng.")
    lines.append("")
    lines.append("### 7. Định Luật Show, Don't Tell (Hành Động Hóa Trạng Thái)")
    lines.append("- Không viết: *'Cô ấy rất tức giận và đau lòng'*.")
    lines.append("- Viết: *'Bàn tay tôi run lên, chiếc nhẫn cưới trượt khỏi ngón tay rơi xuống ly rượu vang đỏ kêu 'keng' một tiếng đanh gọn'*.")
    lines.append("")
    lines.append("### 8. Định Luật Đảo Chiều Đa Tầng (Multi-Layered Plot Twist)")
    lines.append("- Twist 1 (Bề mặt): Phản diện bị vả mặt.")
    lines.append("- Twist 2 (Nguyên nhân): Phơi bày âm mưu thực sự đằng sau.")
    lines.append("- Twist 3 (Dư âm): Động cơ thực sự của người hy sinh hoặc bản án lương tâm suốt đời.")
    lines.append("")
    lines.append("### 9. Định Luật Trả Thù Bằng Sự Nghiệp & Sự Tự Do (Sober Autonomy)")
    lines.append("- Độc giả thế hệ mới không còn hứng thú với việc nhân vật chính tranh giành đàn ông. Họ hả dạ nhất khi nhân vật chính độc lập tài chính, sở hữu sự nghiệp rực rỡ và coi kẻ phản bội như rác rưởi không đáng bận tâm.")
    lines.append("")
    lines.append("### 10. Định Luật Cliffhanger Điểm Rơi Nghẹt Thở")
    lines.append("- Cuối mỗi phần (Part 1, Part 2), không dừng lại khi câu chuyện đã giải quyết xong; dừng lại đúng 0.5 giây trước khi bí mật động trời được xé toạc.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN II: CHI TIẾT 100 BỘ TRUYỆN NGẮN KINH ĐIỂN & ĐÚC KẾT KINH NGHIỆM BIÊN KỊCH")
    lines.append("")

    total_count = 0
    for group_name, stories in GENRE_GROUPS:
        lines.append(f"### {group_name}")
        lines.append("")
        for story in stories:
            total_count += 1
            s_id = story["id"]
            title_vn = story["title_vn"]
            title_cn = story["title_cn"]
            author = story["author_platform"]
            genre = story["genre"]
            premise = story["premise"]
            characters = story["characters"]
            hook = story["golden_hook"]
            acts = story["acts_and_pacing"]
            twist = story["plot_twist"]
            lessons = story["core_lessons"]

            lines.append(f"#### Tác phẩm {s_id}: 《{title_vn}》( {title_cn} )")
            lines.append(f"- **Tác giả & Nền tảng:** {author}")
            lines.append(f"- **Thể loại:** {genre}")
            lines.append(f"- **Tiền đề & Bối cảnh cốt truyện (Premise):** {premise}")
            lines.append("- **Thiết lập & Tạo hình nhân vật (Character Dynamics):**")
            for char_line in characters.split("\n"):
                if char_line.strip():
                    lines.append(f"  {char_line}")
            lines.append(f"- **Golden Retention Hook (Mở màn 5s):** {hook}")
            lines.append("- **Cấu trúc 3 Hồi & Nhịp điệu (Acts & Pacing):**")
            for act_line in acts.split("\n"):
                if act_line.strip():
                    lines.append(f"  {act_line}")
            lines.append(f"- **Điểm xoay chuyển & Kết cục (Plot Twist):** {twist}")
            lines.append("- **Tinh hoa & Bài học biên kịch đúc kết:**")
            for lesson_line in lessons.split("\n"):
                if lesson_line.strip():
                    lines.append(f"  {lesson_line}")
            lines.append("")
            lines.append("---")
            lines.append("")

    lines.append("## PHẦN III: BỘ QUY CHUẨN KỊCH BẢN CHO HỆ THỐNG AUDIO/VIDEO 30 PHÚT (TỐC ĐỘ ĐỌC 1.5X CHUẨN GEMINI.MD)")
    lines.append("")
    lines.append("Dựa trên 100 tác phẩm kinh điển trên, chúng tôi thiết lập Ma trận chuẩn hóa kịch bản áp dụng tự động cho Agent 2 (Biên kịch) trong dây chuyền sản xuất của xưởng:")
    lines.append("")
    lines.append("### 1. Ma Trận Dung Lượng & Thời Lượng (Chuẩn Tốc Độ Đọc 1.5x FFmpeg `atempo=1.5`)")
    lines.append("- Tốc độ đọc thực tế của giọng Edge-TTS (Nam Minh / Hoài My) ở 1.5x: **346 từ / phút**.")
    lines.append("- Định mức cho video đơn tập 30 phút: **>= 10,380 từ** (chuẩn 10,440 - 10,500 từ).")
    lines.append("- Định mức cho series 3 tập (TikTok/Douyin): **>= 3,460 từ / tập** (Tổng >= 10,380 từ).")
    lines.append("")
    lines.append("### 2. Quy Chuẩn Phân Bổ 3 Hồi Cho Kịch Bản 3 Tập")
    lines.append("")
    lines.append("| Tập | Thời lượng Audio (1.5x) | Dung lượng từ | Nhiệm vụ kịch bản cốt lõi | Điểm kết thúc (Ending) |")
    lines.append("| :---: | :---: | :---: | :--- | :--- |")
    lines.append("| **Tập 1** | **>= 10 phút** | **>= 3,460 từ** | Hook 5s ném vào xung đột $\\rightarrow$ Giới thiệu bối cảnh qua hành động $\\rightarrow$ Cài cắm súng Chekhov $\\rightarrow$ Nén ức chế bậc 1. | **Cliffhanger 1:** Phát hiện bí mật chấn động hoặc đối phương ra đòn hiểm độc. |")
    lines.append("| **Tập 2** | **>= 10 phút** | **>= 3,460 từ** | Nối tiếp tự nhiên (Zero recap) $\\rightarrow$ Leo thang xung đột $\\rightarrow$ Phản đòn ngầm $\\rightarrow$ Dồn nhân vật chính vào đường cùng. | **Cliffhanger 2:** Bẫy chuẩn bị sập hoặc sự thật tầng 1 hé lộ. |")
    lines.append("| **Tập 3** | **>= 10 phút** | **>= 3,460 từ** | Đại đối đầu trực diện $\\rightarrow$ Tháo ngòi toàn bộ Chekhov's gun $\\rightarrow$ Vả mặt triệt để / Hỏa táng tràng $\\rightarrow$ Dư âm nhân văn. | **Comment Trigger:** Câu hỏi phân cực kích hoạt bình luận tranh luận. |")
    lines.append("")
    lines.append("### 3. Phân Định Giọng Đọc Độc Quyền Theo Thể Loại (Zero Voice Mixing)")
    lines.append("- **Nam Minh (`vi-VN-NamMinhNeural`)**: Chỉ định cho Huyền nghi trinh thám, Vô hạn lưu, Mạt thế, Án mạng High-IQ, Tổng tài quyền mưu.")
    lines.append("- **Hoài My (`vi-VN-HoaiMyNeural`)**: Chỉ định cho Ngược luyến tàn tâm, Trọng sinh báo thù nữ cường, Mẹ chồng nàng dâu, Chữa lành thanh xuân, Sa điêu tấu hài.")
    lines.append("- **Tuyệt đối cấm gTTS fallback**: 100% sử dụng duy nhất một chất giọng xuyên suốt toàn bộ tác phẩm.")
    lines.append("")
    lines.append("### 4. Quy Chuẩn Video & Thumbnail (Bảo Toàn 16:9 Gốc)")
    lines.append("- **Video nền:** Giữ nguyên tỷ lệ 16:9 widescreen gốc (1920x1080), cắt phân đoạn slice có IDR Keyframe ở $t=0$, BGM melodious -13 LUFS.")
    lines.append("- **Thumbnail:** Sinh ảnh bìa 1080p có typography ấn tượng, trích xuất câu thoại đắt giá nhất của từng tập nhúng trực tiếp vào MP4.")
    lines.append("")
    lines.append("---")
    lines.append("*Tài liệu được tổng hợp và đúc kết bởi Hệ thống AI Tự Động Hóa Biên Kịch 10-Agent.*")

    content = "\n".join(lines)
    return content, total_count

def update_learned_patterns():
    pattern_file = root_dir / "data" / "learned_patterns.json"
    if not pattern_file.exists():
        data = {}
    else:
        with open(pattern_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception:
                data = {}

    data["chinese_storytelling_masterclass"] = {
        "status": "ACQUIRED_100_STORIES",
        "total_stories_analyzed": 100,
        "genres_covered": [
            "Ngược Luyến Tàn Tâm & Hỏa Táng Tràng Truy Thê",
            "Trọng Sinh Báo Thù & Vả Mặt Sảng Văn",
            "Huyền Nghi, Trinh Thám & High-IQ Án Mạng",
            "Mẹ Chồng Nàng Dâu & Hiện Thực Hôn Nhân",
            "Hào Môn Tổng Tài & Khế Ước Hôn Nhân",
            "Kinh Dị Đô Thị & Quy Tắc Quái Đàm",
            "Sa Điêu Hài Hước & Đọc Suy Nghĩ",
            "Cung Đấu & Nữ Quyền Cổ Đại",
            "Cứu Rỗi, Chữa Lành & Thanh Xuân Học Đường",
            "Vô Hạn Lưu & Mạt Thế Sinh Tồn"
        ],
        "top_10_golden_rules": [
            "In Medias Res (Golden Retention Hook 5s)",
            "Suppression & Catharsis (Pressure Building & Release)",
            "Chekhov's Gun (Hidden Clues in Act 1 exploded in Act 3)",
            "Extreme Archetype Contrast",
            "Subverting Tropes (Anti-trope surprise)",
            "Punchy Pacing & Cadence (10-20 words per sentence at 1.5x)",
            "Show, Don't Tell (Actionized states)",
            "Multi-Layered Plot Twist (Surface -> Deep Motive -> Echo)",
            "Sober Autonomy (Career & self-worth over romantic begging)",
            "Mid-point Cliffhangers (Cut 0.5s before resolution)"
        ],
        "audio_pacing_at_1_5x": {
            "speed_multiplier": 1.5,
            "words_per_minute": 346,
            "min_words_per_30m": 10380,
            "standard_words_per_part": 3480
        }
    }

    with open(pattern_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {pattern_file} successfully.")

def main():
    print("Building comprehensive master handbook...")
    content, total_count = build_markdown()
    target_path = root_dir / "docs" / "CAM_NANG_100_KICH_BAN_TRUYEN_NGAN_TRUNG_QUOC.md"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    sys.stdout.reconfigure(encoding="utf-8")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated handbook with {total_count} stories ({len(content)} characters, {len(content.splitlines())} lines).")
    update_learned_patterns()

if __name__ == "__main__":
    main()
