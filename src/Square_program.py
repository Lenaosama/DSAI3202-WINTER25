import time
import random
import multiprocessing
import concurrent.futures

# 1. Square function
def square(n):
    return n * n

# 2. Generate list of 10^6 (1 million) random numbers
def generate_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

# 3. Sequential for loop
def sequential_square(numbers):
    results = []
    for num in numbers:
        results.append(square(num))
    return results

# 4. Multiprocessing with a separate process for each number
def process_square(n):
    return square(n)

def multiprocessing_separate_process(numbers):
    # Use a pool with a number of processes equal to the number of available CPUs
    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(process_square, numbers)
    return results

# 5. Multiprocessing Pool with `map()`
def pool_map_square(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    return results

# 6. Multiprocessing Pool with `apply()`
def pool_apply_square(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = [pool.apply(square, args=(num,)) for num in numbers]
    return results

# 7. Using concurrent.futures ProcessPoolExecutor
def executor_square(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(square, numbers))
    return results

# Test function for both 10^6 and 10^7 numbers
def run_tests(numbers):
    print(f"Running test with {len(numbers)} numbers...")

    # Sequential test
    start_time = time.time()
    sequential_square(numbers)
    print(f"Sequential for loop time: {time.time() - start_time:.4f} seconds")

    # Multiprocessing separate process test
    start_time = time.time()
    multiprocessing_separate_process(numbers)
    print(f"Multiprocessing separate process time: {time.time() - start_time:.4f} seconds")

    # Multiprocessing Pool with map()
    start_time = time.time()
    pool_map_square(numbers)
    print(f"Multiprocessing pool map() time: {time.time() - start_time:.4f} seconds")

    # Multiprocessing Pool with apply()
    start_time = time.time()
    pool_apply_square(numbers)
    print(f"Multiprocessing pool apply() time: {time.time() - start_time:.4f} seconds")

    # ProcessPoolExecutor
    start_time = time.time()
    executor_square(numbers)
    print(f"ProcessPoolExecutor time: {time.time() - start_time:.4f} seconds")

if __name__ == "__main__":
    # Generate list of 10^6 numbers
    numbers_1_million = generate_numbers(10**6)

    # Run tests with 10^6 numbers
    run_tests(numbers_1_million)

    # Now test with 10^7 numbers (10 million)
    numbers_10_million = generate_numbers(10**7)

    print("\nRunning tests with 10 million numbers...")
    run_tests(numbers_10_million)
