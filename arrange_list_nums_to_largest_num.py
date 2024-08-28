'''
Given a list of numbers, create an algorithm that arranges them in order to form
the largest possible integer. For example, given [10, 7, 76, 415], 
you should return 77641510
'''

from functools import cmp_to_key

def compare(x, y):
    # Compare two numbers by their concatenated strings in both possible orders
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def largest_number(numbers):
    # Convert the numbers to strings
    str_numbers = list(map(str, numbers))
    
    # Sort the numbers based on the custom comparison function
    sorted_numbers = sorted(str_numbers, key=cmp_to_key(compare))
    
    # Concatenate the sorted numbers
    largest_num = ''.join(sorted_numbers)
    
    # Convert to integer and back to string to remove leading zeros
    return str(int(largest_num))

numbers = [10, 7, 76, 415]
print(largest_number(numbers))


'''
from functools import cmp_to_key

# List to be sorted
numbers = [5, 2, 4, 3, 1]

# Convert the comparison function to a key function
key_func = cmp_to_key(my_compare)

# Use the key function with sorted()
sorted_numbers = sorted(numbers, key=key_func)

print(sorted_numbers)

'''