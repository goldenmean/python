from itertools import permutations 

def nextPermutation(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        perms = list(permutations(nums))
        sortedperms=sorted(perms)
        b=tuple(nums)
        idx = len(sortedperms) - 1 - sortedperms[::-1].index(b)
        #idx=sortedperms.index(b)
        if idx < len(perms)-1:
            print(f"A idx is {idx} perms is {perms}")
            nums[:] = list(sortedperms[idx+1])            
        else:
            print(f"A idx is {idx} perms is {perms}")
            nums[:] = list(sortedperms[0])
            
        print(nums)

## Memory efficient solution
from typing import List
def efficientnextPermutation(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        brk = -1
        #Find the index "i" at which the element is smaller than its next element, i is the break index
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                brk = i
                break
        
        print(f"brk is {brk}")
        #If break index is -1 then the array is already sorted in decreasing order, so maximum possible
        # permutation. So in this case sort it in increasing order and return that smallest permutation
        if brk == -1:
            nums.sort()            
            print(f"Early exit {nums}")
            return None
        #Swap the break index with the next larger valued element to make the permutation larger than
        # the current value
        for i in range(n-1, -1, -1):
            if nums[i] > nums[brk]:
                nums[i], nums[brk] = nums[brk], nums[i]
                break
        #Once element at index brk is swapped with a larger valued element at index "i", in above loop
        #sort in increasing order the elements from index brk+1 to n-1 to ensure we get smallest value
        #created from the remaining elements, because swapping of break and "i" would have got a larger digit 
        #at index brk gives us next larger permutation
        if brk+1 != n-1:
            l = nums[brk+1:]
            l.sort()
            nums[brk+1:] = l[:]

        print(nums)

#nums = [1,2,3]
#nums = [3,2,1]
#nums=[1,1,5]
nums =[1,1,6,5,4]
#nextPermutation(nums)

efficientnextPermutation(nums)
