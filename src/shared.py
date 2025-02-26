# src/shared.py
from threading import Lock

# Shared data structures and synchronization objects
latest_temperatures = {}  # Dictionary to store the latest temperature readings
temperature_averages = {}  # Dictionary to store the calculated average temperatures
lock = Lock()  # Lock to synchronize access to the shared data
