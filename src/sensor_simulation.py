# src/sensor_simulation.py
import random
import time
from threading import Thread
from src.shared import latest_temperatures, lock  # Import from shared.py

def simulate_sensor(sensor_id):
    while True:
        temperature = random.randint(15, 40)  # Random temperature between 15°C and 40°C
        with lock:  # Ensure thread-safe access to shared data
            latest_temperatures[sensor_id] = temperature
        time.sleep(1)  # Update every second

def start_sensor_threads():
    threads = []
    for i in range(3):  # Assuming 3 sensors for example
        thread = Thread(target=simulate_sensor, args=(i,))
        thread.daemon = True
        thread.start()
        threads.append(thread)
    return threads
