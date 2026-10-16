# -*- coding: utf-8 -*-
"""
scripts/auto_tiktok_uploader.py
Tool tự động điều khiển Google Chrome (Playwright) đăng video lên TikTok Creator Studio 100% tự động.
Hỗ trợ lưu Cookie đăng nhập vĩnh viễn tại data/tiktok_chrome_profile.
"""

import sys
import os
import time
import argparse
from pathlib import Path

# Đảm bảo in tiếng Việt trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.sync_api import sync_playwright

def find_latest_video():
    """Tìm video thành phẩm mới nhất trong assets/output"""
    out_dir = Path(__file__).resolve().parent.parent / "assets" / "output"
    mp4_files = [f for f in out_dir.glob("*.mp4") if "part1" in f.name or "final" in f.name]
    if not mp4_files:
        mp4_files = list(out_dir.glob("*.mp4"))
    if not mp4_files:
        return None, ""
    
    latest_file = max(mp4_files, key=lambda f: f.stat().st_mtime)
    
    # Tìm file caption tương ứng
    meta_files = list(out_dir.glob(f"{latest_file.stem}*.txt"))
    caption = ""
    if meta_files:
        try:
            with open(meta_files[0], "r", encoding="utf-8") as f:
                content = f.read()
                if "Caption SEO:" in content:
                    caption = content.split("Caption SEO:")[1].split("---")[0].strip()
        except Exception:
            pass
    if not caption:
        caption = f"[TRUYỆN AUDIO] {latest_file.stem} #audiotruyen #kểchuyện #xuhuong #fyp"

    return str(latest_file), caption

def upload_video_to_tiktok(video_path: str, caption: str, auto_click_post: bool = True):
    print("=" * 70)
    print("🤖 CHƯƠNG TRÌNH ĐIỀU KHIỂN GOOGLE CHROME TỰ ĐỘNG ĐĂNG VIDEO TIKTOK")
    print("=" * 70)
    print(f"🎬 Video: {Path(video_path).name} ({round(os.path.getsize(video_path)/(1024*1024), 1)} MB)")
    print(f"📝 Caption: {caption[:100]}...")
    print(f"⚡ Tự động bấm nút Đăng: {'BẬT (Full-Auto)' if auto_click_post else 'TẮT (Chỉ điền sẵn)'}")
    print("-" * 70)

    profile_dir = Path(__file__).resolve().parent.parent / "data" / "tiktok_chrome_profile"
    profile_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        print("[1/5] Khởi động Google Chrome với Profile lưu trữ an toàn...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            channel="chrome",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ],
            no_viewport=True
        )

        page = browser.new_page()
        upload_url = "https://www.tiktok.com/creator-center/upload?from=webapp"
        
        print("[2/5] Đang truy cập trang TikTok Creator Studio...")
        page.goto(upload_url, timeout=90000)
        time.sleep(3)

        # Kiểm tra xem có đang ở trang Đăng Nhập không
        login_indicators = ["Log in to TikTok", "Đăng nhập vào TikTok", "login", "Use QR code"]
        is_login_page = any(kw in page.content() or kw in page.url for kw in ["login", "signin"]) or "Log in to TikTok" in page.content()

        if is_login_page:
            print("\n" + "!" * 70)
            print("⚠️ PHÁT HIỆN CHƯA ĐĂNG NHẬP TÀI KHOẢN TIKTOK TRÊN PROFILE NÀY!")
            print("👉 VUI LÒNG QUÉT MÃ QR HOẶC ĐĂNG NHẬP TRÊN CỬA SỔ CHROME VỪA MỞ.")
            print("💡 (Chỉ cần đăng nhập 1 LẦN DUY NHẤT này, Cookie sẽ được lưu mãi mãi cho các lần sau!)")
            print("!" * 70 + "\n")

            # Tự động click vào 'Use QR code' nếu có để hiện to mã QR cho người dùng quét
            try:
                qr_btn = page.locator('text="Use QR code"').or_(page.locator('text="Sử dụng mã QR"'))
                if qr_btn.count() > 0:
                    qr_btn.first.click()
                    print(" -> Đã tự động mở giao diện quét mã QR cho bạn.")
            except Exception:
                pass

            # Chờ người dùng đăng nhập (chờ tối đa 5 phút)
            print("⏳ Đang chờ bạn hoàn tất đăng nhập trên màn hình...")
            logged_in = False
            for _ in range(60):
                time.sleep(5)
                # Nếu đã vào trang creator-center/upload và không còn ở trang login
                if "creator-center/upload" in page.url and "login" not in page.url:
                    # Kiểm tra xem có input file hoặc avatar chưa
                    if page.locator('input[type="file"]').count() > 0 or page.locator('iframe').count() > 0:
                        logged_in = True
                        break
                elif page.locator('input[type="file"]').count() > 0:
                    logged_in = True
                    break

            if not logged_in:
                print("❌ Hết thời gian chờ đăng nhập (5 phút). Vui lòng thử lại sau!")
                browser.close()
                return False
            else:
                print("✅ ĐÃ ĐĂNG NHẬP THÀNH CÔNG! Đang tiếp tục quy trình tự động...")
                time.sleep(3)

        # Đảm bảo đang ở trang Upload
        if "creator-center/upload" not in page.url:
            page.goto(upload_url, timeout=60000)
            time.sleep(3)

        print("[3/5] Đang tải file video lên hệ thống TikTok...")
        # Tìm input type="file" (có thể nằm trong iframe hoặc trang chính)
        file_input = None
        for _ in range(10):
            if page.locator('input[type="file"]').count() > 0:
                file_input = page.locator('input[type="file"]').first
                break
            # Kiểm tra trong các iframes
            for frame in page.frames:
                if frame.locator('input[type="file"]').count() > 0:
                    file_input = frame.locator('input[type="file"]').first
                    break
            if file_input:
                break
            time.sleep(1)

        if not file_input:
            print("❌ Không tìm thấy ô tải file trên trang TikTok Studio.")
            browser.close()
            return False

        # Đẩy file video vào input
        abs_video_path = os.path.abspath(video_path)
        file_input.set_input_files(abs_video_path)
        print(f" -> Đã chọn file: {Path(abs_video_path).name}")
        print("⏳ Đang chờ TikTok upload và xử lý video...")
        time.sleep(6)

        print("[4/5] Đang điền Caption SEO & Hashtags...")
        # Tìm ô nhập Caption (ContentEditable div)
        caption_box = None
        selectors = [
            'div[contenteditable="true"]',
            'div.notranslate[contenteditable="true"]',
            'div.public-DraftEditor-content',
            'div[data-placeholder*="caption"]',
            'div[data-placeholder*="mô tả"]'
        ]

        for _ in range(15):
            for sel in selectors:
                if page.locator(sel).count() > 0:
                    caption_box = page.locator(sel).first
                    break
            if caption_box:
                break
            # Kiểm tra trong iframe
            for frame in page.frames:
                for sel in selectors:
                    if frame.locator(sel).count() > 0:
                        caption_box = frame.locator(sel).first
                        break
                if caption_box:
                    break
            if caption_box:
                break
            time.sleep(2)

        if caption_box:
            try:
                caption_box.click()
                time.sleep(0.5)
                # Xóa caption cũ tự sinh (tên file video)
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                time.sleep(0.5)
                # Điền Caption mới
                caption_box.fill(caption)
                print(" -> Đã điền xong Caption & Hashtags thành công!")
            except Exception as e_cap:
                print(f" -> [Caption fallback]: {e_cap}, thử qua keyboard type...")
                caption_box.click()
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(caption, delay=15)
        else:
            print("⚠️ Không tìm thấy ô caption tự động, vui lòng kiểm tra.")

        # Chờ video tải lên hoàn tất (thường nút Đăng sẽ enable)
        print("[5/5] Đang kiểm tra trạng thái video và chuẩn bị Đăng...")
        time.sleep(5)

        if auto_click_post:
            post_button = None
            btn_selectors = [
                'button:has-text("Post")',
                'button:has-text("Đăng")',
                'button.btn-post',
                'button[type="button"]:has-text("Post")',
                'button[type="button"]:has-text("Đăng")'
            ]

            print("⏳ Đang chờ nút Đăng (Post) khả dụng...")
            for _ in range(30):
                for b_sel in btn_selectors:
                    btn = page.locator(b_sel).first
                    if btn.count() > 0 and btn.is_visible() and btn.is_enabled():
                        post_button = btn
                        break
                if post_button:
                    break
                # Check trong iframe
                for frame in page.frames:
                    for b_sel in btn_selectors:
                        btn = frame.locator(b_sel).first
                        if btn.count() > 0 and btn.is_visible() and btn.is_enabled():
                            post_button = btn
                            break
                    if post_button:
                        break
                if post_button:
                    break
                time.sleep(2)

            if post_button:
                post_button.click()
                print("🚀 ĐÃ BẤM NÚT ĐĂNG (POST) THÀNH CÔNG!")
                time.sleep(5)
                print("🎉 VIDEO CỦA BẠN ĐÃ ĐƯỢC ĐĂNG LÊN TIKTOK HOÀN TẤT 100%!")
            else:
                print("⚠️ Chưa tìm thấy nút Đăng sẵn sàng (có thể video đang còn render trên máy chủ TikTok).")
                print("👉 Vui lòng nhìn lên màn hình Chrome và bấm nút 'Đăng' để hoàn tất!")
        else:
            print("👉 Video và Caption đã được điền sẵn trên Chrome. Bạn chỉ cần nhấn nút 'Đăng'!")

        # Giữ màn hình vài giây rồi kết thúc
        time.sleep(5)
        browser.close()
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto TikTok Studio Web Uploader")
    parser.add_argument("--video", default=None, help="Đường dẫn file video mp4")
    parser.add_argument("--caption", default=None, help="Nội dung caption SEO")
    parser.add_argument("--no-click", action="store_true", help="Không tự động bấm nút Đăng (chỉ upload và điền sẵn)")
    args = parser.parse_args()

    v_path = args.video
    c_text = args.caption

    if not v_path:
        v_path, auto_c = find_latest_video()
        if not c_text:
            c_text = auto_c

    if not v_path or not os.path.exists(v_path):
        print(f"❌ Không tìm thấy video hợp lệ để đăng: {v_path}")
        sys.exit(1)

    upload_video_to_tiktok(v_path, c_text, auto_click_post=not args.no_click)
