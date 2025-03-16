
"""
Given a array of numbers, give count of even length subarrays , which have 
odd numbered odd elements. 

e.g. [1,2,3] , output is 2 , [1,2] and [2,3] are two even length subarrays 
which have 1(odd numbered) odd elements , 1 and 3 respectively
"""

"""
We initialize a prefix sum array odd_count to keep track of the cumulative
 count of odd numbers.

We iterate through the array, filling the odd_count array.

We then use two nested loops to generate all possible even length subarrays.

For each subarray, we calculate the number of odd elements by subtracting the 
prefix sums.

If the number of odd elements in the subarray is odd, we increment our count.

Finally, we return the total count.
"""

def count_even_subarrays_odd_elements(arr):
    n = len(arr)
    count = 0
    odd_count = [0] * (n + 1)
    
    for i in range(n):
        odd_count[i + 1] = odd_count[i] + (arr[i] % 2)
    
    for i in range(n):
        for j in range(i + 1, n + 1, 2):
            if (odd_count[j] - odd_count[i]) % 2 == 1:
                count += 1
    
    return count

# Example usage
arr = [1, 2, 3]
result = count_even_subarrays_odd_elements(arr)
print(f"Number of even length subarrays with odd number of odd elements: {result}")