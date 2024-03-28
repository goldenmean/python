'''
Problem:
Given a sorted array of non-zero integers, remove the duplicate elements from the array and return the number of unique elements found.

At the end of your algorithm, the array should contain unique elements. If the number of unique elements is less than the size of the array, fill the remaining indices with 0. For example:

ex. Input - arr[] = {1, 2, 2, 3}
ex. Output - arr[] = {1, 2, 3, 0} - return 3

ex. Input - arr[] = {1, 1, 1, 1}
ex. Output - arr[] = {1, 0, 0, 0} - return 1
'''


def remove_duplicates(arr):
    # Initialize two pointers at the beginning of the array
    i, j = 0, 0

    # Iterate over the array
    while j < len(arr):
        # If the current element is not equal to the next one, move it to the front
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1

    # Fill the remaining indices with 0
    for k in range(i+1, len(arr)):
        arr[k] = 0

    print(arr)
    # Return the number of unique elements
    return i + 1
	

nums=[1, 1, 1, 1]
print(remove_duplicates(nums))