'''
A numeric array of length N is given. We need to design a function that finds all positive numbers in the array that have their opposites in it as well. Describe approaches for solving optimal worst case and optimal average case performance, respectively.

Hide answer
Let us first design an approach with optimal worst case time.

We need to compare numbers to see if they have their opposites in the array. The trivial solution of comparing all numbers has a consistent time of O(N^2). The great number of comparisons involved should suggest trying to establish a total order operator that allows us to use sorting for solving the problem. If we define a comparison operator that places all instances of a number right after all instances of its opposite, we would have exactly pair of consecutive opposite numbers for each number that has its opposite in the array.

An example of what we want to achieve:

Array: -7 4 -3 2 2 -8 -2 3 3 7 -2 3 -2
Sorted: -2 -2 -2 2 2 -3 3 3 4 -7 7 -8

'''

import functools 

def special_sort(a,b):
    if a!=b and a!=-b:
        return abs(a) < abs(b)
    else:
        return a < b
        

arr=[-7, 4, -3, 2, 2, -8, -2, 3, 3, 7, -2, 3, -2]

print(arr)
arr.sort(key=functools.cmp_to_key(special_sort))
print(arr)

