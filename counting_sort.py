# Counting sort - only suitable for sorting +ve integers. Does not work for -ve integers

def counting_sort(nums):
    max_elem = max(nums)

    count = [0] * (max_elem + 1)
    
    for num in nums:
        count[num] += 1
        
    j=0
    for i in range(len(count)):
        while count[i] > 0:
            nums[j] = i
            count[i] -= 1
            j += 1

    print(__file__)
    return nums

# Example 
#nums = [1,17,3,5,7,9,11,13,25,27,29,15,17,19,21,23]   
nums = [4,4,2,2,1]

print(counting_sort(nums))  


    

