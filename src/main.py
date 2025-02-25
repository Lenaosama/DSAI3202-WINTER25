import argparse
import time
import threading
import multiprocessing

from src.computation import generate_and_add_numbers, generate_and_join_letters
from src.performance import measure_execution_time

def run_sequential():
    print("Running in sequential mode...")
    start_time = time.time()
    
    generate_and_add_numbers(int(1e7))
    generate_and_join_letters(int(1e7))

    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time} seconds")

def run_threading():
    print("Running with threading...")
    start_time = time.time()

    thread_numbers = threading.Thread(target=generate_and_add_numbers, args=[int(1e7)])
    thread_letters = threading.Thread(target=generate_and_join_letters, args=[int(1e7)])

    thread_numbers.start()
    thread_letters.start()

    thread_numbers.join()
    thread_letters.join()

    end_time = time.time()
    print(f"Threading execution time: {end_time - start_time} seconds")

def run_multiprocessing():
    print("Running with multiprocessing...")
    start_time = time.time()

    process_numbers = multiprocessing.Process(target=generate_and_add_numbers, args=[int(1e7)])
    process_letters = multiprocessing.Process(target=generate_and_join_letters, args=[int(1e7)])

    process_numbers.start()
    process_letters.start()

    process_numbers.join()
    process_letters.join()

    end_time = time.time()
    print(f"Multiproces
