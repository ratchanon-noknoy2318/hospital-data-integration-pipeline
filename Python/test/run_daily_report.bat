@echo off
:: 1. สั่งให้ย้ายไปที่โฟลเดอร์ที่ไฟล์ .bat นี้วางอยู่ (ไม่ว่าจะเป็นที่ไหนก็ตาม)
cd /d "%~dp0"

:: 2. รันไฟล์ Python ที่อยู่ในโฟลเดอร์เดียวกัน
python test_line_report_format.py
python test_line_empty_data.py

pause