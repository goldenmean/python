


def search(nums, target):        
    n=len(nums)
    l=0
    r=n-1

    # Find index of smallest element(minimum) in the sorted rotated array
    while l < r:
        mid = (l+r)//2
        if nums[mid] > nums[r]: 
            # it means array is rotated and minimum element is to right of the mid
            l = mid + 1
        else:
            r = mid
    # After above loop exits l has index of the minimum element
    
    # Find which sorted segment of the rotated array we should search 
    index = l
    l=0
    r=n-1

    if target >= nums[index] and target <= nums[r]: 
        l=index
    else:
        r=index
    # after above logic we have a exact segment of sorted array to perform the binary search in

    # Binary search in the segment decided to find the target 
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1


nums = [4,5,6,7,0,1,2]; target = 9

print(search(nums,target))

    

              

