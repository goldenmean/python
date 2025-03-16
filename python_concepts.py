'''
Python concepts 
'''

#1] LRU cache decorator

from functools import lru_cache
import time


@lru_cache(maxsize=128)
def slow_function(x):
    time.sleep(2)  # Simulates a time-consuming computation
    return x * x

# First call - takes 2 seconds
s1=time.time_ns()
print(slow_function(4))  # Output: 16
e1=time.time_ns() # time.time()

print(f"First call took {e1-s1} nano seconds" )
# Second call with the same argument - returns instantly
s2=time.time_ns()
print(slow_function(4))  # Output: 16
e2=time.time_ns()
print(f"Second call took {e2-s2} nano seconds" )


# 2] Cleaner approach using setdefault for Python dictionaries default values
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = {}
for item in items:
    counts.setdefault(item, 0)
    counts[item] += 1

print(counts)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 3] Walrus operator
#A code example Without walrus operator 
data = input("Enter something: ")
while data != "exit":
    print(f"You entered: {data}")
    data = input("Enter something: ")

#With the Walrus operator:
while (data := input("Enter something: ")) != "exit":
    print(f"You entered: {data}")


import math

if (result := math.sin(3.14)) > 0.5:
    print(result)
    print("Result is greater than 0.5")

# Mutable list side-effect
'''
The function add_to_list has side effects because it uses a mutable default 
argument (lst=[]). In Python, default arguments are evaluated only once when
the function is defined, not each time the function is called. As a result,
the same list is used across multiple calls to the function if the lst argument
is not provided.
'''
def add_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(add_to_list(1))  # [1]
print(add_to_list(2))  #[1,2]

# IF you want to avoid this behavior, you can use None as the default value 
# and create a local variable inside the function which does not persist across calls.
def add_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

# Now each call works with its own list
print(add_to_list(1))  # Output: [1]
print(add_to_list(2))  # Output: [2]


"""
Given a list of subjects with the corresponding number of students who opted
for each subject, design a function where each subject is picked with a
probability proportional to its student count.
"""

import random
def get_random_item(input_array):
  return random.choice(input_array)

#Another way to pick a random element 
import time

input_array = [1,2,3,4,5]
def get_random_item_using_time(input_array):
  timestamp = time.time()
  array_size = len(input_array)
  return input_array[timestamp % array_size]

def get_item(subject_count_map):
  array = []
  for subject, count in subject_count_map:
    array.extend([subject]*count)
    return get_random_item(array) # 