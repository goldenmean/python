'''
Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.
'''

# Solution by Phind
'''
In this version, dp[i] stores the minimum number of perfect squares needed to sum up to i.
 We iterate through each number from 1 to n, and for each number, we try to subtract every 
 possible perfect square less than or equal to it. We update dp[i] with the minimum value 
 found so far, which is either the current value of dp[i] or dp[i - j * j] + 1 (where j * j is a 
 perfect square less than or equal to i). This way, we build up the solution incrementally, 
 avoiding deep recursion and thus preventing the RecursionError.
'''




def numSquares(n):
    dp = [0] + [float('inf')] * n  # Initialize dp array with infinite values except for 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            print(i,j,dp[i])
            j += 1
            
    return dp[n]

n=27
print(numSquares(n))
