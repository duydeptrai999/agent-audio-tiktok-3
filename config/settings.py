import os
from pathlib import Path

# Thư mục gốc dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Tự động nạp cấu hình từ file .env (thuần Python, không phụ thuộc thư viện)
env_path = BASE_DIR / ".env"
if env_path.exists():
    try:
        with open(env_path, "r", encoding="utf-8") as _f:
            for _line in _f:
                _line = _line.strip()
                if _line and not _line.startswith("#") and "=" in _line:
                    _k, _v = _line.split("=", 1)
                    _k = _k.strip()
                    _v = _v.strip().strip('"').strip("'")
                    if _k and _k not in os.environ:
                        os.environ[_k] = _v
    except Exception:
        pass

# Thư mục chứa tài nguyên
ASSETS_DIR = BASE_DIR / "assets"
AUDIO_DIR = ASSETS_DIR / "audio"
SUBTITLES_DIR = ASSETS_DIR / "subtitles"
FOOTAGE_DIR = ASSETS_DIR / "footage"
BGM_DIR = ASSETS_DIR / "bgm"
OUTPUT_DIR = ASSETS_DIR / "output"
DATABASE_DIR = BASE_DIR / "data"

# Tự động tạo các thư mục nếu chưa có
for directory in [ASSETS_DIR, AUDIO_DIR, SUBTITLES_DIR, FOOTAGE_DIR, BGM_DIR, OUTPUT_DIR, DATABASE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Cấu hình Model AI (Gemini / OpenAI)
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")  # "gemini" hoặc "openai"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Cấu hình Telegram Bot & Đăng Bài Di Động / Máy Ảo
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
EMULATOR_SHARED_DIR = os.getenv("EMULATOR_SHARED_DIR", "")  # Thư mục chia sẻ máy ảo tùy biến

# Cấu hình Giọng đọc Edge-TTS (Chuẩn Master Codex 8.0)
VOICE_HIGH_IQ = "vi-VN-NamMinhNeural"   # Giọng nam trầm ấm, đĩnh đạc, bí ẩn (rate +3% đến +6%)
VOICE_SLEEP = "vi-VN-HoaiMyNeural"     # Giọng nữ ấm, truyền cảm, tâm sự, sắc sảo (rate +5% đến +8%)
VOICE_SPEED_MULTIPLIER = float(os.getenv("VOICE_SPEED_MULTIPLIER", "1.06"))

# Cấu hình Thời lượng & Dung lượng Kịch bản Audio 30 Phút
AUDIO_TARGET_DURATION_MINUTES = 30     # Thời lượng tổng bộ truyện audio mục tiêu: 30 phút
TARGET_DURATION_MINUTES = 10           # Thời lượng mỗi tập mục tiêu trong chuỗi 3 tập (10 phút/tập)

# Tốc độ đọc thực tế đo đạc từ FFmpeg trên giọng đọc AI Edge-TTS tiếng Việt:
WORDS_PER_MINUTE_BASE = 208
EFFECTIVE_WORDS_PER_MINUTE = int(WORDS_PER_MINUTE_BASE * VOICE_SPEED_MULTIPLIER)
WORDS_PER_MINUTE_VIETNAMESE = EFFECTIVE_WORDS_PER_MINUTE

# Dung lượng kịch bản chuẩn để đạt ĐÚNG >= 30 PHÚT AUDIO THÀNH PHẨM TRÊN ĐỒNG HỒ:
SCRIPT_MIN_WORDS_PER_PART_10MIN = int(10 * EFFECTIVE_WORDS_PER_MINUTE)
SCRIPT_TARGET_WORDS_PER_PART_10MIN = int(SCRIPT_MIN_WORDS_PER_PART_10MIN * 1.02)
SCRIPT_MIN_WORDS_30MIN = SCRIPT_MIN_WORDS_PER_PART_10MIN * 3
SCRIPT_TARGET_WORDS_30MIN = SCRIPT_TARGET_WORDS_PER_PART_10MIN * 3

# Ngưỡng sàn cơ sở tối thiểu tuyệt đối
SCRIPT_BASELINE_MIN_WORDS_30MIN = SCRIPT_MIN_WORDS_30MIN
SCRIPT_BASELINE_MIN_WORDS_PER_PART = SCRIPT_MIN_WORDS_PER_PART_10MIN

# Cấu hình Chuẩn Hóa Âm Thanh TikTok / YouTube Mastering
TARGET_LUFS = -16.0
TRUE_PEAK = -1.5

# Cấu hình Sidechain Ducking Chuẩn Điện Ảnh (BGM -22dB đến -24dB theo Codex 8.0)
DUCKING_RELEASE_MS = 750    # Xả nén từ từ trong 850ms để BGM dâng lên êm ái
DUCKING_ATTACK_MS = 25      # Ép BGM xuống nhanh trong 20ms khi có tiếng nói
DUCKING_THRESHOLD = 0.079   # Ngưỡng kích hoạt nhạy bén giữ giọng đọc luôn tách bạch
DUCKING_RATIO = 4.0         # Tỷ lệ nén 4.5:1 chuẩn cinema
DUCKING_KNEE = 2.5          # Độ mềm đường cong nén

# Phương thức phát hành video: "WEB_STUDIO" (Phương án B - Trợ lý 1-chạm đăng TikTok Web), "ADB" (máy ảo), "TELEGRAM"
PUBLISH_METHOD = os.getenv("PUBLISH_METHOD", "WEB_STUDIO")

# Cấu hình Render Video Chuẩn Dọc TikTok 9:16 (1080x1920 Full-Screen)
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30
BGM_VOLUME = 0.08   # Chuẩn Codex 8.0: Nhạc nền -22dB đến -24dB (nâng đỡ cảm xúc, không át tiếng nói)
VOICE_VOLUME = 0.96 # Giọng đọc rõ ràng, ấm áp, nổi bật ngay từ giây 0.0

# Cấu hình Phụ đề Động (Kinetic Captions 3-6 từ/cụm ở 1/3 dưới màn hình Safe Zone)
ENABLE_SUBTITLES = True    # Bật phụ đề động vàng chanh viền đen giúp khóa chặt thị giác 3 giây đầu
TIKTOK_AUTO_CAPTION = True # Bật tính năng Auto-caption CC tự động của TikTok Studio khi đăng video
SUBTITLE_COLOR = "yellow"  # Chữ vàng chanh viền đen nổi bật trên mọi nền B-roll ASMR
SUBTITLE_FONT_SIZE = 16    # Cỡ chữ chuẩn libass (PlayResY=288) trên khung dọc 9:16 (1080x1920)
SUBTITLE_MARGIN_V = 68     # Vị trí 1/3 dưới màn hình Safe Zone (tránh icon thả tim và caption TikTok)

# Cấu hình Tuyển Tập / Danh Sách Phát (Playlist)
AUTO_ADD_TO_PLAYLIST = True # Tự động tạo hoặc thêm 3 Part vào Danh sách phát / Tuyển tập trên TikTok Studio

# Cấu hình Phong cách Video Nền & BGM (Ưu tiên Trung Quốc / ASMR theo thị hiếu tệp Nữ)
PREFERRED_BG_THEME = "chinese_asmr"         # "chinese_asmr", "chinese_beauty", "chinese_cooking", "chinese_pastry", "chinese_craft"
PREFERRED_BGM_STYLE = "chinese_instrumental" # "chinese_instrumental", "nhoi_nho_ngan_ha", "dai_ngu", "co_cung_hoi_uc"
