from flask import Flask, jsonify, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Load data from CSV
    stats_file = "temp_stats.csv"
    log_file = "temperature.log"

    try:
        df_stats = pd.read_csv(stats_file)
        with open(log_file, "r") as log:
            lines = log.readlines()

        latest_data = None
        for line in lines:
            try:
                latest_data = json.loads(line.strip())
            except json.JSONDecodeError:
                continue

        if latest_data is None:
            raise ValueError("No valid JSON data found in log file.")

        # Prepare data for rendering
        description = latest_data["description"].capitalize()
        stats_data = {
            "temp_min": df_stats["Min Temp (°C)"].iloc[0],
            "temp_max": df_stats["Max Temp (°C)"].iloc[0],
            "temp_current": latest_data["temperature"],
            "humidity": latest_data["humidity"],
            "pressure": latest_data["pressure"],
            "wind_speed": latest_data["wind_speed"],
            "rain": latest_data["rain"],
            "clouds": latest_data["clouds"]
        }

        return render_template("index.html", description=description, stats_data=stats_data)

    except Exception as e:
        return f"Error loading data: {e}"

if __name__ == "__main__":
    app.run(debug=True)
