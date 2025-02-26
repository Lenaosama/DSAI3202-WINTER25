# src/display.py

import time
from threading import RLock, Condition

def initialize_display():
    """Initialize the display with the layout."""
    print("Current temperatures:")
    print("Latest Temperatures:")
    for i in range(3):  # Assuming 3 sensors
        print(f"Sensor {i}: --°C")
    for i in range(3):
        print(f"Sensor {i} Average: --°C")
    print("\n")

def update_display():
    """Update the display with the latest temperatures and averages every 5 seconds."""
    while True:
        with lock:
            print("\033[H\033[J")  # Clear the screen (works in most terminals)
            print("Current temperatures:")
            print("Latest Temperatures:")
            for i in range(3):  # Assuming 3 sensors
                print(f"Sensor {i}: {latest_temperatures.get(i, '--')}°C")
            print("\n")
            for i in range(3):
                avg_temp = temperature_averages.get(i, '--')
                print(f"Sensor {i} Average: {avg_temp:.2f}°C")
        time.sleep(5)  # Update every 5 seconds
