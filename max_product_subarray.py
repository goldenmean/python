
def maxProductSubarray(nums):
    currmax, currmin = 1,1 
    res = max(nums)

    for n in nums:
        if n == 0:
            currmax, currmin = 1,1
            continue
        tmp=n*currmax
        currmax=max(n,n*currmax,currmin*n)
        currmin=min(n,tmp,n*currmin)
        res = max(res,currmax)
        print(f"n is {n}, currmax is {currmax}, currmin is {currmin}, res is {res}")
    return res


nums = [-1, -2, -3]
#nums=[2,3,-2,4]
print(maxProductSubarray(nums))
