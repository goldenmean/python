'''Leetcode: 2966. Divide Array Into Arrays With Max Difference
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

Example 1:

Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
Example 2:

Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
'''

# My Submitted and working solution - 739msec beats 43% of other solutions in time complexity
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        finalsoln = []
        n=len(nums)
        i=0
        soln=[]
        while i<=(n-3):
            soln=nums[i:i+3]
            maxdiff=soln[2]-soln[0]
            print(f"maxdiff is {maxdiff}")
            if maxdiff <= k:
                finalsoln.append(soln)
            else:
                #pass
                return []
            print(finalsoln)
            i+=3
            print(f"i is {i}")
        return finalsoln
        

#Some other solution with 257msec time of execution
'''
def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
    
        nums.sort()

        # Build them
        res = []
        for i in range(0, len(nums), 3):
            res.append([nums[i], nums[i+1], nums[i+2]])

        # Check them
        for can in res:
            if can[-1] - can[0] > k:
                return []

        return res
'''		
		