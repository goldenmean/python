"""
Given an array of positive integers, nums, return the largest sum we can create such
that it is divisible by three.

Ex: Given the following nums…

nums = [3, 1, 5, 8, 2], return 18 (3 + 5 + 8 + 2).
Ex: Given the following nums…

nums = [2, 4, 9], return 15.
"""

def max_sum_divisible_by_three(nums):
    total_sum = sum(nums)
    remainder = total_sum % 3

    if remainder == 0:
        return total_sum

    # Collect elements with remainders 1 and 2 when divided by 3
    remainder_one = []
    remainder_two = []

    for num in nums:
        if num % 3 == 1:
            remainder_one.append(num)
        elif num % 3 == 2:
            remainder_two.append(num)

    remainder_one.sort()
    remainder_two.sort()

    if remainder == 1:
        # Remove one smallest from remainder_one or two smallest from remainder_two
        option1 = total_sum - remainder_one[0] if remainder_one else float('-inf')
        option2 = total_sum - sum(remainder_two[:2]) if len(remainder_two) >= 2 else float('-inf')
        return max(option1, option2)

    if remainder == 2:
        # Remove one smallest from remainder_two or two smallest from remainder_one
        option1 = total_sum - remainder_two[0] if remainder_two else float('-inf')
        option2 = total_sum - sum(remainder_one[:2]) if len(remainder_one) >= 2 else float('-inf')
        return max(option1, option2)

# Example usage
nums1 = [3, 1, 5, 8, 2]
print(max_sum_divisible_by_three(nums1))  # Output: 18

nums2 = [2, 4, 9]
print(max_sum_divisible_by_three(nums2))  # Output: 15

nums3 = [3,1,8,5,0] 
print(max_sum_divisible_by_three(nums3)) 