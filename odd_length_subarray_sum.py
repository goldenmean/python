
'''
Given an integer array, nums, return the sum of all subarrays within nums that have an odd 
length.
Ex: Given the following nums…
nums = [1, 2, 3], return 12 ([1], [2], [3], [1, 2, 3] sum to 12).

Ex: Given the following nums…
nums = [3, 1, 5, 2, 4], return 58.
'''


def sum_of_odd_length_subarrays(nums):
    total_sum = 0
    n = len(nums)
    
    # Iterate through the start index of the subarray
    for start in range(n):
        # Iterate through possible end indexes of the subarray
        for end in range(start, n):
            # Check the length of the subarray
            if (end - start + 1) % 2 != 0:
                # Sum the subarray
                total_sum += sum(nums[start:end + 1])
    
    return total_sum


def efficient_sum_of_odd_length_subarrays(nums):
    total_sum = 0
    n = len(nums)
    
    for i in range(n):
        # Number of subarrays that include nums[i]
        total_subarrays = (i + 1) * (n - i)
        
        # Number of odd-length subarrays that include nums[i]
        odd_length_subarrays = (total_subarrays + 1) // 2
        
        # Add the contribution of nums[i] to the total sum
        total_sum += odd_length_subarrays * nums[i]
    
    return total_sum

# Test cases
#print(sum_of_odd_length_subarrays([1, 2, 3]))  # Output: 12
#print(sum_of_odd_length_subarrays([3, 1, 5, 2, 4]))  # Output: 58

print(efficient_sum_of_odd_length_subarrays([1, 2, 3]))  # Output: 12
print(efficient_sum_of_odd_length_subarrays([3, 1, 5, 2, 4]))  # Output: 58
