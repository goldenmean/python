





def find_missing_from_duplicates(nums):
    xorres = 0
    for n in nums:
        xorres ^= n

    return xorres

nums =[1,2,3,2,1]

print(find_missing_from_duplicates(nums))
