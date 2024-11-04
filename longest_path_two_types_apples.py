"""
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.
For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""

def longest_two_types_path(apples):
    # Dictionary to store the count of each type of apple in the current window
    apple_count = {}
    left = 0
    max_length = 0

    for right in range(len(apples)):
        # Add the current apple to the dictionary
        if apples[right] in apple_count:
            apple_count[apples[right]] += 1
        else:
            apple_count[apples[right]] = 1
        
        # If there are more than 2 types of apples, shrink the window from the left
        while len(apple_count) > 2:
            apple_count[apples[left]] -= 1
            if apple_count[apples[left]] == 0:
                del apple_count[apples[left]]
            left += 1
        
        # Update the maximum length of the window       
        max_length = max(max_length, right - left + 1)
        print(right, left, max_length)

    return max_length

# Example usage:
apples = [2, 1, 2, 3, 3, 1, 3, 5]
print(longest_two_types_path(apples))  # Output: 4

