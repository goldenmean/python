'''
You are given an array of integers, where each element represents the maximum number of steps
that can be jumped going forward from that element. Write a function to return the minimum 
number of jumps you must take in order to get from the start to the end of the array.
For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal
solution involves jumping from 6 to 5, and then from 5 to 9
'''

def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return float('inf')  # Cannot move anywhere

    # Initialize variables
    max_reach = arr[0]
    step = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps

        # Update max_reach
        max_reach = max(max_reach, i + arr[i])
        print(f"A:i is {i}, Jumps: {jumps}, Max Reach: {max_reach}, Step: {step}")
        # Use a step to get to the current index
        step -= 1

        if step == 0:
            jumps += 1
            print(f"B:Jumps: {jumps}, Max Reach: {max_reach}, Step: {step}")
            if i >= max_reach:
                return float('inf')  # Cannot move further
            step = max_reach - i

    return float('inf')  # If end is not reachable

# Example usage:
arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
print(min_jumps(arr))  # Output: 2


def min_jumps_dp(arr):
    n = len(arr)
    if n <= 1:
        return 0

    # Initialize dp array with maximum possible jumps
    dp = [float('inf')] * n
    dp[0] = 0  # It takes 0 jumps to reach the first element

    for i in range(1, n):
        for j in range(i):
            if i <= j + arr[j]:
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n-1] if dp[n-1] != float('inf') else -1

# Example usage
arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
#print(f"Minimum number of jumps: {min_jumps_dp(arr)}")  # Output: 2