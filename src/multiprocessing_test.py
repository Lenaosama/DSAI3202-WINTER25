import multiprocessing
from computation import generate_and_add_numbers, generate_and_join_letters
from performance import measure_execution_time

print("Starting the multiprocessing program")
total_start_time = time.time()

process_numbers = multiprocessing.Process(target=generate_and_add_numbers, args=[int(1e7)])
process_letters = multiprocessing.Process(target=generate_and_join_letters, args=[int(1e7)])

process_numbers.start()
process_letters.start()

process_numbers.join()
process_letters.join()

total_end_time = time.time()
print("Exiting the multiprocessing program")
print(f"It took {total_end_time - total_start_time}s to execute the tasks using multiprocessing.")
