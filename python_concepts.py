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