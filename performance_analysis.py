# performance_analysis.py

def compute_speedup(sequential_time, parallel_time):
    return sequential_time / parallel_time

def compute_efficiency(speedup, num_processors):
    return speedup / num_processors

def amdahls_law(p, n):
    return 1 / ((1 - p) + (p / n))

def gustafsons_law(p, n):
    return n - ((1 - p) * n)

def analyze_performance(sequential_time, parallel_time, num_processors):
    speedup = compute_speedup(sequential_time, parallel_time)
    efficiency = compute_efficiency(speedup, num_processors)

    print(f"Speedup: {speedup}")
    print(f"Efficiency: {efficiency}")
    print(f"Amdahl's Law Speedup (assuming parallelizable portion = 0.9): {amdahls_law(0.9, num_processors)}")
    print(f"Gustafson's Law Speedup (assuming parallelizable portion = 0.9): {gustafsons_law(0.9, num_processors)}")

if __name__ == "__main__":
    # Example times for sequential and parallel (replace with actual timing results)
    sequential_time = 5.0  # Replace with your actual sequential time
    parallel_time = 2.0    # Replace with your actual parallel time
    num_processors = 4     # Replace with the actual number of threads or processes used

    analyze_performance(sequential_time, parallel_time, num_processors)
