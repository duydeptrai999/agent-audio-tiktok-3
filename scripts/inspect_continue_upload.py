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
    page.goto("https://www.tiktok.com/tiktokstudio/upload?from=webapp", timeout=60000)
    time.sleep(4)
    
    # Click "Tiếp tục"
    btn_cont = page.locator('button:has-text("Tiếp tục")')
    if btn_cont.count() > 0 and btn_cont.first.is_visible():
        btn_cont.first.click(force=True)
        print("Đã click 'Tiếp tục'")
        time.sleep(5)
    
    page.screenshot(path="data/debug_after_continue.png")
    
    # Scroll down to bottom and screenshot
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    page.screenshot(path="data/debug_bottom_buttons.png")
    
    buttons = page.locator("button")
    print(f"Total buttons on page: {buttons.count()}")
    for i in range(buttons.count()):
        try:
            b = buttons.nth(i)
            txt = b.inner_text().strip().replace("\n", " ")
            vis = b.is_visible()
            dis = b.is_disabled()
            if txt:
                print(f"  Btn {i}: '{txt}' (visible={vis}, disabled={dis})")
        except Exception:
            pass
            
    browser.close()
