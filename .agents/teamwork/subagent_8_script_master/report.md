# BÁO CÁO NGHIÊN CỨU & TÁI CẤU TRÚC KỊCH BẢN AUDIO DRAMA 10 PHÚT TRIỆU VIEW
## Sub-Agent 8: Narrative Pacing & Scriptwriting Master
**Target Audience:** 80% Nữ giới (91.4% độ tuổi 18-34) | **Traffic Source:** 93% FYP (TikTok Đề Xuất)  
**Tác giả:** Sub-Agent 8 (Narrative Pacing & Scriptwriting Master)  
**Ngày báo cáo:** 2026-10-17  

---

## I. EXECUTIVE SUMMARY & GIẢI MÃ NGUYÊN NHÂN TỬ HUYỆT 4-7 GIÂY (HOOK DEATH AUTOPSY)

### 1. Thực Trạng Số Liệu Khốc Liệt
Dữ liệu từ `data/tiktok_studio_metrics.json` và studio analytics cho thấy nghịch lý nghiêm trọng:
- Tổng 240 bài đăng, 7.7K views tuần qua, phân phối tới **93% qua luồng Đề xuất (FYP)**.
- Thời lượng video: **~10 phút (09:55 - 10:02)** cho mỗi tập.
- **Thời gian xem trung bình (Average Watch Time): chỉ đạt 4 - 7 giây / lượt xem.**
- Tỷ lệ xem hết (Completion Rate): **gần như bằng 0%**.
- Tương tác bình luận: **0 bình luận** trên các tập gần nhất.

### 2. Mổ Xẻ Tử Huyệt Biên Kịch (Scriptwriting Fatal Flaws)
Sau khi kiểm toán trực tiếp các file kịch bản thực tế đã xuất bản (`core/stories/me_chong_thuc_tinh_masterpiece.py`, `detective_masterpiece.py`, `VID_new_1_sadieu.json`...), chúng tôi phát hiện 4 căn bệnh kịch bản chí mạng:

#### 🔴 Căn bệnh 1: Bẫy "Văn học miêu tả lê thê" (Novelistic Atmospheric Trap) trong 30 giây đầu
- **Minh chứng thực tế từ `me_chong_thuc_tinh_masterpiece.py`:**
  > *"Tiếng mưa gào rít bên ngoài khung cửa kính khách sạn năm sao như một bản nhạc đệm ai oán cho ký ức của bảy năm về trước. Trong khán phòng dát vàng lộng lẫy, ánh mắt của Tô Nhược Dao lạnh buốt như lưỡi dao cạo vừa được mài sắc. Bảy năm trước, cũng chính những con người đang ngồi đây đã nhìn mẹ con cô bằng ánh mắt khinh miệt..."*
- **Phân tích:** Đoạn mở đầu mất tới 6 đoạn văn (~150 từ, tương đương 30-40 giây đọc ở tốc độ 1.5x) chỉ để tả thời tiết mưa rơi, cửa kính khách sạn 5 sao, chiếc vòng ngọc va lách cách, và hồi tưởng 7 năm trước. Đến tận dòng 28 (giây thứ 35) cái tát đầu tiên mới xuất hiện!
- **Hệ quả trên FYP:** Người dùng lướt TikTok cho một video cơ hội sống sót tối đa **1.5 đến 3 giây**. Khi nghe câu đầu tiên miêu tả thời tiết mưa gào ngoài cửa sổ, não bộ người dùng tự động phân loại đây là "văn mẫu ru ngủ / sách nói cổ điển" và **quẹt ngay lập tức**. Con số 4-7 giây chính là thời gian người dùng nghe xong câu miêu tả trời mưa và vuốt ngón tay lên clip khác!

#### 🔴 Căn bệnh 2: Định nghĩa Hook sai lệch ("Hook 5-10 giây đầu vàng" là bản án tử trên FYP)
- Trong file `core/prompts.py`, prompt hiện tại ghi: *"HOOK 5 - 10 GIÂY ĐẦU VÀNG"*.
- **Thực tế thuật toán FYP:** 5-10 giây là quá muộn! Trên FYP, quyết định quẹt xảy ra ở **0 - 3 giây (tương đương 10 - 15 từ đầu tiên)**. Nếu 15 từ đầu tiên không chứa động từ mạnh, xung đột đanh thép, âm thanh sốc hoặc một nghịch lý đạo đức gây phẫn nộ, clip coi như chết yểu.

#### 🔴 Căn bệnh 3: Lệch pha tệp khán giả (Audience Mismatch)
- Tệp người xem thực tế 7 ngày qua: **80% Nữ giới, 91.4% từ 18-34 tuổi**. Thói quen tiêu thụ: **VTV Giải Trí** (phim truyền hình gia đình, mẹ chồng độc ác, trà xanh giật chồng, bắt gian tại trận, chia tài sản), **KÊNH SHOWBIZ**, **Vũ Trụ Showbiz**.
- Kênh lại sản xuất các đề tài: *Mạt Thế Kỷ Băng Hà Tích Trữ 100 Tỷ* (tệp Nam/Game thủ), *Kỳ Án Căn Phòng Số 13* (Trinh thám nặng nề, câu thoại mở màn kiểu hoạt hình Conan: "Sự thật chỉ có một..."). Ngay cả bộ *Nàng Dâu Thức Tỉnh* dù đúng đề tài phụ nữ nhưng lại bị bẫy mở màn chậm rãi.

#### 🔴 Căn bệnh 4: Hiện tượng "Mất tập trung giữa dòng" (Tension Fatigue) - Thiếu Micro-Hooks
- Video 10 phút là một trường đoạn dài vô tận trên TikTok. Kịch bản cũ triển khai theo lối tự sự đều đều, thiếu các **cú sốc gián đoạn (Pattern Interrupt)**.
- Người xem sau khi vượt qua được 30 giây đầu sẽ tiếp tục quẹt đi ở phút thứ 1:30 hoặc 3:00 vì mạch kể chùng xuống, toàn những đoạn kể lể tâm trạng nội tâm mà không có biến cố mới.

---

## II. TÁI CẤU TRÚC NHỊP ĐIỆU KỊCH BẢN 10 PHÚT: TRIẾT LÝ "IN MEDIAS RES" & KHẮC PHỤC TRIỆT ĐỂ

### 1. Nguyên Tắc Cốt Tử: Zero Descriptive Exposition (Xóa Bỏ Miêu Tả Khởi Đầu)
- **CẤM TUYỆT ĐỐI trong 60 giây đầu:**
  - Cấm tả thời tiết: *"Đêm mưa giông bão bùng...", "Ánh nắng le lói..."*
  - Cấm tả bối cảnh tĩnh: *"Căn biệt thự nguy nga nằm bên bờ sông...", "Căn phòng khách sạn năm sao..."*
  - Cấm giới thiệu lý lịch / hoàn cảnh: *"Tôi tên là Lan, năm nay 28 tuổi, kết hôn được 3 năm..."*
  - Cấm triết lý suy tư: *"Cuộc đời con người ta vốn dĩ vô thường..."*

### 2. Triết Lý "In Medias Res" (Ném Khán Giả Thẳng Vào Giữa Bãi Chiến Trường)
- **Quy tắc 0.5 Giây Đầu (Thính giác):** Bắt đầu bằng một hiệu ứng âm thanh kích thích mạnh (SFX: tiếng bạt tai đanh thép `CHÁT!`, tiếng gốm sứ vỡ vụn `CHOẢNG!`, tiếng còi máy theo dõi nhịp tim kêu dài `TÍT...`, tiếng ném xấp ảnh xuống bàn).
- **Quy tắc 3 Giây Đầu (12-15 từ đầu tiên):** Phải là một câu thoại có tính sát thương cực đại, một sự thật động trời không thể tin nổi, hoặc một hành vi ngược đãi tột cùng khiến máu trong người người nghe sôi lên vì bất bình.
- **Công thức Hook 3s:**
  $$\text{Hook 3s} = \text{[Âm Thanh Xung Đột]} + \text{[Câu Thoại Áp Chế / Đòn Đánh Chí Mạng]} + \text{[Nghịch Lý Đạo Đức / Tài Sản Cực Hạn]}$$

---

## III. BẢN ĐỒ LƯU GIỮ 10 PHÚT (10-MINUTE RETENTION ARC & 45S MICRO-HOOKS)

Với tốc độ đọc chuẩn `atempo=1.5` (~346 từ/phút), video 10 phút có dung lượng chuẩn toán học: **3,460 - 3,500 từ**.  
Để giữ chân người xem suốt 600 giây, kịch bản phải được chia thành **5 giai đoạn chiến lược** với **13 Micro-Hooks (cứ 45 giây / ~250 từ xuất hiện một lần)**.

```
0s        30s               3m                                7m                           10m
|--Hook---|--Inciting Evt---|-------Climax 1 & Đấu Trí-------|--Leo Thang & Turning Point--|--Đại Cao Trào & Cliffhanger--|
(0-5s)    (5-30s)           (1-3 phút / ~1,000 từ)           (4-7 phút / ~1,400 từ)        (8-10 phút / ~1,050 từ)
[SFX+Thoại] [Bí mật nổ tung] [Phản diện lấn tới / Nén ức chế] [Micro-hook mỗi 45s / Phản đòn] [Bẫy sập / Cắt đúng đỉnh 0.5s]
```

### 1. Chi Tiết Từng Phân Đoạn & Điểm Rơi Tâm Lý Khán Giả

| Mốc Thời Gian | Số Từ Lũy Kế | Tên Giai Đoạn | Mục Tiêu Giữ Chân (Retention Strategy) | Trạng Thái Tâm Lý Khán Giả |
| :--- | :--- | :--- | :--- | :--- |
| **00:00 - 00:05** | Từ 1 - 30 | **Shocking Hook (Cú Sốc 3s)** | Cắt đứt quán tính lướt màn hình. SFX bạo liệt + Thoại đanh thép sát thương cực đỉnh. | Bị giật mình, sốc, dừng ngón tay quẹt. |
| **00:05 - 00:30** | Từ 31 - 170 | **Inciting Incident (Biến Cố Chấn Động)** | Khai hỏa quả bom cốt truyện: Ngoại tình tráo trở, đuổi khỏi nhà, xét nghiệm ADN giả mạo, hoặc thừa kế ngầm. | Tò mò cực độ: *"Chuyện gì đang xảy ra vậy?"* |
| **00:30 - 01:15** | Từ 171 - 430 | **Micro-hook 1 & Nén Áp Suất Bậc 1** | Phản diện pháo hôi (mẹ chồng/tiểu tam) lấn tới, sỉ nhục nhân vật chính. Ném ra bằng chứng bất lợi. | Bất bình, uất ức thay cho nữ chính. |
| **01:15 - 02:00** | Từ 431 - 690 | **Micro-hook 2 & Khẩu Súng Chekhov 1** | Xuất hiện vật chứng tưởng vô hại (chiếc camera hành trình, tờ biên lai ngân hàng, vết son lạ). | Tập trung suy đoán, ghi nhớ chi tiết. |
| **02:00 - 03:00** | Từ 691 - 1,040 | **Cao Trào 1 & Màn Đấu Trí Đầu Tiên** | Nhân vật chính không khóc lóc, tung đòn đáp trả lý tính đầu tiên khiến phản diện chột dạ. | Thỏa mãn bước đầu (Mini-catharsis), muốn nghe tiếp. |
| **03:00 - 03:45** | Từ 1,041 - 1,300 | **Micro-hook 3 & Âm Mưu Tầng Sâu** | Phát hiện kẻ chủ mưu không chỉ có mẹ chồng mà chồng hoặc bạn thân cũng nhúng tay. | Cảm giác bị phản bội nhân đôi, căm phẫn tột cùng. |
| **03:45 - 04:30** | Từ 1,301 - 1,560 | **Micro-hook 4 & Hiểm Cảnh Tột Cùng** | Tài khoản bị phong tỏa, người thân bị đe dọa, bị dồn vào chân tường (The Lowest Point). | Lo âu tột độ: *"Làm sao cô ấy thoát được đây?"* |
| **04:30 - 05:15** | Từ 1,561 - 1,820 | **Bước Ngoặt Thức Tỉnh (The Turning Point)** | Nữ chính thức tỉnh hoàn toàn. Chuyển từ phòng thủ sang tấn công. Kích hoạt kế hoạch phản gián. | Hưng phấn, chờ đợi màn lật kèo trả thù. |
| **05:15 - 06:00** | Từ 1,821 - 2,080 | **Micro-hook 5 & Liên Minh Bí Mật** | Nhân vật bí ẩn xuất hiện (Luật sư hàng đầu, chủ tịch đối thủ, hoặc bố đẻ quyền lực). | Hy vọng bùng nổ, thế cờ bắt đầu đảo chiều. |
| **06:00 - 06:45** | Từ 2,081 - 2,340 | **Micro-hook 6 & Cái Bẫy Đã Sập** | Phản diện tưởng mình thắng lớn, tổ chức tiệc mừng / ký hợp đồng nhưng không biết đã rơi vào bẫy. | Cười thầm, mong chờ khoảnh khắc vả mặt. |
| **06:45 - 07:30** | Từ 2,341 - 2,600 | **Micro-hook 7 & Bóc Tách Bằng Chứng 1** | Tung ra đòn vả mặt đầu tiên: đoạn ghi âm hoặc tài liệu tài chính phơi bày sự trơ tráo của phản diện. | Sảng khoái cực độ, hả dạ. |
| **07:30 - 08:30** | Từ 2,601 - 2,950 | **Đại Cao Trào Leo Thang (Escalating Climax)** | Phản diện hoảng loạn, cố cãi chày cãi cối, giở trò bạo lực hoặc tung đòn bẩn cuối cùng. | Tim đập nhanh, căng thẳng nghẹt thở. |
| **08:30 - 09:30** | Từ 2,951 - 3,300 | **Đòn Đánh Đoạt Mạng & Tháo Ngòi Chekhov** | Khẩu súng Chekhov từ phút thứ 2 được kích hoạt: Sự thật ADN hoặc hợp đồng chuyển nhượng vạch trần tất cả! | Bùng nổ cảm xúc cao nhất của video. |
| **09:30 - 09:55** | Từ 3,301 - 3,450 | **Cliffhanger Nghẹt Thở (Điểm Cắt 0.5s)** | Đúng lúc sự thật lớn nhất sắp được thốt ra hoặc một hiểm nguy mới ập đến $\rightarrow$ **CẮT PHỤT NGAY LẬP TỨC!** | Bức bối, không chịu nổi, bắt buộc phải xem Part 2! |
| **09:55 - 10:00** | Từ 3,451 - 3,480 | **Comment Magnet CTA** | Đặt câu hỏi phân cực 1 hoặc 2 đánh trúng đạo đức / cảm xúc để người nghe gõ phím tranh luận. | Để lại bình luận tranh cãi, kích hoạt thuật toán. |

### 2. Bản Chất Tâm Lý Học Của 13 Micro-Hooks (Mỗi 45 Giây)
- **Hiệu ứng Zeigarnik (Vòng lặp chưa hoàn thành):** Cứ mỗi 45 giây, khi người xem vừa nhận được câu trả lời cho mâu thuẫn trước, kịch bản phải **ngay lập tức mở ra một câu hỏi mới lớn hơn**.
- **Chống mệt mỏi âm thanh (Acoustic Reset):** Giọng đọc AI 1.5x rất dễ gây mỏi tai nếu đơn điệu. Cứ mỗi 45 giây, một câu ngắn đanh thép ngắt bằng dấu ba chấm `...` hoặc tiếng động kịch tính sẽ "đánh thức" màng nhĩ người nghe.

---

## IV. BỘ 3 TEMPLATE HOOK 3 GIÂY ĐỘT PHÁ DÀNH RIÊNG CHO TỆP NỮ 18-34 TUỔI

Đây là 3 kịch bản mẫu mở màn thực chiến, đạt chuẩn **In Medias Res**, tối ưu từng dấu câu cho giọng đọc AI (`vi-VN-HoaiMyNeural` hoặc `vi-VN-NamMinhNeural`), tích hợp sẵn hiệu ứng âm thanh (SFX) và cầu nối 5-30 giây.

---

### TEMPLATE 1: NGOẠI TÌNH TRÁO TRỞ & PHÒNG TÂN HÔN (Infidelity & Sacred Milestone Betrayal)
- **Đối tượng mục tiêu:** Nữ 18-34 (quan tâm hôn nhân, bạn thân, trà xanh, trả thù phản bội).
- **Cảm xúc kích hoạt:** Phẫn nộ tột cùng, hả hê vả mặt.
- **Giọng đọc đề xuất:** `vi-VN-HoaiMyNeural` (Tông giọng lạnh lùng, dứt khoát, sắc như dao).

#### 📜 Kịch Bản Chi Tiết:
- **[00:00 - 00:03] HOOK 3 GIÂY ĐẦU (14 từ):**
  > `[SFX: Tiếng kính vỡ choảng / Khóa cửa rầm rầm]`  
  > *"Ngay đêm tân hôn, tôi mở tủ quần áo ra... thì thấy cô bạn thân đang khỏa thân trốn bên trong!"*

- **[00:03 - 00:05] ĐÒN ÁP CHẾ GIA TĂNG (15 từ):**
  > *"Chồng tôi lao đến che chắn cho ả, quát lớn: 'Cô ấy say rượu, em đừng làm ầm ĩ mất mặt gia đình!'."*

- **[00:05 - 00:30] CẦU NỐI BIẾN CỐ & CHÂM NGÒI BOM XUNG ĐỘT (85 từ):**
  > *"Tôi không rơi một giọt nước mắt, khóe môi khẽ nhếch lên một nụ cười lạnh buốt. Bàn tay tôi thong thả rút chiếc điện thoại ra, bấm nút kết nối với màn hình LED khổng lồ ngoài phòng khách – nơi bố mẹ chồng và toàn thể họ hàng gia tộc đang ngồi uống trà mừng hạnh phúc.  
  > 'Mất mặt sao? Vậy để tôi chiếu đoạn camera tại khách sạn năm sao của hai người đêm qua cho cả dòng họ cùng chiêm ngưỡng!'...  
  > Khuôn mặt chồng tôi lập tức cắt không còn một giọt máu!"*

- **Cơ chế giữ chân:** Biến khoảnh khắc thiêng liêng nhất (đêm tân hôn) thành hiện trường phản trắc kinh tởm nhất; nữ chính không khóc lóc mà lập tức có sẵn bài tẩy phản đòn công khai, khiến khán giả nữ muốn xem màn vả mặt tiếp theo.

---

### TEMPLATE 2: MẸ CHỒNG ĐỘC ÁC & ĐÊM MƯA BỊ ĐUỔI KHỎI NHÀ (Mother-in-law Tyranny & Family Clash)
- **Đối tượng mục tiêu:** Nữ 22-34 (nội trợ, nhân viên văn phòng, đồng cảm với áp bức mẹ chồng nàng dâu phong cách VTV Giải Trí).
- **Cảm xúc kích hoạt:** Uất ức thắt ruột $\rightarrow$ Khao khát thấy kẻ ác bị trừng phạt.
- **Giọng đọc đề xuất:** `vi-VN-HoaiMyNeural` (Ngắt nhịp uất nghẹn rồi đanh thép).

#### 📜 Kịch Bản Chi Tiết:
- **[00:00 - 00:03] HOOK 3 GIÂY ĐẦU (15 từ):**
  > `[SFX: Tiếng tát trời giáng CHÁT! + Tiếng mưa rào xối xả]`  
  > *"Mẹ chồng hắt thẳng bát canh nóng vào mặt tôi: 'Đồ cau điếc! Mau ký đơn ly hôn rồi cút khỏi nhà tao!'."*

- **[00:03 - 00:05] ĐÒN ÁP CHẾ GIA TĂNG (14 từ):**
  > *"Chiếc vali rách của hai mẹ con tôi bị bà ta hất tung qua cổng sắt, rơi xuống vũng bùn lầy!"*

- **[00:05 - 00:30] CẦU NỐI BIẾN CỐ & CHÂM NGÒI BOM XUNG ĐỘT (88 từ):**
  > *"Đứa con gái ba tuổi của tôi khóc ngất giữa cơn giông bão, trán va vào bậc thềm rướm máu. Chồng tôi đứng sau cánh cửa kính phòng khách ấm cúng, tay ôm eo cô ả mang bầu con trai, lạnh lùng rút chốt khóa cổng sắt: 'Đi đi, đừng làm phiền cuộc sống mới của tôi'.  
  > Tôi ôm chặt đứa con thơ vào lòng, giọt nước mắt hòa lẫn nước mưa buốt giá. Nhưng bà ta và anh ta không hề biết rằng... căn biệt thự năm mươi tỷ họ đang ở... người đứng tên trên sổ đỏ thực chất chính là tôi!"*

- **Cơ chế giữ chân:** Nén ức chế cực đại bằng đòn tấn công bạo lực và đứa trẻ thơ vô tội, sau đó bẻ lái ngoạn mục bằng "Khẩu súng sổ đỏ đứng tên vợ", tạo sự hả hê và thôi thúc người xem chờ xem ngày cô quay lại lấy lại nhà.

---

### TEMPLATE 3: NGHIỀN ÉP THÂN PHẬN & TIẾNG LÒNG BÓC PHỐT HÀO MÔN (Mind-Reading / Identity Crushing)
- **Đối tượng mục tiêu:** Nữ 18-28 (Gen Z, mê truyện Douyin độc tâm, sa điêu, nữ cường giả ngốc).
- **Cảm xúc kích hoạt:** Tò mò thích thú, cười sảng khoái, hưng phấn theo dõi kịch hay.
- **Giọng đọc đề xuất:** `vi-VN-HoaiMyNeural` (Biểu cảm châm biếm, diễn xuất hai mặt giữa lời nói và tiếng lòng).

#### 📜 Kịch Bản Chi Tiết:
- **[00:00 - 00:03] HOOK 3 GIÂY ĐẦU (14 từ):**
  > `[SFX: Tiếng ném xấp séc 'BẸP' + Tiếng nhịp tim đập dồn dập]`  
  > *"Mẹ chồng ném xấp séc mười tỷ vào mặt tôi: 'Cầm tiền rồi biến khỏi mắt con trai tôi ngay lập tức!'."*

- **[00:03 - 00:05] TIẾNG LÒNG BÓC PHỐT TỨC THÌ (16 từ):**
  > *"Bề ngoài tôi run rẩy khóc lóc, nhưng trong lòng thì reo hò: 'Ôi mẹ ơi, cho thêm mười tỷ nữa con bay sang sao Hỏa luôn!'."*

- **[00:05 - 00:30] CẦU NỐI BIẾN CỐ & CHÂM NGÒI BOM XUNG ĐỘT (86 từ):**
  > *"Tôi giả vờ ôm ngực nghẹn ngào: 'Mẹ... con và anh ấy là tình yêu đích thực...'.  
  > Nhưng trong đầu tôi lại gào thét: 'Trời ơi, bà mẹ chồng ngốc nghếch này sắp bị lão quản gia lừa sạch cổ phiếu rồi, con trai bà ta tuần sau cũng bị bạn thân chuốc thuốc phá sản, mau đưa tiền đây để tôi còn chuồn sớm!'.  
  > Đột nhiên, bà mẹ chồng khựng lại, đôi mắt trợn tròn nhìn tôi như nhìn thấy quái vật... Bà ta... bà ta có thể nghe thấy toàn bộ tiếng lòng của tôi!"*

- **Cơ chế giữ chân:** Đảo ngược mô-típ mẹ chồng nàng dâu truyền thống thành trò chơi tâm lý độc tâm hài hước, tạo sự tò mò mãnh liệt xem phản ứng của nhà chồng khi nghe hết bí mật gia tộc.

---

## V. MASTER PROMPT ENGINEERING TEMPLATES CHO HỆ THỐNG LLM SCRIPT GENERATION

Để tự động hóa sản xuất kịch bản 10 phút triệu view không bị AI "lạc đề" sang văn xuôi miêu tả cảnh vật, hệ thống Prompt cần được nâng cấp với các **rào chắn phủ định nghiêm ngặt (Negative Constraints)** và **khung toán học nhịp điệu**.

### 1. Master System Prompt: `SCRIPTWRITER_PROMPT_10MIN_PACED`

```python
# SCRIPTWRITER_PROMPT_10MIN_PACED (Bậc Thầy Biên Kịch Audio Drama Triệu View 10 Phút)

SCRIPTWRITER_PROMPT_10MIN_PACED = """Bạn là Bậc Thầy Biên Kịch Trưởng chuyên sáng tác AUDIO DRAMA TRIỆU VIEW định dạng 10 PHÚT (phân phối trên TikTok FYP cho tệp 80% Nữ giới 18-34 tuổi).
Nhiệm vụ: Viết kịch bản KỂ CHUYỆN AUDIO DÀI ĐÚNG 10 PHÚT (~3,460 đến 3,500 từ ở tốc độ đọc 1.5x) với cấu trúc giữ chân người xem đến giây cuối cùng.

=========================================
🚨 CÁC ĐIỀU CẤM KỴ TUYỆT ĐỐI (NEGATIVE CONSTRAINTS - VI PHẠM SẼ BỊ HỦY BỎ):
=========================================
1. CẤM TUYỆT ĐỐI TẢ CẢNH, TẢ THỜI TIẾT Ở 60 GIÂY ĐẦU:
   - KHÔNG mở đầu bằng: "Đó là một đêm mưa...", "Tiếng gió rít qua ô cửa...", "Ánh đèn đường hiu hắt...".
   - KHÔNG tả phòng ốc, nội thất, trang phục trước khi xung đột bùng nổ.
2. CẤM TUYỆT ĐỐI ĐỌC SƠ YẾU LÝ LỊCH HOẶC TRIẾT LÝ SỐNG:
   - KHÔNG mở đầu bằng: "Tôi tên là...", "Năm nay tôi...", "Hôn nhân là nấm mồ...".
3. CẤM NỮ CHÍNH YẾU ĐUỐI, QUỴ LỤY HOẶC THA THỨ CHO KẺ BỘI BẠC:
   - Tệp nữ 18-34 tuổi ghét cay ghét đắng nhân vật khóc lóc van xin hoặc tha thứ cho tra nam/tiểu tam. Nữ chính PHẢI lý tính, tự chủ tài chính và phản đòn quyết đoán.
4. CẤM TỪ NGỮ SIÊU VĂN BẢN (META WORDS):
   - CẤM nói: "Chào mừng các bạn đến với kênh", "Ở tập trước", "Hãy like và follow", "Đón xem phần 2". Toàn bộ văn bản 100% thuần cốt truyện tiểu thuyết.

=========================================
⚡ NGUYÊN TẮC VÀNG BẮT BUỘC TUÂN THỦ:
=========================================
1. QUY TẮC 0 - 3 GIÂY ĐẦU TIÊN (COLD OPEN CONFLICT):
   - 15 TỪ ĐẦU TIÊN BẮT BUỘC phải là: Một cú tát trời giáng [SFX: CHÁT!], một câu thoại áp chế tàn nhẫn của phản diện, hoặc một hành động bắt gian/đuổi nhà gây sốc cực độ.
2. CẤU TRÚC NHỊP ĐIỆU TOÁN HỌC 10 PHÚT (TỔNG 3,460 - 3,500 TỪ):
   - 00:00 - 00:05 (1-30 từ): Hook 3s giật gân, đập thẳng vào màng nhĩ.
   - 00:05 - 00:30 (31-170 từ): Khai hỏa biến cố chấn động (Ngoại tình, tráo con, đuổi nhà, di chúc ngầm).
   - 01:00 - 03:00 (171-1,040 từ): Cao trào 1 & Nén áp suất uất ức cực đại. Nữ chính bắt đầu tương kế tựu kế.
   - 04:00 - 07:00 (1,041-2,400 từ): Xung đột bước ngoặt. Cài cắm MICRO-HOOK MỖI 45 GIÂY (~250 từ/lần) để liên tục reset sự chú ý của người xem (tiết lộ bí mật mới, câu thoại sắc lẹm, bẫy tâm lý).
   - 08:00 - 09:55 (2,401-3,450 từ): Đại cao trào & Vả mặt giai đoạn 1. 
   - 09:55 (Giây 595): CLIFFHANGER CỰC HẠN. Cắt đúng 0.5 giây trước khi bí mật lớn nhất hoặc kết quả xét nghiệm được công bố!
3. KỸ THUẬT NGẮT NHỊP CHO GIỌNG ĐỌC AI 1.5X:
   - Câu văn gãy gọn: 8 - 18 từ/câu.
   - Sử dụng dày đặc dấu phẩy `,`, dấu ba chấm `...`, dấu gạch ngang ` - ` và dấu chấm than `!` tại các điểm nhấn kịch tính để Edge-TTS nhấn nhá, ngắt giọng truyền cảm.
   - Tỷ lệ đối thoại: 45% - 55% toàn bài. Thoại phải đanh thép, mang tính công kích hoặc bóc mẽ sắc bén.

=========================================
📋 CẤU TRÚC JSON ĐẦU RA BẮT BUỘC:
=========================================
{
  "title": "Tên kịch bản giật gân, chuẩn SEO tệp Nữ 18-34",
  "genre": "ME_CHONG" | "TRONG_SINH" | "NGOAI_TINH" | "HAO_MON_DOC_TAM",
  "word_count": 3480,
  "opening_hook_3s": "15 từ đầu tiên giật gân kèm SFX",
  "cliffhanger_line": "Câu ngắt lửng nghẹt thở cuối tập tại giây 595",
  "comment_magnet_cta": "👉 Câu hỏi phân cực 1 hoặc 2 đánh vào cảm xúc/đạo đức",
  "full_script_for_tts": "Toàn bộ văn bản kể chuyện 3,480 từ, đã tích hợp dấu ngắt nhịp và micro-hooks"
}
"""
```

---

### 2. Bảng Đối Chuẩn Anti-Pattern vs Golden Pattern (Cẩm Nang Kiểm Duyệt)

| Tiêu Chí | ❌ Kịch Bản Hỏng (Gây Drop-Off 4-7s) | ✅ Kịch Bản Chuẩn Triệu View (Retention > 60%) |
| :--- | :--- | :--- |
| **0 - 3 giây đầu** | *"Tiếng mưa đêm qua ngoài cửa sổ làm tôi nhớ lại câu chuyện buồn của cuộc đời mình..."* (18 từ buồn ngủ) | `[SFX: CHÁT!]` *"Mẹ chồng hắt thẳng bát canh gà sôi sùng sục vào mặt tôi: 'Ký đơn ly hôn rồi cút!'."* (15 từ bạo liệt) |
| **5 - 30 giây** | Kể lể quá trình yêu nhau 5 năm, hai gia đình quen biết nhau thế nào. | Tung ngay bằng chứng ngoại tình: Bạn thân đang mang thai 3 tháng với chồng, giấy tờ nhà bị sang tên lén. |
| **Nhịp điệu câu văn** | Câu phức kéo dài 30-40 từ không có dấu phẩy khiến giọng AI đọc liền một hơi mệt tai. | Câu ngắn 10-15 từ, ngắt nhịp bằng `...`, `,`, `!`. Tạo cảm giác dồn dập, nghẹt thở. |
| **Xây dựng Nữ chính** | Yếu đuối, quỳ gối van xin mẹ chồng và chồng rủ lòng thương. | Lạnh lùng thu thập chứng cứ, rút vốn, gọi kiểm toán và khóa mã cửa biệt thự. |
| **Điểm kết 10 phút** | Kết thúc êm đềm hoặc giải quyết xong xuôi: *"Và rồi tôi sống hạnh phúc một mình."* | Cắt ngang khi chiếc phong bì ADN sắp mở ra hoặc tiếng bước chân bí mật tiến vào phòng! |

---

## VI. ĐỀ XUẤT NÂNG CẤP HỆ THỐNG CODE (`core/prompts.py`, `core/script_generator.py`)

Để biến toàn bộ phương pháp luận trên thành sức mạnh kỹ thuật tự động hóa, Sub-Agent 8 đề xuất lộ trình nâng cấp 3 module trọng yếu:

### 1. Nâng Cấp `core/prompts.py`:
- Thay thế hoàn toàn quy tắc *"HOOK 5 - 10 GIÂY ĐẦU VÀNG"* bằng **"IN MEDIAS RES COLD OPEN 0 - 3 GIÂY (15 TỪ ĐẦU TIÊN CẤM TẢ CẢNH)"**.
- Thêm prompt chuyên sâu `SCRIPTWRITER_PROMPT_FEMALE_DRAMA` tích hợp sẵn tâm lý học độc giả nữ 18-34, cơ chế độc tâm (mind-reading), vả mặt hào môn, và bảo vệ quyền lợi tài sản.
- Bổ sung rào chắn kiểm duyệt tự động trong `REVIEWER_PROMPT`: Đánh trượt ngay nếu 30 từ đầu tiên có xuất hiện từ khóa tả thời tiết (*mưa, nắng, gió, đêm, mây...*) mà không có câu thoại hoặc xung đột.

### 2. Nâng Cấp `core/script_generator.py`:
- Thêm bộ đếm **Micro-Hooks Checker**: Kiểm tra trong mỗi phân đoạn 250 từ (~45 giây) xem có xuất hiện ít nhất một dấu hiệu kịch tính (dấu `!`, câu hỏi tu từ, hoặc từ khóa biến cố).
- Tích hợp SFX Cues tự động vào văn bản lồng tiếng: Định vị các vị trí vàng để chèn âm thanh va đập, tát, đổ vỡ, còi xe nhằm hỗ trợ Sub-Agent 4 (TTS) và Sub-Agent 5 (BGM) mix nhạc chính xác từng giây.

### 3. Điều Chỉnh Danh Mục Đề Tài Trong `core/knowledge_base.py`:
- Nâng tỷ trọng các thể loại phù hợp tệp Nữ 18-34:
  - Thể loại 4 (Mẹ chồng nàng dâu & Hôn nhân cực phẩm): Tăng tỷ trọng lên **35%**.
  - Thể loại 2 (Trọng sinh vả mặt tra nam & trà xanh): Tăng lên **30%**.
  - Thể loại 5 (Hào môn độc tâm & Nữ cường tài chính): Tăng lên **25%**.
  - Giảm tỷ trọng các thể loại Mạt thế sinh tồn, Trinh thám hình sự nặng nề xuống dưới **10%** cho đến khi kênh mở rộng thêm tệp nam.

---

## VII. KẾT LUẬN & ACTIONABLE ROADMAP

1. **Thành tựu phân tích:** Đã chỉ đúng tim đen của căn bệnh Drop-off 4-7 giây (do mở đầu bằng văn tả cảnh 30 giây đầu tiên trên luồng FYP lướt nhanh).
2. **Giải pháp đột phá:** Tái cấu trúc toàn bộ 10 phút thành 13 nhịp sóng cảm xúc (Micro-hooks 45 giây) và 3 mẫu Hook 3 giây sát thương cao sẵn sàng đưa vào sản xuất ngay lập tức.
3. **Sẵn sàng chuyển giao:** Tài liệu này cung cấp đầy đủ thông số cho Sub-Agent 4 (TTS ngắt nhịp), Sub-Agent 5 (BGM phối hợp sidechain), Sub-Agent 7 (Phụ đề giật gân), và Sub-Agent 10 (Master Growth Plan).
