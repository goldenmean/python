def customSort(nums1, nums2):
    # Count frequencies of elements in nums1
    freq = {}
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
    
    result = []
    
    # First add elements according to nums2 order
    for num in nums2:
        if num in freq:
            result.extend([num] * freq[num])
            del freq[num]
    
    # Add remaining elements in sorted order
    remaining = []
    for num in freq:
        remaining.extend([num] * freq[num])
    remaining.sort()
    
    return result + remaining


# Example test case
nums1 = [3, 2, 5, 8, 2, 7]; nums2 = [7, 8, 3]
print(customSort(nums1, nums2))