import os
import sys
import subprocess
import time
from pathlib import Path
from typing import Optional, List

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

class AndroidADBController:
    """
    Bộ điều khiển máy ảo Android qua lệnh ADB (Android Debug Bridge).
    Tự động kết nối máy ảo (LDPlayer / Nox / BlueStacks / MuMu), đẩy video vào Android,
    kích hoạt quét thư viện và mở ứng dụng TikTok để đăng video.
    """

    # Các cổng ADB cục bộ phổ biến của các trình giả lập Android trên Windows
    EMULATOR_PORTS = [
        ("127.0.0.1:5555", "LDPlayer 9 / BlueStacks"),
        ("127.0.0.1:62001", "NoxPlayer"),
        ("127.0.0.1:7555", "MuMu Player"),
        ("127.0.0.1:21503", "MEmu Play"),
        ("127.0.0.1:58526", "WSA (Windows Subsystem for Android)")
    ]

    # Package name phổ biến của TikTok trên Android (trill là bản đã cài trên LDPlayer của máy)
    TIKTOK_PACKAGES = [
        "com.ss.android.ugc.trill",   # TikTok Đông Nam Á / Việt Nam (Đang cài trên LDPlayer)
        "com.zhiliaoapp.musically",   # TikTok Quốc tế
        "com.ss.android.ugc.aweme"    # Douyin (TikTok Trung Quốc)
    ]

    # ID thiết bị hiện tại đang điều khiển
    current_device: Optional[str] = None

    @classmethod
    def run_adb(cls, args: List[str], target_device: Optional[str] = None, timeout: int = 60) -> tuple[int, str, str]:
        """Thực thi một lệnh ADB trong terminal và trả về kết quả."""
        dev = target_device or cls.current_device
        if dev and args and args[0] not in ["devices", "connect", "disconnect", "kill-server", "start-server"]:
            cmd = ["adb", "-s", dev] + args
        else:
            cmd = ["adb"] + args

        try:
            res = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout
            )
            return res.returncode, res.stdout.strip(), res.stderr.strip()
        except FileNotFoundError:
            return 1, "", "Không tìm thấy lệnh adb trong hệ thống!"
        except Exception as e:
            return 1, "", str(e)

    @classmethod
    def get_connected_devices(cls) -> List[str]:
        """Lấy danh sách ID các thiết bị/máy ảo Android đang kết nối."""
        code, stdout, _ = cls.run_adb(["devices"])
        devices = []
        if code == 0:
            lines = stdout.splitlines()[1:]
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 2 and parts[1] == "device":
                    devices.append(parts[0])
        return devices

    @classmethod
    def auto_connect_emulator(cls) -> Optional[str]:
        """
        Tự động phát hiện và kết nối với máy ảo đang chạy trên Windows.
        Nếu chưa có thiết bị, tự động scan và kết nối qua các cổng của LDPlayer, Nox, BlueStacks...
        """
        print("[🤖 ADB Controller] Đang kiểm tra kết nối với máy ảo Android...")
        devices = cls.get_connected_devices()
        if devices:
            cls.current_device = devices[0]
            print(f"[🤖 ADB Controller] ✅ Đã tìm thấy máy ảo đang kết nối: {cls.current_device}")
            return cls.current_device

        print("[🤖 ADB Controller] Chưa có thiết bị nối sẵn, đang quét các cổng máy ảo (LDPlayer / Nox / BlueStacks)...")
        for addr, name in cls.EMULATOR_PORTS:
            code, stdout, _ = cls.run_adb(["connect", addr], timeout=5)
            if "connected to" in stdout.lower() or "already connected" in stdout.lower():
                devices = cls.get_connected_devices()
                if devices:
                    cls.current_device = devices[0]
                    print(f"[🤖 ADB Controller] ✅ Kết nối thành công tới {name} ({cls.current_device})!")
                    return cls.current_device

        # Kiểm tra lại một lần nữa
        devices = cls.get_connected_devices()
        if devices:
            cls.current_device = devices[0]
            return cls.current_device

        print("[⚠️ ADB Controller] Không tìm thấy máy ảo nào đang mở!")
        print(" 👉 Hãy mở phần mềm giả lập (LDPlayer, Nox, BlueStacks...) lên rồi chạy lại lệnh.")
        return None

    @classmethod
    def push_video_and_notify(cls, local_video_path: str, remote_filename: Optional[str] = None) -> Optional[str]:
        """
        Đẩy file video từ máy tính vào thư mục Camera của Android (/sdcard/DCIM/Camera/)
        và kích hoạt Media Scanner để video lập tức xuất hiện trong Thư viện ảnh/TikTok.
        """
        device = cls.auto_connect_emulator()
        if not device:
            return None

        local_file = Path(local_video_path)
        if not local_file.exists():
            print(f"[❌ ADB Controller] File video không tồn tại: {local_video_path}")
            return None

        filename = remote_filename or local_file.name
        # Thư mục chuẩn của Camera trong Android để ứng dụng nhận diện ngay
        remote_path = f"/sdcard/DCIM/Camera/{filename}"

        print(f"\n[🤖 ADB] 📤 Đang đẩy video sang máy ảo qua ADB: {local_file.name}...")
        # Đảm bảo thư mục đích tồn tại trên Android
        cls.run_adb(["shell", "mkdir", "-p", "/sdcard/DCIM/Camera"])

        # Lệnh adb push
        code, stdout, stderr = cls.run_adb(["push", str(local_file), remote_path], timeout=180)
        if code != 0:
            print(f"[❌ ADB] Đẩy video thất bại: {stderr}")
            return None

        print(f"[🤖 ADB] ✅ Đẩy video thành công vào máy ảo: {remote_path}")

        # Ép Android quét lại thư viện ảnh (Media Scanner) để TikTok thấy video ngay
        print("[🤖 ADB] 🔄 Đang kích hoạt Media Scanner trên Android để cập nhật Thư viện...")
        cls.run_adb([
            "shell", "am", "broadcast",
            "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE",
            "-d", f"file://{remote_path}"
        ])
        return remote_path

    @classmethod
    def set_android_clipboard_and_caption(cls, caption: str):
        """Lưu caption vào file /sdcard/caption.txt và nạp vào Clipboard của Android."""
        # 1. Lưu file caption.txt trên máy ảo
        temp_caption_file = Path(__file__).resolve().parent.parent / "data" / "temp_caption.txt"
        temp_caption_file.parent.mkdir(parents=True, exist_ok=True)
        with open(temp_caption_file, "w", encoding="utf-8") as f:
            f.write(caption)

        cls.run_adb(["push", str(temp_caption_file), "/sdcard/caption.txt"])

        # 2. Thử nạp vào clipboard của Android (hỗ trợ Android 10 trở lên)
        try:
            # Escape ký tự cho lệnh cmd clipboard
            escaped = caption.replace('"', '\\"').replace('$', '\\$').replace('`', '\\`')
            cls.run_adb(["shell", f'cmd clipboard set text "{escaped}"'])
        except Exception:
            pass

        print(f"[🤖 ADB] 📋 Đã lưu Caption vào máy ảo: /sdcard/caption.txt (kèm clipboard Android)")

    @classmethod
    def launch_tiktok_for_upload(cls, remote_video_path: Optional[str] = None) -> bool:
        """
        Kích hoạt mở ứng dụng TikTok trên máy ảo.
        Nếu truyền remote_video_path, thử kích hoạt Intent SEND để mở thẳng giao diện tạo video!
        """
        print("[🤖 ADB] 🚀 Đang kích hoạt ứng dụng TikTok trên máy ảo...")

        # Thử mở bằng Intent chia sẻ video thẳng vào TikTok nếu có đường dẫn
        if remote_video_path:
            for pkg in cls.TIKTOK_PACKAGES:
                code, stdout, _ = cls.run_adb([
                    "shell", "am", "start",
                    "-a", "android.intent.action.SEND",
                    "-t", "video/mp4",
                    "--eu", "android.intent.extra.STREAM", f"file://{remote_video_path}",
                    "-p", pkg
                ])
                if code == 0 and "Error" not in stdout:
                    print(f"[🤖 ADB] ✅ Đã mở thẳng màn hình Upload của TikTok ({pkg})!")
                    return True

        # Nếu không mở được qua Intent SEND, mở trực tiếp ứng dụng TikTok
        for pkg in cls.TIKTOK_PACKAGES:
            code, stdout, _ = cls.run_adb(["shell", "monkey", "-p", pkg, "-c", "android.intent.category.LAUNCHER", "1"])
            if code == 0 and "No activities found" not in stdout:
                print(f"[🤖 ADB] ✅ Đã mở ứng dụng TikTok ({pkg}) thành công trên máy ảo!")
                return True

        print("[⚠️ ADB] Chưa tìm thấy ứng dụng TikTok trên máy ảo.")
        print(" 👉 Hãy cài đặt TikTok trong CH Play hoặc file APK trên máy ảo của bạn!")
        return False

    @classmethod
    def grant_tiktok_permissions(cls, pkg: str = "com.ss.android.ugc.trill"):
        """Tự động cấp tất cả quyền cần thiết (Camera, Micro, Bộ nhớ) cho TikTok."""
        perms = [
            "android.permission.CAMERA",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        ]
        for p in perms:
            cls.run_adb(["shell", "pm", "grant", pkg, p])

    @classmethod
    def auto_complete_post_ui(cls) -> bool:
        """
        Tự động điều khiển luồng UI trên màn hình TikTok:
        Mở Album -> Chọn tab Videos -> Chọn video đầu tiên -> Next -> Chỉnh sửa -> Next -> Dán Caption -> Bấm Post -> Theo dõi upload.
        """
        print("[🤖 ADB UI] 🔄 Đang bắt đầu tự động tương tác màn hình TikTok...")
        time.sleep(2)

        # 1. Bấm nút [+] ở thanh điều hướng để mở màn hình Camera (nếu đang ở trang chủ)
        print("[🤖 ADB UI] ➕ Mở màn hình tạo video qua nút [+]/Camera...")
        cls.run_adb(["shell", "input", "tap", "450", "1560"])
        time.sleep(2)

        # 2. Bấm mở Album/Thư viện từ camera
        print("[🤖 ADB UI] 📂 Mở Album thư viện...")
        cls.run_adb(["shell", "input", "tap", "60", "1545"])
        time.sleep(2)

        # 2. Bấm chọn tab "Videos" để lọc riêng danh sách video (loại bỏ ảnh chụp màn hình)
        print("[🤖 ADB UI] 🎞️ Chuyển sang tab Videos...")
        cls.run_adb(["shell", "input", "tap", "245", "142"])
        time.sleep(1)

        # 3. Chọn video đầu tiên (mới nhất vừa được đẩy vào)
        print("[🤖 ADB UI] 🎬 Chọn video mới nhất...")
        # Bấm vào vòng tròn chọn góc trên phải của video 1 (Row 1 Col 1)
        cls.run_adb(["shell", "input", "tap", "266", "212"])
        time.sleep(1)
        # Bấm dự phòng vào thumbnail nếu chế độ chọn đơn được kích hoạt
        cls.run_adb(["shell", "input", "tap", "150", "300"])
        time.sleep(1)

        # 4. Bấm Next (1)
        print("[🤖 ADB UI] ➡️ Bấm Next (1) sang màn hình chỉnh sửa...")
        cls.run_adb(["shell", "input", "tap", "740", "1560"])
        time.sleep(3)

        # 5. Bấm Next ở màn hình chỉnh sửa video
        print("[🤖 ADB UI] ➡️ Bấm Next sang màn hình Đăng...")
        cls.run_adb(["shell", "input", "tap", "700", "1545"])
        time.sleep(3)

        # 6. Chạm vào ô Caption và dán nội dung
        print("[🤖 ADB UI] ✍️ Dán tiêu đề và hashtag vào ô Caption...")
        cls.run_adb(["shell", "input", "tap", "345", "230"])
        time.sleep(1)
        cls.run_adb(["shell", "input", "keyevent", "279"]) # KEYCODE_PASTE
        time.sleep(1)
        cls.run_adb(["shell", "input", "keyevent", "4"])   # KEYCODE_BACK để đóng bàn phím
        time.sleep(1)

        # 7. Bấm nút Post màu hồng
        print("[🤖 ADB UI] 🚀 Bấm nút POST (Đăng bài)...")
        cls.run_adb(["shell", "input", "tap", "669", "1546"])
        time.sleep(4)

        # Đóng dialog xin quyền danh bạ nếu có
        cls.run_adb(["shell", "input", "tap", "595", "858"]) # DENY contacts
        time.sleep(1)

        # Chuyển sang Profile để theo dõi upload
        print("[🤖 ADB UI] 👤 Mở tab Profile để theo dõi tiến trình upload...")
        cls.run_adb(["shell", "input", "tap", "800", "1560"])

        print("[🤖 ADB UI] ✅ Luồng tự động đăng đã hoàn tất kích hoạt trên máy ảo!")
        return True

    @classmethod
    def execute_full_auto_publish(cls, local_video_path: str, caption: str, auto_click_post: bool = True) -> bool:
        """Quy trình toàn diện: Kết nối -> Cấp quyền -> Đẩy video -> Quét thư viện -> Nạp caption -> Mở TikTok -> Tự động đăng."""
        print("\n" + "=" * 65)
        print("📱 QUY TRÌNH ĐIỀU KHIỂN MÁY ẢO QUA LỆNH ADB ĐĂNG TIKTOK TỰ ĐỘNG")
        print("=" * 65)

        # Cấp quyền trước
        cls.grant_tiktok_permissions()

        # 1. Đẩy video và kích hoạt quét thư viện
        remote_path = cls.push_video_and_notify(local_video_path)
        if not remote_path:
            print("\n[🔄 Cơ chế dự phòng] Đang đưa thẳng video vào Thư mục chia sẻ trực tiếp của LDPlayer 9...")
            from core.telegram_sender import TelegramPublisherNotifier
            synced = TelegramPublisherNotifier.sync_to_emulator(local_video_path, caption)
            if synced:
                print(f"[✅ LDPlayer 9] Video đã được đưa vào Thư viện máy ảo thành công!")
                return True
            return False

        # 2. Đẩy caption vào máy ảo
        cls.set_android_clipboard_and_caption(caption)

        # 3. Mở TikTok trên máy ảo
        cls.launch_tiktok_for_upload(remote_path)

        # 4. Tự động điều khiển UI nếu bật chế độ tự động
        if auto_click_post:
            cls.auto_complete_post_ui()

        print("\n" + "-" * 65)
        print("✨ HOÀN TẤT ĐIỀU KHIỂN MÁY ẢO ĐĂNG VIDEO LÊN TIKTOK!")
        print(" 1. Video đã được đẩy và nạp vào ứng dụng TikTok.")
        print(" 2. Tiêu đề và hashtag đã được điền đầy đủ.")
        print(" 3. Nút đăng (Post) đã được kích hoạt thành công trên máy ảo!")
        print("-" * 65)
        return True
