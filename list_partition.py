
'''
Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], 
one partition may be [9, 3, 5, 10, 10, 12, 14]
'''


def partition_list_in_place(lst, x):
    low, mid, high = 0, 0, len(lst) - 1
    
    while mid <= high:
        if lst[mid] < x:
            lst[low], lst[mid] = lst[mid], lst[low]
            low += 1
            mid += 1
        elif lst[mid] > x:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1            
        else:
            mid += 1
    print(low,mid,high)
            

# Example usage
x = 10
lst = [9, 12, 3, 5, 14, 10, 10]
partition_list_in_place(lst, x)
print(lst)