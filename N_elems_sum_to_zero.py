"""
Given an integer N, return any array that contains N elements who sum to zero.

Ex: Given the following N...

N = 1, return [0] (1 number that sums to zero is 0 itself).
Ex: Given the following N...

N = 2, return [-1, 1] (this is one possible solution).
"""

def sum_to_zero(N):
    result = []
    if N % 2 == 1:
        result.append(0)
        N -= 1
    for i in range(1, N // 2 + 1):
        result.append(i)
        result.append(-i)
    return result

# Examples
print(sum_to_zero(1))  # Output: [0]
print(sum_to_zero(2))  # Output: [1, -1]
print(sum_to_zero(5))  # Output: [0, 1, -1, 2, -2]