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

# Cấu hình Giọng đọc Edge-TTS
VOICE_HIGH_IQ = "vi-VN-NamMinhNeural"   # Giọng nam dứt khoát, thông thái
VOICE_SLEEP = "vi-VN-HoaiMyNeural"     # Giọng nữ truyền cảm, sâu lắng, nhấn nhá kịch tính
VOICE_SPEED_MULTIPLIER = 1.5           # BẮT BUỘC: Luôn tua âm thanh giọng đọc nhanh 1.5x (atempo=1.5)

# Cấu hình Thời lượng & Dung lượng Kịch bản Audio 30 Phút
AUDIO_TARGET_DURATION_MINUTES = 30     # Thời lượng tổng bộ truyện audio mục tiêu: 30 phút
TARGET_DURATION_MINUTES = 10           # Thời lượng mỗi tập mục tiêu trong chuỗi 3 tập (10 phút/tập)

# Tốc độ đọc thực tế đo đạc từ FFmpeg trên giọng đọc AI Edge-TTS tiếng Việt:
# - Ở 1.0x (gốc): ~230 từ/phút
# - Ở 1.5x (atempo=1.5): ~346 từ/phút (chuẩn xác thực tế đo đạc để đạt >= 30 phút audio)
WORDS_PER_MINUTE_BASE = 230
EFFECTIVE_WORDS_PER_MINUTE = 346       # Tốc độ đọc thực tế khi tua 1.5x (346 từ/phút)
WORDS_PER_MINUTE_VIETNAMESE = EFFECTIVE_WORDS_PER_MINUTE  # Tương thích ngược

# Dung lượng kịch bản chuẩn để đạt ĐÚNG >= 30 PHÚT AUDIO THÀNH PHẨM TRÊN ĐỒNG HỒ Ở TỐC ĐỘ 1.5X:
# - Mỗi tập 10 phút audio ở 1.5x: 10 * 346 = 3,460 từ (lý tưởng ~3,480 - 3,500 từ)
# - Toàn bộ 30 phút audio ở 1.5x: 30 * 346 = 10,380 từ (lý tưởng ~10,440 - 10,500 từ)
SCRIPT_MIN_WORDS_30MIN = 10380
SCRIPT_TARGET_WORDS_30MIN = 10500
SCRIPT_MIN_WORDS_PER_PART_10MIN = 3460
SCRIPT_TARGET_WORDS_PER_PART_10MIN = 3500

# Ngưỡng sàn cơ sở tối thiểu tuyệt đối (Bắt buộc theo chuẩn GEMINI.md)
SCRIPT_BASELINE_MIN_WORDS_30MIN = 10380
SCRIPT_BASELINE_MIN_WORDS_PER_PART = 3460

# Cấu hình Chuẩn Hóa Âm Thanh TikTok / YouTube Mastering
TARGET_LUFS = -13.0
TRUE_PEAK = -1.0

# Phương thức phát hành video: "WEB_STUDIO" (Phương án B - Trợ lý 1-chạm đăng TikTok Web), "ADB" (máy ảo), "TELEGRAM"
PUBLISH_METHOD = os.getenv("PUBLISH_METHOD", "WEB_STUDIO")

# Cấu hình Render Video (Ngang 16:9 nguyên bản theo video tải về)
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_FPS = 30
BGM_VOLUME = 0.22  # Nhạc nền nhỏ hơn (22%) êm dịu, không lấn át giọng đọc
VOICE_VOLUME = 1.0 # Giọng đọc 100%

# Cấu hình Phụ đề Động trên Video (Kinetic Subtitles High-CTR)
ENABLE_SUBTITLES = True   # Bật phụ đề chữ động để neo giữ mắt người xem 3s đầu và đẩy tỷ lệ xem hết (AVD)
SUBTITLE_COLOR = "yellow" # "yellow" (vàng tươi viền đen) hoặc "white" (trắng tuyết viền đen)
SUBTITLE_FONT_SIZE = 28   # Kích thước font chữ rõ ràng, dễ đọc trên di động
SUBTITLE_MARGIN_V = 220   # Vị trí cách đáy màn hình 220px để không bị che bởi thanh công cụ TikTok


