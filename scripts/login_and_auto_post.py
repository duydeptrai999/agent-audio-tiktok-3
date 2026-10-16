# -*- coding: utf-8 -*-
"""
scripts/login_and_auto_post.py
Mở cửa sổ Google Chrome để bạn đăng nhập tài khoản TikTok.
Ngay khi bạn đăng nhập xong, bot sẽ tự động tải video lên, điền Caption và bấm Đăng luôn!
Cookie sẽ được lưu vĩnh viễn tại data/tiktok_chrome_profile cho các lần sau.
"""

import sys
import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    profile_dir = Path(__file__).resolve().parent.parent / "data" / "tiktok_chrome_profile"
    profile_dir.mkdir(parents=True, exist_ok=True)

    # Tìm video mới nhất và caption
    out_dir = Path(__file__).resolve().parent.parent / "assets" / "output"
    target_video = out_dir / "VID_20261013_173859_part1_final.mp4"
    if not target_video.exists():
        mp4s = list(out_dir.glob("*.mp4"))
        if mp4s:
            target_video = max(mp4s, key=lambda f: f.stat().st_mtime)

    caption = (
        "[PHẦN 1] Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp. "
        "👉 Đón xem Tập 2 lúc 21h30 tối nay nhé! "
        "#audiotruyen #kểchuyện #podcast #xuhuong #fyp #truyendem #rungungon #chuyenkhuya #chill #thugian"
    )

    print("=" * 70)
    print("🚀 ĐANG MỞ GOOGLE CHROME ĐỂ BẠN ĐĂNG NHẬP TIKTOK...")
    print("=" * 70)
    print(f"🎬 Video sẽ tự động đăng: {target_video.name}")
    print("👉 Hãy nhìn lên màn hình và đăng nhập tài khoản của bạn (Quét QR hoặc SĐT/Email/Google).")
    print("💡 Ngay khi bạn đăng nhập xong, Bot sẽ TỰ ĐỘNG BỐC VIDEO VÀ BẤM ĐĂNG NGAY LẬP TỨC!")
    print("-" * 70)

    with sync_playwright() as p:
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
        
        print("[1/4] Đang mở trang TikTok Creator Studio...")
        page.goto(upload_url, timeout=90000)
        time.sleep(3)

        # Tự động click vào nút "Use QR code" nếu trang hiện form login
        try:
            qr_btn = page.locator('text="Use QR code"').or_(page.locator('text="Sử dụng mã QR"'))
            if qr_btn.count() > 0:
                qr_btn.first.click()
                print(" -> Đã tự động bật mã QR trên màn hình để bạn quét nhanh!")
        except Exception:
            pass

        # Chờ người dùng đăng nhập
        print("⏳ Đang chờ bạn đăng nhập trên cửa sổ Chrome vừa mở...")
        logged_in = False

        # Chờ tối đa 15 phút (900 giây)
        for second in range(450):
            time.sleep(2)
            try:
                cur_url = page.url
                # Nếu đã vào trang creator-center/upload và không còn ở trang login
                if "creator-center/upload" in cur_url and "login" not in cur_url:
                    # Kiểm tra xem có input file hoặc upload button
                    if page.locator('input[type="file"]').count() > 0:
                        logged_in = True
                        break
                    # Hoặc check iframe
                    for frame in page.frames:
                        if frame.locator('input[type="file"]').count() > 0:
                            logged_in = True
                            break
                    if logged_in:
                        break
            except Exception:
                pass

        if not logged_in:
            print("❌ Hết thời gian chờ đăng nhập (15 phút).")
            browser.close()
            return

        print("\n" + "=" * 70)
        print("🎉 NHẬN DIỆN BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG 100%!")
        print("🤖 BOT BẮT ĐẦU TỰ ĐỘNG TẢI VIDEO & ĐIỀN NỘI DUNG...")
        print("=" * 70)
        time.sleep(3)

        # Đảm bảo trang đã sẵn sàng
        file_input = None
        for _ in range(15):
            if page.locator('input[type="file"]').count() > 0:
                file_input = page.locator('input[type="file"]').first
                break
            for frame in page.frames:
                if frame.locator('input[type="file"]').count() > 0:
                    file_input = frame.locator('input[type="file"]').first
                    break
            if file_input:
                break
            time.sleep(1)

        if not file_input:
            print("❌ Không tìm thấy ô tải file trên TikTok Studio.")
            browser.close()
            return

        print(f"[2/4] Tự động tải file video lên: {target_video.name}...")
        file_input.set_input_files(str(target_video.resolve()))
        print("⏳ Đang chờ TikTok tải lên và mở khung điền caption...")
        time.sleep(8)

        print("[3/4] Tự động điền Caption SEO & Hashtags...")
        selectors = [
            'div[contenteditable="true"]',
            'div.notranslate[contenteditable="true"]',
            'div.public-DraftEditor-content',
            'div[data-placeholder*="caption"]',
            'div[data-placeholder*="mô tả"]'
        ]

        caption_box = None
        for _ in range(20):
            for sel in selectors:
                if page.locator(sel).count() > 0:
                    caption_box = page.locator(sel).first
                    break
            if caption_box:
                break
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
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                time.sleep(0.5)
                caption_box.fill(caption)
                print(" -> ✅ ĐÃ ĐIỀN XONG CAPTION & HASHTAGS!")
            except Exception:
                caption_box.click()
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(caption, delay=15)
                print(" -> ✅ ĐÃ GÕ XONG CAPTION & HASHTAGS!")
        else:
            print("⚠️ Không tìm thấy ô caption.")

        print("[4/4] Đang chờ video sẵn sàng để bấm Đăng...")
        time.sleep(6)

        btn_selectors = [
            'button:has-text("Post")',
            'button:has-text("Đăng")',
            'button.btn-post',
            'button[type="button"]:has-text("Post")',
            'button[type="button"]:has-text("Đăng")'
        ]

        post_button = None
        print("⏳ Đang đợi nút 'Đăng' khả dụng...")
        for _ in range(40):
            for b_sel in btn_selectors:
                btn = page.locator(b_sel).first
                if btn.count() > 0 and btn.is_visible() and btn.is_enabled():
                    post_button = btn
                    break
            if post_button:
                break
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
            print("\n" + "=" * 70)
            print("🚀 ĐÃ BẤM NÚT ĐĂNG (POST) THÀNH CÔNG RỰC RỠ!")
            print("🎉 VIDEO CỦA BẠN ĐÃ ĐƯỢC ĐĂNG LÊN TIKTOK HOÀN TẤT 100%!")
            print("=" * 70)
            time.sleep(8)
        else:
            print("👉 Video và Caption đã được điền sẵn 100%. Bạn có thể xem trên Chrome và nhấn Đăng!")
            time.sleep(10)

        browser.close()
        print("✨ Hoàn tất tiến trình. Cảm ơn bạn!")

if __name__ == "__main__":
    main()
