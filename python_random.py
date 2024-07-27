

import random

# Generate 5 random numbers between 1 and 50 (no repetition)
random_numbers = set()

while len(random_numbers) < 5:
    random_number = random.randint(1, 59)
    random_numbers.add(random_number)

print(random_numbers)


