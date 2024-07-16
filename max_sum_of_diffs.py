




## O(N^2) solution
def maxDistance(A):
    """
    Finds the maximum sum of the absolute difference between numbers and their positions in the list.
    
    Parameters:
        A (List[int]): The list of numbers.
        
    Returns:
        int: The maximum sum of the absolute difference between numbers and their positions.
    """
    max_sum = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            current_sum = abs(A[i] - A[j]) + abs(i - j)
            max_sum = max(max_sum, current_sum)
    return max_sum


## O(N) solution
def maxDistanceEfficient(A):
    """
    Efficiently finds the maximum sum of the absolute difference between numbers and their positions.
    
    Parameters:
        A (List[int]): The list of numbers.
        
    Returns:
        int: The maximum sum of the absolute difference between numbers and their positions.
    """
    max_plus = max_minus = min_plus = min_minus = None
    
    for i, a in enumerate(A):
        if max_plus is None or a + i > max_plus:
            max_plus = a + i
        if min_plus is None or a + i < min_plus:
            min_plus = a + i
        if max_minus is None or a - i > max_minus:
            max_minus = a - i
        if min_minus is None or a - i < min_minus:
            min_minus = a - i
            
    return max(max_plus - min_plus, max_minus - min_minus)

nums = [5,9,2,8]
print(maxDistance(nums))
print(maxDistanceEfficient(nums))

