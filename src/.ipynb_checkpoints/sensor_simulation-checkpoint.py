# src/sensor_simulation.py

import random
import time
import threading
from threading import RLock, Condition

# Global shared data
latest_temperatures = {}
lock = RLock()  # Lock to synchronize access to latest_temperatures
condition = Condition(lock)

def simulate_sensor(sensor_id):
    """Simulate temperature readings and update the global dictionary every second."""
    while True:
        temperature = random.randint(15, 40)  # Random temperature between 15°C and 40°C
        with lock:  # Ensure thread-safe access to shared data
            latest_temperatures[sensor_id] = temperature
            condition.notify_all()  # Notify other threads about the updated data
        time.sleep(1)  # Update every second

def start_sensor_threads(num_sensors=3):
    """Start sensor simulation threads."""
    threads = []
    for i in range(num_sensors):
        thread = threading.Thread(target=simulate_sensor, args=(i,), daemon=True)
        threads.append(thread)
        thread.start()
    return threads
