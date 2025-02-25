import multiprocessing
import time
from performance_tasks import generate_and_add_numbers, generate_and_join_letters

def run_processes():
    print("Starting Multiprocessing Execution")
    start_time = time.time()

    process1 = multiprocessing.Process(target=generate_and_add_numbers, args=(int(1e7),))
    process2 = multiprocessing.Process(target=generate_and_join_letters, args=(int(1e7),))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Multiprocessing Execution Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    run_processes()
