@echo off
cd /d "C:\Users\Administrator\Live Climate_Impact_Dashboard"
call C:\Users\Administrator\anaconda3\Scripts\activate.bat base
python fetch_weather.py >> run_log.txt 2>&1