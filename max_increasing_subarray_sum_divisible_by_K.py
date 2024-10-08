"""
Given a array of elements, find the length of the 
a) Longest increasing contiguous subarray 
and b) whose sum is multiple of K , which is a input argument to the function

Input: arr = [1,2,3,9] ; k = 3
Output: 4
Explanation: [1,2,3,4] is the longest increasing subarray whose sum is multiple of 3

"""

from typing import List

def longestSubarraySumDivisiblebyK(n : int, arr : List[int], k : int) -> int:
    # code here
    
    n = len(arr)
    max_len = 0

    for i in range(n):
        current_sum = 0
        current_len = 0

        for j in range(i, n):
            if j == i or (j > 0 and arr[j] > arr[j - 1]):
                current_sum += arr[j]
                current_len += 1

                if current_sum % k == 0:
                    max_len = max(max_len, current_len)
            else:
                break

    return max_len

#arr = [1,2,3,9] ; k = 3
#arr = [3,2,1]; k = 1
arr = [4]; k = 2
#arr = [7,9,6]; k = 9
print(longestSubarraySumDivisiblebyK(len(arr),arr,k))


## If we want only length of longest increasing subarray(contiguous), use below
def longestSubarray(n: int, arr: List[int], k: int) -> int:
    max_length = 0
    current_length = 1  # Length of the current increasing subarray
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1  # Reset the length for the next subarray
    
    # Check the last subarray
    max_length = max(max_length, current_length)
    
    return max_length