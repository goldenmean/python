'''
You’ve broken into an art gallery and want to maximize the value of the paintings you steal.
 All the paintings you steal you place in your bag which can hold at most W pounds. Given 
 that the weight and value of the ith painting is given by weights[i] and values[i] respectively,
 return the maximum value you can steal.

Ex: Given the following W, weights array and values array…

W = 10, weights = [4, 1, 3], values = [4, 2, 7], return 13.

Ex: Given the following W, weights array and values array…

W = 5, weights = [2, 4, 3], values = [3, 7, 2], return 7.

Ex: Given the following W, weights array and values array…

W = 7, weights = [1, 3, 4], values = [3, 5, 6], return 11.

'''


def max_value(W, weights, values):
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
                print(f"In if dp is {dp[i][w]}")
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                print(f"In elif dp is {dp[i][w]}")
            else:
                dp[i][w] = dp[i - 1][w]
                print(f"In else dp is {dp[i][w]}")
    
    return dp[n][W]

# Test the function with the given examples
#print(max_value(10, [4, 1, 3], [4, 2, 7]))  # Output: 13
#print(max_value(5, [2, 4, 3], [3, 7, 2]))  # Output: 7
#print(max_value(7, [1, 3, 4], [3, 5, 6]))  # Output: 11
print(max_value(5, [1, 3, 5], [3, 5, 6]))  # Output: 8
