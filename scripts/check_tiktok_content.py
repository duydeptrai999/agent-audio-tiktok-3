# -*- coding: utf-8 -*-
import sys
import os
import time
import subprocess
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")

subprocess.run(["taskkill", "/F", "/IM", "browser.exe"], capture_output=True)
time.sleep(1)

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir=coccoc_ud,
        executable_path=coccoc_exe,
        headless=True,
        args=["--disable-blink-features=AutomationControlled"]
    )
    page = browser.new_page()
    page.goto("https://www.tiktok.com/tiktokstudio/content", timeout=60000)
    time.sleep(5)
    page.screenshot(path="data/coccoc_current_content.png")
    print(f"URL: {page.url}")
    print("Page Title:", page.title())
    content = page.content()
    print("Has 'Chiếc Áo Đồng Phục':", "Chiếc Áo Đồng Phục" in content)
    browser.close()
