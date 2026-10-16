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

    # Nếu có nút "Tiếp tục"
    btn_cont = page.locator('button:has-text("Tiếp tục")')
    if btn_cont.count() > 0 and btn_cont.first.is_visible():
        btn_cont.first.click(force=True)
        print("Đã bấm 'Tiếp tục'")
        time.sleep(3)

    # Click nút Đăng
    post_btn = None
    buttons = page.locator("button")
    for i in range(buttons.count()):
        b = buttons.nth(i)
        if b.inner_text().strip() == "Đăng":
            post_btn = b
            break
            
    if post_btn:
        post_btn.scroll_into_view_if_needed()
        time.sleep(1)
        post_btn.click(force=True)
        print("Đã bấm 'Đăng'")
        time.sleep(2)

    # Click "Đăng ngay" nếu có popup xác nhận
    btn_dang_ngay = page.locator('button:has-text("Đăng ngay")')
    if btn_dang_ngay.count() > 0 and btn_dang_ngay.first.is_visible():
        btn_dang_ngay.first.click(force=True)
        print("🎉 ĐÃ BẤM 'ĐĂNG NGAY' XÁC NHẬN!")
        time.sleep(5)
    else:
        print("Không thấy popup 'Đăng ngay'")

    # Chờ 15s để chuyển trang
    for s in range(5):
        time.sleep(3)
        page.screenshot(path=f"data/confirm_dang_ngay_step_{s}.png")
        if "content" in page.url:
            print(f"Đã chuyển sang: {page.url}")
            break

    browser.close()
