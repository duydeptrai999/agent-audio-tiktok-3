# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.tiktok_publisher_core import clean_stale_singleton_locks
from playwright.sync_api import sync_playwright

coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")
coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
if not os.path.exists(coccoc_exe):
    coccoc_exe = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\Application\browser.exe")

clean_stale_singleton_locks(coccoc_ud)

print("Checking recent posts via Cốc Cốc Profile...")
with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=coccoc_ud,
        executable_path=coccoc_exe if os.path.exists(coccoc_exe) else None,
        headless=True,
        args=["--profile-directory=Default", "--no-sandbox"]
    )
    page = browser.new_page()
    page.goto("https://www.tiktok.com/tiktokstudio/content")
    page.wait_for_timeout(8000)
    print("Current URL:", page.url)
    screenshot_path = ROOT / "scratch" / "manage_content.png"
    page.screenshot(path=str(screenshot_path))
    print(f"Screenshot saved to: {screenshot_path}")

    all_text = page.inner_text("body")
    print("--- LINES WITH KEYWORDS ---")
    for line in all_text.split("\n"):
        line = line.strip()
        if any(w in line for w in ["TẬP", "Đích Nữ", "Phượng Hoàng", "Vụng Trộm", "Công Chúa"]):
            print(f"  * {line}")
    browser.close()
