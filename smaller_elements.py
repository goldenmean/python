

import bisect

def smaller_than2(nums):
    sorted_nums = sorted(nums)
    result = []
    for num in nums:
        result.append(bisect.bisect_left(sorted_nums, num))
    return result

def smaller_than(nums):
    sorted_nums = sorted(nums)
    result = []
    for num in nums:
        result.append(sorted_nums.index(num))
    return result

num = [4,2,9,10,3]
print(smaller_than(num))