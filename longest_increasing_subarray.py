'''
Given an integer array, nums, return the length of the longest increasing subarray.
Note: The subarray must be strictly increasing.

Ex: Given the following nums.

nums = [1, 2, 3], return 3.
Ex: Given the following nums.

nums = [3, 4, 1, 2, 8], return 3.
'''

def longest_increasing_subarray(nums):
    max_length = 0
    l=0

    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            max_length = max(max_length,i-l+1)
        else:
            l=i
    return max_length

nums = [3, 4, 1, 2, 8]
#nums = [1, 2, 3]
print(longest_increasing_subarray(nums))

        