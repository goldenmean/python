


def min_number_of_jumps(nums):
    l = r = 0
    res = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        #if window is just one element,
        if l == r:
            return -1
        res += 1
    return res

"""
def min_number_of_jumps(nums):
    res = 0
    n = len(nums)
    end = far = 0
    for i in range(n-1):
        far = max(far, i + nums[i])

        if i == end:
            end = far
            res += 1
    return res
"""

#num=[2,3,1,1,4]
#num=[2,0,1,0,4]
num=[2,3,0,0,2,1,4]
print(min_number_of_jumps(num))