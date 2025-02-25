import time

def sequential_sum(n):
    total = sum(range(1, n + 1))
    return total

if __name__ == "__main__":
    n = 10**6  # Large number
    start_time = time.time()
    total_sum = sequential_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Sum: {total_sum}")
    print(f"Execution Time: {execution_time} seconds")
