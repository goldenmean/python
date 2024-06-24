

'''
Give python code to solve this coding problem: Given a non-empty integer array, nums,
return the minimum number of moves to make all values in nums equal. A move consists of
incrementing all but one element in the array by one. E.g. nums = [1, 2, 3], return 3. 
[1, 2, 3] -> [2, 3, 3] -> [3, 4, 3] -> [4, 4, 4]

Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
'''

def minMoves(nums):
    min_value = min(nums)
    moves = sum(num - min_value for num in nums)
    return moves

# Example usage:
nums = [1, 2, 3]
print(minMoves(nums))  # Output should be 3