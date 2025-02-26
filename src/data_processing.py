# src/data_processing.py
import time
from threading import Thread
from src.shared import latest_temperatures, temperature_averages, lock  # Import from shared.py

def process_temperatures():
    while True:
        with lock:  # Ensure thread-safe access
            if latest_temperatures:  # If there are any new temperature readings
                for sensor_id, temperature in latest_temperatures.items():
                    # Add the latest temperature to the queue or list (this is just an example)
                    temperature_queue = [temperature]
                    average_temp = sum(temperature_queue) / len(temperature_queue)
                    temperature_averages[sensor_id] = average_temp
        time.sleep(5)  # Update every 5 seconds

def start_data_processing():
    thread = Thread(target=process_temperatures)
    thread.daemon = True
    thread.start()
