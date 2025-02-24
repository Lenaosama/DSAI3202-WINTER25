# threading.py
import threading
import time
from utils import generate_random_characters, generate_random_numbers_and_add

# Threading function for characters
def thread_generate_random_characters():
    generate_random_characters()

# Threading function for numbers
def thread_generate_random_numbers_and_add():
    generate_random_numbers_and_add()

def time_threading():
    """Time the execution using threads."""
    start_time = time.time()

    # Create threads
    t1 = threading.Thread(target=thread_generate_random_characters)
    t2 = threading.Thread(target=thread_generate_random_numbers_and_add)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    end_time = time.time()
    print(f"Time for threading execution: {end_time - start_time} seconds")

def time_advanced_threading():
    """Time the execution using two threads per function."""
    start_time = time.time()

    # Create threads (two per function)
    t1 = threading.Thread(target=thread_generate_random_characters)
    t2 = threading.Thread(target=thread_generate_random_characters)
    t3 = threading.Thread(target=thread_generate_random_numbers_and_add)
    t4 = threading.Thread(target=thread_generate_random_numbers_and_add)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    end_time = time.time()
    print(f"Time for advanced threading execution: {end_time - start_time} seconds")

if __name__ == "__main__":
    time_threading()
    time_advanced_threading()
