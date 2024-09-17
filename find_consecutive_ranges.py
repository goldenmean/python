'''
Given a sorted list of numbers, return a list of strings that represent all of the 
consecutive numbers.
e.g. 
Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']

'''

def find_consecutive_ranges(nums):
    if not nums:
        return []

    result = []
    start = nums[0]

    for i in range(1, len(nums) + 1):
        # Check if we reached the end or the next number is not consecutive
        if i == len(nums) or nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            if start == end:
                result.append(f"{start}->{start}")
            else:
                result.append(f"{start}->{end}")
            if i < len(nums):
                start = nums[i]

    return result

# Example usage:
nums = [0, 1, 2, 5, 7, 8, 9, 9, 10, 15, 15, 15]
print(find_consecutive_ranges(nums))