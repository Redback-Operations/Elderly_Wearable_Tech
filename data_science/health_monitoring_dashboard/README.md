
# Health Monitoring Dashboard

This project is a **Health Monitoring Dashboard** built using **Dash** and **Plotly**. The dashboard is designed for **elderly individuals** to monitor and visualize their key health metrics such as heart rate, blood oxygen level, body temperature, and hydration levels. It provides easy-to-use, interactive visualizations, comparisons to healthy ranges, and gauges for quick insights.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Structure](#data-structure)
6. [Dashboard Pages](#dashboard-pages)
7. [Future Enhancements](#future-enhancements)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

The **Health Monitoring Dashboard** is a web-based dashboard created using **Dash** and **Plotly** libraries in Python. The dashboard loads data from a CSV file (`HealthData.csv`) that contains health metrics for elderly individuals and visualizes them through interactive graphs, gauge charts, and comparisons to standard healthy ranges. The dashboard is designed to help elderly users easily monitor their health over time.

---

## Features

- **Summary Page**: Displays a summary of key health metrics, including heart rate, blood oxygen levels, body temperature, and more.
- **Time-Series Analysis**: Visualizes how key metrics such as heart rate, oxygen level, and body temperature change over time.
- **Gauge Charts**: Shows easy-to-read gauge charts for heart rate, blood oxygen levels, and hydration levels, with ranges color-coded for easy interpretation.
- **Comparison with Healthy Ranges**: Compares the user’s average health metrics with standard healthy ranges for elderly individuals.
- **HRV Distribution**: A histogram showing Heart Rate Variability (HRV) distribution, helping users understand fluctuations in their heart rate.
- **Room vs. Body Temperature**: Compares room temperature with body temperature over time.
- **Fall Detection Analysis**: Visualizes heart rate behavior during fall incidents.
- **Correlation Heatmap**: Displays correlations between different health metrics to highlight potential relationships.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Redback-Operations/redback-senior-tech
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd health-monitoring-dashboard
   ```

3. **Install Required Dependencies**: You need Python 3.x installed along with the following libraries:
   ```bash
   pip install dash plotly pandas numpy
   ```

4. **Run the Dashboard**: Simply run the Python script or Jupyter Notebook file:
   ```bash
   python health_dashboard.py
   ```
   OR, if you're using a Jupyter Notebook:
   ```bash
   jupyter notebook Health_monitoring_dashboard.ipynb
   ```

---

## Usage

### Upload Health Data:
The dashboard loads a CSV file (`HealthData.csv`) which can be found in the data warehouse and contains the health metrics of elderly individuals. Ensure that your data file is structured as expected before running the dashboard.

### Start the Dashboard:
After running the script or notebook, open your browser and go to the following address to view the dashboard:
   ```bash
   http://127.0.0.1:8052/
   ```

### Explore the Tabs:
- **Summary**: A quick summary of key health metrics.
- **Time-Series Analysis**: Explore time-based changes in heart rate, oxygen levels, and temperature.
- **Gauge Charts**: Visual representations of the user's current health metrics compared to healthy ranges.
- **Comparison with Healthy Ranges**: Compare your health data to ideal standards.
- **HRV Distribution, Fall Detection, Temperature Comparison, and Heatmap**: More detailed visualizations for tracking and analysis.

---

## Data Structure

The CSV file (`HealthData.csv`) should have the following columns:

- `date`: Date of the health data entry.
- `timestamp`: Time of the health data entry.
- `heartrate`: The heart rate of the user.
- `blood_oxygen_level`: Blood oxygen levels (SpO2) of the user.
- `body_temperature`: Body temperature in Celsius.
- `air_quality`: Air quality readings (if available).
- `room_temperature`: Room temperature in Celsius.
- `hydration_levels`: User’s hydration levels.
- `fall_detection`: Indicator of whether a fall was detected (1 for fall, 0 for no fall).

---

## Dashboard Pages

The dashboard includes several pages (tabs) for different types of visualizations:

- **Summary Page**: Displays quick health stats like heart rate, body temperature, and an overall health score.
- **Gauge Charts**: Shows vertical gauges for heart rate, oxygen levels, and hydration levels, with color-coded health zones.
- **Time-Series Analysis**: Provides time-series graphs for key health metrics.
- **HRV Distribution**: Displays heart rate variability (HRV) in a histogram.
- **Fall Detection**: Visualizes heart rate before and after a detected fall.
- **Room vs Body Temperature**: Compares room and body temperatures over time.
- **Correlation Heatmap**: Displays the correlation between various health metrics.
- **Comparison with Healthy Ranges**: Compares user data to standard healthy ranges.

---

## Future Enhancements

Possible future features and improvements:

- **Sleep Tracking**: Incorporate sleep pattern analysis if data is available.
- **Anomaly Detection**: Implement algorithms to flag health anomalies (e.g., abnormal spikes in heart rate).
- **Report Generation**: Allow users to download or email their health report for doctor consultations.
- **Mobile-Friendly Design**: Adapt the dashboard for better usability on mobile devices.

---

## Contributing

Contributions are welcome! Feel free to open a pull request or submit an issue if you have suggestions or improvements. Please follow the standard GitHub workflow for contributing to the project.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
