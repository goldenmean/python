'''
Given an array of integers, nums, sort the array in any manner such that when i is even, 
nums[i] is even and when i is odd, nums[i] is odd.
Note: It is guaranteed that a valid sorting of nums exists.

Ex: Given the following array nums…

nums = [1, 2, 3, 4], one possible way to sort the array is [2,1,4,3]

'''

def arr_shfl(arr):
    l=0
    r=0
    while r < len(arr):
        if r%2 != arr[r]%2:
            if l!=r:
                arr[l],arr[r] = arr[r],arr[l]    
            l=r

        r+=1
    print(arr)

    
    
#arr=[3,4] #=> o/p is 4,3
arr=[1,2,3,4] #=> o/p is 2,3,4,1 
#arr=[2,3,4,1] #=> o/p is 
#arr=[1,3,2,4]
arr_shfl(arr)
        

                        

