"""
Given an array of integers, nums, return the minimum number of operations
needed to make every value in nums unique.
Note: An operation consists of selecting a value in nums and incrementing it by one.

Ex: Given the following nums…

nums = [2, 2, 1, 3], return 2 (increment one of the twos twice or increment
one 2 once and the 3 once).
Ex: Given the following nums…

nums = [4, 1, 2], return 0 (no operations are needed).

"""

def minOperations(nums):
    nums.sort()  # Sort array to make it easier to handle duplicates
    operations = 0
    
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            # If current number is less than or equal to previous
            # We need to increment it to be at least previous + 1
            increment = nums[i-1] - nums[i] + 1
            nums[i] += increment
            operations += increment

    print(nums)            
    return operations

#print(minOperations([2, 1, 3, 2, 2]))
#print(minOperations([2, 2, 1, 3]))  
#print(minOperations([4, 1, 2]))     
#print(minOperations([1, 1, 1]))     
print(minOperations([3, 2, 1, 2, 1, 7]))  
