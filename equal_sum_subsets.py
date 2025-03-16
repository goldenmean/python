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

    #We will check below if we can make a sum of total_sum//2 using some subset of n elements
    #if so, the we can divide the arrray into 2 subsets of same sum total_sum//2
    target_sum = total_sum // 2
    n = len(arr)
    #define a 2D DP array of size [n+1] rows x [target_sum+1] cols
    #so dp[i][j] is True if we can form a sum of j using any subset of i elements  
            # is False if such sum j is not possible to obtain using any subset of i elements 
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # Initialization: there is always a subset with sum 0
    for i in range(n + 1):
        #it is always possible to select subset of i elements such that their sum is zero
        # we can do so by not selecting any of the i elements 
        dp[i][0] = True

    for i in range(1, n + 1): #i can run from 1 to n elements,i.e. we can consider subset of 1 element to n elements
        for j in range(1, target_sum + 1):# j will be from sum 1 to target_sum which is total_sum // 2
            #check if the current element which is i-1 , is less than current target sum j 
            if arr[i - 1] <= j:
                #if the current element is less than or equal to j, then we have 2 choices
                #1. include the current element in the subset i.e. if dp[i-1][j-arr[i-1]] is True which means 
                # we can form the remaining sum j-arr[i-1] using the previous elements of array 
                # if dp[i-1[j-arr[i]] is False then check if we can exclude current element and form the sum
                # j using subset of previous i-1 elements i.e. dp[i-1][j] 
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                #if the current element arr[i-1] is greater than the current target sum j,
                # then dp[i][j] is same as dp[i-1][j] as we cannot include the current element in the subset, 
                # and it will be True if it was possible to form sum j using subset of previous i-1 elements
                dp[i][j] = dp[i - 1][j]

    # return the dp element dp[n][target_sum] which will be True if we can form the sum target_sum using subset of n elements
    return dp[n][target_sum]

# Test the function
print(can_be_divided([5, 9, 7, 21]))  # Output: True
print(can_be_divided([9, 3, 1]))  # Output: False

