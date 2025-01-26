"""
Given an array of integers, nums, and an integer, k, return the least number of 
unique numbers left in nums after removing k elements.
Note: At least one integer will exist in nums and k will always be between zero 
and nums.length.

Ex: Given the following nums and k…

nums = [1, 4, 3, 3], k = 2, return 1 (remove 1 and 4 and only one unique integer
 is left which is 3).
"""

from collections import Counter

def findLeastUnique(nums, k):
    # Count frequency of each number
    freq = Counter(nums)
    
    # Sort numbers by their frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1])
    
    #initial number of unique numbers is equal to the dictionary keys
    #if we can't remove any number then this should be the answer
    unique_count = len(freq)
    
    # For the case [1,1,1], freq will be {1: 3}
    # unique_count will be 1
    # Since we're removing k=2 elements from a group of same numbers,
    # we still have 1 unique number left
    
    # We only reduce unique_count if we can remove ALL occurrences 
    # of a number within our k limit
    elements_removed = 0
    for num, count in sorted_freq:
        #check if we can remove all occurrences of num within our k limit
        if elements_removed + count <= k:
            # if yes, increase the elements_removed by the count of num
            elements_removed += count
            #decrease unique_count by 1 as we removed all occurrences of num
            unique_count -= 1
        else:
            #if we can't remove all occurrences of num, it means wea reached limit of k
            #so we break out of the loop
            break
            
    return unique_count

print(findLeastUnique([1, 1, 1], 2))  
print(findLeastUnique([1, 4, 3, 3], 2)) 
print(findLeastUnique([1, 1, 2, 2, 3, 3], 3))