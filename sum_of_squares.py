




def sorted_squares(nums):
    l, r = 0, len(nums) - 1
    res = []
    while l <= r:
        if (nums[l]*nums[l]) > (nums[r]*nums[r]):
            res.append(nums[l]*nums[l])
            l += 1
        else:
            res.append(nums[r]*nums[r])
            r -= 1
    
    return res[::-1]




#Example code 
nums = [-9, -2, 0, 2, 3] # [0, 4, 4, 9, 81].

print(sorted_squares(nums))