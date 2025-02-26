# src/data_processing.py

from collections import deque
import time
from threading import RLock, Condition

# Global shared data
temperature_averages = {}
temperature_queue = deque(maxlen=10)  # Queue to store the last 10 readings for averaging
lock = RLock()  # Lock to synchronize access to shared data
condition = Condition(lock)

def process_temperatures():
    """Continuously calculate the average temperature from the readings."""
    while True:
        with lock:
            if latest_temperatures:  # If there are any new temperature readings
                for sensor_id, temperature in latest_temperatures.items():
                    # Add the latest temperature to the queue for averaging
                    temperature_queue.append(temperature)
                    average_temp = sum(temperature_queue) / len(temperature_queue)
                    temperature_averages[sensor_id] = average_temp
            condition.notify_all()  # Notify other threads that the averages were updated
        time.sleep(5)  # Update every 5 seconds
