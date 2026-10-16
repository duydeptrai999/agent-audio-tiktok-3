@echo off
taskkill /F /IM chrome.exe >nul 2>&1
timeout /t 1 >nul
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 "https://www.tiktok.com/creator-center/upload?from=webapp"
echo Chrome started with remote debugging on port 9222!
