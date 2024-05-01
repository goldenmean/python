'''
Dutch national flag sorting algorithm

'''

def dutch_national_flag_sort(arr):
    """
    Sorts an array of 0s, 1s, and 2s using the Dutch National Flag algorithm.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    # Initialize pointers for next positions of 0, 1, and 2
    n=len(arr)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        print(f"arr[mid]: {arr[mid]}")
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        print(f"after iteration: {arr}")
        print(f"low: {low},mid: {mid},high: {high}")

    return arr

# Example usage
#arr = [1, 0, 2, 1, 0, 2, 1, 0, 2]
arr = [1,2,2,0,2,1]
print("Original array:", arr)
sorted_arr = dutch_national_flag_sort(arr)
print("Sorted array:", sorted_arr)