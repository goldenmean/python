'''
Given an array of integers, nums, and a value k, return the number of continuous 
subarrays that sum to k.

Ex: Given the following nums and k…

nums = [1,1,4], k = 5, return 1.
Ex: Given the following nums and k…

nums = [3, 2, 2, 1, 1, 1], k = 5, return 3.
'''

def continuous_sums(nums, k):
    res = 0
    for i in range(len(nums)):
        sum = nums[i]
        j=i+1
        while j < len(nums):
            sum += nums[j]
            if sum == k:
                res += 1
                break
            j += 1

    return res


#nums = [3, 2, 2, 1, 1, 1]; k = 5
nums = [1,1,4]; k = 5

print(continuous_sums(nums, k))
