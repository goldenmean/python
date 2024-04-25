'''
Given an integer array, nums, return the total number of “partners” in the array.
Note: Two numbers in our array are partners if they reside at different indices and both contain the same value.

Ex: Given the following array nums…

nums = [5, 5, 3, 1, 1, 3, 3], return 5.
5 (index 0) and 5 (index 1) are partners.
1 (index 3) and 1 (index 4) are partners.
3 (index 2) and 3 (index 5) are partners.
3 (index 2) and 3 (index 6) are partners.
3 (index 5) and 3 (index 6) are partners.

'''

def partner(nums):
    currep = 1
    partner_nums=0
    atleastone = 0

    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            currep+=1  
            atleastone = 1         
        else:
            if atleastone != 0:
                partner_nums+=currep
                currep=1

    return  partner_nums

nums = [5, 5, 3, 1, 1, 3, 3]
#nums = [ 5, 7, 0, -3]
print(partner(nums))