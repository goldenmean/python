"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
from typing import List

def all_subsets(nums: List[int]) -> List[List[int]]:
    answer = [ ]

    def backtrack(startidx: int, subset: List[int]):
        #add this subset to answer
        answer.append(subset[:]) 

        #Explore further subsets
        for i in range(startidx, len(nums)):
            #Add current element to the subset
            print(subset)
            subset.append(nums[i])
            #After adding current element, call backtrack recursively on rest of the elements
            backtrack(i+1, subset)
            #Back track: remove current element from subset & continue exploring subsets with further elements
            subset.pop()

    
    backtrack(0,[])
    return answer

# Example 
set1 = [1,2,3]
print(all_subsets(set1))

set2 = [1,2,3,4]
#print(all_subsets(set2))

set3 = [0]
#print(all_subsets(set3))

set4 = [1,[2,3]]
#print(all_subsets(set4))
