import time
from src.threading import parallel_sum_threaded

def test_threaded_sum():
    n = 10**6
    num_threads = 4
    start_time = time.time()
    total_sum = parallel_sum_threaded(n, num_threads)
    end_time = time.time()
    execution_time = end_time - start_time
    assert total_sum == sum(range(1, n + 1)), f"Test failed! Total sum is incorrect."
    print(f"Threading Test Passed. Sum: {total_sum}, Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    test_threaded_sum()
