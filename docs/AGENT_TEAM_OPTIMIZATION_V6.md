# TỐI ƯU HÓA TOÀN DIỆN ĐỘI NGŨ 10 SUBAGENT TEAMWORK (PHIÊN BẢN 6.0)
## KẾT TINH TỪ NGHIÊN CỨU THỰC TẾ 100 AUDIO TRUYỆN VIRAL TRIỆU VIEW TIKTOK VIỆT NAM

---

### TỔNG QUAN NÂNG CẤP HỆ THỐNG AGENT:
Dựa trên dữ liệu thực chứng từ 88+ case study triệu view (Dứa Audio, Túi Mù Audio, Tâm Hồn Ăn Uống, Truyện Audio TTH...) và nguyên nhân gốc rễ dẫn đến các video 49s vừa qua, toàn bộ 10 subagent trong `.agents/teamwork/` được nâng cấp quy chuẩn hoạt động đồng bộ:

```
[Subagent 1: Data Auditor] ──> [Subagent 8: Script Master] ──> [Subagent 4: TTS Engineer]
            │                                 │                               │
            ▼                                 ▼                               ▼
[Subagent 2: Retention]      [Subagent 3: Audience Specialist]   [Subagent 5: BGM Specialist]
            │                                 │                               │
            ▼                                 ▼                               ▼
[Subagent 7: Subtitle]       [Subagent 6: Visual Curator]        [Subagent 9: Playlist Architect]
                                              │
                                              ▼
                             [Subagent 10: Master Strategist & Gatekeeper]
```

---

### 1. SUBAGENT 1: DATA & SYSTEM METRIC AUDITOR (`subagent_1_data_auditor`)
- **Nhiệm vụ mới**: Giám sát dữ liệu và thời lượng toán học của toàn bộ các file audio trước khi render video.
- **Tiêu chuẩn kiểm duyệt mới (Gate Requirement)**:
  - Độ dài mỗi tập (Part 1, 2, 3): **TỐI THIỂU 1.400 TỪ** (tương đương >= 8 phút ở tốc độ 1.1x).
  - Tổng độ dài series 3 tập: **TỐI THIỂU 4.500 TỪ** (tương đương >= 25 - 30 phút audio).
  - Bất kỳ kịch bản nào dưới 1.200 từ/tập lập tức bị gắn cờ `CRITICAL_FAILURE: SCRIPT_TOO_SHORT` và chặn quy trình sản xuất ngay lập tức.
- **Kiểm tra mã nguồn**: Loại bỏ hoàn toàn các module `cycles_11_to_50_masterpieces.py` (vốn là bản tóm tắt 200 từ) ra khỏi danh sách nạp truyện ưu tiên.

---

### 2. SUBAGENT 2: RETENTION DIAGNOSTICIAN (`subagent_2_retention_diagnostician`)
- **Nhiệm vụ mới**: Thiết kế và kiểm soát biểu đồ giữ chân thính giả (Retention Curve) xuyên suốt 8 - 10 phút / tập.
- **Quy luật Micro-Pacing 45 Giây (Micro-Hook Escalation)**:
  - Cứ mỗi 100 - 130 từ (45-60 giây đọc), câu chuyện BẮT BUỘC thả một biến số vật lý mới: một tiếng bước chân dừng lại, một vệt mực nhòe, một tin nhắn báo biến động số dư, một ánh mắt nhìn trộm qua khe cửa.
  - CẤM các đoạn văn suy nghĩ nội tâm hoặc miêu tả phong cảnh kéo dài quá 60 từ.
- **Cơ Chế Cliffhanger Đỉnh Điểm (Action-Apex Cliffhanger)**:
  - Tập 1 PHẢI ngắt đúng khoảnh khắc biến cố kích hoạt (Inciting Incident) đẩy nhân vật vào thế chân tường.
  - Tập 2 PHẢI ngắt ở "Thời khắc đen tối nhất" (Darkest Hour) ngay trước khi chiếc bẫy phản đòn được kích hoạt.
  - Tuyệt đối không ngắt tập khi nhân vật đi ngủ, thở dài hoặc suy ngẫm miên man.

---

### 3. SUBAGENT 3: AUDIENCE PSYCHOLOGY SPECIALIST (`subagent_3_audience_specialist`)
- **Nhiệm vụ mới**: Định hình tâm lý và thói quen nghe của thính giả Việt Nam trên TikTok:
  - **Hành vi nghe**: 85% người nghe bật audio trong lúc làm việc nhà (rửa bát, nấu ăn, dọn dẹp), đi xe buýt / xe máy, hoặc nằm nghe trước khi đi ngủ.
  - **Nhu cầu cảm xúc**:
    - Ban ngày (Slots 1-7): Cần sự sảng khoái (vả mặt kẻ ác, tiểu tam bị trừng trị, mẹ chồng thấu hiểu, nỗ lực thanh xuân được đền đáp).
    - Ban đêm (Slots 8-10): Cần sự hồi hộp, gay cấn, giải mã bí ẩn hoặc rùng rợn tâm linh đô thị (kỳ án trinh thám, phòng kín quái đàm).
- **Ngôn ngữ thuần Việt**: Loại bỏ 100% từ ngữ convert Trung Quốc (không dùng *"khí chất bức người"*, *"đứng sững như trời trồng"*, *"bất giác"*, *"sét đánh ngang tai"*). Thay bằng tiếng Việt đời thường, sắc sảo và hiện đại.

---

### 4. SUBAGENT 4: TTS & ACOUSTIC CADENCE ENGINEER (`subagent_4_tts_engineer`)
- **Nhiệm vụ mới**: Tinh chỉnh động cơ âm học Edge-TTS để giọng đọc truyền cảm, có hồn và tự nhiên như người thật.
- **Thiết lập Tốc Độ Đọc Chuẩn**:
  - Tốc độ đọc: **rate="+5%" đến "+10%"** (tương đương 160 - 180 từ / phút).
  - **TUYỆT ĐỐI CẤM đọc 1.5x (rate="+50%")**: Việc đẩy tốc độ lên 1.5x làm giọng đọc bị méo, nuốt chữ, mất nhịp cảm xúc và làm giảm một nửa thời lượng video của kênh!
- **Kỹ Thuật Ngắt Nghỉ Sinh Học**:
  - Tự động chèn các ký tự ngắt hơi (`,`, ` - `, `:`) sau mỗi cụm từ 10 - 14 từ.
  - Chốt hạ câu kịch tính bằng thanh trắc dứt khoát.
- **Chỉ Định Giọng Đọc Chuẩn**:
  - `vi-VN-NamMinhNeural`: Giọng nam trầm ấm, đĩnh đạc, bí ẩn dành cho Trinh thám, Kỳ án, Quái đàm, Mạt thế.
  - `vi-VN-HoaiMyNeural`: Giọng nữ truyền cảm, mượt mà, sâu lắng dành cho Gia đấu, Chữa lành, Thanh xuân, Hào môn.

---

### 5. SUBAGENT 5: BGM & SOUNDSCAPE SPECIALIST (`subagent_5_bgm_specialist`)
- **Nhiệm vụ mới**: Quản lý nhạc nền và hiệu ứng âm thanh môi trường (Soundscape).
- **Quy chuẩn Âm lượng Nhạc Nền (BGM Ducking)**:
  - Âm lượng BGM cố định ở ngưỡng: **-22dB đến -24dB** (nhỏ hơn giọng đọc từ 18dB đến 20dB).
  - Không để BGM lấn át giọng kể; nhạc nền đóng vai trò làm đệm cảm xúc (Emotional Undercurrent).
- **Phối Khí Theo Thể Loại**:
  - Hài hước / Sa điêu: Lofi Jazz nhẹ nhàng, Marimba dí dỏm.
  - Thanh xuân / Chữa lành: Piano Acoustic trong trẻo, tiếng mưa rơi dịu nhẹ.
  - Gia đấu / Vả mặt: Cello u uất chuyển sang dàn dây dồn dập ở cao trào.
  - Trinh thám / Kỳ án: Dark Ambient Synth, Drone bass trầm tạo áp lực phòng kín.
  - CẤM các hiệu ứng âm thanh giật mình chói tai (còi xe, tiếng thét the thé).

---

### 6. SUBAGENT 6: VISUAL & B-ROLL CURATOR (`subagent_6_visual_curator`)
- **Nhiệm vụ mới**: Tuyển chọn và ghép nối video nền (B-roll) chuẩn chất lượng điện ảnh 1080x1920 dọc.
- **Top 4 Danh Mục B-roll Thôi Miên Thị Giác (Hypnotic Visuals)**:
  1. *ASMR Làm Bánh & Nấu Nướng*: Cận cảnh nhào bột, quết kem, đổ sốt caramen, xếp dâu tây (chuẩn phong cách các kênh triệu view Tâm Hồn Ăn Uống, Truyện Audio TTH).
  2. *Thủ Công Mỹ Nghệ & Điêu Khắc*: Khắc gỗ nghệ thuật, mài ngọc, gọt xà phòng, đổ khuôn resin.
  3. *Không Gian Mưa & Đêm Đô Thị*: Mưa rơi trên khung cửa sổ cà phê, ánh đèn vàng ấm cúng, bàn học đêm.
  4. *Hoạt Hình 2D Nghệ Thuật Vòng Lặp*: Nhân vật ngồi uống trà, vẽ tranh, mèo nằm ngủ bên cửa sổ.
- **Tiêu Chuẩn Kỹ Thuật**: Video sắc nét 1080x1920, chuyển động êm dịu, không bị giật lag, không chứa watermark hay phụ đề nước ngoài rối mắt.

---

### 7. SUBAGENT 7: SUBTITLE & LAYOUT DESIGNER (`subagent_7_subtitle_designer`)
- **Nhiệm vụ mới**: Thiết kế bố cục hiển thị phụ đề động và tiêu đề nhận diện tập trên màn hình.
- **Quy chuẩn Phụ đề Động (Kinetic Captions)**:
  - Hiển thị từng cụm **3 - 5 từ** đồng bộ theo giọng đọc.
  - Phông chữ dày dặn (Bold Sans-Serif), màu trắng viền đen mỏng, vị trí đặt ở 1/3 phía dưới màn hình (tránh nút like/share của TikTok).
- **Khung Tiêu Đề Đỉnh Màn Hình (Series Header)**:
  - Luôn có banner nổi bật: `[TẬP 1/3: TÊN BỘ TRUYỆN]` giúp người xem nhận biết tập và dễ dàng tìm kiếm trọn bộ.

---

### 8. SUBAGENT 8: SCRIPTWRITING MASTER (`subagent_8_script_master`)
- **Nhiệm vụ mới**: Kiến tạo các bộ kịch bản đoản văn dài chuẩn 30 phút điện ảnh, loại bỏ toàn bộ các bản tóm tắt sơ sài.
- **Cấu Trúc Độ Dài Tuyệt Đối**:
  - Tập 1: 1.500 - 2.000 từ (~8 - 10 phút audio).
  - Tập 2: 1.500 - 2.000 từ (~8 - 10 phút audio).
  - Tập 3: 1.500 - 2.000 từ (~8 - 10 phút audio).
  - Tổng series: 4.500 - 6.000 từ (~25 - 30 phút audio).
- **Mở Đầu 3 Giây Bắt Buộc (The 3s Physical Hook)**:
  - 15 từ đầu tiên phải chứa một dị thường vật chất hoặc hành động đảo nghịch.
- **Chekhov's Gun & Chuỗi Hành Trình Vật Chứng**:
  - Mọi mâu thuẫn và lật kèo phải neo vào vật thể vật lý cụ thể (bản di chúc dính vết cà phê, chiếc thìa bạc sủi bọt, thẻ nhớ giấu trong đế giày, biên lai chuyển khoản ngân hàng).
- **Đối Thoại Có Dao Găm**:
  - Thoại ngắn 5 - 14 từ, đanh thép, ngầm gài bẫy, không diễn giải bệnh án dài dòng.
- **100% Zero Chính Trị & Giải Quyết Bằng Trí Tuệ Dân Sự**:
  - Không liên quan đến chính trị, đảng phái, nhà nước. Phá án bằng khoa học công nghệ, pháp y, kiểm toán và chuyên môn đời thường.

---

### 9. SUBAGENT 9: PLAYLIST & SERIES ARCHITECT (`subagent_9_playlist_architect`)
- **Nhiệm vụ mới**: Quy hoạch danh sách phát (TikTok Playlists) để tối ưu hóa tỷ lệ chuyển đổi thính giả từ Tập 1 sang Tập 2 và Tập 3.
- **Quy tắc Đặt Tên & Nhãn Dán Thumbnail**:
  - Thẻ nhận diện rõ ràng: `#Tap1, #Tap2, #Tap3` trong caption và ảnh bìa.
  - Tự động thêm video vào đúng Playlist của series trên kênh TikTok.

---

### 10. SUBAGENT 10: MASTER STRATEGIST & GATEKEEPER (`subagent_10_master_strategist`)
- **Nhiệm vụ mới**: Tổng chỉ huy vận hành và là "Người gác cổng tối cao" (Ultimate Quality Gatekeeper).
- **Quyền Lực Phủ Quyết Tuyệt Đối**:
  - Nếu bất kỳ video nào có thời lượng dưới 8 phút hoặc kịch bản dưới 1.400 từ, Subagent 10 có quyền hủy lệnh đăng ngay lập tức.
  - Đảm bảo 10 slot phát sóng mỗi ngày đều nạp từ **Kho 26 Kiệt Tác 30 Phút Đạt Chuẩn**, xoay vòng khoa học không bao giờ trùng lặp nội dung.
