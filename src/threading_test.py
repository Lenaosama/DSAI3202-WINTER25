import threading
from computation import generate_and_add_numbers, generate_and_join_letters
from performance import measure_execution_time

print("Starting the thread program")
total_start_time = time.time()

thread_numbers = threading.Thread(target=generate_and_add_numbers, args=[int(1e7)])
thread_letters = threading.Thread(target=generate_and_join_letters, args=[int(1e7)])

thread_numbers.start()
thread_letters.start()

thread_numbers.join()
thread_letters.join()

total_end_time = time.time()
print("Exiting the thread program")
print(f"It took {total_end_time - total_start_time}s to execute the tasks using threading.")
