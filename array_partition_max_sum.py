
'''
You are given an integer array, nums, that contains 2N integers. Return the maximum sum you can 
create by pairing integers together and summing the minimum values in each of the pairs.

Ex: Given the following nums…
nums = [1, 3, 2, 4], return 4 (min(1, 2) + min(3, 4) = 4).

Ex: Given the following nums…
nums = [2, 4, 2, 8, 4, 3], return 9.
'''

from typing import List

def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    n=len(nums)
    res = 0
    res = sum(nums[i] for i in range(0,n,2))
    return res

nums1 = [1, 3, 2, 4]
print(arrayPairSum(nums1))  # Output: 4

nums2 = [2, 4, 2, 8, 4, 3]
print(arrayPairSum(nums2))  # Output: 9