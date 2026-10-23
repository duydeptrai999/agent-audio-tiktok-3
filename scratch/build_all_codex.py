# -*- coding: utf-8 -*-
"""
scratch/build_all_codex.py
Biên dịch toàn bộ Đại Điển Tri Thức 100 Bộ Truyện Ngắn và đồng bộ hóa hệ thống.
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from genre_1_2 import GENRE_1_STORIES, GENRE_2_STORIES
from genre_3_4 import GENRE_3_STORIES, GENRE_4_STORIES
from genre_5_6 import GENRE_5_STORIES, GENRE_6_STORIES
from genre_7_8 import GENRE_7_STORIES, GENRE_8_STORIES
from genre_9_10 import GENRE_9_STORIES, GENRE_10_STORIES

GENRES_MAP = [
    {
        "index": 1,
        "name_vi": "NGƯỢC LUYẾN TÀN TÂM & HỎA TÁNG TRÀNG TRUY THÊ (虐恋残心 · 追妻火葬场)",
        "file_name": "01_Kinh_Nghiem_Nguoc_Luyen_Tan_Tam.md",
        "py_file": "genre1_nguoc_tam.py",
        "var_name": "STORIES_GENRE_1",
        "stories": GENRE_1_STORIES,
        "platform_desc": "Zhihu 盐选, Jinjiang (晋江文学城)",
        "axis": "Đau xót dằn vặt, hối hận muộn màng, giải thoát bi tráng, BE mỹ học"
    },
    {
        "index": 2,
        "name_vi": "TRỌNG SINH VẢ MẶT & THỨC TỈNH NỮ PHỤ / PHÁT ĐIÊN VĂN HỌC (重生打脸 · 恶毒女配觉醒 · 发疯文学)",
        "file_name": "02_Kinh_Nghiem_Trong_Sinh_Va_Mat.md",
        "py_file": "genre2_trong_sinh.py",
        "var_name": "STORIES_GENRE_2",
        "stories": GENRE_2_STORIES,
        "platform_desc": "Zhihu 盐言故事, Fanqie (番茄短篇), Douyin 短剧",
        "axis": "Hả hê sảng khoái, không nội hao, xé nát kịch bản, tự chủ kinh tế"
    },
    {
        "index": 3,
        "name_vi": "HUYỀN NGHI TRINH THÁM & HÌNH SỰ PHÁP Y / NGHẸT THỞ ĐA TẦNG BẺ LÁI (硬核悬疑 · 刑侦法医 · 极致反转)",
        "file_name": "03_Kinh_Nghiem_Huyen_Nghi_Trinh_Tham.md",
        "py_file": "genre3_huyen_nghi.py",
        "var_name": "STORIES_GENRE_3",
        "stories": GENRE_3_STORIES,
        "platform_desc": "Zhihu 盐选 (Chuyên mục Phá Án), Điện ảnh hóa",
        "axis": "Nghẹt thở, rùng mình lạnh gáy (细思极恐), đấu trí logic, công lý phục hồi"
    },
    {
        "index": 4,
        "name_vi": "GIA ĐẤU MẸ CHỒNG & CỰC PHẨM THÂN THÍCH / CẮT DÒNG TIỀN (家庭婆媳 · 极品亲戚 · 经济断供)",
        "file_name": "04_Kinh_Nghiem_Me_Chong_Gia_Dinh_Cuc_Pham.md",
        "py_file": "genre4_me_chong.py",
        "var_name": "STORIES_GENRE_4",
        "stories": GENRE_4_STORIES,
        "platform_desc": "Douyin 短剧 (Hiện tượng 1.4 tỷ view), Zhihu 盐选",
        "axis": "Ức chế đời thường, giải phóng bằng luật pháp và tài chính, bài trừ gia trưởng"
    },
    {
        "index": 5,
        "name_vi": "HÀO MÔN TỔNG TÀI & HỢP ĐỒNG HÔN NHÂN / THỢ SĂN & CON MỒI (豪门世家 · 契约婚姻 · 猎手博弈)",
        "file_name": "05_Kinh_Nghiem_Hao_Mon_Tong_Tai_Khe_Uoc.md",
        "py_file": "genre5_hao_mon.py",
        "var_name": "STORIES_GENRE_5",
        "stories": GENRE_5_STORIES,
        "platform_desc": "Zhihu 盐选, Fanqie, Jinjiang",
        "axis": "Thương chiến cá mập, tình cảm bình đẳng trí tuệ, bóc trần đạo đức giả"
    },
    {
        "index": 6,
        "name_vi": "KINH DỊ QUÁI ĐÀM & QUY TẮC SINH TỒN / TÂN QUÁI ĐÀM (规则怪谈 · 都市惊悚 · 克苏鲁收容)",
        "file_name": "06_Kinh_Nghiem_Kinh_Di_Quy_Tac_Quai_Dam.md",
        "py_file": "genre6_kinh_di.py",
        "var_name": "STORIES_GENRE_6",
        "stories": GENRE_6_STORIES,
        "platform_desc": "A Đảo, Zhihu 盐选, Toàn mạng bạo hồng",
        "axis": "Ô nhiễm nhận thức, quy tắc mâu thuẫn rợn gáy, sinh tồn bằng logic lạnh lùng"
    },
    {
        "index": 7,
        "name_vi": "SA ĐIÊU HÀI HƯỚC & PHẢN SÁO LỘ / TIẾNG LÒNG THẦN DỤ (沙雕反套路 · 读心术 · 脑洞逆袭)",
        "file_name": "07_Kinh_Nghiem_Sa_Dieu_Hai_Huoc_Phan_Sao_Lo.md",
        "py_file": "genre7_sa_dieu.py",
        "var_name": "STORIES_GENRE_7",
        "stories": GENRE_7_STORIES,
        "platform_desc": "Zhihu 盐言故事, Bilibili, Douyin",
        "axis": "Cười ra nước mắt, giải tỏa áp lực (No Overthinking), phản sáo lộ triệt để"
    },
    {
        "index": 8,
        "name_vi": "CUNG ĐẤU TRẠCH ĐẤU & ĐẠI NỮ CHỦ QUYỀN MƯU (大女主权谋 · 宫廷宅斗 · 颠覆封建)",
        "file_name": "08_Kinh_Nghiem_Cung_Dau_Trach_Dau_Nu_Quyen.md",
        "py_file": "genre8_cung_dau.py",
        "var_name": "STORIES_GENRE_8",
        "stories": GENRE_8_STORIES,
        "platform_desc": "Zhihu 盐言三绝 (听银, 照殿红, 相术师), Phim truyền hình",
        "axis": "Đại nữ chủ chưởng quyền, mưu lược giang sơn, kinh tế tiền tệ, bẻ gãy gông xiềng"
    },
    {
        "index": 9,
        "name_vi": "CỨU RỖI THANH XUÂN & CHỮA LÀNH TÌNH THÂN / DÂN TỤC CHÍ QUÁI (治愈救赎 · 亲情意难平 · 中式志怪)",
        "file_name": "09_Kinh_Nghiem_Cuu_Roi_Chua_Lanh_Thanh_Xuan.md",
        "py_file": "genre9_cuu_roi.py",
        "var_name": "STORIES_GENRE_9",
        "stories": GENRE_9_STORIES,
        "platform_desc": "Zhihu 盐言三绝 (鱼灯引魂记, 外婆的时光机), Douyin (逃出大英博物馆)",
        "axis": "Rơi nước mắt, ấm áp tình thân, mỹ học phương Đông, chữa lành tâm hồn"
    },
    {
        "index": 10,
        "name_vi": "VÔ HẠN LƯU & MẠT THẾ SINH TỒN / NIÊN ĐẠI NGHỊCH TẬP (无限流 · 末世基建 · 年代爽剧)",
        "file_name": "10_Kinh_Nghiem_Vo_Han_Luu_Mat_The_Sinh_Ton.md",
        "py_file": "genre10_vo_han.py",
        "var_name": "STORIES_GENRE_10",
        "stories": GENRE_10_STORIES,
        "platform_desc": "Fanqie (番茄短篇), Douyin 短剧 (我在八零年代当后妈), Phim 開端",
        "axis": "Khoái cảm tích trữ, sinh tồn cực hạn, làm giàu niên đại, vòng lặp định mệnh"
    }
]

def format_story_markdown(s):
    characters_str = "\n".join([f"  - {c}" for c in s['characters']])
    takeaways_str = "\n".join([f"  - {t}" for t in s['mastery_takeaways']])
    
    return f"""#### 📜 [{s['id']}/100] 《{s['title_vi']}》 ({s['title_cn']})
- **Tác giả & Nền tảng**: `{s['author']} - {s['platform']}`
- **Phân loại**: *{s['category']}*
- **Bối cảnh & Tiền đề kịch tính (Premise)**: {s['premise']}

**1. Thiết Lập & Xây Dựng Nhân Vật (Character Archetypes & Dynamics):**
{characters_str}

**2. Mở Đầu Audio 3 Giây Giữ Chân (The 3-Second Retention Hook):**
> ⚡ *'{s['hook_3s']}'*

**3. Cấu Trúc 3 Hồi & Nhịp Độ Micro-Pacing (Acts & Pacing):**
- {s['act_structure']['act_1']}
- {s['act_structure']['act_2']}
- {s['act_structure']['act_3']}

**4. Cú Twist Đa Tầng & Điểm Sảng Bùng Nổ (Satisfaction Peak & Plot Twist):**
💥 **{s['plot_twist']}**

**5. Tinh Hoa Đúc Kết & Bài Học Biên Kịch Audio TikTok (Master Scriptwriting Takeaways):**
{takeaways_str}

> [!TIP]
> **Ứng dụng thực chiến của bộ {s['id']}**: Khi sản xuất audio cho thể loại này, luôn neo đạo cụ vật lý chính vào phân đoạn mở màn và sử dụng đòn lật kèo logic, triệt tiêu hoàn toàn sáo ngữ kể lể.
"""

def generate_master_document():
    doc_lines = []
    
    # Header & Part I
    doc_lines.append("""# ĐẠI ĐIỂN TRI THỨC & KINH NGHIỆM BIÊN KỊCH 100 BỘ ĐOẢN VĂN TRUNG QUỐC KINH ĐIỂN

> **Sổ Tay Bách Khoa Toàn Thư Về Biên Kịch Kịch Bản Đoản Văn & Audio Drama TikTok Triệu View.**
> *Nguồn dữ liệu thực chiến: Tổng hợp và mổ xẻ chuyên sâu 100 tác phẩm đoản văn kinh điển và hiện tượng mạng nổi tiếng nhất từ Zhihu 盐选专栏 (初代三绝, 新三绝, 2025盐言三绝, Kim Bàn Phím), Douyin 短剧 (hiện tượng hàng tỷ lượt xem), Fanqie (番茄小说), Jinjiang (晋江文学城) và Qidian (起点中文网).*
> *Được thiết kế làm kim chỉ nam bất biến cho toàn bộ Hệ thống Agent và Động cơ Biên Kịch Antigravity TikTok Studio.*

---

## PHẦN I: TỔNG LUẬN PHƯƠNG PHÁP LUẬN BIÊN KỊCH ĐOẢN VĂN VIRAL (ZHIHU & DOUYIN)

### 1. Triết Lý Cốt Lõi: '12 Chữ Vàng' Của Đoản Văn Giữ Chân Người Nghe
> **'Ba giây một cái móc (Hook), năm giây một đảo chiều (Twist), tập nào cũng có điểm sảng (Shuangdian)!'**

- **Quy tắc 1.5 - 3 Giây Đầu**: Quyết định sinh tử của video. Thính giả lướt qua màn hình cực nhanh. Nếu 15 từ đầu tiên không chứa xung đột cực hạn, nghịch lý hành động hoặc vật chứng rợn gáy, tỷ lệ vuốt bỏ (Swipe Away) đạt trên 85%.
- **Công Thức Sảng Điểm Định Lượng (The Shuangdian Neuro-Equation)**:

$$\\text{Mức Độ Sảng} = (\\text{Độ Ức Chế Tột Cùng} \\times \\text{Độ Trì Hoãn Thỏa Mãn}) \\times \\text{Tốc Độ & Cường Độ Phản Đòn}$$

- **Chu Trình 4 Giai Đoạn Áp Chế - Bộc Phát**:
  1. `ÁP CHẾ (压抑 - Yayi)`: Tạo bất công phi lý, hạ thấp nhân vị, tước đoạt danh dự của NV chính (nạp đầy phẫn nộ cho khán giả).
  2. `TÍCH TỤ / KÉO NÉN (蓄势 - Xushi)`: NV chính không manh động, ẩn nhẫn mài dao, giăng bẫy âm thầm (kỳ vọng đòn trừng phạt).
  3. `BỘC PHÁT VẢ MẶT (爆发打脸 - Bofa Dalian)`: Lật mở sự thật ngay tại đỉnh cao đắc thắng của phản diện (giải phóng Dopamine cực hạn).
  4. `THANH TOÁN TRIỆT ĐỂ (清算 - Qingsuan)`: Phản diện mất hết tiền tài, danh dự, địa vị; cầu xin trong tuyệt vọng (tuyệt đối không tha thứ rẻ rúng).

### 2. Mô Hình Nhịp Độ 1 Phút / 1 Tập Chuẩn Điện Ảnh (Micro-Pacing Model)
```mermaid
flowchart LR
    A["00s - 03s: Hook 3 Giây
(Va chạm vật lý / Nghịch lý)"] --> B["03s - 15s: Nén Ức Chế
(Phản diện áp chế tột cùng)"]
    B --> C["15s - 45s: Biến Số & Lật Kèo
(Rút bài tẩy / Bóc trần tử huyệt)"]
    C --> D["45s - 55s: Điểm Sảng Bùng Nổ
(Vả mặt sòng phẳng / Sụp đổ)"]
    D --> E["55s - 60s: Cliffhanger Cắt Đỉnh
(Mở ra hiểm nguy lớn hơn)"]
```

### 3. Bảng Phân Bổ Âm Thanh & Nhịp Thở Audio Drama (Sound Design Pacing)
| Thời Gian | Chức Năng Âm Thanh / Kịch Bản | Mục Tiêu Giữ Chân (Retention) | Kỹ Thuật Sound Design |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:03** | **GOLDEN HOOK:** Lời thoại gây sốc / Mâu thuẫn đạo đức tột độ | Ngăn người dùng lướt đi (Stop-scrolling) | Tiếng tát vang dội, tiếng máy thở tít dài, tiếng đập bàn, âm bass drop đột ngột |
| **00:03 - 00:15** | **ESCALATION:** Phản diện dồn ép, nhân vật chính rơi vào tuyệt lộ | Tạo cảm xúc phẫn nộ / tò mò tột đỉnh | Nhạc nền căng thẳng (Violin dồn dập, tiếng đồng hồ đếm ngược) |
| **00:15 - 00:25** | **PRE-TWIST:** Một biến số lạ xuất hiện, hé lộ tia hy vọng | Kích hoạt tò mò trí tuệ | Nhạc nền im bặt đột ngột (Audio Pause / Negative Space) |
| **00:25 - 00:30** | **CLIFFHANGER / MINI-PUNCH:** Câu nói lật đổ cục diện hoặc tiếng mở cửa | Buộc người nghe phải nghe tiếp tập sau | Tiếng hiệu ứng Whoosh + Câu thoại bỏ lửng then chốt |

### 4. Bộ 5 Mô Thức 'Hook 3 Giây' Triệu View (Golden Hook Templates)
1. **Hook Nghịch Luân Lý / Khiêu Khích Đạo Đức**: *'Ngày tôi sinh non trong phòng cấp cứu, chồng tôi đang ký giấy đồng ý hiến thận của tôi cho người yêu cũ của anh ta.'*
2. **Hook Đếm Ngược Tử Thần**: *'Bác sĩ nói tôi chỉ còn sống được ba mươi ngày, và việc đầu tiên tôi làm là rút năm mươi tỷ tiền tiết kiệm.'*
3. **Hook Phản So Sai Thân Phận Cực Đoan**: *'Mẹ chồng tống tôi ra khỏi biệt thự với hai trăm nghìn đồng dằn túi, bà không hề biết tập đoàn mà con trai bà đang làm thuê mang chính tên lót của tôi.'*
4. **Hook Quái Đàm / Cấm Kỵ Quy Tắc**: *'Nếu bạn thức giấc lúc ba giờ sáng và thấy mẹ bạn đang đứng gõ cửa phòng tắm... Đừng mở cửa! Mẹ bạn đã mất ba năm trước rồi.'*
5. **Hook Thẳng Tay Vả Mặt (Direct Slap Hook)**: *'Cầm năm mươi tỷ này và cút khỏi con trai tôi? Bác gái à, công ty của con trai bác tháng trước vừa vay của tôi một trăm tỷ đấy!'*

### 5. Thiết Kế Nhân Vật Phản Diện 3 Chiều (Chống Bẫy Não Tàn)
```
           [LỚP NGOÀI: MẶT NẠ ĐẠO ĐỨC & TRÍ TUỆ]
   - Lịch thiệp, được xã hội công nhận, lời nói luôn nhân danh lợi ích chung.
   - Thấu hiểu luật pháp, dùng kẽ hở quy định để triệt hạ đối thủ.
                         ↓
           [LỚP GIỮA: ĐỘNG CƠ HỢP LÝ HÓA (JUSTIFICATION)]
   - 'Ta không ác, ta chỉ đang giành lại những gì thế giới nợ ta.'
   - Xuất thân chấn thương tâm lý, nghèo đói cùng cực hoặc bị áp bức thời niên thiếu.
                         ↓
           [LỚP LÕI: TỬ HUYỆT BẢO THỦ & KIÊU NGẠO]
   - Không tin trên đời có người vô tư không tham lam.
   - Đánh giá thấp nhân tính và tình yêu thương chân thành.
```

---

## PHẦN II: MỔ XẺ CHI TIẾT 100 TÁC PHẨM ĐOẢN VĂN KINH ĐIỂN THEO 10 THỂ LOẠI
""")

    # Part II: 10 Genres with 10 stories each
    for g in GENRES_MAP:
        idx_str = f"{g['index']:02d}"
        doc_lines.append(f"""
### 📂 THỂ LOẠI {idx_str}: {g['name_vi']}
- **Nền tảng tiêu biểu**: {g['platform_desc']}
- **Trục cảm xúc chủ đạo**: *{g['axis']}*
- **Số lượng tác phẩm nghiên cứu**: 10 tác phẩm nổi tiếng chuẩn mực.

---
""")
        for s in g['stories']:
            doc_lines.append(format_story_markdown(s))
            doc_lines.append("\n---\n")

    # Part III & Part IV
    doc_lines.append("""
## PHẦN III: MA TRẬN 10 CÔNG THỨC ĐIỂM SẢNG (SHUANGDIAN FORMULAS) & CƠ CHẾ LẬT KÈO ĐỘC BẢN

Qua việc mổ xẻ 100 tác phẩm kinh điển, hệ thống Agent đúc kết 10 cơ chế tạo điểm sảng mãnh liệt và lật kèo logic nhất:

### 1. Margin Call Liquidation (Cháy tài khoản đòn bẩy tài chính)
- **Cơ chế**: Nhân vật chính lợi dụng sự tham lam dùng đòn bẩy tài chính cao của đối thủ, bất ngờ tung đòn phong tỏa thanh khoản hoặc kích hoạt Short Squeeze khiến tài khoản đối phương bốc hơi trong 30 phút.
- **Áp dụng Audio**: Tiếng chuông reo báo mở cửa sàn chứng khoán, tiếng đọc lệnh khớp giá bán giải chấp dồn dập.

### 2. Rule Inversion Trap (Đảo ngược quy tắc phòng kín)
- **Cơ chế**: Phản diện nghĩ mình nắm rõ quy tắc sinh tồn để ép người khác vào chỗ chết, nhân vật chính phát hiện ra lỗ hổng logic hoặc tính giả mạo của quy tắc, biến chính cái bẫy đó thành lò thiêu kẻ săn mồi.
- **Áp dụng Audio**: Tiếng loa phát thanh rè rè công bố điều lệ bổ sung, tiếng cửa sắt tự động khóa trái từ bên trong.

### 3. Digital Forensic Stream (Camera ngầm phát sóng trực tiếp)
- **Cơ chế**: Thay vì đôi co ngoài đời, nhân vật chính để đối phương tự do diễn trò bỉ ổi trước ống kính camera 4K ngụy trang, đồng thời phát trực tiếp lên màn hình LED quảng trường hoặc cuộc họp cổ đông.
- **Áp dụng Audio**: Tiếng 'Ting' thông báo bắt đầu livestream, tiếng ồ lên sững sờ của hàng vạn người xem.

### 4. Forensic Pathology Match (Giám định pháp y ADN & cơ học vết thương)
- **Cơ chế**: Mọi lời nói dối về ngoại phạm hoặc hiện trường giả đều bị bẻ gãy hoàn toàn bởi góc nghiêng của vết cắt, nhóm máu lạ, hoặc ADN trùng khớp dưới kính hiển vi quang học.
- **Áp dụng Audio**: Tiếng giấy biên bản pháp y lật soạt, câu kết luận đanh thép của giám định viên trưởng.

### 5. Time Capsule Will (Di chúc ủy thác thời gian & thu hồi tài sản)
- **Cơ chế**: Tài sản mà kẻ tham lam tranh giành thực chất đã được chủ sở hữu lập quỹ tín thác thời gian hoặc có điều khoản ràng buộc; chỉ cần vi phạm đạo đức là toàn bộ quyền thừa kế bị thu hồi về 0.
- **Áp dụng Audio**: Tiếng gõ búa của luật sư công chứng, tiếng tin nhắn ngân hàng báo số dư tài khoản bị phong tỏa.

### 6. Chemical Toxic Indicator (Chỉ thị hóa học & trung hòa độc tố)
- **Cơ chế**: Dùng phản ứng hóa học (giấy quỳ đổi màu, ngọn lửa xanh lưu huỳnh, kết tủa trắng) để vạch trần độc dược hoặc chất cấm ngay trước mặt đông đảo nhân chứng.
- **Áp dụng Audio**: Tiếng chất lỏng sủi bọt xèo xèo, tiếng kim loại trâm bạc sủi bọt xám tro.

### 7. Server Audit Log Extraction (Địa chỉ MAC & trích xuất dữ liệu máy chủ)
- **Cơ chế**: Kẻ thủ ác xóa dấu vết điện tử nhưng quên mất nhật ký truy cập máy chủ (Audit Log) cấp thấp và địa chỉ MAC vật lý; dữ liệu được khôi phục tại chỗ khiến hắn chết lặng.
- **Áp dụng Audio**: Tiếng gõ bàn phím cơ gõ lệnh `grep` dồn dập, tiếng phím Enter nhấn dứt khoát.

### 8. Pressure Isolation Containment (Khóa van điều áp & cô lập vật lý)
- **Cơ chế**: Dùng kiến thức cơ học và van điều áp để cô lập kẻ phản nghịch ở khoang ngoài boong-ke hoặc buồng khử trùng; đối phương chỉ có thể bất lực nhìn qua lớp kính chống đạn.
- **Áp dụng Audio**: Tiếng van xả khí áp lực cao xì mạnh, tiếng chốt thép ba lớp sập cạch.

### 9. Civil Fraud Void Judgment (Tuyên hủy giao dịch dân sự lừa dối)
- **Cơ chế**: Dẫn chiếu điều luật Bộ luật Dân sự về hành vi lừa dối hoặc vi phạm trật tự công cộng để tòa tuyên hủy toàn bộ hợp đồng tặng cho nhà cửa, xe cộ cho tiểu tam/kẻ lừa đảo.
- **Áp dụng Audio**: Tiếng gõ búa dứt khoát của thẩm phán, tiếng đọc bản án tuyên phạt nghiêm minh.

### 10. Satirical Psychological Collapse (Tự thú tâm lý do tiếng lòng thần dụ)
- **Cơ chế**: Phản diện tự tin vào tội ác hoàn hảo bỗng hoang mang cực độ khi nghe thấy suy nghĩ bên trong của mình bị bóc trần hoặc bị dẫn dắt bởi tiếng lòng của đối phương, tự mình làm lộ sơ hở trước cơ quan điều tra.
- **Áp dụng Audio**: Hai âm sắc giọng đan xen: Giọng chính kịch trầm ấm và giọng thì thầm châm biếm sâu cay.

---

## PHẦN IV: BỘ TIÊU CHUẨN VĨNH VIỄN NẠP VÀO HỆ THỐNG AGENT BIÊN KỊCH ANTIGRAVITY

1. **Bắt Buộc Tra Cứu Trước Khi Viết**: Bất kỳ kịch bản nào được Agent tạo ra đều phải đối chiếu ít nhất 3 Case Study trong Đại Điển 100 Bộ Truyện này.
2. **Quy Tắc Chống Đồng Hóa Tuyệt Đối (Anti-Homogenization Standard)**:
   - Jaccard Similarity < 28% so với 10 video gần nhất.
   - Luân chuyển qua 10 trường phái mở đầu (Hook Archetypes) và 20 vũ trụ nhân vật nghề nghiệp chuyên sâu.
3. **Chuẩn Âm Học Đoản Văn Edge-TTS (Acoustic Cadence Engine)**:
   - Từng câu thoại được mài giũa dưới 12 từ, có dấu ngắt hơi lấy hơi (`,`, `-`, `:`).
   - Chốt câu bằng thanh trắc dứt khoát, triệt tiêu hoàn toàn sáo ngữ convert Trung Quốc.

---
*Biên soạn và nâng cấp bởi Hệ Thống Committee 10 Agents - Antigravity TikTok Studio.*
*Bản quyền tri thức thuộc về Hệ thống Sản xuất Audio Drama Triệu View.*
""")

    master_content = "".join(doc_lines)
    with open('docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md', 'w', encoding='utf-8') as f:
        f.write(master_content)
    print("Successfully written docs/DAI_KINH_NGHIEM_100_BO_TRUYEN_NGAN_TRUNG_QUOC.md")

def generate_genre_individual_files():
    for g in GENRES_MAP:
        file_path = os.path.join('docs', 'kinh_nghiem_chi_tiet', g['file_name'])
        lines = []
        lines.append(f"""# ĐÚC KẾT KINH NGHIỆM BIÊN KỊCH CHUYÊN SÂU: {g['index']}. {g['name_vi']}
**Đặc trưng thể loại:** {g['axis']}

> [!NOTE]
> File tài liệu này phân tích chi tiết 10 bộ truyện nổi tiếng nhất thuộc nhóm {g['index']}. {g['name_vi']}, đúc kết tinh hoa kịch bản, nghệ thuật xây dựng nhân vật, bối cảnh, cú hook và kỹ thuật đảo chiều cốt truyện thực chiến.

---

## MỤC LỤC CÁC TÁC PHẨM TRONG THỂ LOẠI

""")
        for s in g['stories']:
            lines.append(f"- **Tác phẩm {s['id']}:** 《{s['title_vi']}》( {s['title_cn']} ) - *{s['category']}*\n")
        
        lines.append("\n---\n\n")
        
        for s in g['stories']:
            lines.append(f"""## Tác phẩm {int(s['id']) % 10 or 10}: 《{s['title_vi']}》( {s['title_cn']} )
- **Tác giả & Nền tảng:** {s['author']} - {s['platform']}
- **Thể loại chi tiết:** {s['category']}
- **Tiền đề & Bối cảnh cốt truyện (Premise & Setting):**
  {s['premise']}

- **Thiết lập & Tạo hình nhân vật (Character Dynamics & Arcs):**
""")
            for c in s['characters']:
                lines.append(f"  - {c}\n")
            
            lines.append(f"""
- **Golden Retention Hook (Mở màn 5s giữ chân độc giả):**
  > "{s['hook_3s']}"

- **Cấu trúc 3 Hồi & Nhịp điệu kịch tính (Acts & Pacing Beat-Sheet):**
  - {s['act_structure']['act_1']}
  - {s['act_structure']['act_2']}
  - {s['act_structure']['act_3']}

- **Điểm xoay chuyển cốt truyện & Đại kết cục (Plot Twist & Climax):**
  {s['plot_twist']}

- **Tinh hoa nghệ thuật & Bài học biên kịch đúc kết:**
""")
            for t in s['mastery_takeaways']:
                lines.append(f"  - {t}\n")
            
            lines.append("\n---\n\n")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("".join(lines))
        print(f"Successfully written {file_path}")

def generate_python_data_files():
    for g in GENRES_MAP:
        py_path = os.path.join('data', 'stories_study', g['py_file'])
        enriched_stories = []
        for s in g['stories']:
            s_dict = dict(s)
            s_dict['title_vn'] = s.get('title_vi', '')
            s_dict['genre'] = s.get('category', '')
            s_dict['golden_hook'] = s.get('hook_3s', '')
            s_dict['author_platform'] = f"{s.get('author', '')} - {s.get('platform', '')}"
            s_dict['core_lessons'] = s.get('mastery_takeaways', [])
            enriched_stories.append(s_dict)

        content = f"""# -*- coding: utf-8 -*-
\"\"\"
data/stories_study/{g['py_file']}
Tập dữ liệu phân tích chuyên sâu 10 tác phẩm kinh điển Thể loại {g['index']}: {g['name_vi']}
\"\"\"

{g['var_name']} = {repr(enriched_stories)}
"""
        with open(py_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {py_path}")

if __name__ == '__main__':
    generate_master_document()
    generate_genre_individual_files()
    generate_python_data_files()
    print("ALL 100 STORIES PROCESSED AND SYNCHRONIZED SUCCESSFULLY!")
