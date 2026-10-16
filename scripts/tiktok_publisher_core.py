# -*- coding: utf-8 -*-
"""
scripts/tiktok_publisher_core.py
Module cốt lõi đăng video TikTok Studio qua Cốc Cốc:
- Tự động hóa 100% không lỗi popup
- Quản lý vòng đời tiến trình Cốc Cốc (browser.exe) với taskkill /F /T và active polling
- Khóa liên tiến trình CoccocFileLock chống xung đột ProcessSingleton
- Dọn dẹp an toàn file SingletonLock / SingletonSocket khi 0 tiến trình browser.exe chạy
- Đảm bảo quyền riêng tư "Mọi người" (Public) trước khi đăng
- Chờ thông minh 30-45s hoàn tất "Kiểm tra nội dung nhanh"
- Xử lý dứt điểm popup xác nhận "Tiếp tục đăng? / Đăng ngay"
- Bọc toàn bộ Playwright trong try...finally: browser.close() chống zombie processes
- Để TikTok tự động hoàn tất redirect tự nhiên (chống hủy request AJAX)
- Chụp ảnh xác minh danh sách bài đăng
"""

import sys
import os
import time
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ==============================================================================
# 1. QUẢN LÝ TIẾN TRÌNH & DỌN DẸP ZOMBIE (CỐC CỐC LIFECYCLE)
# ==============================================================================

def wait_for_process_exit(process_name: str = "browser.exe", timeout: float = 5.0) -> bool:
    """Vòng lặp active polling kiểm tra tasklist xác nhận tiến trình đã thoát hoàn toàn."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            res = subprocess.run(
                ["tasklist", "/FI", f"IMAGENAME eq {process_name}"],
                capture_output=True,
                text=True,
                check=False
            )
            # Nếu tên tiến trình không còn xuất hiện trong stdout -> đã thoát sạch 100%
            if process_name.lower() not in res.stdout.lower():
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False

def kill_and_clean_coccoc(timeout: float = 5.0) -> bool:
    """Tiêu diệt toàn bộ cây tiến trình (process tree) browser.exe bằng /F /T và chờ xác nhận thoát."""
    try:
        subprocess.run(["taskkill", "/F", "/T", "/IM", "browser.exe"], capture_output=True, check=False)
    except Exception:
        pass
    return wait_for_process_exit("browser.exe", timeout=timeout)

def clean_stale_singleton_locks(user_data_dir: Optional[str] = None) -> bool:
    """Dọn dẹp file SingletonLock / SingletonSocket trong thư mục User Data CHỈ KHI có 0 tiến trình browser.exe chạy."""
    if not wait_for_process_exit("browser.exe", timeout=5.0):
        print("  ⚠️ Cảnh báo: browser.exe vẫn đang chạy! Bỏ qua dọn dẹp singleton lock để tránh xung đột.")
        return False

    ud_path = Path(user_data_dir or os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data"))
    if not ud_path.exists():
        return True

    lock_names = ["SingletonLock", "SingletonSocket", "SingletonCookie"]
    for lock_name in lock_names:
        for target in [ud_path / lock_name, ud_path / "Default" / lock_name]:
            if target.exists() or target.is_symlink():
                try:
                    if target.is_dir() and not target.is_symlink():
                        import shutil
                        shutil.rmtree(target, ignore_errors=True)
                    else:
                        target.unlink(missing_ok=True)
                    print(f"  🧹 Đã dọn dẹp file singleton cũ: {target.name}")
                except Exception as e:
                    print(f"  ⚠️ Không thể xóa {target.name}: {e}")
    return True

# ==============================================================================
# 2. KHÓA LIÊN TIẾN TRÌNH (INTER-PROCESS FILELOCK)
# ==============================================================================

class CoccocFileLock:
    """Khóa tệp liên tiến trình điều phối truy cập Cốc Cốc, ngăn chặn ProcessSingleton lock contention."""
    def __init__(self, lock_path: Optional[Path] = None, timeout: float = 900.0, poll_interval: float = 1.0):
        if lock_path is None:
            self.lock_path = Path(__file__).resolve().parent.parent / "data" / ".coccoc_publisher.lock"
        else:
            self.lock_path = Path(lock_path)
        self.timeout = timeout
        self.poll_interval = poll_interval
        self._file_handle = None

    def acquire(self) -> bool:
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            f = None
            try:
                f = open(self.lock_path, "a+b")
                f.seek(0)
                # Đảm bảo file có ít nhất 1 byte để lock
                f.write(b" ")
                f.flush()
                f.seek(0)
                try:
                    import msvcrt
                    msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                except ImportError:
                    try:
                        import fcntl
                        fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    except ImportError:
                        pass
                
                # Chiếm lock thành công, ghi thông tin tiến trình
                f.seek(0)
                f.truncate()
                info = f"PID: {os.getpid()}\nAcquiredAt: {time.time()}\n"
                f.write(info.encode("utf-8"))
                f.flush()
                self._file_handle = f
                return True
            except (BlockingIOError, PermissionError, OSError):
                if f is not None:
                    try:
                        f.close()
                    except Exception:
                        pass
                time.sleep(self.poll_interval)
            except Exception:
                if f is not None:
                    try:
                        f.close()
                    except Exception:
                        pass
                time.sleep(self.poll_interval)
        return False

    def release(self):
        if self._file_handle:
            try:
                self._file_handle.seek(0)
                try:
                    import msvcrt
                    msvcrt.locking(self._file_handle.fileno(), msvcrt.LK_UNLCK, 1)
                except ImportError:
                    try:
                        import fcntl
                        fcntl.flock(self._file_handle.fileno(), fcntl.LOCK_UN)
                    except ImportError:
                        pass
            except Exception:
                pass
            try:
                self._file_handle.close()
            except Exception:
                pass
            self._file_handle = None

    def __enter__(self):
        if not self.acquire():
            raise TimeoutError(f"Không thể chiếm khóa Cốc Cốc publisher tại {self.lock_path} sau {self.timeout}s!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

# ==============================================================================
# 3. GIA CỐ GIAO DIỆN TIKTOK STUDIO & XỬ LÝ POPUP
# ==============================================================================

def dismiss_popups(page):
    """Đóng các popup phiền toái trên TikTok Studio."""
    try:
        btn_bat = page.locator('button:has-text("Bật")').or_(page.locator('button:has-text("Turn on")'))
        if btn_bat.count() > 0 and btn_bat.first.is_visible():
            btn_bat.first.click(force=True)
            time.sleep(0.5)
    except Exception:
        pass

    try:
        btn_hieu = page.locator('button:has-text("Đã hiểu")').or_(page.locator('button:has-text("Got it")'))
        if btn_hieu.count() > 0 and btn_hieu.first.is_visible():
            btn_hieu.first.click(force=True)
            time.sleep(0.5)
    except Exception:
        pass

    try:
        # Nếu có popup "Bạn có chắc bạn muốn thoát?", bấm "Hủy" để ở lại trang
        btn_huy_exit = page.locator('div[role="dialog"] button:has-text("Hủy")').or_(
            page.locator('button:text-is("Hủy")')
        )
        if btn_huy_exit.count() > 0 and btn_huy_exit.first.is_visible():
            btn_huy_exit.first.click(force=True)
            time.sleep(0.5)
    except Exception:
        pass

def ensure_public_privacy(page) -> bool:
    """Pre-publish check: Đảm bảo tùy chọn 'Mọi người' (Public) được kích hoạt và chọn trước khi xuất bản."""
    try:
        # 1. Tìm nhãn / radio "Mọi người" / "Everyone" / "Công khai"
        lbl = (
            page.locator('label:has-text("Mọi người")')
            .or_(page.locator('label:has-text("Công khai")'))
            .or_(page.locator('label:has-text("Everyone")'))
            .or_(page.locator('span:has-text("Mọi người")'))
        )
        if lbl.count() > 0 and lbl.first.is_visible():
            lbl.first.click(force=True)
            print("  🌐 [Privacy] Đã xác nhận chọn chế độ hiển thị 'Mọi người' (Public)!")
            return True

        # 2. Nếu ở dạng dropdown "Người có thể nhìn thấy bài đăng này"
        privacy_dropdown = page.locator('div:has-text("Người có thể xem bài đăng này")').or_(
            page.locator('div:has-text("Người có thể nhìn thấy bài đăng này")')
        )
        if privacy_dropdown.count() > 0 and privacy_dropdown.first.is_visible():
            curr_text = privacy_dropdown.first.inner_text()
            if "Mọi người" not in curr_text and "Everyone" not in curr_text:
                privacy_dropdown.first.click(force=True)
                time.sleep(0.8)
                opt = (
                    page.locator('div[role="option"]:has-text("Mọi người")')
                    .or_(page.locator('li:has-text("Mọi người")'))
                    .or_(page.locator('span:has-text("Mọi người")'))
                )
                if opt.count() > 0 and opt.first.is_visible():
                    opt.first.click(force=True)
                    print("  🌐 [Privacy] Đã chọn 'Mọi người' từ menu dropdown!")
                    return True
        print("  🌐 [Privacy] Quyền riêng tư: Mặc định hoặc đã sẵn sàng chế độ 'Mọi người'.")
        return True
    except Exception as e:
        print(f"  ⚠️ [Privacy Check Warning] {e}")
        return False

def wait_for_content_checks(page, max_wait: int = 40) -> bool:
    """Graceful check wait: Chờ thông minh 30-45s cho 'Kiểm tra nội dung nhanh' hoàn tất trước khi bấm Đăng."""
    print(f"  🔍 [Check] Đang chờ hoàn tất 'Kiểm tra nội dung nhanh' (tối đa {max_wait}s)...")
    start = time.time()
    steps = max(1, max_wait // 2)
    for _ in range(steps):
        time.sleep(2)
        dismiss_popups(page)
        try:
            body_text = page.locator("body").inner_text()
        except Exception:
            body_text = ""

        # Nếu đã hoàn thành hoặc không có vấn đề
        if "Không phát hiện vấn đề nào" in body_text or "No issues detected" in body_text:
            elapsed = int(time.time() - start)
            print(f"  ✅ [Check] Kiểm tra nội dung hoàn tất (Không phát hiện vấn đề nào) sau {elapsed}s!")
            return True

        is_checking = any(k in body_text for k in [
            "Đang kiểm tra", "Đang phân tích", "Kiểm tra bản quyền đang diễn ra", "Checking..."
        ])
        if not is_checking and ("Kiểm tra nội dung nhanh" in body_text or "Kiểm tra bản quyền" in body_text):
            time.sleep(1)
            elapsed = int(time.time() - start)
            print(f"  ✅ [Check] Các mục kiểm tra nội dung đã sẵn sàng sau {elapsed}s!")
            return True

    elapsed = int(time.time() - start)
    print(f"  ⏳ [Check] Đã chờ {elapsed}s, chuyển sang bước bấm Đăng...")
    return False

def handle_post_confirmation_modal(page, max_wait: int = 8) -> bool:
    """Xử lý dứt điểm popup xác nhận 'Tiếp tục đăng? / Đăng ngay' modal dialog."""
    for _ in range(max_wait):
        time.sleep(1)
        try:
            btn_dang_ngay = (
                page.locator('button:has-text("Đăng ngay")')
                .or_(page.locator('button:has-text("Post now")'))
                .or_(page.locator('div[role="dialog"] button:has-text("Đăng ngay")'))
                .or_(page.locator('.modal-content button:has-text("Đăng ngay")'))
            )
            if btn_dang_ngay.count() > 0 and btn_dang_ngay.first.is_visible():
                btn_dang_ngay.first.scroll_into_view_if_needed()
                btn_dang_ngay.first.click(force=True)
                print("  🎉 [Modal] ĐÃ BẤM 'ĐĂNG NGAY' XÁC NHẬN TRÊN POPUP KIỂM DUYỆT!")
                time.sleep(1.5)
                return True
        except Exception:
            pass
    return False

# ==============================================================================
# 4. HÀM XUẤT BẢN VIDEO CHÍNH
# ==============================================================================

def upload_and_publish_video(
    video_path: Path,
    caption: str,
    screenshot_prefix: str = "upload",
    thumbnail_path: Optional[Path] = None,
    wait_content_checks: bool = True
) -> bool:
    """Tải lên và xuất bản 1 video lên TikTok Studio qua Cốc Cốc. Trả về True nếu thành công."""
    if not video_path.exists():
        print(f"❌ File video không tồn tại: {video_path}")
        return False

    size_mb = video_path.stat().st_size / (1024 * 1024)
    print("\n" + "=" * 70)
    print(f"🚀 TIẾN HÀNH ĐĂNG VIDEO: {video_path.name} ({size_mb:.1f} MB)")
    print(f"📝 Caption: {caption[:90]}...")
    print("=" * 70)

    # Sử dụng Inter-process FileLock để tránh xung đột ProcessSingleton giữa các scheduler
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    lock_file = data_dir / ".coccoc_publisher.lock"

    with CoccocFileLock(lock_path=lock_file, timeout=900.0):
        # 1. Dọn dẹp triệt để cây tiến trình browser.exe cũ
        kill_and_clean_coccoc(timeout=5.0)

        # 2. Xóa các file singleton cũ nếu đã chắc chắn 0 browser.exe chạy
        coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")
        clean_stale_singleton_locks(user_data_dir=coccoc_ud)

        coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
        success = False
        browser = None

        try:
            with sync_playwright() as p:
                try:
                    browser = p.chromium.launch_persistent_context(
                        user_data_dir=coccoc_ud,
                        executable_path=coccoc_exe,
                        headless=False,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--start-maximized",
                            "--profile-directory=Default"
                        ],
                        no_viewport=True
                    )

                    page = browser.new_page()
                    upload_url = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
                    print("  🌐 Đang mở trang TikTok Studio Upload...")
                    page.goto(upload_url, timeout=90000)
                    time.sleep(4)

                    # Nếu có thông báo "Video bạn đang chỉnh sửa chưa được lưu. Tiếp tục chỉnh sửa?"
                    try:
                        btn_cancel_draft = page.locator('button:has-text("Hủy bỏ")')
                        if btn_cancel_draft.count() > 0 and btn_cancel_draft.first.is_visible():
                            print("  [Init] Phát hiện bản nháp cũ -> Bấm 'Hủy bỏ' để tải video mới...")
                            btn_cancel_draft.first.click(force=True)
                            time.sleep(2)
                    except Exception:
                        pass

                    # Nạp file video vào input (hỗ trợ cả iframe nếu có)
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
                        print("❌ Không tìm thấy ô tải video!")
                        return False

                    file_input.set_input_files(str(video_path.resolve()))
                    print(f"  [File] Đã nạp file video: {video_path.name}")
                    time.sleep(3)
                    dismiss_popups(page)

                    # Điền Caption & Hashtags
                    selectors = [
                        'div[contenteditable="true"]',
                        'div.notranslate[contenteditable="true"]',
                        'div.public-DraftEditor-content'
                    ]
                    for sel in selectors:
                        try:
                            box = page.locator(sel).first
                            if box.count() > 0 and box.is_visible():
                                box.click(force=True)
                                page.keyboard.press("Control+A")
                                page.keyboard.press("Backspace")
                                time.sleep(0.3)
                                box.fill(caption)
                                print("  [Caption] Đã điền xong Caption & Hashtags!")
                                break
                        except Exception:
                            pass

                    # Đợi upload xong 100%
                    print("  [Upload] Đang theo dõi tiến trình tải lên dữ liệu...")
                    start_time = time.time()
                    for tick in range(180):  # Tối đa 6 phút
                        time.sleep(2)
                        dismiss_popups(page)

                        try:
                            page_text = page.locator("body").inner_text()
                        except Exception:
                            page_text = ""

                        is_uploading = any(m in page_text for m in ["Còn ", " giây", " phút", "MB/", "Đang tải lên"])
                        
                        if tick % 5 == 0:
                            lines = [l.strip() for l in page_text.split("\n") if "MB" in l or "%" in l or "Còn" in l]
                            info = " | ".join(lines[:2]) if lines else "Đang xử lý..."
                            elapsed = int(time.time() - start_time)
                            print(f"    [{elapsed}s] {info}")

                        is_uploaded = ("Đã tải lên" in page_text) or ("100%" in page_text) or ("Uploaded" in page_text)
                        # Khi không còn tiến trình MB/MB mà hiển thị "Đang xử lý..." hoặc "Đang kiểm tra", file đã tải lên máy chủ xong
                        if not is_uploading and any(p in page_text for p in ["Đang xử lý", "Đang kiểm tra", "Thay thế video"]):
                            is_uploaded = True

                        if is_uploaded and tick >= 2:
                            print("  🎯 VIDEO ĐÃ TẢI LÊN XONG 100%! BƯỚC SANG BƯỚC KIỂM TRA & ĐĂNG!")
                            break

                        # Kiểm tra nút Đăng sẵn sàng
                        try:
                            btn_loc = page.locator('button:text-is("Đăng"), button:text-is("Post"), button.btn-post').last
                            if btn_loc.count() > 0 and not btn_loc.is_disabled() and (is_uploaded or not is_uploading):
                                print("  🎯 VIDEO ĐÃ TẢI LÊN XONG 100%! NÚT ĐĂNG ĐÃ SẴN SÀNG!")
                                break
                        except Exception:
                            pass

                    dismiss_popups(page)
                    time.sleep(1)

                    # Pre-publish check: Đảm bảo chế độ Public ("Mọi người") được kích hoạt
                    ensure_public_privacy(page)

                    # Graceful check wait: Chờ thông minh hoàn tất "Kiểm tra nội dung nhanh"
                    if wait_content_checks:
                        wait_for_content_checks(page, max_wait=35)
                        ensure_public_privacy(page)

                    # Click nút Đăng
                    post_btn = None
                    try:
                        # Tìm nút có text chính xác là "Đăng" hoặc "Post" (loại trừ menu "Bài đăng")
                        buttons = page.locator("button")
                        for i in range(buttons.count()):
                            b = buttons.nth(i)
                            try:
                                txt = b.inner_text().strip()
                                if txt in ["Đăng", "Post"]:
                                    print(f"  🎯 Đã phát hiện nút Đăng chuẩn: '{txt}'")
                                    post_btn = b
                                    break
                            except Exception:
                                pass
                    except Exception:
                        pass

                    if not post_btn:
                        try:
                            btn_loc = page.locator('button:text-is("Đăng"), button:text-is("Post"), button.btn-post').last
                            if btn_loc.count() > 0:
                                post_btn = btn_loc
                        except Exception:
                            pass

                    if not post_btn:
                        print("❌ Không tìm thấy nút Đăng!")
                        return False

                    try:
                        try:
                            page.screenshot(path=str(data_dir / "debug_before_post_click.png"))
                        except Exception:
                            pass
                        post_btn.scroll_into_view_if_needed()
                        time.sleep(1)
                        print("  🔘 Đang click nút 'Đăng'...")
                        post_btn.click(force=True)
                        print("  ✅ ĐÃ CLICK NÚT 'ĐĂNG'!")
                        time.sleep(2)
                        try:
                            page.screenshot(path=str(data_dir / "debug_after_post_click.png"))
                        except Exception:
                            pass
                    except Exception as e:
                        print(f"  ❌ Lỗi click nút Đăng: {e}")
                        return False

                    # XỬ LÝ POPUP 'ĐĂNG NGAY' (NẾU CÓ)
                    handle_post_confirmation_modal(page, max_wait=6)

                    # Chờ TikTok tự động điều hướng sang /content tự nhiên
                    print("  ⏳ Đang chờ máy chủ TikTok xử lý và tự động chuyển trang...")
                    for s in range(15):
                        time.sleep(3)
                        dismiss_popups(page)
                        handle_post_confirmation_modal(page, max_wait=2)

                        try:
                            cur_url = page.url
                            if "content" in cur_url:
                                print("  🎉 TikTok đã tự động chuyển sang trang quản lý bài đăng!")
                                success = True
                                break
                            body = page.locator("body").inner_text()
                            if "Quản lý bài đăng" in body or "Đã tải video của bạn lên" in body:
                                print("  🎉 Phát hiện thông báo xuất bản thành công!")
                                success = True
                                btn_m = page.locator('button:has-text("Quản lý bài đăng")')
                                if btn_m.count() > 0 and btn_m.first.is_visible():
                                    btn_m.first.click(force=True)
                                    time.sleep(3)
                                break
                        except Exception:
                            pass

                    time.sleep(3)
                    try:
                        shot_path = data_dir / f"{screenshot_prefix}_verified.png"
                        page.screenshot(path=str(shot_path))
                        print(f"  📸 Đã chụp ảnh xác minh tại: {shot_path.name}")
                    except Exception as e:
                        print(f"  Lỗi chụp ảnh: {e}")

                finally:
                    if browser:
                        try:
                            browser.close()
                        except Exception:
                            pass
                        browser = None
        finally:
            kill_and_clean_coccoc(timeout=3.0)

    return success

if __name__ == "__main__":
    pass
