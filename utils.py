# utils.py
import random
import string

def generate_random_characters():
    """Generate 1000 random characters and return them as a string."""
    return ''.join(random.choice(string.ascii_letters) for _ in range(1000))

def generate_random_numbers_and_add():
    """Generate 1000 random numbers and return their sum."""
    numbers = [random.randint(0, 100) for _ in range(1000)]
    return sum(numbers)
