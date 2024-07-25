# Find second largest element of a list without sorting it

def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements for a second largest
    
    first_largest = second_largest = float('-inf')
    for num in nums:
        if num > first_largest:
            second_largest, first_largest = first_largest, num
        elif first_largest > num > second_largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return None  # There isn't a second largest element
    return second_largest

# Example usage
nums = [12, 35, 1, 10, 34, 35]
print(find_second_largest(nums))

