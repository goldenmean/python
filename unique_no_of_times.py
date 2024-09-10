
"""
Given an integer array, nums, return true if all values within nums occur a unique number of
times. Otherwise, return false.
Ex: Given the following nums…
nums = [1, 3, 3, 2, 2, 2], return true (1 appears once, 3 appears twice, two appears 3 times).

Ex: Given the following nums…
nums = [4, 10], return false (both 4 and 10 occur once).
"""



from collections import Counter

def unique_occurrences(nums):
    # Count occurrences of each number
    count_dict = Counter(nums)
    
    # Check if all occurrence counts are unique
    return len(count_dict.values()) == len(set(count_dict.values()))

# Test cases
print(unique_occurrences([1, 3, 3, 2, 2, 2]))  # Should return True
print(unique_occurrences([4, 10]))  # Should return False
print(unique_occurrences([1, 2]))  # Should return False
print(unique_occurrences([1, 2, 2, 3, 3, 3]))  # Should return True