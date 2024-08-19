
'''
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
'''

def find_smallest_missing_positive(arr):
    smallest_missing = 1

    for num in arr:
        if num > smallest_missing:
            break
        smallest_missing += num
    
    return smallest_missing

# Example usage:
#arr = [1, 2, 3, 10] # Output: 7
arr = [1,2,3,5,7,19]
print(find_smallest_missing_positive(arr))  