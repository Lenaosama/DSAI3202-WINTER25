# sequential.py
import time
from utils import generate_random_characters, generate_random_numbers_and_add

def time_sequential():
    """Time the sequential execution of the functions."""
    
    # Timing character generation
    start_time = time.time()
    generate_random_characters()
    end_time = time.time()
    print(f"Time for character generation: {end_time - start_time} seconds")

    # Timing number addition
    start_time = time.time()
    generate_random_numbers_and_add()
    end_time = time.time()
    print(f"Time for number addition: {end_time - start_time} seconds")

if __name__ == "__main__":
    time_sequential()
