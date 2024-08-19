'''
Given an array of n positive integers and a positive integer s, find the minimal length of a 
contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

# Sliding window approach used to keep track of the sum of the subarray
def minSubArrayLen(nums, s):
    n=len(nums)
    l=0
    minlen=float('+inf')
    sum = 0
    r=0
    while l<n and r<n:
        sum += nums[r]
        while sum>=s:
            minlen = min(minlen, r-l+1)
            sum -= nums[l]  
            l+=1

        r+=1 
    return 0 if minlen==float('+inf') else minlen


nums = [2,3,1,2,4,3]
s = 7
print(minSubArrayLen(nums, s))
