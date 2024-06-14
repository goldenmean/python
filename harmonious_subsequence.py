'''
Given an integer array, nums, return the length of the longest harmonious 
subsequence it contains.
Note: A harmonious subsequence is a subsequence in which the difference 
between the largest value and the smallest value in the subsequence is exactly one.

Ex: Given the following nums...

nums = [1, 1], return 0.
Ex: Given the following nums...

nums = [3, 4, 5], return 2.
Ex: Given the following nums...

nums = [3, 2, 2, 2, 4, 3, 3], return 6.
'''

#Find the length of longest harmonious subsequence
def findLHS(nums):
    # Step 1: Count the frequency of each element
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    print(freq_map)
    
    # Step 2 & 3: Check for harmonious pairs and calculate the length
    max_length = 0
    for num in sorted(freq_map.keys()):
        if num + 1 in freq_map:
            max_length = max(max_length, freq_map[num] + freq_map[num + 1])
    
    return max_length
            
    
   

#nums = [3, 2, 2, 2, 4, 3, 3]    
#nums = [2,4,6]
#nums = [1, 1]
#nums = [3, 4, 5]
nums = [3, 3, 3, 3]

print(findLHS(nums))                
    