def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
 
        merge_sort(left_half)
        merge_sort(right_half)
 
        merge(arr, left_half, right_half)
 
def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
 
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
 
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
		


mylist = [ 2, 0, 7, -8, 100 , 54, 23 ]
merge_sort(mylist)		
print(mylist)