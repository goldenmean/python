
"""
You are given a list of N numbers, in which each number is located at most k places away from its sorted position.
For example, if k = 1, a given element at index 4 might end up at indices 3,4, or 5.
Come up with an algorithm that sorts this list in O(N log k) time
"""
# Time complexity : O(N log k)
# Space Complexity : O(k) 
from heapq import heappush, heappop

def sort_k_sorted_array(arr, k):
    n = len(arr)
    # Create a min heap to store first k+1 elements
    heap = []
    result = []
    
    # Add first k+1 elements to the heap , maintain the heap of size k+1 elements
    for i in range(min(k + 1, n)):
        heappush(heap, arr[i])
    
    # Process remaining elements
    for i in range(k + 1, n):
        # Get minimum element from heap and add to result
        result.append(heappop(heap))
        # Add next element to heap
        heappush(heap, arr[i])
    
    # Pop remaining elements from heap
    while heap:
        result.append(heappop(heap))
    
    return result

# Test example 
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
sorted_arr = sort_k_sorted_array(arr, k)
print(f"Original array: {arr}")
print(f"Sorted array: {sorted_arr}")



"""
If the array elements are not guaranteed to be at most k places away from their sorted positions, two key things would change:

The algorithm would still produce a correctly sorted array, but it would lose its performance advantage. The time complexity would degrade to O(n log n) instead of O(n log k), making it no better than standard sorting algorithms like quicksort or mergesort.

The space optimization of using only k+1 elements in the heap would no longer be valid. We would need to store all n elements in the heap at once, increasing the space complexity from O(k) to O(n).
"""
#Time Complexity : O(N log N)
# Space Complexity : O(N)

from heapq import heappush, heappop

def sort_with_heap(arr, k):
    n = len(arr)
    heap = []
    result = []
    
    # With k > actual displacement, we end up using the entire array
    for i in range(n):
        heappush(heap, arr[i])
    
    while heap:
        result.append(heappop(heap))
    
    return result

# Example where elements are far from their sorted positions
arr = [10, 1, 20, 2, 30, 3]
k = 2  # This k is too small for the actual displacements