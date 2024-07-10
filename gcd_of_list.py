




def gcd_recursive(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_of_nums(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return gcd(nums[0], gcd_of_nums(nums[1:]))  
    

#nums = [42, 56, 14]
nums = [4, 6, 8, 16]

print(gcd_of_nums(nums))

