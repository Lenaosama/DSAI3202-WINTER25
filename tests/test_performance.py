import unittest
import time
from src.performance import measure_execution_time
from src.computation import generate_and_add_numbers

class TestPerformance(unittest.TestCase):
    def test_measure_execution_time(self):
        exec_time = measure_execution_time(generate_and_add_numbers, 100)
        self.assertTrue(exec_time >= 0)

if __name__ == "__main__":
    unittest.main()
