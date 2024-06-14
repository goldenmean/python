'''
Given a list of elements, find the majority element, which appears more 
than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.
'''

def find_majority_element(lst):
    count = 0
    majority = None
    for elem in lst:
        if count == 0:
            majority = elem
        if elem == majority:
            count += 1
        else:
            count -= 1
        print(majority, count)
    
    print(f"majority after 1st for loop is {majority}")

    count = 0
    for elem in lst:
        if elem == majority:
            count += 1
    if count > len(lst) / 2.0:
        return majority
    else:
        return None

        
'''
#For below code to work it has to have the majority element at Greater than N/2 places in the list of size N

def find_majority_element(nums):
    count = 0
    candidate = None 

    for num in nums: 
        if count == 0: 
            candidate = num 

        if candidate == num: 
            count+=1 
        else: 
            count-=1 

    return candidate 

'''


#lst = [1, 2, 1, 7, 1, 5]
lst = [5, 1, 1, 1, 2, 7]
print(find_majority_element(lst))