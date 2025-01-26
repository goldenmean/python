"""
Write a program that determines the smallest number of perfect squares that sum up to N.
Here are a few examples:
Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1) 
Given N = 18, return 2 (9 + 9) 
N = 15, return4 (9,4,1,1)
N = 9, return 
"""

#Dynamic programming solution

def numSquares(n):
    if n <= 0:
        return 0

    # Initialize the dp array where dp[i] means the least number of perfect square numbers that sum to i.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Loop through each perfect square number less than or equal to i
        j = 1
        while j * j <= i:
            # j*j is perfect square number, dp[i-j*j] is the least number of perfect square numbers that sum to i-j*j, add 1 to it to use the perfect sq. j*j
            #Find minimum of dp[i] and dp[i-j*j]+1 for each j*j less than or equal to i
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            print(f"i: {i}, j: {j}, dp[{i}]: {dp[i]}")
            j += 1
            

    return dp[n]

# Test cases
print(numSquares(8))
#print(numSquares(4))  # Output: 1
#print(numSquares(17)) # Output: 2
#print(numSquares(18)) # Output: 2
#print(numSquares(15)) # Output: 4