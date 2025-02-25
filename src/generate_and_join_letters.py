
def generate_and_join_letters(n: int = 1000):
    letters = ''
    for i in range(n):
        letters += chr(random.randint(33, 126))
        # letters += random.choice(string.ascii_letters + string.digits)
    return letters
