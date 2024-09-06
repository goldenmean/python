'''
Given an array of elements, return the length of the longest subarray where all its elements are unique.
For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of
 unique elements is [5, 2, 3, 4, 1]
'''

def longest_subarray_of_unique_elements(arr):
    # This set will store the unique elements in the current window
    elements_set = set()
    # Initialize the left pointer of the window
    left = 0
    # This will keep track of the maximum length of the subarray of unique elements
    max_length = 0
    
    for right in range(len(arr)):        
        # Slide the window right, ensuring all elements are unique        
        while arr[right] in elements_set:
            print(f"right={right}, arr[right]={arr[right]}")
            # If the right element is already in the set, remove the left element from the set
            # and move the left pointer one step to the right
            elements_set.remove(arr[left])
            left += 1
            print(f"B: left={left}, elements_set={elements_set}")
        
        # Add the current element to the set
        elements_set.add(arr[right])
        # Update the max_length if the current window is larger
        print(f"A: right={right}, left={left}, arr[right]={arr[right]}, elements_set={elements_set}")
        max_length = max(max_length, right - left + 1)
        print(f"max_length={max_length}")
    
    return max_length

# Example usage
#arr = [5, 1, 3, 5, 2, 3, 4]
#arr = [1, 5, 3, 5, 2, 3, 4, 1]
arr = [1, 5, 3, 5, 2]
print(longest_subarray_of_unique_elements(arr))