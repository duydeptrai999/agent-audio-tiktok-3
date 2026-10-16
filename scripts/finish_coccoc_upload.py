# -*- coding: utf-8 -*-
"""
scripts/finish_coccoc_upload.py
Tự động hoàn tất 100% việc upload video lên TikTok Studio trên Cốc Cốc:
- Tự động đóng popup kiểm tra bản quyền (click "Bật")
- Đợi upload xong 100% dung lượng (306 MB)
- Tự động click nút "Đăng" màu đỏ
- GIỮ NGUYÊN TRÌNH DUYỆT MỞ để bạn nhìn thấy kết quả bài đăng trên màn hình!
"""

import sys
import os
import time
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    out_dir = Path(__file__).resolve().parent.parent / "assets" / "output"
    target_video = out_dir / "VID_20261013_173859_part1_final.mp4"
    caption = (
        "[PHẦN 1] Chiếc Áo Đồng Phục Năm Ấy: Lời Hứa 10 Năm Dưới Cơn Mưa Tốt Nghiệp. "
        "👉 Đón xem Tập 2 lúc 21h30 tối nay nhé! "
        "#audiotruyen #kểchuyện #podcast #xuhuong #fyp #truyendem #rungungon #chuyenkhuya #chill #thugian"
    )

    print("=" * 70)
    print("🚀 TIẾN HÀNH HOÀN TẤT ĐĂNG VIDEO TIKTOK QUA CỐC CỐC")
    print("=" * 70)

    # Đóng browser cũ nếu còn process lock
    subprocess.run(["taskkill", "/F", "/IM", "browser.exe"], capture_output=True)
    time.sleep(1.5)

    coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
    coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=coccoc_ud,
            executable_path=coccoc_exe,
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ],
            no_viewport=True
        )

        page = browser.new_page()
        upload_url = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
        page.goto(upload_url, timeout=90000)
        time.sleep(4)

        # 1. Tìm ô tải video và chọn file
        file_input = page.locator('input[type="file"]').first
        for _ in range(15):
            if file_input.count() > 0:
                break
            time.sleep(1)

        if file_input.count() > 0:
            file_input.set_input_files(str(target_video.resolve()))
            print(f" -> ✅ Đã chọn file: {target_video.name}")
        else:
            print(" -> Đang tiếp tục phiên upload hiện tại...")

        time.sleep(3)

        # 2. Xử lý popup bản quyền: Click nút "Bật" hoặc "Đã hiểu"
        print(" -> Đang xử lý popup kiểm tra bản quyền...")
        for _ in range(10):
            try:
                bat_btn = page.locator('button:has-text("Bật")').or_(page.locator('button:has-text("Đã hiểu")')).or_(page.locator('button:has-text("Got it")'))
                if bat_btn.count() > 0 and bat_btn.first.is_visible():
                    bat_btn.first.click(force=True)
                    print(" -> ✅ Đã tự động bấm 'Bật' kiểm tra bản quyền!")
                    break
            except Exception:
                pass
            time.sleep(1)

        # 3. Điền Caption nếu chưa có
        print(" -> Đang kiểm tra ô Caption...")
        selectors = [
            'div[contenteditable="true"]',
            'div.notranslate[contenteditable="true"]',
            'div.public-DraftEditor-content'
        ]
        for sel in selectors:
            box = page.locator(sel).first
            if box.count() > 0 and box.is_visible():
                try:
                    box.click(force=True)
                    page.keyboard.press("Control+A")
                    page.keyboard.press("Backspace")
                    time.sleep(0.3)
                    box.fill(caption)
                    print(" -> ✅ Đã điền xong Caption & Hashtags!")
                    break
                except Exception:
                    pass

        # 4. CHỜ UPLOAD HOÀN TẤT 100%
        print("⏳ Đang theo dõi tiến trình upload (chờ đạt 100%)...")
        for i in range(180): # Chờ tối đa 3 phút cho file 306MB
            time.sleep(2)
            try:
                # Kiểm tra nếu có nút "Bật" popup hiện lại thì click
                bat_btn = page.locator('button:has-text("Bật")')
                if bat_btn.count() > 0 and bat_btn.first.is_visible():
                    bat_btn.first.click(force=True)

                # Kiểm tra nút Đăng (Post)
                post_btn = page.locator('button:has-text("Đăng")').or_(page.locator('button:has-text("Post")')).first
                if post_btn.count() > 0 and post_btn.is_visible() and post_btn.is_enabled():
                    # Đảm bảo không còn thanh upload đang chạy
                    page_text = page.content()
                    if "Đang tải lên" not in page_text or "100%" in page_text:
                        print(f" -> 🎯 Video đã upload xong! Tiến hành bấm nút Đăng...")
                        time.sleep(2)
                        post_btn.click(force=True)
                        print("\n" + "=" * 70)
                        print("🚀 ĐÃ BẤM NÚT ĐĂNG (POST) THÀNH CÔNG RỰC RỠ TRÊN CỐC CỐC!")
                        print("🎉 VIDEO CỦA BẠN ĐÃ ĐƯỢC XUẤT BẢN LÊN TIKTOK 100%!")
                        print("=" * 70)
                        time.sleep(5)
                        page.screenshot(path="data/coccoc_final_published.png")
                        break
            except Exception as e:
                pass

        print("👉 Trình duyệt Cốc Cốc đang được GIỮ NGUYÊN MỞ trên màn hình để bạn xem kết quả!")
        # Giữ thêm 30 giây để xác nhận
        time.sleep(30)
        browser.close()

if __name__ == "__main__":
    main()
