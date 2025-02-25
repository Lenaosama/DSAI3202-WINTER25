def generate_and_add_numbers(n: int = 1000):
    total = 0
    for i in range(n):
        total += random.randint(0,1000000)
    return total
