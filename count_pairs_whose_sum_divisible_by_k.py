
'''
Given an array of integers and a positive integer , determine the number of  pairs
where arr[i] +arr[j]  is divisible by k
'''


def count_divisible_pairs(arr, k):
    # Array to keep the count of remainders
    remainder_count = [0] * k
    
    # Fill the remainder_count array
    for num in arr:
        remainder_count[num % k] += 1
    
    # Initialize count of pairs
    count = 0
    
    # Count pairs with remainder 0
    count += (remainder_count[0] * (remainder_count[0] - 1)) // 2
    print(count, remainder_count)
    
    # Count pairs for other remainders - complementary remainders(i, k-i) - 
    # count += is multiplication of the number of elements with those remainders
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += remainder_count[i] * remainder_count[k - i]
    print(count)
    
    # If k is even, count pairs where both elements are k/2
    if k % 2 == 0:
        count += (remainder_count[k // 2] * (remainder_count[k // 2] - 1)) // 2
    print(count)
    
    return count

# Example usage:
arr = [1, 3, 2, 6, 1, 2]
k = 3
print(count_divisible_pairs(arr, k))  # Output: 5