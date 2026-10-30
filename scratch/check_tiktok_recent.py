# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from playwright.sync_api import sync_playwright

USER_DATA_DIR = ROOT / "data" / "tiktok_browser_profile"

print("Checking recent posts on TikTok Studio...")
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=str(USER_DATA_DIR),
        headless=True,
        channel="chrome",
        viewport={"width": 1280, "height": 800}
    )
    page = browser.new_page()
    try:
        page.goto("https://www.tiktok.com/tiktokstudio/content", wait_until="networkidle", timeout=45000)
    except Exception as e:
        print(f"Navigation warning: {e}")

    # Chụp ảnh màn hình trang quản lý bài đăng
    screenshot_path = ROOT / "scratch" / "manage_content.png"
    screenshot_path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(screenshot_path))
    print(f"Screenshot saved to: {screenshot_path}")

    # Lấy tiêu đề các bài đăng gần nhất
    try:
        page.wait_for_selector("div, span, p", timeout=10000)
        content_text = page.inner_text("body")
        lines = [line.strip() for line in content_text.split("\n") if line.strip()]
        # In các dòng có chứa TẬP hoặc tiêu đề truyện
        print("\n--- Recent Posts Found ---")
        for line in lines:
            if any(k in line for k in ["TẬP", "Tập", "Chiếu", "Hoàng Hậu", "Vụng Trộm", "Đích Nữ", "Cung"]):
                print(f"  * {line}")
    except Exception as e:
        print(f"Error parsing content: {e}")

    browser.close()
