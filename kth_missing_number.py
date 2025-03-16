
"""
Given an array of sorted positive integers, nums, and a value k, return the kth missing number in nums.

Ex: Given the following nums and k…

nums = [1, 9, 13, 22], k = 4, return 5 (5 is the 4th missing number).
Ex: Given the following nums and k…

nums = [3, 4, 5], k = 2, return 2.
"""
def find_kth_missing(nums, k):
    # Initialize the current number to check and the count of missing numbers found
    current = 1
    missing_count = 0
    
    # Convert nums to a set for O(1) lookups
    nums_set = set(nums)
    
    while True:
        if current not in nums_set:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

# Example usage:
nums1 = [1, 9, 13, 22]
k1 = 4
print(find_kth_missing(nums1, k1))  # Output: 5