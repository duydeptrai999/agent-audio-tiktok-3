# BÁO CÁO CHUYÊN SÂU SUB-AGENT #10: PHÁP Y MÃ NGUỒN & KỊCH BẢN (8 TỬ HUYỆT LÀM SẬP THỜI GIAN PHÁT) & PHÁC ĐỒ CẢI TỔ TOÀN DIỆN

## 1. 8 Tử Huyệt Cốt Lõi Trong Codebase & Quy Trình Sản Xuất Đang Giết Chết Thời Gian Xem

Qua đối chiếu trực tiếp dữ liệu TikTok Studio của 192 video với mã nguồn trong [`core/stories/daily_story_factory.py`](file:///c:/Users/duydo/OneDrive/Ta%CC%80i%20li%C3%AA%CC%A3u/idk/core/stories/daily_story_factory.py) và [`scripts/daily_24h_master_autopilot.py`](file:///c:/Users/duydo/OneDrive/Ta%CC%80i%20li%C3%AA%CC%A3u/idk/scripts/daily_24h_master_autopilot.py), chúng tôi đã bóc trần **8 nguyên nhân gốc rễ** giải thích tại sao 100% các chỉ số giữ chân đều sụp đổ ở giây thứ 2:

### 🚨 Tử Huyệt #1: Lỗi 'Nhân Bản Vô Tính 10 Kịch Bản Suốt 7 Ngày' & 'Treo Đầu Dê Bán Thịt Chó' Trong `daily_story_factory.py` (Nghiêm trọng nhất!)
- **Vị trí lỗi**: [`core/stories/daily_story_factory.py`](file:///c:/Users/duydo/OneDrive/Ta%CC%80i%20li%C3%AA%CC%A3u/idk/core/stories/daily_story_factory.py#L228-L300).
- **Cơ chế gây lỗi**:
  - Trong `SLOT_STORY_LOADERS` (dòng 228–239), mỗi Slot từ 1 đến 10 bị gắn cứng vào **đúng 1 hàm trả về 1 kịch bản cố định duy nhất** (ví dụ Slot 5 luôn gọi `get_mat_the_sinh_ton_masterpiece_story(title=chosen_title)`).
  - Mỗi ngày mới (`17/10`, `18/10`, `19/10`, `20/10`, `21/10`, `22/10`, `23/10`), hàm `generate_daily_10_stories(date_str)` lấy một **tiêu đề mới** từ `DAILY_THEME_TITLES[s_idx]`, rồi gắn cái tiêu đề mới đó đè lên phần ruột văn bản cũ!
- **Hậu quả thảm khốc trên TikTok Studio**:
  1. **Khán giả bị lừa ('Treo đầu dê bán thịt chó')**: Ví dụ ngày 18/10 người xem thấy tiêu đề *'Tận Thế Hồng Thủy: Tôi Nâng Cấp Tàu Ngầm Hạt Nhân 100 Tầng'*, ngày 21/10 thấy *'Nhiệt Độ Hạ Âm 70 Độ'*, ngày 22/10 thấy *'Siêu Thị Không Gian Giữa Tận Thế Zombie'*... nhưng vừa bật nghe ở giây thứ 2 thì tất cả đều đọc: *'Cánh cửa thép chống đạn ba lớp vừa đóng sập... Giữa cái nóng sáu mươi độ của trận bão cát đỏ...'*! Khán giả thấy tiêu đề một đằng, truyện đọc một nẻo nên **vuốt bỏ ngay lập tức ở giây `0:02` – `0:04`**!
  2. **192 video đăng trong tuần thực chất chỉ là 10 bộ kịch bản phát đi phát lại 6–7 lần!** Khi 1 người xem trên FYP lướt trúng kênh lần thứ 2 trong tuần, họ nghe thấy đúng câu chuyện hôm qua vừa nghe -> Thoát ngay ở giây thứ 1!

### 🚨 Tử Huyệt #2: Tắt Phụ Đề (`enable_subtitles=False`) Trong `daily_24h_master_autopilot.py`
- **Vị trí lỗi**: [`scripts/daily_24h_master_autopilot.py`](file:///c:/Users/duydo/OneDrive/Ta%CC%80i%20li%C3%AA%CC%A3u/idk/scripts/daily_24h_master_autopilot.py#L173-L179).
- **Bằng chứng trong code**:
  ```python
  create_podcast_video(
      ...
      enable_subtitles=False,
      title_text=f"{story['title']} - Tập {p_num}"
  )
  ```
- **Hậu quả**: 88.9% người xem của kênh ở độ tuổi 18–34. Trên TikTok, **0.5 – 1.5 giây đầu tiên là phản xạ thị giác**. Khi không có phụ đề chữ nổi (Subtitles/Karaoke word-by-word) chạy giữa màn hình, mắt người xem không có điểm neo thị giác, dẫn tới **21.59% vuốt bỏ ngay ở giây `0:01` và 56.17% vuốt bỏ ở giây `0:02`**!

### 🚨 Tử Huyệt #3: 5/10 Slot Kịch Bản Không Đạt Độ Dài 10 Phút Mà Chỉ Dài 1 Phút 38 Giây – 5 Phút 30 Giây
- **Bằng chứng định lượng**:
  - **Slot 1 (`sa_dieu_tieng_long_masterpiece.py`)**: Tập 1 = `605 từ` (`~1m55s - 3m54s`), Tập 2 = `588 từ` (`~1m56s - 3m26s`), Tập 3 = `510 từ` (`~1m38s - 3m42s`).
  - **Slot 5 (`mat_the_sinh_ton_masterpiece.py`)**: Tập 1 = `1.132 từ` (`~3m50s`), Tập 2 = `1.045 từ` (`~3m13s`), Tập 3 = `980 từ` (`~3m02s`).
  - **Slot 9 (`quai_dam_rap_chieu_phim_masterpiece.py`)**: Tập 1 = `1.280 từ` (`~4m25s`), Tập 2 = `995 từ` (`~3m23s`), Tập 3 = `1.340 từ` (`~4m38s`).
  - **Slot 10 (`kinh_di_phong_so_7_masterpiece.py`)**: Nhiều tập chỉ dài `4m01s – 5m19s`.
- **Còn 5 Slot dài ~10 phút (Slot 2, 4, 6, 7, 8)**: Được kéo dài lên `~3.450 – 3.550 từ/tập` bằng cách **nhồi nhét các đoạn văn mô tả cảnh vật, độc thoại nội tâm lặp đi lặp lại** (vi phạm quy tắc Micro-Pacing 25 giây trong `GEMINI.md`), khiến chỉ số giữ chân từ giây 15 đến giây 60 sập từ `2.78%` xuống `1.01%`!

### 🚨 Tử Huyệt #4: Tập 2 & Tập 3 Bị Phân Phối Lạnh 100% Trên FYP Mà Không Có 'Câu Dẫn Nhập 3 Giây (Recap Hook)'
- **Bằng chứng TikTok Studio**: Traffic của Tập 2 và Tập 3 có tới **88.2% – 100% đến từ trang Đề xuất (For You)**, chỉ có **1.0% – 2.6% đến từ Hồ sơ cá nhân**.
- Mở đầu của Tập 2 và Tập 3 trong cả 10 file kịch bản đều nhảy thẳng vào hội thoại tiếp nối Tập 1 mà không có 1 câu tóm tắt 5 giây đầu cho người mới xem.
- Khi người lạ trên FYP lướt vào Tập 2/Tập 3, họ không hiểu nhân vật là ai và đang đối đầu vì chuyện gì -> **74% thoát ngay ở giây thứ 3**!

### 🚨 Tử Huyệt #5: Caption Của 162/192 Video Bị Ghi Đè Bằng Câu Sáo Rỗng Vô Nghĩa Trong `daily_story_factory.py`
- **Vị trí lỗi**: [`core/stories/daily_story_factory.py`](file:///c:/Users/duydo/OneDrive/Ta%CC%80i%20li%C3%AA%CC%A3u/idk/core/stories/daily_story_factory.py#L286-L292).
- Khi `chosen_title != base_story.get('title')` (tức là tất cả các ngày từ 18/10 đến 23/10), code tự động xóa sạch phần tóm tắt kịch tính của từng tập và thay bằng câu mẫu:
  - Tập 1: `"Đón xem tập 1 của {chosen_title}!"`
  - Tập 2: `"Nút thắt kịch tính trong tập 2 của {chosen_title}!"`
  - Tập 3: `"Đại kết cục bùng nổ của {chosen_title}!"`
- Thậm chí video `7698036752354643221` (ngày 18/10 lúc 22:54) còn bị đăng lên TikTok với nguyên tên file thô: `VID_20261018_s09_slot_09_quaidam_part2_final` không có nổi tiêu đề hay hashtag!

### 🚨 Tử Huyệt #6: Vi Phạm Trực Tiếp Các Điều Cấm Trong `GEMINI.md` Ở Kịch Bản Gốc
1. **Dùng tên nhân vật bị cấm**: `Cố Bắc Thần` vẫn xuất hiện xuyên suốt trong `trong_sinh_va_mat_masterpiece.py` (24 video trong tuần).
2. **Đọc bảng nội quy cứng nhắc (Ruleboard Dump)**: Trong `quai_dam_rap_chieu_phim_masterpiece.py`, nhân vật vẫn đọc nguyên văn: *'Điều một: Rạp chiếu phim chỉ bán vé cho khách đi một mình... Điều hai:... Điều ba:...'* — vi phạm Điều cấm số 4 của `GEMINI.md`.

### 🚨 Tử Huyệt #7: Đứt Gãy Phễu Chuyển Đổi Hồ Sơ (`25.600 Views -> 52 Profile Views = 0.20%`) & Không Có Danh Sách Phát (Playlist)
- Không có hướng dẫn thị giác trên màn hình (như mũi tên chỉ vào Avatar/Playlist ở 5 giây cuối hoặc ghim bình luận dẫn link Tập 2, Tập 3), khiến người xem Tập 1 xong không biết tìm Tập 2 ở đâu.

### 🚨 Tử Huyệt #8: Độ Lệch Tệp Follower Cũ (59% Nam, 18.7% Nước Ngoài) Làm Loãng Tín Hiệu Khởi Đầu
- Tệp 2.542 follower cũ không khớp với tệp người nghe truyện Nữ频 (75% Nữ, 97.5% Việt Nam), khiến tab `Đã Follow` có `0%` lượt xem.

---

## 2. Phác Đồ Cải Tổ Toàn Diện Để Đưa Tổng Thời Gian Phát Vượt 30–60 Phút/Video & Tỷ Lệ Xem Hết Lên 5% – 12%

| Thứ tự Ưu tiên | Hạng mục Cải tổ | Giải pháp Kỹ thuật & Biên kịch Cụ thể | Tác động Kỳ vọng |
| :---: | :--- | :--- | :--- |
| **1 (Khẩn cấp)** | **Xóa bỏ cơ chế 'Bình mới rượu cũ' trong `daily_story_factory.py`** | Mỗi bộ truyện đăng lên BẮT BUỘC là 1 kịch bản độc bản 100% khớp tuyệt đối với tiêu đề (`Title == Story Content`). Tuyệt đối không lấy tiêu đề ngày mới gắn vào ruột kịch bản ngày cũ! | Chấm dứt hoàn toàn tình trạng khán giả thoát ở giây thứ 2–4 vì tiêu đề lệch nội dung và lặp truyện cũ. |
| **2 (Khẩn cấp)** | **Bật lại Phụ đề Karaoke (`enable_subtitles=True`) trong `daily_24h_master_autopilot.py`** | Bật phụ đề chữ vàng/trắng viền đen chạy từng cụm 4–6 từ giữa màn hình ngay từ giây `0.00` để khóa mắt tệp Gen Z & Millennials (88.9% người xem). | Giữ chân giây `0:01 -> 0:03` tăng từ `26.18%` lên `55% – 65%`. |
| **3 (Cốt lõi)** | **Thiết kế '3-Second Recap Hook' bắt buộc cho Tập 2 & Tập 3** | Vì 88.5% người xem Tập 2 & Tập 3 đến từ FYP, 15 từ đầu tiên của Tập 2 & Tập 3 phải là 1 câu tóm tắt xung đột cực gắt độc lập (VD: *"Vừa ném tờ giấy ly hôn trước mặt nhà chồng, tôi lập tức bấm nút phong tỏa một trăm hai mươi tỷ..."*). | Kéo thời gian xem trung bình của Tập 2 & Tập 3 từ `4.97s` lên `>25s`. |
| **4 (Chiến lược)** | **Chuẩn hóa độ dài mỗi Part về mức Vàng `3 phút 30 giây – 4 phút 30 giây` (hoặc nếu làm 10 phút thì gộp Trọn Bộ Full 1 Tập)** | Dữ liệu thực nghiệm trên kênh tuần này chứng minh: Các video dài `2p – 4p` (như Slot 1) có tỷ lệ xem hết cao gấp **4–8 lần** (`0.90%` - `3.85%`) so với các video kéo giãn 10 phút bằng văn bản lặp (`0.08%`). Nếu muốn giữ format **10 phút/video**, hãy đăng **TRỌN BỘ FULL 1 VIDEO 10 PHÚT (Không chia lẻ 3 part)** để khán giả FYP nghe trọn vẹn từ đầu đến kết cục trong 1 video! | Nếu đăng Full 10 phút/bộ (không cắt vụn 3 part), khán giả không bị bức xúc vì cắt tập và không bị lạc ở Part 2/Part 3 trên FYP; Tổng thời gian phát sẽ tăng vọt gấp 4–6 lần! |
| **5 (Phễu)** | **Khôi phục Caption kịch tính riêng cho từng tập & Tự động ghim Comment dẫn tập** | Bỏ ngay câu mẫu `"Nút thắt kịch tính trong tập 2 của..."`. Mỗi video phải có mô tả 2 câu tóm tắt tình tiết đắt giá nhất + câu hỏi tranh luận đúng tình tiết trong truyện. | Tăng tỷ lệ Bình luận từ `0` lên hàng chục bình luận/tuần và kéo tỷ lệ vào Hồ sơ từ `0.20%` lên `>2.5%`. |