import sys, os, time
from pathlib import Path
from playwright.sync_api import sync_playwright

coccoc_exe = r"C:\Program Files\CocCoc\Browser\Application\browser.exe"
coccoc_ud = os.path.expandvars(r"%LocalAppData%\CocCoc\Browser\User Data")

print(f"Exe exists: {os.path.exists(coccoc_exe)}")
print(f"User data exists: {os.path.exists(coccoc_ud)}")

with sync_playwright() as p:
    try:
        print("Attempting launch_persistent_context...")
        browser = p.chromium.launch_persistent_context(
            user_data_dir=coccoc_ud,
            executable_path=coccoc_exe,
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--profile-directory=Default"
            ]
        )
        print("Success! Pages:", len(browser.pages))
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.goto("https://www.google.com", timeout=30000)
        print("Google page title:", page.title())
        browser.close()
    except Exception as e:
        print("Failed to launch:", e)
