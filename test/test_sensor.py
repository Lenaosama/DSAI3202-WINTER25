# test/test_sensor.py

import unittest
from src.sensor_simulation import simulate_sensor, latest_temperatures
import threading
import time

class TestSensorSimulation(unittest.TestCase):

    def test_sensor_update(self):
        """Test if the sensor updates the temperature correctly."""
        sensor_id = 0
        # Start the sensor simulation in a thread
        thread = threading.Thread(target=simulate_sensor, args=(sensor_id,))
        thread.daemon = True
        thread.start()

        time.sleep(2)  # Allow some time for the sensor to update the temperature
        self.assertIn(sensor_id, latest_temperatures)
        self.assertIsInstance(latest_temperatures[sensor_id], int)
        self.assertGreaterEqual(latest_temperatures[sensor_id], 15)
        self.assertLessEqual(latest_temperatures[sensor_id], 40)

if __name__ == "__main__":
    unittest.main()
