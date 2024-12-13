import requests
import csv
import json

# Lấy dữ liệu từ OpenWeather API
API_KEY = "7a6e76a0bbd37d996eb469a87a4d0303"
city = "Ho Chi Minh"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    # Dữ liệu thời tiết
    temperature = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    rain = data.get("rain", {}).get("1h", 0)  # Lượng mưa trong 1 giờ (nếu có)
    clouds = data["clouds"]["all"]

    print(f"Nhiệt độ hiện tại ở {city}: {temperature}°C")
    print(f"Độ ẩm: {humidity}%, Áp suất: {pressure} hPa, Mô tả: {weather_description}")
    print(f"Tốc độ gió: {wind_speed} m/s, Hướng gió: {wind_deg}°, Lượng mưa: {rain} mm, Mây: {clouds}%")

    # Ghi dữ liệu vào log
    log_entry = {
        "temperature": temperature,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "humidity": humidity,
        "pressure": pressure,
        "description": weather_description,
        "wind_speed": wind_speed,
        "wind_deg": wind_deg,
        "rain": rain,
        "clouds": clouds,
    }

    with open("temperature.log", "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    # Chỉ giữ lại 60 dòng cuối cùng
    with open("temperature.log", "r", encoding="utf-8") as log_file:
        lines = log_file.readlines()[-60:]

    with open("temperature.log", "w", encoding="utf-8") as log_file:
        log_file.writelines(lines)

    # Tính toán thống kê
    temperatures = [
        json.loads(line)["temperature"] for line in lines if line.strip()
    ]
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    avg_temp = sum(temperatures) / len(temperatures)

    # Ghi thống kê vào CSV
    with open("temp_stats.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "Min Temp (°C)",
                "Max Temp (°C)",
                "Avg Temp (°C)",
                "Humidity (%)",
                "Pressure (hPa)",
                "Weather Description",
            ]
        )
        writer.writerow(
            [
                min_temp,
                max_temp,
                avg_temp,
                humidity,
                pressure,
                weather_description,
            ]
        )

    print("Dữ liệu đã được lưu vào temp_stats.csv.")
except requests.exceptions.RequestException as e:
    print(f"Không thể lấy dữ liệu từ OpenWeather: {e}")
except json.JSONDecodeError as e:
    print(f"Lỗi đọc dữ liệu JSON: {e}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")
