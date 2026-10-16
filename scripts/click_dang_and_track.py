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
    time.sleep(3)
    
    # 1. Bấm "Tiếp tục" nếu có
    btn_cont = page.locator('button:has-text("Tiếp tục")')
    if btn_cont.count() > 0 and btn_cont.first.is_visible():
        btn_cont.first.click(force=True)
        print("Đã bấm 'Tiếp tục'")
        time.sleep(3)
        
    # 2. Tìm nút Đăng
    # Nút Đăng trong danh sách buttons:
    post_btn = None
    buttons = page.locator("button")
    for i in range(buttons.count()):
        b = buttons.nth(i)
        txt = b.inner_text().strip()
        if txt == "Đăng":
            post_btn = b
            print(f"Tìm thấy nút Đăng tại index {i}: class='{b.get_attribute('class')}'")
            break
            
    if post_btn:
        post_btn.scroll_into_view_if_needed()
        time.sleep(1)
        page.screenshot(path="data/before_click_dang.png")
        print("Đang click nút Đăng...")
        post_btn.click(force=True)
        print("ĐÃ CLICK NÚT ĐĂNG!")
    else:
        print("KHÔNG TÌM THẤY NÚT ĐĂNG!")
        
    # 3. Theo dõi 30 giây tiếp theo, mỗi 3s chụp 1 ảnh
    for s in range(10):
        time.sleep(3)
        page.screenshot(path=f"data/after_click_step_{s}.png")
        cur_url = page.url
        body_text = page.locator("body").inner_text()
        print(f"[{s*3}s] URL: {cur_url}")
        # Kiểm tra các từ khóa xuất hiện
        keywords = ["Đã tải video", "Quản lý bài đăng", "Đang xử lý", "Thành công", "Lỗi", "bản quyền", "xác minh"]
        found = [k for k in keywords if k.lower() in body_text.lower()]
        if found:
            print(f"  Từ khóa phát hiện: {found}")
            
    browser.close()
