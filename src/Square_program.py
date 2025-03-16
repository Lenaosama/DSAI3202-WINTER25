import time
from multiprocessing import Process, Manager, Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor

# Function to calculate the square of a number
def square(n):
    return n * n

# Function to generate a list of numbers
def generate_numbers(size):
    return list(range(1, size + 1))

# Sequential execution
def sequential_execution(numbers):
    start_time = time.time()
    squares = [square(n) for n in numbers]
    end_time = time.time()
    print(f"Sequential Execution Time: {end_time - start_time:.4f} seconds")

# Multiprocessing: Fixed number of processes
def multiprocessing_individual(numbers):
    start_time = time.time()
    manager = Manager()
    results = manager.list()
    processes = []

    # Use a fixed number of processes (number of CPU cores)
    num_processes = cpu_count()
    chunk_size = len(numbers) // num_processes

    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_processes - 1 else len(numbers)
        p = Process(target=lambda x: results.extend([square(n) for n in x]), args=(numbers[start:end],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()
    print(f"Multiprocessing (Fixed Processes) Execution Time: {end_time - start_time:.4f} seconds")

# Multiprocessing using Pool (map and apply)
def multiprocessing_pool(numbers):
    # Using map (synchronous)
    start_time = time.time()
    with Pool() as pool:
        squares = pool.map(square, numbers)
    end_time = time.time()
    print(f"Multiprocessing (Pool - map) Execution Time: {end_time - start_time:.4f} seconds")

    # Using apply_async (asynchronous)
    start_time = time.time()
    with Pool() as pool:
        results = [pool.apply_async(square, (n,)) for n in numbers]
        squares = [result.get() for result in results]
    end_time = time.time()
    print(f"Multiprocessing (Pool - apply_async) Execution Time: {end_time - start_time:.4f} seconds")

# Multiprocessing using ProcessPoolExecutor
def multiprocessing_futures(numbers):
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        squares = list(executor.map(square, numbers))
    end_time = time.time()
    print(f"Multiprocessing (ProcessPoolExecutor) Execution Time: {end_time - start_time:.4f} seconds")

# Main script
if __name__ == "__main__":
    # Test with 1 million numbers
    print("Testing with 1 million numbers")
    numbers_1m = generate_numbers(1_000_000)
    sequential_execution(numbers_1m)
    multiprocessing_individual(numbers_1m)
    multiprocessing_pool(numbers_1m)
    multiprocessing_futures(numbers_1m)

    # Test with 10 million numbers
    print("\nTesting with 10 million numbers")
    numbers_10m = generate_numbers(10_000_000)
    sequential_execution(numbers_10m)
    multiprocessing_individual(numbers_10m)
    multiprocessing_pool(numbers_10m)
    multiprocessing_futures(numbers_10m)
