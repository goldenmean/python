
'''
You are given a dataset represented as an integer array, nums that contains values 
between one and n. Inside the data set, an error has occurred such that one of the
values between one and n has been duplicated to another number between one
and n. Because of this, one of the values between one and n appears twice and one 
value does not appear at all. Return the missing value and the values that appears twice.
Ex: Given the following nums… nums = [1, 3, 2, 5, 5], return [5, 4]. 
Ex: Given the following nums… nums = [1, 2, 3, 3], return [3,4].

'''


def findErrorNums(nums):
    n = len(nums)
    # Calculate the expected sum of the first n natural numbers
    expected_sum = n * (n + 1) // 2
    # Calculate the expected sum of the squares of the first n natural numbers
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    
    # Calculate the actual sum and sum of squares of the numbers in the array
    actual_sum = sum(nums)
    actual_sq_sum = sum(x**2 for x in nums)
    
    # The difference between the expected sum and actual sum
    diff = expected_sum - actual_sum
    if diff == 0:
        return [0,0]
    
    # The difference between the expected and actual sum of squares, divided by diff, gives the sum of the duplicate and missing number
    sum_dup_missing = (expected_sq_sum - actual_sq_sum) // diff
    print(f"diff is {diff} sum_dup_missing is {sum_dup_missing} ")

    # Using the differences, calculate the duplicate and missing numbers
    # Solve the system of equations:
    # missing - dup = diff
    # missing + dup = sum_dup_missing    
    missing = (diff + sum_dup_missing) // 2
    dup = missing - diff

    print(f"dup is {dup} ")
    print(f"missing is {missing} ")

    # Return the duplicate and the missing numbers
    return [dup, missing]

# Test the function
#print(findErrorNums([1, 3, 2, 5, 5]))  # Output: [5, 4]
#print(findErrorNums([1, 2, 3, 3]))  # Output: [3, 4]
print(findErrorNums([2, 3, 4, 5, 5])) 
#print(findErrorNums([1, 2, 3, 4, 5])) 