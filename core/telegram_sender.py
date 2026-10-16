import sys
import os
import shutil
from pathlib import Path
from typing import Optional, List
import requests

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    EMULATOR_SHARED_DIR,
    BASE_DIR
)

class TelegramPublisherNotifier:
    """
    Module phụ trách gửi video và Caption tối ưu qua Telegram Bot,
    đồng thời tự động đồng bộ video vào Thư Mục Chia Sẻ của Máy Ảo Android (LDPlayer / Nox / BlueStacks).
    """

    @staticmethod
    def get_common_emulator_paths() -> List[Path]:
        """Tự động tìm kiếm các thư mục chia sẻ hình ảnh/video của các máy ảo phổ biến trên Windows."""
        user_home = Path.home()
        candidates = [
            # Thư mục cấu hình tùy chọn trong settings / .env
            Path(EMULATOR_SHARED_DIR) if EMULATOR_SHARED_DIR else None,
            # LDPlayer 9 / 4 (Mặc định hoặc thư mục XuanZhi9 trên máy bạn)
            Path(r"C:\Users\duydo\OneDrive\Tài liệu\XuanZhi9\Pictures"),
            user_home / "OneDrive" / "Tài liệu" / "XuanZhi9" / "Pictures",
            user_home / "Documents" / "XuanZhi9" / "Pictures",
            user_home / "Documents" / "LDPlayer" / "Pictures",
            user_home / "Documents" / "LDPlayer9" / "Pictures",
            # NoxPlayer
            user_home / "Nox_share" / "Image",
            user_home / "Nox_share" / "Other",
            # BlueStacks
            Path(r"C:\ProgramData\BlueStacks_nxt\Engine\UserData\SharedFolder"),
            # Thư mục chia sẻ mặc định trong dự án nếu máy ảo mount folder này
            BASE_DIR / "data" / "emulator_share"
        ]
        valid_paths = [p for p in candidates if p and p.exists()]
        return valid_paths

    @classmethod
    def sync_to_emulator(cls, video_path: str, caption: str = "") -> Optional[Path]:
        """
        Tự động copy file video và file caption.txt sang Thư Mục Chia Sẻ Máy Ảo Android.
        Giúp video xuất hiện ngay trong Thư viện (Gallery) của TikTok trên máy ảo mà không cần truyền tải mạng!
        """
        source_vid = Path(video_path)
        if not source_vid.exists():
            return None

        target_dirs = cls.get_common_emulator_paths()
        
        # Nếu chưa tìm thấy thư mục của LDPlayer/Nox, tạo sẵn thư mục chia sẻ chuẩn tại data/emulator_share
        if not target_dirs:
            fallback_dir = BASE_DIR / "data" / "emulator_share"
            fallback_dir.mkdir(parents=True, exist_ok=True)
            target_dirs = [fallback_dir]

        synced_path = None
        for target_dir in target_dirs:
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
                dest_file = target_dir / source_vid.name
                shutil.copy2(source_vid, dest_file)
                
                # Lưu kèm file caption.txt để trong máy ảo chỉ cần mở lên bấm Ctrl+C hoặc copy
                caption_file = target_dir / f"{source_vid.stem}_caption.txt"
                with open(caption_file, "w", encoding="utf-8") as f:
                    f.write(caption)

                synced_path = dest_file
                print(f"[📲 Máy Ảo Android] ✅ Đã đồng bộ video vào Thư mục chia sẻ máy ảo:")
                print(f"    📂 Đường dẫn: {dest_file}")
                print(f"    📋 Caption kèm theo: {caption_file}")
            except Exception as e:
                print(f"[⚠️ Máy Ảo Android] Lỗi khi đồng bộ tới {target_dir}: {e}")

        return synced_path

    @classmethod
    def send_to_telegram(
        cls, 
        video_path: str, 
        caption: str, 
        schedule_time: str = "19:30", 
        title: str = "Video TikTok",
        bot_token: Optional[str] = None,
        chat_id: Optional[str] = None
    ) -> bool:
        """
        Gửi thông báo, caption (bọc trong thẻ <code> để 1-chạm copy), và file video (nếu <= 48MB)
        hoặc ảnh thumbnail (nếu > 48MB) vào Telegram Bot.
        """
        token = bot_token or TELEGRAM_BOT_TOKEN
        cid = chat_id or TELEGRAM_CHAT_ID

        if not token or not cid:
            print(f"\n[📢 Telegram Bot] ℹ️ Chưa cấu hình TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID trong .env")
            print(f" 👉 Hãy thêm vào file .env để kích hoạt tính năng bắn video & caption tự động!")
            return False

        vid_file = Path(video_path)
        if not vid_file.exists():
            print(f"[❌ Telegram Bot] Không tìm thấy file video: {video_path}")
            return False

        file_size_mb = vid_file.stat().st_size / (1024 * 1024)
        print(f"\n[📢 Telegram Bot] Đang chuẩn bị gửi video sang Telegram ({file_size_mb:.1f} MB)...")

        # Soạn tin nhắn HTML (Thẻ <code> cho phép bấm 1 chạm trên điện thoại/máy ảo là tự copy toàn bộ caption)
        formatted_message = (
            f"🎬 <b>XUẤT XƯỞNG VIDEO TIKTOK THÀNH CÔNG!</b>\n\n"
            f"📌 <b>Tiêu đề:</b> {title}\n"
            f"⏰ <b>Khung giờ vàng đề xuất:</b> <code>{schedule_time}</code>\n"
            f"📦 <b>Dung lượng:</b> {file_size_mb:.1f} MB\n"
            f"📁 <b>Tên file:</b> <code>{vid_file.name}</code>\n\n"
            f"👇 <b>CAPTION & HASHTAGS (CHẠM ĐỂ COPY 1 GIÂY):</b>\n"
            f"<code>{caption}</code>\n\n"
            f"💡 <i>Mẹo viral: Khi đăng trên app TikTok, chọn 'Thêm âm thanh' -> Tìm nhạc thịnh hành bất kỳ -> Chỉnh âm lượng nhạc trend về 1% để kéo đề xuất!</i>"
        )

        base_url = f"https://api.telegram.org/bot{token}"

        # 1. Nếu video <= 48MB: Gửi trực tiếp file Video qua Telegram Bot API
        if file_size_mb <= 48.0:
            print(f"[📢 Telegram Bot] Video {file_size_mb:.1f} MB (<= 50MB) -> Đang upload trực tiếp video lên Telegram...")
            try:
                with open(vid_file, "rb") as f:
                    # Gửi tin nhắn video kèm caption
                    payload = {
                        "chat_id": cid,
                        "caption": formatted_message[:1024],  # Telegram giới hạn caption của media là 1024 ký tự
                        "parse_mode": "HTML",
                        "supports_streaming": "true"
                    }
                    files = {"video": (vid_file.name, f, "video/mp4")}
                    res = requests.post(f"{base_url}/sendVideo", data=payload, files=files, timeout=300)
                    res_data = res.json()
                    
                    if res_data.get("ok"):
                        print(f"[📢 Telegram Bot] ✅ ĐÃ GỬI VIDEO THÀNH CÔNG LÊN TELEGRAM!")
                        return True
                    else:
                        print(f"[⚠️ Telegram Bot] sendVideo thất bại ({res_data.get('description')}). Đang thử gửi tin nhắn văn bản...")
            except Exception as e:
                print(f"[⚠️ Telegram Bot] Lỗi kết nối khi gửi video: {e}")

        # 2. Nếu video > 48MB (Vượt giới hạn Bot API của Telegram) hoặc gửi video lỗi:
        # Gửi tin nhắn thông báo kèm Caption đầy đủ và ảnh chụp Thumbnail đại diện
        print(f"[📢 Telegram Bot] Video {file_size_mb:.1f} MB vượt ngưỡng 50MB của Telegram Bot API.")
        print(f"[📢 Telegram Bot] Đang gửi thông báo kèm Caption 1-chạm và hướng dẫn lấy video...")
        
        # Thử tìm ảnh thumbnail đại diện
        thumb_candidates = [
            BASE_DIR / "final_proof_frame.png",
            BASE_DIR / "latest_proof_frame.png",
            BASE_DIR / "test_frame.png"
        ]
        thumb_path = next((p for p in thumb_candidates if p.exists()), None)

        try:
            if thumb_path:
                with open(thumb_path, "rb") as f:
                    payload = {
                        "chat_id": cid,
                        "caption": formatted_message[:1024],
                        "parse_mode": "HTML"
                    }
                    files = {"photo": (thumb_path.name, f, "image/png")}
                    res = requests.post(f"{base_url}/sendPhoto", data=payload, files=files, timeout=60)
            else:
                payload = {
                    "chat_id": cid,
                    "text": formatted_message,
                    "parse_mode": "HTML"
                }
                res = requests.post(f"{base_url}/sendMessage", json=payload, timeout=60)

            res_data = res.json()
            if res_data.get("ok"):
                print(f"[📢 Telegram Bot] ✅ Đã gửi Caption và thông báo thành công vào Telegram!")
                return True
            else:
                print(f"[❌ Telegram Bot] Gửi thất bại: {res_data.get('description')}")
                return False
        except Exception as e:
            print(f"[❌ Telegram Bot] Lỗi kết nối: {e}")
            return False
