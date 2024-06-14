
from typing import List 
def longestConsecutiveSequence(nums: List[int]) -> int:
    if not nums: return 0
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        #Check if it is the start of a sequence
        if num-1 not in num_set:
            current_num = num
            current_streak = 1
            # Expand the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            # Update the maximum length
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


#nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutiveSequence(nums))
