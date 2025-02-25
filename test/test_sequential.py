import time
from src.sequential import sequential_sum

def test_sequential_sum():
    n = 10**6
    start_time = time.time()
    total_sum = sequential_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    assert total_sum == sum(range(1, n + 1)), f"Test failed! Total sum is incorrect."
    print(f"Sequential Test Passed. Sum: {total_sum}, Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    test_sequential_sum()
