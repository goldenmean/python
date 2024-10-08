"""
Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum 
of the list using less than 2 * (n - 1) comparisons.
"""


def find_min_max(arr):
    n = len(arr)
    
    # Initialize min and max
    if n % 2 == 0:
        if arr[0] > arr[1]:
            current_max = arr[0]
            current_min = arr[1]
        else:
            current_max = arr[1]
            current_min = arr[0]
        i = 2
    else:
        current_max = current_min = arr[0]
        i = 1

    # Compare in pairs
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            current_max = max(current_max, arr[i])
            current_min = min(current_min, arr[i + 1])
        else:
            current_max = max(current_max, arr[i + 1])
            current_min = min(current_min, arr[i])
        i += 2

    return current_min, current_max
#nums = [3, 5, 1, 2, 4, 8]
#nums = [3, 5, 1, 2, 4, 8]
nums = [ 8 , 7 , 19]
print(find_min_max(nums))