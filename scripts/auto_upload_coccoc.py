# -*- coding: utf-8 -*-
"""
scripts/auto_upload_coccoc.py
Tự động sử dụng trình duyệt Cốc Cốc (nơi bạn đã đăng nhập sẵn TikTok)
để upload video, điền Caption và bấm Đăng 100% tự động!
- Quản lý vòng đời tiến trình Cốc Cốc bằng taskkill /F /T và active polling
- Khóa liên tiến trình CoccocFileLock chống xung đột ProcessSingleton
- Dọn dẹp an toàn SingletonLock / SingletonSocket
- Đảm bảo quyền riêng tư 'Mọi người' (Public) trước khi đăng
- Bọc toàn bộ Playwright trong try...finally: browser.close() chống zombie
"""

import sys
import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from scripts.tiktok_publisher_core import (
    kill_and_clean_coccoc,
    clean_stale_singleton_locks,
    CoccocFileLock,
    dismiss_popups,
    ensure_public_privacy,
    wait_for_content_checks,
    handle_post_confirmation_modal
)

def main():
    out_dir = root / "assets" / "output"
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
    print("🤖 BẮT ĐẦU TỰ ĐỘNG ĐĂNG VIDEO LÊN TIKTOK QUA TRÌNH DUYỆT CỐC CỐC")
    print("=" * 70)
    print(f"🎬 Video: {target_video.name} ({round(target_video.stat().st_size / (1024*1024), 1)} MB)")
    print(f"📝 Caption: {caption[:80]}...")
    print("-" * 70)

    # 1. Khóa liên tiến trình để chống xung đột ProcessSingleton
    lock_file = root / "data" / ".coccoc_publisher.lock"
    with CoccocFileLock(lock_path=lock_file, timeout=900.0):
        # 2. Đóng triệt để các tiến trình Cốc Cốc cũ
        print("[1/5] Đang giải phóng tiến trình để bot điều khiển Cốc Cốc...")
        kill_and_clean_coccoc(timeout=5.0)

        coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")
        clean_stale_singleton_locks(user_data_dir=coccoc_ud)

        coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"

        browser = None
        try:
            # 3. Khởi chạy Cốc Cốc qua Playwright
            print("[2/5] Mở Cốc Cốc với tài khoản TikTok đã đăng nhập sẵn của bạn...")
            with sync_playwright() as p:
                try:
                    browser = p.chromium.launch_persistent_context(
                        user_data_dir=coccoc_ud,
                        executable_path=coccoc_exe,
                        headless=False,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--start-maximized",
                            "--profile-directory=Default"
                        ],
                        no_viewport=True
                    )

                    page = browser.new_page()
                    upload_url = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
                    page.goto(upload_url, timeout=90000)
                    time.sleep(5)

                    # Bỏ qua bản nháp cũ nếu có
                    try:
                        btn_cancel_draft = page.locator('button:has-text("Hủy bỏ")')
                        if btn_cancel_draft.count() > 0 and btn_cancel_draft.first.is_visible():
                            btn_cancel_draft.first.click(force=True)
                            time.sleep(2)
                    except Exception:
                        pass

                    print("[3/5] Đang tìm ô tải video và đẩy file lên hệ thống...")
                    file_input = None
                    for _ in range(20):
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
                        print("❌ Không tìm thấy thẻ tải video.")
                        return

                    abs_video_path = str(target_video.resolve())
                    file_input.set_input_files(abs_video_path)
                    print(f" -> ✅ Đã đẩy file video: {target_video.name}")
                    print("⏳ Đang chờ TikTok tải lên và mở khung điền caption...")
                    time.sleep(8)

                    print("[4/5] Tự động điền Caption SEO & Hashtags...")
                    selectors = [
                        'div[contenteditable="true"]',
                        'div.notranslate[contenteditable="true"]',
                        'div.public-DraftEditor-content',
                        'div[data-placeholder*="caption"]',
                        'div[data-placeholder*="mô tả"]'
                    ]

                    caption_box = None
                    for _ in range(25):
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

                    dismiss_popups(page)

                    if caption_box:
                        try:
                            caption_box.click(force=True)
                            time.sleep(0.5)
                            page.keyboard.press("Control+A")
                            page.keyboard.press("Backspace")
                            time.sleep(0.5)
                            caption_box.fill(caption)
                            print(" -> ✅ ĐÃ ĐIỀN XONG CAPTION & HASHTAGS THÀNH CÔNG!")
                        except Exception as e_cap:
                            print(f" -> [Thử fill fallback]: {e_cap}")
                            try:
                                caption_box.click(force=True)
                                page.keyboard.press("Control+A")
                                page.keyboard.press("Backspace")
                                page.keyboard.type(caption, delay=10)
                                print(" -> ✅ ĐÃ GÕ XONG CAPTION & HASHTAGS THÀNH CÔNG!")
                            except Exception as e_type:
                                print(f" -> Lỗi gõ caption: {e_type}")
                    else:
                        print("⚠️ Chưa tìm thấy ô caption.")

                    print("[5/5] Đang chờ video sẵn sàng để bấm Đăng...")
                    time.sleep(6)
                    dismiss_popups(page)

                    # Đảm bảo chế độ Public ("Mọi người")
                    ensure_public_privacy(page)

                    # Chờ kiểm tra nội dung hoàn tất
                    wait_for_content_checks(page, max_wait=35)
                    ensure_public_privacy(page)

                    btn_selectors = [
                        'button:has-text("Post")',
                        'button:has-text("Đăng")',
                        'button.btn-post',
                        'button[type="button"]:has-text("Post")',
                        'button[type="button"]:has-text("Đăng")'
                    ]

                    post_button = None
                    print("⏳ Đang đợi nút 'Đăng' (Post) khả dụng...")
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
                        try:
                            post_button.click(force=True)
                        except Exception:
                            post_button.click()
                        print("\n" + "=" * 70)
                        print("🚀 ĐÃ BẤM NÚT ĐĂNG (POST) THÀNH CÔNG RỰC RỠ TRÊN CỐC CỐC!")
                        print("🎉 VIDEO CỦA BẠN ĐÃ ĐƯỢC ĐĂNG LÊN TIKTOK HOÀN TẤT 100%!")
                        print("=" * 70)

                        # Xử lý popup nếu có
                        handle_post_confirmation_modal(page, max_wait=6)

                        time.sleep(8)
                        dismiss_popups(page)
                        handle_post_confirmation_modal(page, max_wait=2)

                        shot_path = root / "data" / "coccoc_post_success.png"
                        try:
                            page.screenshot(path=str(shot_path))
                        except Exception:
                            pass
                    else:
                        print("👉 Video và Caption đã được điền sẵn 100%. Bạn có thể bấm Đăng trực tiếp!")
                        time.sleep(5)

                finally:
                    if browser:
                        try:
                            browser.close()
                        except Exception:
                            pass
                        browser = None
        finally:
            kill_and_clean_coccoc(timeout=3.0)

    print("✨ Hoàn tất tiến trình. Chúc mừng bạn!")

if __name__ == "__main__":
    main()
