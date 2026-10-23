@echo off
chcp 65001 >nul
title TikTok 24/7 Master Autopilot - 10 Series Daily
cd /d "%~dp0"

echo ======================================================================
echo 🚀 KHỞI ĐỘNG HỆ THỐNG 24/7 TỰ ĐỘNG HÓA 10 BỘ AUDIO MỖI NGÀY
echo ⏰ Lịch 10 slot cố định, 3 slot đêm chuyên trị Kinh Dị / Quái Đàm
echo 🛡️ Giãn cách: 20p/tập, nghỉ tối thiểu 80p giữa 2 bộ
echo ======================================================================

:LOOP
echo [%date% %time%] Đang khởi chạy Daily Master Autopilot...
python scripts\daily_24h_master_autopilot.py

echo ⚠️ Tiến trình tạm dừng hoặc gặp sự cố! Tự động khởi động lại sau 10 giây...
timeout /t 10
goto LOOP
