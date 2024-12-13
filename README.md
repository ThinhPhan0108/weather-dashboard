# Weather Dashboard 🌦️

A real-time weather dashboard that fetches and visualizes weather data using the OpenWeather API.

## Features
- Displays current weather data:
  - Temperature (min, max, current, average)
  - Humidity
  - Pressure
  - Wind speed
  - Rainfall
  - Cloud cover
- Interactive bar chart and line chart visualizations.
- Styled using modern design with Bootstrap.

## Screenshots

### Dashboard Overview
![Dashboard Overview](images/dashboard_overview.png)

### Weather Data Visualization
![Weather Visualization](images/weather_visualization.png)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThinhPhan0108/weather-dashboard.git
   cd weather-dashboard
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Linux/Mac
   venv\Scripts\activate          # On Windows
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
5. Open your browser and visit:
   ```arduino
   http://127.0.0.1:5000

### Project Structure
```plaintext
.
├── app.py               # Flask app for dashboard
├── get_temp_from_api.py # Script to fetch data from OpenWeather API
├── plot_temp_stats.py   # Script to create visualizations
├── Temperature_ETL.bat  # ETL pipeline automation script
├── temperature.log      # Log file storing weather data
├── temp_stats.csv       # CSV file storing aggregated statistics
├── requirements.txt     # Dependencies for the project
├── templates/           # HTML templates for Flask
│   └── index.html       # Dashboard HTML
├── static/              # Static files (CSS, images)
│   └── style.css        # Custom styling for the dashboard
└── images/              # Screenshots for README
    ├── dashboard_overview.png
    └── weather_visualization.png
```
### Notes
 - Ensure you have Python 3.6+ installed.
 - Update the get_temp_from_api.py file with your own OpenWeather API key.

### License
This project is licensed under the MIT License.
