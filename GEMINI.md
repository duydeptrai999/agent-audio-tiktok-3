# BỘ QUY CHUẨN & KINH NGHIỆM VẬN HÀNH HỆ THỐNG AUDIO TIKTOK (GEMINI.MD)
*Tài liệu hướng dẫn vĩnh viễn (Always-on Rules) tự động nạp vào bộ nhớ của Agent trong mọi phiên làm việc.*
*Phiên bản MASTER CODEX 8.5 - Chuyển hóa toàn diện sau Đại Khảo Sát 100 Audio Triệu View TikTok Việt Nam.*

> 📚 **FILE KINH NGHIỆM GỐC DUY NHẤT BẮT BUỘC ĐỌC TRƯỚC KHI BIÊN KỊCH / LÀM VIDEO**:
> 🌟 **[DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md](file:///c:/Users/duydo/OneDrive/Tài%20liệu/idk/docs/DAI_KHAO_SAT_100_AUDIO_TIKTOK_TRIEU_VIEW_VA_TOI_UU_TEAM_AGENT.md)** - **Đại Khảo Sát 100 Audio Triệu View & Cẩm Nang Tối Ưu Team Agent (Codex 8.0)**:
>    * Toàn bộ phân tích chuyên sâu 100 Audio dẫn đầu xu hướng TikTok Việt Nam (*Túi Mù Audio, Dứa Audio, AnAn Audio, Dịt Dàng Audio, Tâm Hồn Ăn Uống, Truyện Audio TTH...*).
>    * Giải mã 5 Trụ Cột Đa Chiều: Kịch bản khẩu ngữ đời thường, Âm học Edge-TTS nhịp thở tự nhiên, BGM ducking -22dB, Video nền ASMR thôi miên, Comment magnets phân cực.
>    * Deep Dive chi tiết 1 Audio mẫu mực (Túi Mù Audio - 1.13M views) từ giây 0 đến kết thúc.
>    * Ma trận 6 Subagent tối ưu toàn diện diệt trừ 100% kịch bản sượng trân, ngượng mồm, hoạt hình ba xu!

---

## 0. QUY TẮC THỜI LƯỢNG SỐNG CÒN: CHUẨN 30 PHÚT ĐIỆN ẢNH (ZERO 49S TOLERANCE)

> 🚨 **CẢNH BÁO TỐI CAO TỪ NGHIÊN CỨU 100 AUDIO TRIỆU VIEW THỰC TẾ**:
> 100% video truyện viral triệu view tại Việt Nam (*Dứa Audio, Túi Mù Audio, Tâm Hồn Ăn Uống, Truyện Audio TTH, AnAn Audio, Dịt Dàng Audio...*) đều có thời lượng từ **25 đến 45 phút** (khi chia 3 tập tương đương **8 - 12 phút / tập**).
> Khán giả nghe audio TikTok trong lúc làm việc nhà, nấu ăn, đi xe hoặc đi ngủ; họ cần một hành trình cảm xúc trọn vẹn, sâu sắc và nghẹt thở. Các video 40 - 50 giây bị người nghe tẩy chay vì hời hợt, làm hỏng tỷ lệ giữ chân và vi phạm chính sách video dài (TikTok Long-Form Program)!

1. **Độ Dài Kịch Bản Bắt Buộc**:
   - **Mỗi tập (Part 1, Part 2, Part 3)**: TỐI THIỂU **1.400 từ đến 2.200 từ** (thời lượng đọc thực tế **8 đến 12 phút / tập**).
   - **Tổng cả 3 tập**: TỐI THIỂU **4.500 từ đến 6.500 từ** (tổng thời lượng **25 đến 35 phút** cho trọn bộ).
   - **LỆNH CẤM TUYỆT ĐỐI**: Bất kỳ kịch bản nào dưới 1.200 từ/tập hoặc tổng dưới 3.600 từ ĐỀU BỊ COI LÀ LỖI KỸ THUẬT NGHIÊM TRỌNG và bị `script_quality_gate.py` tự động từ chối xuất bản ngay lập tức!

2. **Tốc Độ Đọc Edge-TTS Chuẩn**:
   - Giọng Nữ `vi-VN-HoaiMyNeural`: **rate="+5%" đến "+8%"** (160 - 170 từ / phút). Giọng ấm, truyền cảm, tâm sự, châm biếm sâu cay.
   - Giọng Nam `vi-VN-NamMinhNeural`: **rate="+3%" đến "+6%"** (150 - 160 từ / phút). Giọng trầm ấm, đĩnh đạc, bí ẩn, phong thái trinh thám.
   - TUYỆT ĐỐI CẤM tăng tốc độ lên 1.5x (rate="+50%"). Giọng đọc phải có độ ấm, nhịp thở, độ lắng và tự nhiên như người thật.
   - TUYỆT ĐỐI KHÔNG sử dụng `rubberband` pitch-shifting trên giọng đọc (gây méo tiếng kim loại, robot giật cục).

3. **Âm Lượng Nhạc Nền (BGM Ducking)**:
   - Cố định ở ngưỡng **-22dB đến -24dB** (nhỏ hơn giọng đọc ít nhất 18dB), không át tiếng, không có hiệu ứng giật mình chói tai.

4. **Hình Ảnh Nền (B-roll Thôi Miên Thị Giác)**:
   - GIỮ NGUYÊN BẢN 100% KHUNG HÌNH GỐC 16:9 (1920x1080) CỦA VIDEO, TUYỆT ĐỐI CẤM KÉO RA 9:16: Ưu tiên 4 thể loại triệu view: ASMR làm bánh & nấu ăn, điêu khắc mỹ nghệ thủ công, mưa rơi quán cà phê lofi, dọn dẹp nhà cửa/rửa thảm tối giản.

---

## 1. NGUYÊN TẮC VÀNG VỀ BIÊN KỊCH ĐỜI THƯỜNG (REALISTIC SCRIPTWRITING CODEX 8.5)

> 🚨 **TRIỆT TIÊU VĨNH VIỄN BỆNH "KỊCH BẢN ĐẾN CHÍNH MÌNH NGHE CÒN ĐÉO THẨM ĐƯỢC"**:
> Khán giả nghe chuyện audio là để nghe chuyện **ĐỜI NGƯỜI, CẢM XÚC THẬT, BẤT CÔNG GIA ĐÌNH, PHẢN BỘI TÌNH CẢM, VẢ MẶT HẢ DÊ, TÌNH YÊU NGỌT NGÀO HOẶC KỲ ÁN LY KỲ**.
> TUYỆT ĐỐI CẤM kịch bản hoạt hình hóa ba xu, nhân vật ác ngô nghê, chính diện khoe khoang kệch cỡm!

### 🌟 8 THỂ LOẠI TRIỆU VIEW THỰC CHIẾN ĐƯỢC CHỨNG MINH:
1. **Sa Điêu / Tiếng Lòng / Hài Công Sở**: Cả công ty giả nghèo chỉ mình tôi gánh KPI, Đọc tâm thuật nghe tiếng lòng sếp, Cá mặn biến show hẹn hò thành ăn chực.
2. **Trọng Sinh / Vả Mặt Báo Thù**: Trọng sinh nghe lời bố mẹ nhường tra nam cho em gái, Kiếp này làm ác nữ dẹp loạn cực phẩm, Phú bà trùng sinh vả mặt tra nam.
3. **Mẹ Chồng Nàng Dâu / Gia Đấu Đời Thực**: Mẹ chồng tính toán tiền ăn từng bữa, Em chồng mượn túi hiệu đi hẹn hò, Thức tỉnh ly hôn đòi lại tài sản riêng.
4. **Thật Giả Thiên Kim / Hoán Đổi Vận Mệnh**: Thiên kim thật từ chối diễn kịch hào môn, Con gái nuôi thích đóng vai nạn nhân bị bóc trần, Nhìn thấu âm mưu chiếm đoạt.
5. **Hào Môn Tổng Tài / Cưới Trước Yêu Sau**: Cá mặn gả cho sếp tổng nghiện vợ, Đôi bạn thân cùng gả vào hào môn, Bản hợp đồng hôn nhân độc lập tài chính.
6. **Thanh Xuân Vườn Trường / Học Bá Oan Gia**: Tỏ tình học bá thất bại yêu luôn đại ca trường, Học bá nghèo bận thi thủ khoa không rảnh tiếp đám bắt nạt.
7. **Confession Bóc Phốt / Drama Đời Thực**: Đứa bạn phông bạt sống ảo quỵt nợ, Tiểu tam có học thức ngông cuồng và cái kết, Buổi ra mắt gia đình người yêu éo le.
8. **True Crime / Kỳ Án Pháp Y / Tâm Lý Tội Phạm**: Bí ẩn 50 mét biến mất trước trung tâm thương mại, Vết son môi trên ly rượu vụ án đêm mưa, Tâm lý kẻ đa nhân cách.

---

### 🪝 TRIỆT TIÊU HIỆN TƯỢNG TRÙNG LẶP MỞ ĐẦU (ZERO OPENING REPETITION CODEX):
1. **CẤM 100% CÁC CÔNG THỨC MỞ ĐẦU MÁY MÓC RẬP KHUÔN**:
   - CẤM mẫu: `'[Câu trích dẫn]!' - Đúng X giờ sáng giữa đêm...`
   - CẤM mẫu: `Tôi vừa [bưng/đặt] ... thì ...` lặp lại trên nhiều truyện khác nhau.
   - CẤM mẫu: `Tiếng [âm thanh] vang lên ..., khi ...` sao chép máy móc.
2. **MỖI BỘ TRUYỆN PHẢI CÓ CÂU MỞ ĐẦU ĐỘC BẢN**:
   - 15 từ đầu tiên bắt buộc phải giật ngay màng nhĩ người nghe bằng một hành động dứt khoát hoặc mâu thuẫn sống còn ĐẶC TRƯNG của riêng cốt truyện đó.
3. **TẬP 2 VÀ TẬP 3 TUYỆT ĐỐI KHÔNG LẶP LẠI CÂU CUỐI TẬP TRƯỚC**:
   - CẤM lặp lại nguyên văn câu thoại cliffhanger ở giây 0.0 của tập tiếp theo.
   - Tập 2 và Tập 3 bắt đầu ngay lập tức bằng diễn biến tâm lý hoặc phản ứng tiếp nối của nhân vật.
4. **CẤM 100% ĐOẠN ĐỆM FILLER CHÉP DÁN (ZERO INJECTED FILLER)**:
   - Nghiêm cấm chép dán các đoạn văn độn từ rác (*"Thẩm Băng Tuyết thong thả nhấp ngụm rượu vang..."*, *"Gió đêm từ dòng sông Nam Giang..."*, *"Mọi toan tính bẩn thỉu..."*). Kịch bản phải được phát triển bằng tình tiết thực sự.

---

### ❌ NHỮNG ĐIỀU TUYỆT ĐỐI CẤM (ZERO TOLERANCE):
1. **CẤM Hoạt Hình Hóa & Tình Tiết Ngô Nghê**:
   - Tuyệt đối CẤM: Kẻ ác ác ngu xuẩn như hoạt hình (mẹ chồng mang 3 cổ gà héo úa; em chồng nhảy lên sofa vẽ bậy; giơ điện thoại quay 4K dọa sếp; kéo công an và 4 vệ sĩ bọc thép vào tiệc gia đình; cô bé 18 tuổi rút séc 100 tỷ).
   - Mọi giải pháp tài chính và pháp lý phải có căn cứ: Sổ đỏ đứng tên mình, sao kê tài khoản ngân hàng, hợp đồng ủy quyền, trích xuất camera an ninh, chứng cứ kiểm toán.
2. **CẤM Cơ Khí Dị Hợm & Báo Cáo Kỹ Thuật**:
   - Tuyệt đối CẤM: Máy đo sóng hạ âm 18Hz, đáy lồng mèo bọc chì 3 phân, máy phân tích phổ FFT, van xả áp lực âm, buồng nitơ lỏng trong chung cư.
3. **CẤM Câu Dài Lắt Léo Khiến Edge-TTS Đọc Hụt Hơi**:
   - Tuyệt đối CẤM viết câu trên 25 từ không có dấu phẩy.
   - Phải viết câu ngắn gọn, tự nhiên từ **10 đến 18 từ/câu**, ngắt nghỉ đúng ngữ pháp tiếng Việt bằng dấu phẩy `,` và dấu chấm `.`.
4. **CẤM Sáo Ngữ Convert Trung Quốc & Cải Lương**:
   - Cấm: *"khí chất bức người"*, *"thập phần"*, *"bất giác"*, *"cười lạnh một tiếng"*, *"đứng sững như trời trồng"*, *"tiện nhân"*, *"đồ lăng loàn"*, *"quân giết người quân vô phúc"*, *"bàn tay to bè giáng xuống trong gang tấc"*, *"nước mắt ứa ra vì cay đắng tột cùng"*, *"thập tử nhất sinh"*, *"đồng tử co rút kịch liệt"*, *"bút máy nạm kim cương"*, *"gào khóc như lợn bị chọc tiết"*, *"bò lê lết ôm mũi giày"*.
5. **BẮT BUỘC 100% TỰ SỰ NGÔI THỨ NHẤT ("TÔI")**:
   - 100% drama đời thực, gia đấu, mẹ chồng, ly hôn, sa điêu, confession bắt buộc viết bằng ngôi thứ nhất ("Tôi") tạo sự đồng cảm chân thật.
   - Tuyệt đối CẤM ngôi thứ ba convert dịch máy xa lạ khiến người nghe ngượng tai ("không thẩm được").
6. **CẤM 100% Nội Dung Chính Trị (Zero Politics Guard)**:
   - Tuyệt đối CẤM nhắc đến: đảng phái, chính phủ, bộ ngoại giao, đại sứ quán, quân đội, chế độ, biểu tình, bầu cử.

---

### 🎨 2. QUY CHUẨN ĐỒ HỌA & BAO BÌ THỊ GIÁC (PACKAGING DESIGN SYSTEM CODEX 8.5)

> 🚨 **ĐẠI QUY TẮC SỐNG CÒN: GIỮ NGUYÊN KHUNG HÌNH GỐC CỦA VIDEO (ZERO CROP / ZERO STRETCH / ZERO FIT)**:
> - **TUYỆT ĐỐI GIỮ NGUYÊN VIDEO GỐC**: CẤM 100% các hành vi kéo dãn video, CẤM crop xén mất góc, CẤM cưỡng bức scale ép fit (như scale=1080:1920) làm biến dạng hay méo mó khung hình!
> - Khung hình video gốc như thế nào (16:9 ngang, 9:16 dọc, 4:3, 1:1) thì **GIỮ NGUYÊN BẢN 100%**, chỉ lồng thêm giọng đọc AI và BGM ducking.
> - **KHÔNG làm thumbnail ảnh tĩnh rời**: Để tránh bị TikTok Studio kéo dãn méo hình khi upload cover, TikTok tự động lấy trực tiếp frame nguyên bản từ video MP4 đã có Header Title và Mô Tả thanh lịch.

1. **Bộ Font Chuẩn Độc Tôn: Be Vietnam Pro**:
   - Tên Phim (Main Title): Font `BeVietnamPro-ExtraBold` hoặc `Black` (46pt - 50pt), trắng tinh khiết `(255, 255, 255)`, viền vi mảnh sắc nét (sharp micro-stroke 2px `rgb(12, 16, 24)`), căn giữa, tối đa 2 dòng.
   - Mô Tả Phim / Tập (Subtitle): Font `BeVietnamPro-SemiBold` (30pt - 34pt), màu pastel dịu mắt theo thể loại, viền 2px chống lóa, căn giữa.
   - Huy Hiệu Tập (Episode Pill Badge): Bo tròn capsule hiện đại (`radius=ph//2`), viền trắng mờ tinh tế 1px, màu nền theo thể loại, chữ sắc nét, KHÔNG bóng đen nhòe.
2. **Loại Bỏ Hoàn Toàn Hộp Đen Thô Cứng & Bóng Đen Nhòe (Zero Hard Box & Zero Muddy Shadow)**:
   - TUYỆT ĐỐI CẤM: `drawbox=color=black@0.76` hoặc các dải gradient đen sẫm che tối mịt video B-roll.
   - THAY THẾ BẰNG: Dải scrim siêu nhẹ ở đỉnh (alpha max chỉ 55, mờ dần về trong suốt tại y=360), kết hợp micro-stroke 2px. Video nền ASMR giữ nguyên 100% độ sáng, độ trong và màu sắc tự nhiên.
3. **Bảng Màu Nhận Diện Theo Thể Loại (Genre Palettes)**:
   - `SA_DIEU` / `HAO_MON`: Vàng Ánh Kim Hoàng Gia (`#FFE066`, `#F59E0B`).
   - `THANH_XUAN` / `CHUA_LANH`: Xanh Cyan Ngọc Bích Tươi Sáng (`#38BDF8`, `#0284C7`).
   - `GIA_DAU` / `TRONG_SINH`: Hồng Đào / Đỏ Hồng Quyền Lực (`#FB7185`, `#E11D48`).
   - `TRINH_THAM` / `TRUE_CRIME`: Hổ Phách Cảnh Báo (`#FBBF24`, `#D97706`).
   - `KINH_DI` / `QUAI_DAM`: Đỏ Thẫm Máu Rùng Rợn (`#F43F5E`, `#BE123C`).
4. **Vùng An Toàn Top Safe Zone (y = 135 .. 380)**:
   - Toàn bộ khối tiêu đề nằm chuẩn bên dưới thanh tab "Following | For You" của TikTok, không bị giao diện che khuất, giải phóng 80% màn hình phía dưới cho B-roll thôi miên và phụ đề động.

---

### 🎙️ 3. QUY CHUẨN ÂM HỌC & GIỌNG ĐỌC AI (EDGE-TTS ACOUSTIC FLOW)
1. **Tự Động Nhận Diện & Phân Bổ Voice Chuẩn Xác**:
   - `vi-VN-HoaiMyNeural`: Giọng nữ ấm áp, truyền cảm, tâm sự, châm biếm sâu cay. Dành cho Sa điêu, Gia đấu, Mẹ chồng, Trọng sinh, Hào môn, Thanh xuân, Confession (nhân vật kể chuyện là nữ). Tốc độ `rate="+5%"` đến `"+8%"`.
   - `vi-VN-NamMinhNeural`: Giọng nam trầm ấm, đĩnh đạc, bí ẩn. Dành cho True Crime, Kỳ án, Trinh thám, Kinh dị quái đàm, Mạt thế sinh tồn (nhân vật kể chuyện là nam). Tốc độ `rate="+3%"` đến `"+6%"`.
2. **Loại Bỏ Méo Tiếng Kim Loại (Zero Metallic Distortion)**:
   - TẮT toàn bộ bộ lọc `rubberband` pitch-shifting trên rãnh giọng nói. Giữ nguyên độ ấm, độ trong trẻo và nhịp thở nguyên bản của AI.
3. **Nhạc Nền Ducking**: Cố định **-22dB đến -24dB** (nhỏ hơn giọng nói ít nhất 18dB). Lofi piano nhẹ nhàng cho drama/chữa lành; Suspense dark ambient cho kỳ án/trinh thám.

---

### 📝 4. QUY CHUẨN MÔ TẢ & BÌNH LUẬN ĐỘNG THEO TẬP (DYNAMIC CAPTIONS & MAGNETS)
1. **Cấu Trúc Mô Tả Bài Đăng TikTok Đa Tầng Sang Trọng**:
   - Dòng 1: `[TẬP X] Tên Phim`
   - Dòng 2: `📖 Mô tả phim / Tập`
   - Dòng 3: `💬 Câu hỏi thảo luận / Bẫy tâm lý kích thích tương tác theo tập`
   - Dòng 4: `👉 Cắm tai nghe thưởng thức trọn bộ tại kênh!`
   - Dòng 5: `#audiotruyen #kechuyen #xuhuong #fyp #tagtheloai`
2. **CẤM Tuyệt Đối Câu Hỏi Robot "Bình Luận 1 Hoặc 2"**:
   - Kêu gọi tranh luận đời thường tự nhiên theo đúng tâm lý người nghe, kích thích tương tác giữ chân người xem.

---

### 👥 5. TỔ CHỨC TEAM AGENT BIÊN KỊCH CHUYÊN NGHIỆP (6 SUBAGENTS CODEX 8.5)

```mermaid
flowchart LR
    A["Agent 1: Trend & Conflict Scout"] --> B["Agent 2: Realistic Plot Architect"]
    B --> C["Agent 3: Spoken Dialogist"]
    C --> D["Agent 4: Edge-TTS Acoustic Director"]
    D --> E["Agent 5: Hypnotic Visual Curator"]
    E --> F["Agent 6: Ruthless Taste Auditor"]
    F -->|"Đạt 10/10 Thẩm Mỹ Tai Nghe & Bao Bì Đẹp"| G["TikTok Video Release"]
    F -.->|"Cringe / Sượng trân / Chữ nền đen xấu"| C
```

1. **Agent 1: Real-life Conflict Scout (Trinh Sát Đời Sống & Bẫy Tâm Lý)**: Săn lùng mâu thuẫn thực tế từ 8 thể loại triệu view, chốt câu Hook 3s độc bản theo cốt truyện, triệt tiêu 100% mẫu câu rập khuôn.
2. **Agent 2: Realistic Plot Architect (Kiến Trúc Sư Cốt Truyện Đời Thật)**: Dựng dàn ý 3 hồi chuẩn 1.400 - 2.000 từ/tập, logic tâm lý người thật, cắt tập Action-Apex Cliffhanger, loại bỏ 100% đoạn lặp ở giây 0.0 của Tập 2 & 3.
3. **Agent 3: Natural Spoken Dialogist (Bậc Thầy Khẩu Ngữ & Mỏ Hỗn Tri Thức)**: Chắp bút câu thoại đời thường thuần Việt, độc thoại nội tâm sắc bén, xóa sạch sáo ngữ cải lương và đoạn đệm filler chép dán.
4. **Agent 4: Edge-TTS Acoustic & Prosody Director (Đạo Diễn Ngữ Âm & Nhịp Thở AI)**: Tự động ghép giọng nữ Hoài My / nam Nam Minh theo nhân vật xưng 'Tôi', tắt hoàn toàn rubberband méo tiếng, câu 10-18 từ, BGM ducking -22dB đến -24dB.
5. **Agent 5: Hypnotic Visual & Packaging Curator (Giám Tuyển B-roll & Bao Bì Thị Giác)**: 
   - Giám tuyển 4 thể loại video nền ASMR 1080x1920 (9:16).
   - Thiết kế Thumbnail & Video Header Overlay bằng font **Be Vietnam Pro**, không dùng hộp đen, dải chuyển sắc mềm, đổ bóng chữ Gaussian, huy hiệu bo tròn (Pill Badge), bảng màu theo thể loại.
6. **Agent 6: Ruthless Taste Auditor & Cringe Gatekeeper (Cổng Thẩm Mỹ Khó Tính / Diệt Cringe & Xấu)**:
   - Cổng kiểm định tối cao: Kiểm tra độ dài (>= 4.200 từ), thẩm mỹ tai nghe người thật, độ đẹp của tiêu đề/mô tả/hình ảnh. Chặn đứng 100% kịch bản ngượng mồm, sượng trân hoặc chữ trên nền đen xấu!

---
*Ghi nhớ vĩnh viễn: Khán giả không bao giờ trả tiền thời gian cho một câu chuyện hoạt hình ngô nghê hay một video có chữ trên nền đen xấu xí. Họ chỉ ở lại vì sự chân thật, cảm xúc đời người, đối đáp thông minh và hình ảnh đóng gói tinh tế!*
