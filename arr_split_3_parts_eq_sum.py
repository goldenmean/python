'''
Given an integer array, nums, return whether or not you can split the array into 
three subarrays all of which have an equal sum.
Ex: Given the following nums…
nums = [2, 3, 9, 9, 3, 2, 3, 2, 9], return true.

Ex: Given the following nums…
nums = [1, 2, 3], return false.
'''


def can_split_three_parts(nums):
    total_sum = sum(nums)
    
    # If the total sum is not divisible by 3, it's impossible to split
    if total_sum % 3 != 0:
        return False
    
    target_sum = total_sum // 3
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        if current_sum == target_sum:
            count += 1
            current_sum = 0
        
        # If we've found 2 subarrays, the remaining must be the third
        if count == 2:
            return True
    
    return False

# Test cases
#print(can_split_three_parts([2, 3, 9, 9, 3, 2, 3, 2, 9]))  # Should return True
#print(can_split_three_parts([1, 2, 3]))  # Should return False
print(can_split_three_parts([2, 3, 9, 14, 3, 2, 9]))