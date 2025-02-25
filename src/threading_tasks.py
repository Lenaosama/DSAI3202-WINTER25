import threading
import time
from performance_tasks import generate_and_add_numbers, generate_and_join_letters

def run_threads():
    print("Starting Threaded Execution")
    start_time = time.time()

    thread1 = threading.Thread(target=generate_and_add_numbers, args=(int(1e7),))
    thread2 = threading.Thread(target=generate_and_join_letters, args=(int(1e7),))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Threaded Execution Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    run_threads()
