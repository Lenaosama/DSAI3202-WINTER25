# src/display.py
import time
from src.shared import latest_temperatures, temperature_averages, lock  # Import from shared.py

def update_display():
    while True:
        with lock:  # Ensure thread-safe access
            print("Current temperatures:")
            print("Latest Temperatures:")
            for sensor_id, temp in latest_temperatures.items():
                print(f"Sensor {sensor_id}: {temp}°C")
            
            print("\nSensor Averages:")
            for sensor_id, avg_temp in temperature_averages.items():
                print(f"Sensor {sensor_id} Average: {avg_temp}°C")
            
        time.sleep(5)  # Refresh display every 5 seconds
