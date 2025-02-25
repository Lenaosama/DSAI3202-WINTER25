from src.sequential import sequential_sum
from src.threading import threading_sum
from src.multiprocessing import multiprocessing_sum


if __name__ == "__main__":
    N = 10**6  # Example large number
    
    seq_result, seq_time = sequential_sum(N)
    print(f"Sequential: Sum = {seq_result}, Time = {seq_time:.4f}s")
    
    thread_result, thread_time = threading_sum(N)
    print(f"Threading: Sum = {thread_result}, Time = {thread_time:.4f}s")
    
    process_result, process_time = multiprocessing_sum(N)
    print(f"Multiprocessing: Sum = {process_result}, Time = {process_time:.4f}s")
