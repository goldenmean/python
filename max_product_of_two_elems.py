def maxProductTwoIndices(nums):
    if len(nums) < 2:
        return 0
    
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2, min1 * min2)

# Example usage:
nums1 = [4, 2, 5, 3]
print(maxProductTwoIndices(nums1))  # Output: 20

nums2 = [6, 2, 4, 3]
print(maxProductTwoIndices(nums2))  # Output: 24

nums3 = [-3, -4, 5, 2]
print(maxProductTwoIndices(nums3))  # Output: 20

nums4 = [-10, -2, 5, 3]
print(maxProductTwoIndices(nums4))  # Output: 20
