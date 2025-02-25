import time
from src.multiprocessing import parallel_sum_multiprocessing

def test_multiprocessing_sum():
    n = 10**6
    num_processes = 4
    start_time = time.time()
    total_sum = parallel_sum_multiprocessing(n, num_processes)
    end_time = time.time()
    execution_time = end_time - start_time
    assert total_sum == sum(range(1, n + 1)), f"Test failed! Total sum is incorrect."
    print(f"Multiprocessing Test Passed. Sum: {total_sum}, Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    test_multiprocessing_sum()
