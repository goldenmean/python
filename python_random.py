

import random

# Generate 5 random numbers between 1 and 50 (no repetition)
random_numbers = set()

while len(random_numbers) < 5:
    random_number = random.randint(1, 59)
    random_numbers.add(random_number)

print(random_numbers)



## Python code snippet to shift a set of numbers in range 5 to 50 to a new range of 1 to 10 
import random 

float_num = random.uniform(5, 50) 
print(float_num) 


# Python code to shift a a set of numbers in range between 5 and 50 to a different range of 1 to 10 
numbers = list(range(5, 51)) 
mapped_numbers = [((num - 5) / 45) * 9 + 1 for num in numbers] 
print(mapped_numbers) 