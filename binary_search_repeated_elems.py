'''
Given a sorted array, A, with possibly duplicated elements, find the indices of the first 
and last occurrences of a target element, x. Return -1 if the target is not found.
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]

'''

def find_first_and_last(A, target):
    def binary_search_left(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def binary_search_right(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = binary_search_left(A, target)
    right_index = binary_search_right(A, target)

    if left_index <= right_index:
        return [left_index, right_index]
    else:
        return [-1, -1]

# Example usage
A = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
print(find_first_and_last(A, target))  # Output: [6, 8]

A = [100, 150, 150, 153]
target = 150
#print(find_first_and_last(A, target))  # Output: [1, 2]

A = [1, 2, 3, 4, 5, 6, 10]
target = 9
#print(find_first_and_last(A, target))  # Output: [-1, -1]