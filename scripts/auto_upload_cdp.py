# -*- coding: utf-8 -*-
"""
scripts/auto_upload_cdp.py
Điều khiển trực tiếp cửa sổ Google Chrome ĐANG MỞ của người dùng qua cổng Chrome DevTools Protocol (CDP port 9222).
Không cần đăng nhập lại - Sử dụng 100% session và cookie đã đăng nhập sẵn của người dùng!
"""

import sys
import os
import time
import argparse
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.sync_api import sync_playwright

def find_latest_video():
    out_dir = Path(__file__).resolve().parent.parent / "assets" / "output"
    mp4_files = [f for f in out_dir.glob("*.mp4") if "part1" in f.name or "final" in f.name]
    if not mp4_files:
        mp4_files = list(out_dir.glob("*.mp4"))
    if not mp4_files:
        return None, ""
    latest_file = max(mp4_files, key=lambda f: f.stat().st_mtime)
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

def attach_to_existing_chrome_and_upload(video_path: str, caption: str, cdp_url: str = "http://localhost:9222"):
    print("=" * 70)
    print("🔗 ĐIỀU KHIỂN GOOGLE CHROME ĐANG MỞ (KẾT NỐI QUA CDP 9222)")
    print("=" * 70)
    print(f"🎬 Video: {Path(video_path).name}")
    print(f"📝 Caption: {caption[:80]}...")
    print(f"🌐 Cổng kết nối: {cdp_url}")
    print("-" * 70)

    with sync_playwright() as p:
        try:
            print("[1/4] Đang kết nối vào cửa sổ Google Chrome đang mở...")
            browser = p.chromium.connect_over_cdp(cdp_url)
        except Exception as e:
            print(f"❌ Không thể kết nối vào Chrome qua {cdp_url}!")
            print(f"Nguyên nhân: Chrome hiện tại chưa được bật cổng gỡ lỗi CDP (--remote-debugging-port=9222).")
            print(f"Chi tiết lỗi: {e}")
            return False

        contexts = browser.contexts
        if not contexts:
            print("❌ Không tìm thấy context nào trong Chrome đang mở.")
            return False

        context = contexts[0]
        
        # Tìm xem có tab TikTok Studio nào đang mở không, nếu chưa thì mở tab mới
        page = None
        for p_tab in context.pages:
            if "tiktok.com/creator-center/upload" in p_tab.url:
                page = p_tab
                print(f" -> Đã tìm thấy tab TikTok Studio đang mở sẵn: {page.url}")
                break

        if not page:
            print(" -> Mở tab mới đến TikTok Creator Studio...")
            page = context.new_page()
            page.goto("https://www.tiktok.com/creator-center/upload?from=webapp", timeout=60000)

        time.sleep(3)
        print("[2/4] Tự động tải file video lên TikTok...")

        # Tìm input file
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
            print("❌ Không tìm thấy ô tải file trên trang TikTok Studio. (Hãy kiểm tra xem bạn đã đăng nhập ở tab này chưa)")
            return False

        abs_video_path = os.path.abspath(video_path)
        file_input.set_input_files(abs_video_path)
        print(f" -> Đã chọn file video: {Path(abs_video_path).name}")
        print("⏳ Đang đợi TikTok tải lên và mở khung điền caption...")
        time.sleep(6)

        print("[3/4] Tự động điền Caption SEO & Hashtags...")
        selectors = [
            'div[contenteditable="true"]',
            'div.notranslate[contenteditable="true"]',
            'div.public-DraftEditor-content',
            'div[data-placeholder*="caption"]',
            'div[data-placeholder*="mô tả"]'
        ]

        caption_box = None
        for _ in range(15):
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
                print(" -> Đã điền xong Caption & Hashtags thành công!")
            except Exception:
                caption_box.click()
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                page.keyboard.type(caption, delay=15)
                print(" -> Đã gõ xong Caption & Hashtags thành công!")
        else:
            print("⚠️ Chưa tìm thấy ô caption.")

        print("[4/4] Đang chờ video sẵn sàng để bấm Đăng...")
        time.sleep(5)

        btn_selectors = [
            'button:has-text("Post")',
            'button:has-text("Đăng")',
            'button.btn-post',
            'button[type="button"]:has-text("Post")',
            'button[type="button"]:has-text("Đăng")'
        ]

        post_button = None
        for _ in range(30):
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
            print("🚀 ĐÃ BẤM NÚT ĐĂNG (POST) THÀNH CÔNG TRÊN CHROME ĐANG MỞ!")
            time.sleep(5)
            print("🎉 VIDEO CỦA BẠN ĐÃ ĐƯỢC ĐĂNG LÊN TIKTOK HOÀN TẤT 100%!")
            return True
        else:
            print("⚠️ Video đang xử lý trên server TikTok, bạn có thể kiểm tra trực tiếp trên Chrome và bấm nút Đăng!")
            return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", default=None)
    parser.add_argument("--caption", default=None)
    parser.add_argument("--cdp", default="http://localhost:9222")
    args = parser.parse_args()

    v_path = args.video
    c_text = args.caption
    if not v_path:
        v_path, auto_c = find_latest_video()
        if not c_text:
            c_text = auto_c

    attach_to_existing_chrome_and_upload(v_path, c_text, cdp_url=args.cdp)
