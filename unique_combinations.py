'''
Given a list of positive numbers without duplicates and
 a target number, find all unique combinations of the numbers that sum to the target. 
 Note: You may use the same number more than once.

Ex: Given the following numbers and target…

numbers = [2,4,6,3], target = 6,
return [
    [2,2,2],
    [2,4],
    [3,3],
    [6]
]

'''

#def unique_combns(nums,target):

def find_combinations(candidates, target):
    # A list to store the combination
    combinations = []
    # Call the recursive helper function
    find_combinations_recursive(candidates, target, 0, [], combinations)
    return combinations

def find_combinations_recursive(candidates, target, index, current_combination, combinations):
    # Base case: if the target is 0, we have found a combination
    if target == 0:
        combinations.append(list(current_combination))
        return
    # If the target is less than 0, we have overshot and can stop
    if target < 0:
        return
    # Start from the current index and iterate through the candidates
    for i in range(index, len(candidates)):
        # Add the candidate to the current combination
        current_combination.append(candidates[i])
        # Recursively try to find combinations from the rest of the candidates
        find_combinations_recursive(candidates, target - candidates[i], i, current_combination, combinations)
        # Remove the candidate from the current combination
        current_combination.pop()

# Driver code
numbers = [2,4,6,3]
target = 6
print(find_combinations(numbers, target))
    
