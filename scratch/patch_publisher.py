import sys
from pathlib import Path

p = Path("scripts/tiktok_publisher_core.py")
content = p.read_text(encoding="utf-8")

old = """                    browser = p.chromium.launch_persistent_context(
                        user_data_dir=coccoc_ud,
                        executable_path=coccoc_exe,
                        headless=True,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--profile-directory=Default"
                        ],
                        viewport={"width": 1920, "height": 1080}
                    )"""

new = """                    for launch_attempt in range(1, 4):
                        try:
                            browser = p.chromium.launch_persistent_context(
                                user_data_dir=coccoc_ud,
                                executable_path=coccoc_exe,
                                headless=True,
                                args=[
                                    "--disable-blink-features=AutomationControlled",
                                    "--profile-directory=Default"
                                ],
                                viewport={"width": 1920, "height": 1080}
                            )
                            if browser:
                                break
                        except Exception as launch_err:
                            print(f"  ⚠️ Lỗi khởi động Cốc Cốc (lần {launch_attempt}/3): {launch_err}")
                            kill_and_clean_coccoc(timeout=3.0)
                            clean_stale_singleton_locks(coccoc_ud)
                            time.sleep(2)
                    if not browser:
                        raise RuntimeError("Không thể khởi động trình duyệt Cốc Cốc sau 3 lần thử.")"""

assert old in content, "old block not found in content"
content = content.replace(old, new, 1)
p.write_text(content, encoding="utf-8")
print("SUCCESSFULLY PATCHED TIKTOK_PUBLISHER_CORE")
