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

from collections import Counter

def count_partners(nums):
    # Count the occurrences of each number in the array
    counts = Counter(nums)
    
    # Initialize the total number of partners
    total_partners = 0
    
    # For each unique number in the array
    for count in counts.values():
        # If there is more than one occurrence of the number
        if count > 1:
            # Add the number of partners for this number to the total
            # The number of partners for a number is the number of pairs that can be formed from its occurrences
            # which is given by the formula n*(n-1)/2
            total_partners += count * (count - 1) // 2
    
    # Return the total number of partners
    return total_partners

#nums = [5, 5, 3, 1, 1, 3, 3]
nums = [ 5, 7, 0, -3]
#nums=[1,1,3,4]
#nums=[1,1,1,1]
print(count_partners(nums))