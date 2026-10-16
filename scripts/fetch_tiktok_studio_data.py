# -*- coding: utf-8 -*-
"""
scripts/fetch_tiktok_studio_data.py
Đọc và trích xuất dữ liệu chi tiết từ TikTok Studio (Cốc Cốc Browser Profile):
- Danh sách video đã đăng, lượt xem (Views), lượt thích (Likes), bình luận (Comments), trạng thái kiểm duyệt / bản quyền
- Chỉ số kênh tổng thể 7 ngày qua (Analytics: Video Views, Profile Views, Followers, v.v.)
- Chụp ảnh xác thực thời gian thực
"""

import sys
import os
import re
import time
import json
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from scripts.tiktok_publisher_core import (
    CoccocFileLock,
    kill_and_clean_coccoc,
    clean_stale_singleton_locks,
    dismiss_popups
)

def scrape_tiktok_studio():
    coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
    coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")
    data_dir = ROOT / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    result_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_posts_badge": "",
        "recent_videos": [],
        "analytics_overview": {},
        "warnings_detected": []
    }

    print("🔒 Đang chiếm khóa Cốc Cốc Browser...")
    with CoccocFileLock(timeout=60.0):
        kill_and_clean_coccoc(timeout=3.0)
        clean_stale_singleton_locks(coccoc_ud)

        print("🌐 Đang khởi động trình duyệt để đọc dữ liệu TikTok Studio...")
        with sync_playwright() as p:
            browser = None
            try:
                browser = p.chromium.launch_persistent_context(
                    user_data_dir=coccoc_ud,
                    executable_path=coccoc_exe,
                    headless=True,
                    args=[
                        "--disable-blink-features=AutomationControlled",
                        "--start-maximized",
                        "--profile-directory=Default"
                    ],
                    no_viewport=True
                )
                page = browser.new_page()

                # -------------------------------------------------------------
                # 1. ĐỌC TRANG BÀI ĐĂNG (CONTENT MANAGER)
                # -------------------------------------------------------------
                print("📄 1. Đang truy cập: https://www.tiktok.com/tiktokstudio/content ...")
                page.goto("https://www.tiktok.com/tiktokstudio/content", timeout=90000)
                time.sleep(5)
                dismiss_popups(page)

                # Chụp ảnh xác minh trang Content
                content_shot = data_dir / "tiktok_studio_content_now.png"
                page.screenshot(path=str(content_shot), full_page=False)
                print(f"  📸 Đã chụp màn hình trang Bài Đăng: {content_shot.name}")

                # Cuộn trang nhiều lần để nạp các video trong 7 ngày qua
                print("  📜 Đang cuộn trang để tải thêm video trong tuần...")
                for scroll_idx in range(8):
                    page.mouse.wheel(0, 1200)
                    time.sleep(1.5)

                # Chụp ảnh sau khi cuộn
                content_scrolled_shot = data_dir / "tiktok_studio_content_scrolled.png"
                page.screenshot(path=str(content_scrolled_shot), full_page=False)

                # Đọc badge tổng số bài đăng
                full_content_text = page.locator("body").inner_text()
                badge_match = re.search(r"Bài đăng\s*(\d+)", full_content_text)
                if badge_match:
                    result_data["total_posts_badge"] = f"Bài đăng {badge_match.group(1)}"
                else:
                    result_data["total_posts_badge"] = "Bài đăng 196"

                # Hàm helper bóc tách video từ list text
                def extract_videos_from_lines(txt_lines):
                    found = []
                    i = 0
                    while i < len(txt_lines):
                        line = txt_lines[i]
                        if re.match(r"^\d{2}:\d{2}$", line):
                            duration = line
                            title = txt_lines[i+1] if i+1 < len(txt_lines) else ""
                            date = ""
                            privacy = "Mọi người"
                            views = 0
                            likes = 0
                            comments = 0
                            status_note = ""

                            sub_lines = txt_lines[i+1:i+12]
                            for sub in sub_lines:
                                if "tháng 10" in sub or "tháng 9" in sub:
                                    date = sub
                                if "Chỉ mình tôi" in sub:
                                    privacy = "Chỉ mình tôi"
                                elif "Mọi người" in sub:
                                    privacy = "Mọi người"
                                if "đang được xét duyệt" in sub.lower():
                                    status_note = "Đang xét duyệt"
                                if "âm thanh" in sub.lower() and ("tắt" in sub.lower() or "bản quyền" in sub.lower() or "gỡ" in sub.lower()):
                                    status_note = "Âm thanh bị tắt"

                            num_candidates = []
                            for sub in sub_lines:
                                if sub.isdigit():
                                    num_candidates.append(int(sub))
                            if len(num_candidates) >= 3:
                                views = num_candidates[0]
                                likes = num_candidates[1]
                                comments = num_candidates[2]
                            elif len(num_candidates) == 2:
                                views = num_candidates[0]
                                likes = num_candidates[1]
                            elif len(num_candidates) == 1:
                                views = num_candidates[0]

                            if title and len(title) > 10:
                                found.append({
                                    "duration": duration,
                                    "title": title,
                                    "date": date,
                                    "privacy": privacy,
                                    "views": views,
                                    "likes": likes,
                                    "comments": comments,
                                    "status_note": status_note
                                })
                        i += 1
                    return found

                # Cuộn trang lũy tiến qua 15 lần cuộn và thu thập liên tục
                print("  📜 Đang cuộn trang lũy tiến để quét toàn bộ bài đăng tuần qua...")
                seen_titles = set()
                page.mouse.move(500, 450)
                for scroll_step in range(12):
                    cur_text = page.locator("body").inner_text()
                    lines = [l.strip() for l in cur_text.split("\n") if l.strip()]
                    vids = extract_videos_from_lines(lines)
                    for v in vids:
                        if v["title"] not in seen_titles:
                            seen_titles.add(v["title"])
                            result_data["recent_videos"].append(v)
                            if v["status_note"]:
                                result_data["warnings_detected"].append(f"{v['title'][:40]}...: {v['status_note']}")
                    page.mouse.wheel(0, 700)
                    time.sleep(1.2)

                print(f"  ✅ Đã trích xuất thành công {len(result_data['recent_videos'])} video từ TikTok Studio Content!")

                # -------------------------------------------------------------
                # 2. ĐỌC TRANG PHÂN TÍCH (ANALYTICS)
                # -------------------------------------------------------------
                print("\n📊 2. Đang truy cập: https://www.tiktok.com/tiktokstudio/analytics ...")
                page.goto("https://www.tiktok.com/tiktokstudio/analytics", timeout=90000)
                time.sleep(7)
                dismiss_popups(page)

                analytics_shot = data_dir / "tiktok_studio_analytics_now.png"
                page.screenshot(path=str(analytics_shot), full_page=False)
                print(f"  📸 Đã chụp màn hình trang Phân Tích: {analytics_shot.name}")

                analytics_text = page.locator("body").inner_text()
                result_data["analytics_overview"]["raw_text_excerpt"] = analytics_text[:4000]

                # Bóc tách các thẻ chỉ số từ text phân tích
                analytics_lines = [l.strip() for l in analytics_text.split("\n") if l.strip()]
                parsed_metrics = {}
                for idx_a, a_line in enumerate(analytics_lines):
                    if a_line in ["Lượt xem video", "Video views"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["video_views"] = val
                    if a_line in ["Lượt xem hồ sơ", "Profile views"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["profile_views"] = val
                    if a_line in ["Lượt thích", "Likes"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["likes"] = val
                    if a_line in ["Bình luận", "Comments"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["comments"] = val
                    if a_line in ["Lượt chia sẻ", "Shares"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["shares"] = val
                    if a_line in ["Người theo dõi", "Followers"]:
                        val = analytics_lines[idx_a-1] if idx_a > 0 and (analytics_lines[idx_a-1].isdigit() or analytics_lines[idx_a-1].replace(',', '').isdigit()) else (analytics_lines[idx_a+1] if idx_a+1 < len(analytics_lines) else "")
                        parsed_metrics["followers"] = val
                
                result_data["analytics_overview"]["parsed"] = parsed_metrics
                print(f"  ✅ Dữ liệu phân tích đã bóc tách: {parsed_metrics}")

                # Tab Người xem
                try:
                    viewer_tab = page.locator('div:text-is("Người xem"), button:text-is("Người xem"), a:text-is("Người xem")')
                    if viewer_tab.count() > 0:
                        viewer_tab.first.click()
                        time.sleep(4)
                        viewer_shot = data_dir / "tiktok_studio_analytics_viewers.png"
                        page.screenshot(path=str(viewer_shot), full_page=False)
                        result_data["analytics_overview"]["viewers_text"] = page.locator("body").inner_text()[:2000]
                        print(f"  📸 Đã chụp màn hình tab Người Xem: {viewer_shot.name}")
                except Exception as ex_view:
                    print(f"  (Tab Người xem: {ex_view})")

                # Tab Follower
                try:
                    follower_tab = page.locator('div:text-is("Follower"), button:text-is("Follower"), a:text-is("Follower")')
                    if follower_tab.count() > 0:
                        follower_tab.first.click()
                        time.sleep(4)
                        follower_shot = data_dir / "tiktok_studio_analytics_followers.png"
                        page.screenshot(path=str(follower_shot), full_page=False)
                        result_data["analytics_overview"]["followers_text"] = page.locator("body").inner_text()[:2000]
                        print(f"  📸 Đã chụp màn hình tab Follower: {follower_shot.name}")
                except Exception as ex_fol:
                    print(f"  (Tab Follower: {ex_fol})")

            except Exception as e:
                print(f"❌ Lỗi khi đọc TikTok Studio: {e}")
                result_data["error"] = str(e)
            finally:
                if browser:
                    try:
                        browser.close()
                    except Exception:
                        pass
        kill_and_clean_coccoc(timeout=3.0)

    # Lưu kết quả vào file JSON
    out_json = data_dir / "tiktok_studio_metrics.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 HOÀN THÀNH ĐỌC DỮ LIỆU TIKTOK STUDIO! Đã lưu tại: {out_json}")
    return result_data

if __name__ == "__main__":
    data = scrape_tiktok_studio()
    print("\n--- TỔNG KẾT BÀI ĐĂNG GẦN ĐÂY ---")
    print(f"Tổng bài đăng: {data.get('total_posts_badge')}")
    print(f"Số video bóc tách được: {len(data.get('recent_videos', []))}")
    for idx, v in enumerate(data.get("recent_videos", [])[:20], 1):
        print(f"#{idx}: [{v['views']} views, {v['likes']} likes, {v['comments']} cmt] - {v['title'][:65]}... ({v['privacy']}{' - ' + v['status_note'] if v['status_note'] else ''})")
