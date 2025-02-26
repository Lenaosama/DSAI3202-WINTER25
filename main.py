# main.py

from src.sensor_simulation import start_sensor_threads
from src.data_processing import process_temperatures
from src.display import initialize_display, update_display
import threading
import time

def main():
    # Start the sensor threads to simulate temperature readings
    start_sensor_threads(num_sensors=3)

    # Start the data processing thread
    data_processing_thread = threading.Thread(target=process_temperatures, daemon=True)
    data_processing_thread.start()

    # Initialize the display
    initialize_display()

    # Start the display update thread
    display_thread = threading.Thread(target=update_display, daemon=True)
    display_thread.start()

    # Keep the main thread running to allow daemon threads to operate
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

