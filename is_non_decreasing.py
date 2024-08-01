


def can_be_non_decreasing(nums):
    count = 0  # Count of modifications
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if count == 1:
                return False
            count += 1
            if i < 2:
                # If i < 2, there's no nums[i - 2] to compare with, so we just modify nums[i - 1]
                nums[i - 1] = nums[i]
                print("A",i,nums)
            else:
                # Ensure modifying nums[i - 1] to nums[i] maintains the order
                if nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                    print("B",i,nums)
                else:
                    nums[i] = nums[i - 1]
                    print("C",i,nums)
            
   
    return True

# Example usage:
#print(can_be_non_decreasing([13, 4, 7]))  # Output: True
#print(can_be_non_decreasing([13, 4, 1]))  # Output: False
print(can_be_non_decreasing([4, 4, 3]))
