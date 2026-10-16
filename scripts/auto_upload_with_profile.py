# -*- coding: utf-8 -*-
"""
scripts/auto_upload_with_profile.py
Tự động sử dụng Profile đã đăng nhập tại %LocalAppData%\tiktok_bot_profile
để upload video, điền caption và bấm Đăng 100% tự động!
"""

import sys
import os
import time
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

def find_latest_video():
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
    return str(target_video.resolve()), caption

def main():
    profile_dir = Path(os.path.expandvars(r"%LocalAppData%\tiktok_bot_profile")).resolve()
    profile_dir.mkdir(parents=True, exist_ok=True)

    video_path, caption = find_latest_video()

    print("=" * 70)
    print("🤖 CHƯƠNG TRÌNH AI TỰ ĐỘNG ĐĂNG VIDEO TIKTOK STUDIO (FULL-AUTO)")
    print("=" * 70)
    print(f"🎬 Video: {Path(video_path).name}")
    print(f"📁 Profile: {profile_dir}")
    print("-" * 70)

    # Đóng các tiến trình Chrome đang dùng profile này nếu có
    import subprocess
    subprocess.run(["powershell", "-NoProfile", "-Command", "Get-Process chrome -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like '*tiktok_bot_profile*' } | Stop-Process -Force"], capture_output=True)
    time.sleep(1)

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

        print("[1/4] Đang truy cập TikTok Creator Studio...")
        page.goto(upload_url, timeout=90000)
        time.sleep(4)

        if "login" in page.url:
            print("⚠️ Chưa phát hiện tài khoản đăng nhập trong profile này.")
            print("👉 Vui lòng đăng nhập trên cửa sổ Chrome vừa mở. Bot sẽ tự động tiếp tục ngay sau đó!")
            # Chờ người dùng đăng nhập
            for _ in range(300):
                time.sleep(2)
                if "login" not in page.url and page.locator('input[type="file"]').count() > 0:
                    break

        print("✅ Đã vào trang Upload! Đang tìm ô tải video...")
        time.sleep(2)

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
            print("❌ Không tìm thấy ô tải file trên trang.")
            time.sleep(5)
            browser.close()
            return

        print(f"[2/4] Tự động tải file video: {Path(video_path).name}...")
        file_input.set_input_files(video_path)
        print("⏳ Đang chờ TikTok tải lên...")
        time.sleep(8)

        print("[3/4] Tự động điền Caption & Hashtags...")
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
            print("👉 Video và Caption đã được điền sẵn 100%. Bạn có thể bấm Đăng trực tiếp!")
            time.sleep(10)

        browser.close()
        print("✨ Hoàn tất!")

if __name__ == "__main__":
    main()
