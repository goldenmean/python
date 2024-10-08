"""
Write a function, throw_dice(N, faces, total), that determines how many ways it is
possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15
"""


def throw_dice_recursive(N,faces,total):
    def ways_to_total(n, t):
        if n == 0:
            return 1 if t == 0 else 0
        if t > n*faces or t < n:
            return 0

        ways = 0
        for face in range(1, faces+1):
            print(f"n={n}, t={t}, face={face}, ways={ways}")
            ways += ways_to_total(n-1, t-face)

        return ways
    
    return ways_to_total(N, total)


def throw_dice_DP_iterative(N, faces, total):
    # Initialize the DP table
    dp = [[0] * (total + 1) for _ in range(N + 1)]
    
    # Base case: one way to get 0 with 0 dice
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(1, total + 1):
            for face in range(1, min(faces, j) + 1):
                dp[i][j] += dp[i-1][j-face]
    
    return dp[N][total]



N=3; faces=6; total=7
print("Total ways to get this total: ",throw_dice_recursive(N,faces,total))
print("DP solution ways : ",throw_dice_DP_iterative(N,faces,total))


