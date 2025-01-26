
"""
Given an unsorted integer array nums. Return the smallest positive integer that
is not present in nums. You must implement an algorithm that runs in O(n) time
and uses O(1) auxiliary space e.g. nums = [3,4,-1,1] , output = 2 
nums = [7,8,9,11,12], output = 1
"""

# hash set solution
def firstMissingPositive(nums):
    num_set = set()
    for num in nums:
        if num > 0:
            num_set.add(num)
    
    i = 1
    while True:
        if i not in num_set:
            return i
        i += 1


def firstMissingPositiveCyclicSort(nums):
    n = len(nums)
    # Place each number in its correct position
    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1

nums = [7,11,9,12,8,1]
print(firstMissingPositiveCyclicSort(nums))
