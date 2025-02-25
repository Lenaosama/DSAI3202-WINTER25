import random
import time

def generate_and_add_numbers(n: int = 1000):
    """Generates and sums random numbers."""
    total = 0
    for _ in range(n):
        total += random.randint(0, 1000000)
    return total

def generate_and_join_letters(n: int = 1000):
    """Generates and concatenates random characters."""
    letters = ''
    for _ in range(n):
        letters += chr(random.randint(33, 126))
    return letters

def main():
    print("Starting the Program")
    total_start_time = time.time()
    
    generate_and_add_numbers(int(1e7))
    generate_and_join_letters(int(1e7))
    
    total_end_time = time.time()
    
    print("Exiting the Program")
    sequential_execution_time = total_end_time - total_start_time
    print(f"It took {sequential_execution_time:.2f}s to execute the tasks.")

if __name__ == "__main__":
    main()
