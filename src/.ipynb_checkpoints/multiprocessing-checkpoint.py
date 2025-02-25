import multiprocessing
import time

def worker(process_id):
    print(f"Process {process_id} started")
    # Add your process's code here
    print(f"Process {process_id} finished")

def multiprocessing_sum(n, num_processes=4):
    start_time = time.time()
    processes = []
    
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print("All processes have finished")
    end_time = time.time()
    return 0, end_time - start_time  # Placeholder return