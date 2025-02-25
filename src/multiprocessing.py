import time
import multiprocessing

def process_sum(start, end):
    return sum(range(start, end + 1))

def parallel_sum_multiprocessing(n, num_processes):
    pool = multiprocessing.Pool(processes=num_processes)
    step = n // num_processes
    ranges = [(i * step + 1, (i + 1) * step if i < num_processes - 1 else n) for i in range(num_processes)]
    results = pool.starmap(process_sum, ranges)
    pool.close()
    pool.join()
    return sum(results)

if __name__ == "__main__":
    n = 10**6  # Large number
    num_processes = 4  # Number of processes
    start_time = time.time()
    total_sum = parallel_sum_multiprocessing(n, num_processes)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Sum: {total_sum}")
    print(f"Execution Time with Multiprocessing: {execution_time} seconds")
