# 🎙️ Agent Audio TikTok - Hệ Thống Sản Xuất & Tự Động Hóa Kênh Truyện TikTok Triệu View

Chỉ cần dùng antigravity clone về và dùng thôi ,  lâu lâu thì  cho nó lên cào qua mấy bộ truyện nhiều người xem để update kiến thức làm truyện khôn xíu

[![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)]()
[![Automation](https://img.shields.io/badge/Automation-Playwright%20%7C%20CDP-orange.svg)]()
[![Audio Engine](https://img.shields.io/badge/Audio-Edge--TTS%20%7C%20FFmpeg-red.svg)]()

> **Agent Audio TikTok** là giải pháp toàn diện (End-to-End Autonomous Pipeline) ứng dụng Trí Tuệ Nhân Tạo để tự động hóa toàn bộ chu trình sáng tạo nội dung cho kênh TikTok Audio Drama: từ thu thập ý tưởng, biên kịch cốt truyện giữ chân cao, tạo giọng đọc AI phát thanh, mix nhạc nền động (Dynamic Sidechain Auto-Ducking), ghép video nền chống trùng lặp, tạo phụ đề karaoke, thiết kế ảnh bìa triệu view, cho đến đăng bài và lên lịch phát hành tự động qua trình duyệt.

---

## 🌟 Các Tính Năng Nổi Bật

### 1. 🧠 Bộ Não Biên Kịch AI Chuẩn Douyin & Zhihu
- **Công thức Giữ Chân Người Xem (Retention Optimization)**: Áp dụng quy tắc hook 3 giây đầu giật gân, cao trào dồn dập mỗi 30-45 giây, cú twist bất ngờ và kết thúc lửng (cliffhanger) buộc người xem phải chờ đợi tập tiếp theo.
- **Thư Viện Đa Dạng Thể Loại**:
  - 👑 **Cung Đấu - Nữ Quyền**: Đấu trí hoàng cung, nữ cường phục thù.
  - 🔍 **Huyền Nghi - Trinh Thám**: Vụ án bí ẩn, đấu trí logic tầng tầng lớp lớp.
  - 👻 **Kinh Dị - Quái Đàm Quy Tắc**: Nỗi sợ tâm lý, sinh tồn trong vùng cấm.
  - 💥 **Trọng Sinh - Vả Mặt (Slap-in-the-face)**: Kiếp trước chịu nhục, kiếp này trở lại nghiền nát đối thủ.
  - 🎭 **Sa Điêu - Hài Hước - Tiếng Lòng**: Đọc suy nghĩ hài hước, phản sáo lộ phá vỡ khuôn mẫu.
  - 🌸 **Cứu Rỗi - Chữa Lành - Thanh Xuân**: Cảm xúc ấm áp, hoài niệm học đường sâu lắng.
  - 💼 **Hào Môn - Tổng Tài**: Tình cảm trắc trở, khế ước hôn nhân đầy kịch tính.
- **Phân Tập Tự Động (Series Splitter)**: Chia chuỗi tác phẩm 30 phút thành 3 tập cân bằng (~10 phút/tập), kích thích người xem xem trọn bộ danh sách phát.

### 2. 🛡️ Hệ Thống Chống Trùng Lặp & Bảo Vệ Kênh (Anti-Repost Guard)
- **Kiểm Duyệt Nội Dung & Âm Thanh Độc Quyền**: Trước mỗi lần phát hành, hệ thống đối soát hash văn bản, tiêu đề và phân tích đặc trưng audio với cơ sở dữ liệu `published_audio_registry.json`.
- **Ngăn Chặn Vi Phạm Thuật Toán**: Tự động từ chối đăng tải nếu phát hiện nội dung có nguy cơ bị TikTok quét trùng lặp hoặc vi phạm chính sách nội dung tái sử dụng (unoriginal content).

### 3. 🔊 Xử Lý Âm Thanh Chuyên Nghiệp (Audio & BGM Engine)
- **Giọng Đọc AI Cao Cấp (Edge-TTS)**: Tích hợp giọng đọc tự nhiên chuẩn tiếng Việt (`NamMinh` uy lực hoặc `HoaiMy` truyền cảm), tự động tăng tốc 1.5x (`atempo=1.5`) đạt tốc độ lý tưởng 346 từ/phút giúp tăng nhịp điệu kích thích tâm lý người nghe.
- **Dynamic Sidechain Auto-Ducking**: Tự động hạ âm lượng nhạc nền (BGM) khi có tiếng đọc và nâng âm lượng mượt mà ở các đoạn ngừng nghỉ tạo không gian kịch tính như phòng thu chuyên nghiệp.
- **Cách Ly Bản Quyền BGM**: Bộ lọc cô lập và loại bỏ các bản nhạc có nguy cơ dính bản quyền âm thanh TikTok.

### 4. 🎬 Dựng Video Nền & Phụ Đề Chuẩn TikTok
- **Kho Video Nền Độc Bản (Distinct Slices)**: Quản lý video phong cảnh, thủ công truyền thống 4K/60fps, tự động cắt lát thông minh không trùng lặp phân đoạn giữa các tập.
- **Phụ Đề Karaoke Đồng Bộ Từng Mili-giây**: Xuất phụ đề chuẩn ASS/SRT với font chữ nổi bật, viền đen tương phản cao, định dạng tối ưu khung hình dọc 9:16.
- **Tự Động Sinh Thumbnail Triệu View**: Tạo ảnh bìa bắt mắt kèm tiêu đề lớn, tạo ấn tượng mạnh trên trang cá nhân của kênh.

### 5. 🚀 Tự Động Hóa Đăng Bài & Lên Lịch (Auto Uploader)
- **Playwright & CDP Chrome Controller**: Điều khiển trình duyệt (Chrome, Cốc Cốc) qua profile đăng nhập sẵn để tránh bị TikTok checkpoint / Captcha.
- **Lập Lịch Phát Hành Thông Minh (Smart Scheduler)**: Lên lịch tự động đăng đúng khung giờ vàng (11:30 - 13:00, 19:30 - 21:30).
- **Inter-process FileLock**: Ngăn ngừa xung đột đa tiến trình khi chạy song song nhiều kịch bản đăng bài.
- **Tự Động Điền Caption & Hashtags**: Tạo mô tả chuẩn SEO TikTok theo thể loại giúp video nhanh chóng được đẩy vào đúng tệp người xem mục tiêu.

---

## 📂 Cấu Trúc Dự Án

```
agent-audio-tiktok-3/
├── assets/                     # Tài nguyên đa phương tiện (BGM, video nền, font chữ)
│   ├── bgm/                    # Kho nhạc nền an toàn bản quyền
│   ├── footage/                # Kho video phong cảnh 4K dọc
│   ├── thumbnails/             # Thư mục chứa ảnh bìa sinh tự động
│   └── subtitles/              # Phụ đề SRT/ASS
├── config/                     # Cấu hình hệ thống
│   ├── settings.py             # Cấu hình đường dẫn, giọng đọc, API keys, thông số audio
│   └── __init__.py
├── core/                       # Lõi xử lý nghiệp vụ AI & Media
│   ├── anti_repost_guard.py    # Kiểm duyệt chống trùng lặp kịch bản & audio
│   ├── audio_engine.py         # Bộ máy tổng hợp giọng đọc AI & xử lý âm thanh
│   ├── background_manager.py   # Quản lý video nền, cắt lát phân đoạn thông minh
│   ├── bgm_manager.py          # Mix nhạc nền BGM & Dynamic Sidechain Ducking
│   ├── ffmpeg_utils.py         # Tiện ích render video, ghép âm thanh bằng FFmpeg
│   ├── narrative_synthesizer.py# Biên kịch và lắp ráp cốt truyện giữ chân cao
│   ├── script_generator.py     # Tạo kịch bản chi tiết theo thể loại
│   ├── series_splitter.py      # Phân tập chuẩn chuỗi 3 phần (Part 1 - 2 - 3)
│   ├── subtitle_engine.py      # Bộ tạo phụ đề đồng bộ
│   ├── thumbnail_generator.py  # Tạo ảnh bìa bắt mắt cho TikTok
│   ├── viral_scorer.py         # Chấm điểm tiềm năng viral của kịch bản
│   └── stories/                # Kho kịch bản và siêu phẩm truyện độc quyền
├── data/                       # Dữ liệu trạng thái, lịch trình và bộ nhớ hệ thống
│   ├── agent_memory.json       # Bộ nhớ hoạt động của agent
│   ├── background_video_pool.json # Danh mục video nền khả dụng
│   ├── published_audio_registry.json # Sổ đăng ký các tác phẩm đã phát hành
│   └── generated_scripts/      # Kịch bản JSON đã tạo sẵn sàng render
├── docs/                       # Tài liệu hướng dẫn & bí kíp biên kịch
│   ├── CAM_NANG_100_KICH_BAN_TRUYEN_NGAN_TRUNG_QUOC.md
│   ├── QUY_TRINH_BIEN_KICH_TOI_UU.md
│   ├── SO_TAY_BIEN_KICH_TRIEU_VIEW_DOUYIN_ZHIHU.md
│   └── kinh_nghiem_chi_tiet/   # 10 cẩm nang chuyên sâu từng thể loại
├── scripts/                    # Kịch bản thực thi, render và xuất bản
│   ├── tiktok_publisher_core.py# Lõi đăng video TikTok tự động qua trình duyệt
│   ├── produce_and_schedule_5_new_masterpieces.py # Pipeline sản xuất & lên lịch trọn gói
│   ├── start_chrome_for_ai.bat # Khởi động Chrome chế độ Remote Debugging
│   └── master_scheduler.py     # Bộ điều phối lịch đăng toàn kênh
└── README.md                   # Tài liệu tổng quan dự án
```

---

## 🛠️ Yêu Cầu Cài Đặt

### 1. Môi trường phần mềm
- **Python**: Phiên bản >= 3.10 (Khuyến nghị 3.11 hoặc 3.12).
- **FFmpeg**: Đã được cài đặt và thêm vào biến môi trường `PATH`.
- **Trình duyệt**: Google Chrome hoặc Cốc Cốc.

### 2. Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```
*(Hoặc cài đặt các gói chính: `edge-tts`, `playwright`, `filelock`, `google-genai`, `openai`, `pillow`, `pydub`, `tqdm`)*

### 3. Cấu hình biến môi trường
Tạo file `.env` tại thư mục gốc của dự án (nếu muốn sử dụng LLM biên kịch nâng cao hoặc gửi thông báo Telegram):
```env
# Nhà cung cấp AI (gemini hoặc openai)
AI_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Thông báo Telegram (tùy chọn)
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 🚀 Hướng Dẫn Sử Dụng

### Bước 1: Khởi động Chrome với cổng Debug
Chạy file script để mở trình duyệt Chrome sẵn sàng cho Agent điều khiển:
```cmd
scripts\start_chrome_for_ai.bat
```
> Đăng nhập tài khoản TikTok của bạn trên cửa sổ Chrome vừa mở. Phiên đăng nhập sẽ được lưu lại tự động.

### Bước 2: Sản xuất và lên lịch chuỗi siêu phẩm truyện
Để chạy pipeline sản xuất trọn gói (Tạo audio -> Mix BGM -> Cắt video nền -> Tạo subtitle & thumbnail -> Đăng lên TikTok):
```bash
python scripts/produce_and_schedule_5_new_masterpieces.py
```

### Bước 3: Đăng bài thủ công hoặc kiểm tra trạng thái
```bash
python scripts/check_tiktok_content.py
```

---

## 📖 Cẩm Nang Biên Kịch Kèm Theo
Dự án đi kèm bộ tài liệu cực kỳ đồ sộ tại thư mục `docs/`:
- **Sổ tay biên kịch triệu view**: Quy luật tâm lý học tiếp nhận của khán giả lướt nhanh TikTok.
- **Quy trình biên kịch tối ưu**: Chuẩn hóa cách xây dựng nhân vật, xung đột gia đình, trả thù, tình yêu, phá án.
- **10 bộ kinh nghiệm chi tiết**: Chi tiết cách dẫn truyện cho từng ngách thể loại.

---

## ⚖️ Giấy Phép & Tuyên Bố Miễn Trừ Trách Nhiệm
- Dự án được phát triển nhằm mục đích nghiên cứu tự động hóa và hỗ trợ sáng tạo nội dung số.
- Người dùng cần tuân thủ Điều khoản Dịch vụ và Tiêu chuẩn Cộng đồng của TikTok khi vận hành kênh.
