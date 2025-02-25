import time
import threading

def thread_sum(start, end, result, index):
    result[index] = sum(range(start, end + 1))

def parallel_sum_threaded(n, num_threads):
    threads = []
    result = [0] * num_threads
    step = n // num_threads
    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step if i < num_threads - 1 else n
        thread = threading.Thread(target=thread_sum, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result)

if __name__ == "__main__":
    n = 10**6  # Large number
    num_threads = 4  # Number of threads
    start_time = time.time()
    total_sum = parallel_sum_threaded(n, num_threads)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Sum: {total_sum}")
    print(f"Execution Time with Threading: {execution_time} seconds")
