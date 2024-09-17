'''
Given an integer array, nums, sort the array in increasing order based on 
frequency of elements. If two numbers appear the same number of times, sort
them by their value in decreasing order.

Ex: Given the following nums…
nums = [1, 1, 2, 3], return [3, 2, 1, 1] (3 appears once and 2 appears once
so 3 comes before 2 because it has a larger value, 1 appears twice so it at the
end of our array).
Ex: Given the following nums…
nums = [5, 2, 4, 4, 9, 2, 2], return [9,5,4,4,2,2,2].
'''

from collections import Counter

def frequency_sort(nums):
    # Count the frequency of each element
    freq = Counter(nums)
    
    # Sort the list based on the frequency and then by value in decreasing order
    #Below sorted key sorts first on the frequency and then on the value if there is a tie 
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))

    #Below sorted key sorts based on the frequency only, in case of tie whatever order they are in the dictionary is used
    #sorted_nums = sorted(nums, key=lambda x: freq[x])
    
    return sorted_nums

print(frequency_sort([1, 1, 2, 3]))  # Output: [3, 2, 1, 1]
print(frequency_sort([5, 2, 4, 4, 9, 2, 2]))  # Output: [9, 5, 4, 4, 2, 2, 2]