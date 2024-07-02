
def knapsack(weights, values, i, j):
    if i == 0 or j == 0:
        return 0
    if weights[i-1] > j:
        return knapsack(weights, values, i-1, j)
    else:
        return max(values[i-1] + knapsack(weights, values, i-1, j-weights[i-1]), 
                   knapsack(weights, values, i-1, j))



def knapsack_dp(wt, val, n, capacity):
    dp = [[0 for x in range(capacity+1)] for x in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if wt[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i-1]])
    
    return dp[n][capacity]


# Example usage
weights = [5, 2, 4, 3]
values = [60, 10, 50, 20]
capacity = 4

#Brute force solution
max_value = knapsack(weights, values, len(weights), capacity)
print("Bruteforce Soln: Maximum value:", max_value)

#2D DP solution
max_value = knapsack_dp(weights, values, len(weights), capacity)

print("DP solution Maximum value:", max_value)


