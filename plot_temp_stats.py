import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime

# Đọc dữ liệu từ file log và CSV
log_file = "temperature.log"
stats_file = "temp_stats.csv"

# Đọc file log
with open(log_file, "r") as f:
    lines = f.readlines()

timestamps = []
current_temps = []

latest_data = None  # Lưu dữ liệu JSON hợp lệ cuối cùng

for line in lines:
    try:
        data = json.loads(line.strip())
        timestamps.append(datetime.now().strftime('%H:%M:%S'))  # Thời gian hiện tại
        current_temps.append(data["temperature"])  # Nhiệt độ hiện tại
        latest_data = data  # Lưu lại dữ liệu cuối cùng
    except json.JSONDecodeError:
        print(f"Dòng không hợp lệ bị bỏ qua: {line.strip()}")
        continue

# Kiểm tra nếu không có dữ liệu JSON hợp lệ
if latest_data is None:
    print("Không có dữ liệu JSON hợp lệ trong file log.")
    exit()

# Lấy dữ liệu từ JSON cuối cùng
humidity = latest_data["humidity"]
pressure = latest_data["pressure"]
wind_speed = latest_data["wind_speed"]
rain = latest_data["rain"]
clouds = latest_data["clouds"]
description = latest_data["description"].capitalize()

# Đọc dữ liệu từ temp_stats.csv
df_stats = pd.read_csv(stats_file)
min_temp = df_stats["Min Temp (°C)"][0]
max_temp = df_stats["Max Temp (°C)"][0]
avg_temp = df_stats["Avg Temp (°C)"][0]

# Tạo biểu đồ
fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # 2x2 grid

# Biểu đồ nhiệt độ
categories_temp = ["Temp Min", "Temp Max", "Temp Current", "Avg Temp"]
values_temp = [min_temp, max_temp, latest_data["temperature"], avg_temp]
colors_temp = ['#6495ED', '#FF6347', '#90EE90', '#FFA500']

axs[0, 0].bar(categories_temp, values_temp, color=colors_temp)
axs[0, 0].set_title("Thống kê nhiệt độ", fontsize=14)
axs[0, 0].set_ylabel("Nhiệt độ (°C)", fontsize=12)
axs[0, 0].tick_params(axis='x', rotation=30)
for i, v in enumerate(values_temp):
    axs[0, 0].text(i, v + 0.5, f"{v:.1f}°C", ha='center', fontsize=10)

# Biểu đồ thông số môi trường
categories_env = ["Humidity", "Pressure", "Wind Speed", "Rain", "Clouds"]
values_env = [humidity, pressure, wind_speed, rain, clouds]
colors_env = ['#9370DB', '#8B4513', '#4682B4', '#FF69B4', '#708090']

axs[0, 1].bar(categories_env, values_env, color=colors_env)
axs[0, 1].set_title("Thông số môi trường", fontsize=14)
axs[0, 1].set_ylabel("Giá trị", fontsize=12)
axs[0, 1].tick_params(axis='x', rotation=30)
for i, v in enumerate(values_env):
    axs[0, 1].text(i, v + 5, f"{v}", ha='center', fontsize=10)

# Biểu đồ xu hướng nhiệt độ
if len(timestamps) > 1:
    axs[1, 0].plot(timestamps, current_temps, marker='o', linestyle='-', color='#32CD32')
    axs[1, 0].set_title("Xu hướng nhiệt độ qua thời gian", fontsize=14)
    axs[1, 0].set_xlabel("Thời gian", fontsize=12)
    axs[1, 0].set_ylabel("Nhiệt độ (°C)", fontsize=12)
    axs[1, 0].grid(True)
    axs[1, 0].tick_params(axis='x', rotation=30)
else:
    axs[1, 0].text(0.5, 0.5, "Không đủ dữ liệu để hiển thị xu hướng nhiệt độ.", ha='center', fontsize=12)

# Ẩn ô trống cuối cùng
axs[1, 1].axis('off')

# Tinh chỉnh bố cục
plt.tight_layout()
plt.subplots_adjust(top=0.92)
fig.suptitle(f"Thống kê thời tiết - Mô tả: {description}", fontsize=16)

# Hiển thị biểu đồ
plt.show()
