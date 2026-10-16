# -*- coding: utf-8 -*-
"""
Script: scripts/build_genre_handbooks.py
Purpose: Export individual in-depth genre breakdown files to docs/kinh_nghiem_chi_tiet/
and create docs/SO_TAY_BIEN_KICH_TRIEU_VIEW_DOUYIN_ZHIHU.md
"""

import sys
import os
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

def build_individual_genre_files():
    out_dir = root_dir / "docs" / "kinh_nghiem_chi_tiet"
    out_dir.mkdir(parents=True, exist_ok=True)

    genres_info = [
        ("01_Kinh_Nghiem_Nguoc_Luyen_Tan_Tam.md", "I. NGƯỢC LUYẾN TÀN TÂM & HỎA TÁNG TRÀNG TRUY THÊ", STORIES_GENRE_1, "Khai thác nỗi đau từ sự vô tâm, hiểu lầm, thế thân và đỉnh điểm là sự ra đi vĩnh viễn của nhân vật chính để kẻ bội bạc dằn vặt suốt đời."),
        ("02_Kinh_Nghiem_Trong_Sinh_Va_Mat.md", "II. TRỌNG SINH BÁO THÙ & VẢ MẶT SẢNG VĂN", STORIES_GENRE_2, "Kiếp trước bi thảm, kiếp này tỉnh táo nắm bắt tương lai, bóc trần bộ mặt đạo đức giả và vả mặt triệt để."),
        ("03_Kinh_Nghiem_Huyen_Nghi_Trinh_Tham.md", "III. HUYỀN NGHI, TRINH THÁM & HIGH-IQ ÁN MẠNG", STORIES_GENRE_3, "Án mạng hóc búa, suy luận logic sắc bén, đa tầng sự thật (multi-layered twists) và cài cắm súng Chekhov hoàn hảo."),
        ("04_Kinh_Nghiem_Me_Chong_Gia_Dinh_Cuc_Pham.md", "IV. MẸ CHỒNG NÀNG DÂU & GIA ĐÌNH CỰC PHẨM", STORIES_GENRE_4, "Hiện thực hôn nhân khốc liệt, mâu thuẫn tiền bạc tài sản, mẹ chồng hủ bại và màn đáp trả sắc sảo bảo vệ bản thân."),
        ("05_Kinh_Nghiem_Hao_Mon_Tong_Tai_Khe_Uoc.md", "V. HÀO MÔN TỔNG TÀI & CƯỚI TRƯỚC YÊU SAU", STORIES_GENRE_5, "Hợp đồng hôn nhân, tình cảm ngọt ngào đan xen đấu trí thương trường, che chở thiên vị độc tôn và phá tan định kiến."),
        ("06_Kinh_Nghiem_Kinh_Di_Quy_Tac_Quai_Dam.md", "VI. KINH DỊ ĐÔ THỊ & QUY TẮC QUÁI ĐÀM", STORIES_GENRE_6, "Không khí nghẹt thở, những quy tắc sinh tồn bí ẩn mâu thuẫn và sự thử thách ranh giới nhân tính giữa sinh tử."),
        ("07_Kinh_Nghiem_Sa_Dieu_Hai_Huoc_Phan_Sao_Lo.md", "VII. SA ĐIÊU HÀI HƯỚC & PHẢN SÁO LỘ", STORIES_GENRE_7, "Bẻ gãy mọi khuôn mẫu sáo rỗng (anti-trope), đọc suy nghĩ tấu hài, tư duy ngược đời mang lại tiếng cười và sự sảng khoái."),
        ("08_Kinh_Nghiem_Cung_Dau_Trach_Dau_Nu_Quyen.md", "VIII. CUNG ĐẤU, TRẠCH ĐẤU & NỮ QUYỀN CỔ ĐẠI", STORIES_GENRE_8, "Trí tuệ sinh tồn chốn cung đình phủ trạch, nữ quyền thức tỉnh, trọng sự nghiệp độc lập hơn tình yêu hư ảo."),
        ("09_Kinh_Nghiem_Cuu_Roi_Chua_Lanh_Thanh_Xuan.md", "IX. CỨU RỖI, CHỮA LÀNH & THANH XUÂN HỌC ĐƯỜNG", STORIES_GENRE_9, "Chữa lành vết thương tâm hồn, tình cảm trong sáng thuở thiếu thời và sức mạnh vượt qua bóng tối nghịch cảnh."),
        ("10_Kinh_Nghiem_Vo_Han_Luu_Mat_The_Sinh_Ton.md", "X. VÔ HẠN LƯU, MẠT THẾ SINH TỒN & KHOA HUYỄN", STORIES_GENRE_10, "Tích trữ tài nguyên ngày tận thế, phó bản sinh tồn vô hạn, quy luật đào thải tàn khốc và trí tuệ sinh tồn thực dụng.")
    ]

    for filename, title, stories, desc in genres_info:
        filepath = out_dir / filename
        lines = []
        lines.append(f"# ĐÚC KẾT KINH NGHIỆM BIÊN KỊCH CHUYÊN SÂU: {title}")
        lines.append(f"**Đặc trưng thể loại:** {desc}\n")
        lines.append("> [!NOTE]")
        lines.append(f"> File tài liệu này phân tích chi tiết 10 bộ truyện nổi tiếng nhất thuộc nhóm {title}, đúc kết tinh hoa kịch bản, nghệ thuật xây dựng nhân vật, bối cảnh, cú hook và kỹ thuật đảo chiều cốt truyện.\n")
        lines.append("---")
        lines.append("\n## MỤC LỤC CÁC TÁC PHẨM TRONG THỂ LOẠI\n")
        for s in stories:
            lines.append(f"- **Tác phẩm {s['id']}:** 《{s['title_vn']}》( {s['title_cn']} ) - *{s['genre']}*")
        lines.append("\n---\n")

        for s in stories:
            s_id = s['id']
            lines.append(f"## Tác phẩm {s_id}: 《{s['title_vn']}》( {s['title_cn']} )")
            lines.append(f"- **Tác giả & Nền tảng:** {s['author_platform']}")
            lines.append(f"- **Thể loại chi tiết:** {s['genre']}")
            lines.append(f"- **Tiền đề & Bối cảnh cốt truyện (Premise & Setting):**\n  {s['premise']}\n")
            lines.append("- **Thiết lập & Tạo hình nhân vật (Character Dynamics & Arcs):**")
            for c in s['characters'].split('\n'):
                if c.strip():
                    lines.append(f"  {c}")
            lines.append(f"\n- **Golden Retention Hook (Mở màn 5s giữ chân độc giả):**\n  > \"{s['golden_hook']}\"\n")
            lines.append("- **Cấu trúc 3 Hồi & Nhịp điệu kịch tính (Acts & Pacing Beat-Sheet):**")
            for act in s['acts_and_pacing'].split('\n'):
                if act.strip():
                    lines.append(f"  {act}")
            lines.append(f"\n- **Điểm xoay chuyển cốt truyện & Đại kết cục (Plot Twist & Climax):**\n  {s['plot_twist']}\n")
            lines.append("- **Tinh hoa nghệ thuật & Bài học biên kịch đúc kết:**")
            for l in s['core_lessons'].split('\n'):
                if l.strip():
                    lines.append(f"  {l}")
            lines.append("\n---\n")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Generated {filename} ({len(stories)} stories)")

def build_master_playbook():
    playbook_path = root_dir / "docs" / "SO_TAY_BIEN_KICH_TRIEU_VIEW_DOUYIN_ZHIHU.md"
    lines = []
    lines.append("# SỔ TAY BIÊN KỊCH TRIỆU VIEW (ZHIHU YANXUAN & DOUYIN SHORT DRAMA)")
    lines.append("## Đúc Kết Tinh Hoa 100 Bộ Đoản Văn & Ma Trận Biên Kịch Đỉnh Cao Cho Hệ Thống Video/Audio Tự Động")
    lines.append("")
    lines.append("> [!IMPORTANT]")
    lines.append("> **Giá trị cốt lõi:** Tài liệu này đúc kết toàn bộ phương pháp luận viết kịch bản truyện ngắn/đoản văn từ hơn 100 bộ truyện triệu view trên các nền tảng hàng đầu Trung Quốc (Zhihu Muối Tuyển, Douyin Short Drama, Fanqie, Jinjiang, Qidian). Kết hợp mô hình Kinh tế học Bất đối xứng Thông tin (Information Asymmetry), Quy luật 3 giây đầu, Nhịp 15 giây, Điểm nén ức chế & Xả van Dopamine để tạo ra những kịch bản giữ chân người xem đến giây cuối cùng.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN I: 4 NGUYÊN LÝ TÂM LÝ HỌC ĐỘC GIẢ & MÔ HÌNH THÔNG TIN")
    lines.append("")
    lines.append("### 1. Mô Hình 4 Tầng Bất Đối Xứng Thông Tin (Information Asymmetry Economics)")
    lines.append("Kịch bản xuất sắc không nằm ở câu chữ bay bướm, mà nằm ở việc điều khiển dòng chảy thông tin giữa 4 tầng nhận thức:")
    lines.append("- **Tầng 1 - Sự thật khách quan (Objective Facts):** Điều thực sự đã diễn ra trong thế giới truyện.")
    lines.append("- **Tầng 2 - Lời người kể chuyện (Narrator Layer):** Điều nhân vật xưng 'Tôi' hoặc người dẫn chuyện muốn khán giả tin (có thể là người kể chuyện không đáng tin cậy - Unreliable Narrator).")
    lines.append("- **Tầng 3 - Góc nhìn các nhân vật (Character Layer):** Mỗi nhân vật trong truyện chỉ nắm một mảnh ghép giới hạn.")
    lines.append("- **Tầng 4 - Góc nhìn khán giả (Audience Layer):** Khán giả xâu chuỗi thông tin dựa trên dữ kiện được cung cấp.")
    lines.append("")
    lines.append("#### 3 Cơ Chế Tạo Cảm Xúc Bằng Khoảng Cách Thông Tin:")
    lines.append("1. **Khán giả biết > Nhân vật biết:** Tạo cảm giác **Lo âu & Nghẹt thở** (*'Đừng mở cánh cửa đó!'*, *'Người đứng sau lưng cô ta chính là kẻ sát nhân!'*).")
    lines.append("2. **Nhân vật biết > Khán giả biết:** Tạo cảm giác **Tò mò & Động cơ bí ẩn** (*'Tại sao một tổng tài lại chịu quỳ trước người giao hàng?'*, *'Bức thư trong gối rốt cuộc ghi điều gì?'*).")
    lines.append("3. **Người kể chuyện lừa Khán giả:** Tạo cảm giác **Kinh ngạc cực độ (Mind-blowing Twist)** (*'Hóa ra bác sĩ tâm lý mới chính là kẻ sát nhân nhân cách thứ hai!'*).")
    lines.append("")
    lines.append("### 2. Hiệu Ứng Zeigarnik & Vòng Lặp Dopamine")
    lines.append("- Bộ não con người luôn khó chịu trước một cấu trúc chưa hoàn thiện (Unclosed Loop).")
    lines.append("- **Quy tắc 600 từ / 15 giây:** Cứ mỗi 600 từ (trong văn bản) hoặc 15 giây (trong video/audio), phải ném ra một chi tiết bất thường mới hoặc làm sâu sắc thêm mâu thuẫn để đóng vòng lặp cũ và lập tức mở ra vòng lặp mới.")
    lines.append("")
    lines.append("### 3. Tâm Lý Học Độc Giả Thế Hệ Mới (Reality Resonance & Sober Protagonist)")
    lines.append("- **90%+ độc giả đoản văn Zhihu & Douyin là nữ giới (20 - 35 tuổi).**")
    lines.append("- Họ bài trừ tuyệt đối: Nữ chính yếu đuối khóc lóc (bạch liên hoa), 'Luyến ái não' (coi tình yêu là tất cả), tha thứ mù quáng cho tra nam.")
    lines.append("- Họ khao khát: Nữ chính lý tính, thông minh, độc lập tài chính, bảo vệ người thân, và coi kẻ bội bạc là rác rưởi không đáng lưu tâm.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN II: 5 CỘT TRỤ VÀNG TRONG THIẾT KẾ KỊCH BẢN TRIỆU VIEW")
    lines.append("")
    lines.append("### 1. Golden Hook 3-5 Giây Đầu Tiên (Quy Tắc Sống Còn)")
    lines.append("- **Tối kỵ:** Tuyệt đối không mở màn bằng lý lịch, giới thiệu thời tiết, hoàn cảnh gia thế dài dòng.")
    lines.append("- **Quy tắc Động từ + Hiện trường tức thì (Immediate Action & Scene):**")
    lines.append("  * *Yếu:* 'Tôi và anh ấy cưới nhau được 5 năm, cuộc sống vốn rất bình yên.'")
    lines.append("  * *Mạnh:* 'Cú búa đầu tiên của thợ đập vỡ lớp gạch men phòng tắm, làm rơi ra một chiếc vòng tay của người đã mất tích 3 năm trước.'")
    lines.append("- **4 Công Thức Mở Màn Bất Bại:**")
    lines.append("  1. **Xung đột tiền trí (Conflict Frontloaded):** Mở đầu bằng một cái tát, một bản hợp đồng ly hôn ném vào mặt, hoặc một vụ kiện tụng.")
    lines.append("  2. **Nghịch lý nhận thức (Paradoxical Hook):** 'Là bác sĩ pháp y danh tiếng nhất thành phố, hôm nay tôi phải tự tay giải phẫu cho thi thể của chính mình.'")
    lines.append("  3. **Kết quả cực đoan đảo ngược (Extreme Result Inversion):** 'Vào ngày tôi qua đời vì ung thư giai đoạn cuối, chồng tôi đang chi 50 tỷ mua một hòn đảo để mừng sinh nhật bạch nguyệt quang.'")
    lines.append("  4. **Quy tắc cấm kỵ (Taboo Violation):** 'Bệnh viện có một quy định nghiêm ngặt: Tuyệt đối không được nhìn vào gương sau 12 giờ đêm.'")
    lines.append("")
    lines.append("### 2. Cơ Chế Nén Áp Suất & Điểm Sảng (Suppression & Shuangdian)")
    lines.append("- Khán giả chỉ cảm thấy 'ĐÃ' khi mức độ uất ức được đẩy lên tột độ.")
    lines.append("- **Quy tắc bậc thang uất ức:** Phản diện phải liên tục lấn tới, chiếm đoạt công lao, sỉ nhục, dồn ép nhân vật chính vào chân tường.")
    lines.append("- **Thời điểm xả van:** Không phản đòn lắt nhắt; gom toàn bộ chứng cứ và bùng nổ tại thời khắc phản diện đang huy hoàng và ngạo mạn nhất (lễ đính hôn, đại hội cổ đông, tiệc mừng thăng chức).")
    lines.append("")
    lines.append("### 3. Kỹ Thuật Khẩu Súng Của Chekhov (Chekhov's Gun - 草蛇灰线)")
    lines.append("- Mọi đồ vật, câu thoại, thói quen xuất hiện tưởng như vô tình ở Tập 1 đều phải quay trở lại thành bằng chứng đoạt mạng hoặc chìa khóa lật kèo ở Tập 3.")
    lines.append("- Ví dụ: Một vết ố vàng trên cà vạt, chiếc bánh ngọt hương hạnh nhân, thói quen thuận tay trái, hay một chiếc camera hành trình cũ.")
    lines.append("")
    lines.append("### 4. Nghệ Thuật Đảo Chiều Đa Tầng (Multi-Layered Twists)")
    lines.append("- **Twist Cấp 1 (Bề mặt):** Kẻ ác bị lật tẩy và trừng phạt.")
    lines.append("- **Twist Cấp 2 (Động cơ sâu kín):** Hóa ra kẻ ác cũng chỉ là con cờ trong một kế hoạch lớn hơn.")
    lines.append("- **Twist Cấp 3 (Dư âm lạnh gáy / Cảm động):** Sự hy sinh thầm lặng của người thân hoặc một sự thật khiến độc giả 'ngẫm lại mà kinh hãi' (细思极恐).")
    lines.append("")
    lines.append("### 5. Kỹ Thuật Cắt Điểm Rơi Nghẹt Thở (Cliffhanger / 卡点)")
    lines.append("- Cuối mỗi tập (Tập 1, Tập 2), cắt đúng 0.5 giây trước khi lời giải đáp được thốt ra.")
    lines.append("- *Ví dụ:* 'Tôi bấm nút mở chiếc file ghi âm bí mật của bố chồng... Giọng nói run rẩy của ông vang lên: Thủ phạm năm đó thực ra là...' $\\rightarrow$ **HẾT TẬP 1**.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN III: MA TRẬN 10 THỂ LOẠI ĐOẢN VĂN & CÔNG THỨC THỰC CHIẾN")
    lines.append("")
    lines.append("| STT | Thể loại | Cảm xúc chủ đạo | Công thức cốt lõi | Chiêu thức vả mặt / Twist đỉnh cao |")
    lines.append("| :---: | :--- | :--- | :--- | :--- |")
    lines.append("| 1 | **Ngược Luyến Tàn Tâm** | Day dứt, đau đớn, hối hận muộn màng | Nhẫn nhịn $\\rightarrow$ Rời đi vĩnh viễn / Chết $\\rightarrow$ Tra nam hỏa táng tràng phát điên | Nữ chính buông bỏ hoàn toàn, nam chính ôm di vật sống cô độc suốt phần đời còn lại. |")
    lines.append("| 2 | **Trọng Sinh Vả Mặt** | Sảng khoái, hả hê, công lý được thực thi | Kiếp trước bị hại thảm $\\rightarrow$ Trọng sinh biết trước thời cơ $\\rightarrow$ Đặt bẫy gậy ông đập lưng ông | Tương kế tựu kế, để phản diện tự rơi vào chính cái bẫy chúng đào ra. |")
    lines.append("| 3 | **Huyền Nghi Trinh Thám** | Hồi hộp, tò mò, trí tuệ High-IQ | Án mạng bí ẩn $\\rightarrow$ Manh mối Chekhov $\\rightarrow$ Lật ngược lời khai $\\rightarrow$ Chân tướng kinh hoàng | Kẻ báo án hoặc người thân thiết nhất chính là chủ mưu. |")
    lines.append("| 4 | **Mẹ Chồng Nàng Dâu** | Ức chế hiện thực $\\rightarrow$ Hả dạ giải thoát | Mẹ chồng chèn ép $\\rightarrow$ Chồng nhu nhược đùn đẩy $\\rightarrow$ Nàng dâu dùng pháp lý và tài chính thanh trừng | Tách biệt tài sản, mua nhà đứng tên riêng, để gia đình cực phẩm tự cắn xé nhau. |")
    lines.append("| 5 | **Hào Môn Khế Ước** | Ngọt ngào, tự tôn, an tâm tuyệt đối | Cưới trước yêu sau $\\rightarrow$ Thử thách môn đăng hộ đối $\\rightarrow$ Bảo vệ độc tôn | Tổng tài lạnh lùng với cả thế giới nhưng thiên vị bảo vệ nữ chính vô điều kiện. |")
    lines.append("| 6 | **Kinh Dị Quái Đàm** | Rùng rợn, ngột ngạt, sinh tồn | Quy tắc mâu thuẫn $\\rightarrow$ Phân biệt thật giả $\\rightarrow$ Thoát hiểm trong gang tấc | Nhận ra quy tắc an toàn nhất chính là cái bẫy chết người nhất. |")
    lines.append("| 7 | **Sa Điêu Phản Sáo Lộ** | Hài hước, sảng khoái, bất ngờ | Đọc suy nghĩ / Hệ thống lỗi $\\rightarrow$ Hành xử ngược đời $\\rightarrow$ Phản diện sụp đổ nhân sinh quan | Nữ chính nghĩ một đằng làm một nẻo khiến nam chính lạnh lùng bối rối bật cười. |")
    lines.append("| 8 | **Cung Đấu Nữ Quyền** | Tỉnh táo, sắc sảo, đại cục | Không tranh sủng $\\rightarrow$ Nắm giữ thực quyền / Tài chính $\\rightarrow$ Trở thành người chi phối hậu đình | Phi tần bắt tay nhau làm kinh tế và nuôi dạy hoàng tử, hoàng đế thành công cụ. |")
    lines.append("| 9 | **Cứu Rỗi Chữa Lành** | Xúc động, ấm áp, nhân văn | Vết thương quá khứ $\\rightarrow$ Sự kiên nhẫn dịu dàng $\\rightarrow$ Cùng nhau bước ra ánh sáng | Tình yêu chân thành trở thành điểm tựa giúp nhau vượt qua bóng đen trầm cảm. |")
    lines.append("| 10 | **Vô Hạn Mạt Thế** | Phấn khích tích trữ, kích thích sinh tồn | Thảm họa ập đến $\\rightarrow$ Không gian tích trữ tài nguyên $\\rightarrow$ Xây dựng pháo đài an toàn | Trong khi kẻ ác đói rét cầu xin, nhân vật chính ung dung thưởng thức lẩu nóng. |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## PHẦN IV: QUY CHUẨN KỊCH BẢN CHO HỆ THỐNG SẢN XUẤT AUDIO/VIDEO 30 PHÚT")
    lines.append("")
    lines.append("1. **Định mức câu và từ ngữ:**")
    lines.append("   - Câu đơn 10 - 20 từ. Ngắt nhịp thở bằng dấu phẩy `,` và dấu ba chấm `...` tạo điểm nhấn cảm xúc.")
    lines.append("   - Tốc độ đọc 1.5x (atempo=1.5): **346 từ / phút**.")
    lines.append("   - Tổng dung lượng bộ 3 tập: **>= 10,400 từ** (~3,480 từ / tập).")
    lines.append("2. **Đồng nhất giọng đọc Neural Speech (Zero Voice Mixing):**")
    lines.append("   - Giọng Nam (`vi-VN-NamMinhNeural`): Trinh thám, Kinh dị, Mạt thế, Vô hạn lưu.")
    lines.append("   - Giọng Nữ (`vi-VN-HoaiMyNeural`): Ngược tâm, Trọng sinh, Mẹ chồng nàng dâu, Chữa lành, Hào môn.")
    lines.append("3. **Visual & BGM Sync:**")
    lines.append("   - Background Widescreen 16:9 với các chủ đề ASMR (làm bánh, đồ gốm, cảnh rừng mưa) giúp mắt thư giãn.")
    lines.append("   - Nhạc nền không lời (Piano Lofi / Dark Suspense), Ducking -24dB so với giọng đọc.")
    lines.append("")
    lines.append("---")
    lines.append("*Biên soạn và đúc kết bởi Hệ thống AI Tự Động Hóa Biên Kịch 10-Agent.*")

    with open(playbook_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Generated {playbook_path} successfully.")

def main():
    print("Building individual genre handbooks and master playbook...")
    build_individual_genre_files()
    build_master_playbook()
    print("Done!")

if __name__ == "__main__":
    main()
