@echo off
REM Chạy script Python để cập nhật dữ liệu
py get_temp_from_api.py

REM Chạy script Python để vẽ biểu đồ
py plot_temp_stats.py

REM Thông báo hoàn thành
echo ETL process completed and chart displayed successfully!
