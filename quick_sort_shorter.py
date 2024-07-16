


def quick_sort_shorter(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]    
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort_shorter(left) + [pivot] + quick_sort_shorter(right)


nums = [2, 1, 4, 9, 3, 8]
print(quick_sort_shorter(nums)) 
