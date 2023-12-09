def swap_old(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def swap(A, i, j): 
    A[i],A[j] = A[j],A[i]
 
# Partition using the Lomuto partition scheme
def partition(a, start, end):
 
    # Pick the rightmost element as a pivot from the list
    pivot = a[end]
 
    # elements less than the pivot will be pushed to the left of `pIndex`
    # elements more than the pivot will be pushed to the right of `pIndex`
    # equal elements can go either way
    pIndex = start
 
    # each time we find an element less than or equal to the pivot,
    # `pIndex` is incremented, and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1
 
    print("before swapping pindex with pivot")
    for v in a:
        print(v, end=" ")
	
    print("\nafter swapping pindex with pivot")
	
    # swap `pIndex` with pivot
    swap(a, end, pIndex)
    for v in a:
        print(v, end=" ")
 
    # return `pIndex` (index of the pivot element)
    print("\nNew Pivot index is ",pIndex)
    return pIndex
 
 
# Quicksort routine
def quicksort(a, start, end):
    print("Quicksort: start={}, end={}".format(start,end)) 
    # base condition
    if start >= end:
        return
 
    # rearrange elements across pivot
    pivot = partition(a, start, end)
 
    # recur on sublist containing elements less than the pivot
    quicksort(a, start, pivot - 1)
 
    # recur on sublist containing elements more than the pivot
    quicksort(a, pivot + 1, end)


if __name__ == '__main__':
 
    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
 
    quicksort(a, 0, len(a) - 1)
 
    # print the sorted list
    print(a)