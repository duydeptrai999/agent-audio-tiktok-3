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
        args=["--disable-blink-features=AutomationControlled"],
        viewport={"width": 1920, "height": 1080}
    )
    page = browser.new_page()
    page.goto("https://www.tiktok.com/tiktokstudio/content", timeout=60000)
    time.sleep(5)
    
    # Tìm dropdown quyền riêng tư của video đầu tiên
    privacy_dropdown = page.locator('div:has-text("Chỉ mình")').first
    if privacy_dropdown.count() > 0:
        print("Tìm thấy dropdown 'Chỉ mình', đang click để mở...")
        privacy_dropdown.click(force=True)
        time.sleep(1.5)
        page.screenshot(path="data/privacy_dropdown_open.png")
        
        # Tìm option "Mọi người"
        opt_public = page.locator('div:has-text("Mọi người")').or_(page.locator('li:has-text("Mọi người")')).or_(page.locator('span:has-text("Mọi người")'))
        if opt_public.count() > 0:
            print("Đang chọn 'Mọi người'...")
            opt_public.last.click(force=True)
            time.sleep(2)
            
    page.screenshot(path="data/after_privacy_change.png")
    browser.close()
