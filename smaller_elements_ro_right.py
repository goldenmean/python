'''
Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
'''

def smaller_elements_to_the_right_1(array):
    count = []
    for i in range(len(array)):
        count.append(0)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                count[i] += 1    
    return count   


arr=[3, 4, 9, 6, 1]
arr = [5,4,3,2,1]
print(smaller_elements_to_the_right_1(arr))
