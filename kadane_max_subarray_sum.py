
'''
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.
Example:
[34, -50, 42, 14, -5, 86]
Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].
Your solution should run in linear time.
'''
# Kadane's Algorithm

#import time

def max_subarray_sum(arr):    
    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
        print(max_current, max_global)

    return max_global

'''
def wrapper(arr):
    start = time.time_ns()
    result = max_subarray_sum(arr)
    end = time.time_ns()
    timesec = (end - start)/1000.0
    print(f"Time taken: {timesec} microsec")
    return result

# Example usage
arr = [34, -50, 42, 14, -5, 86]

result = wrapper(arr)
print(result)  # Output: 137

'''

# Using timeit module from command prompt to measure the execution time of a simple python function 
# python -m timeit -s "import kadane_max_subarray_sum" "kadane_max_subarray_sum.wrapper([34, -50, 42, 14, -5, 86])"


# Measure execution time using time.perf_counter( )
'''
import time

start_time = time.perf_counter()
# Your code here
end_time = time.perf_counter()

print(f"Execution time: {end_time - start_time} seconds")
'''

'''
Using the line_profiler package:
This tool provides line-by-line profiling. 
First, install it: pip install line_profiler 
Then use it like this:

from line_profiler import LineProfiler

def my_function():
    # Your code here

lp = LineProfiler()
lp_wrapper = lp(my_function)
lp_wrapper()
lp.print_stats()

'''

# Using cProfile
import cProfile

cProfile.run('max_subarray_sum([34, -50, 42, 14, -5, 86])')

# cProfile from command prompt:
# python -m cProfile -s cumtime kadane_max_subarray_sum.py  or 
# python -m cProfile kadane_max_subarray_sum.py


# Using a decorator: You can create a decorator to time functions
'''
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def my_function():
    # Your code here

'''

'''
# Using pytest-benchmark

This is useful if you're using pytest for testing. It provides detailed benchmarking. 
First, install it: pip install pytest-benchmark 
Then create a test file: test_file.py 

def test_my_function(benchmark):
    result = benchmark(my_function)
    # assertions here

    
# then run the test file    
pytest test_file.py --benchmark-compare    

'''