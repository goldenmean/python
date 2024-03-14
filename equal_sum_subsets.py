'''
We're given a set in the form of an array with a unique integers. 
Can you write a function that tells us whether it can be separated into two subsets whose elements have equal sums?
Here's an example: [5, 9, 7, 21]:
The below would return true because newSet can be divided into [5, 9, 7] and [21]. Both subsets sum to 21 and are equal.

Another input example is [9, 3, 1] below returns false since this set cannot be divided into equal subsets.
'''

def can_be_divided(arr):
    total_sum = sum(arr)
    # If the total sum is odd, it cannot be divided into two equal subsets
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(arr)

    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # Initialization: there is always a subset with sum 0
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

# Test the function
print(can_be_divided([5, 9, 7, 21]))  # Output: True
print(can_be_divided([9, 3, 1]))  # Output: False

