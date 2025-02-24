# multiprocessing.py
import time
from multiprocessing import Process
from utils import generate_random_characters, generate_random_numbers_and_add

# Process function for characters
def process_generate_random_characters():
    generate_random_characters()

# Process function for numbers
def process_generate_random_numbers_and_add():
    generate_random_numbers_and_add()

def time_processes():
    """Time the execution using processes."""
    start_time = time.time()

    # Create processes
    p1 = Process(target=process_generate_random_characters)
    p2 = Process(target=process_generate_random_numbers_and_add)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Time for process execution: {end_time - start_time} seconds")

def time_advanced_processes():
    """Time the execution using two processes per function."""
    start_time = time.time()

    # Create processes (two per function)
    p1 = Process(target=process_generate_random_characters)
    p2 = Process(target=process_generate_random_characters)
    p3 = Process(target=process_generate_random_numbers_and_add)
    p4 = Process(target=process_generate_random_numbers_and_add)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_time = time.time()
    print(f"Time for advanced process execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    time_processes()
    time_advanced_processes()
