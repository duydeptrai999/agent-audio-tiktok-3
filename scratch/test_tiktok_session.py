import sys, os, time
from pathlib import Path
from playwright.sync_api import sync_playwright

coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")
data_dir = Path("data")

with sync_playwright() as p:
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
    page = browser.pages[0] if browser.pages else browser.new_page()
    upload_url = "https://www.tiktok.com/tiktokstudio/upload?from=webapp"
    print("Navigating to TikTok Studio upload page...")
    page.goto(upload_url, timeout=90000)
    time.sleep(5)
    print("Page title:", page.title())
    print("Page URL:", page.url)
    screenshot_path = data_dir / "test_tiktok_session.png"
    page.screenshot(path=str(screenshot_path))
    print(f"Screenshot saved to: {screenshot_path}")
    browser.close()
