'''
Given an integer array, nums, return whether or not you can make
the array strictly non-decreasing by modifying at most one element.
Note: A non-decreasing array is an array in which 
nums[i] <= nums[i + 1] for every i.

Ex: Given the following nums…

nums = [3, 1, 2], return true (you could modify three to one).
Ex: Given the following nums…

nums = [4, 2, 1, 3], return false.
'''


def canBeNonDecreasing(nums):
    modifications = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            modifications += 1
            if modifications > 1:
                return False
            
            # Decide which element to modify
            if i == 1 or nums[i] >= nums[i-2]:
                nums[i-1] = nums[i]  # Modify the previous element
            else:
                nums[i] = nums[i-1]  # Modify the current element
    
    return True

# Test the solution
print(canBeNonDecreasing([3, 1, 2]))  
print(canBeNonDecreasing([4, 2, 1, 3]))
print(canBeNonDecreasing([4, 2, 2, 3]))
print(canBeNonDecreasing([2, 5, 3]))