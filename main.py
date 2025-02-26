# main.py
from src.sensor_simulation import start_sensor_threads
from src.data_processing import start_data_processing
from src.display import update_display

# Start sensor threads, data processing threads, and display updates
if __name__ == "__main__":
    start_sensor_threads()  # Start sensor threads
    start_data_processing()  # Start data processing
    update_display()  # Start the display update
