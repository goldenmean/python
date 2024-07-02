
'''
Given an integer array, nums, return the largest unique value in nums.

Ex: Given the following nums…

nums = [4, 9, 2, 9], return 4.
Ex: Given the following nums…

nums = [8, 1, 10, 1, 4, 8, 4, 10], return -1.
'''

from collections import Counter

def largest_unique_value(nums):
    # Count the occurrences of each number in nums
    num_counts = Counter(nums)
    
    # Initialize the largest unique value to -1 (indicating no unique value found yet)
    largest_unique = -1
    
    # Iterate through the counts
    for num, count in num_counts.items():
        # If the count is 1 (unique) and num is greater than the current largest_unique, update largest_unique
        if count == 1 and num > largest_unique:
            largest_unique = num
            
    return largest_unique

# Example usage
nums1 = [4, 9, 2, 9]
print(largest_unique_value(nums1))  # Output: 4

nums2 = [8, 1, 10, 1, 4, 8, 4, 10]
print(largest_unique_value(nums2))  # Output: -1