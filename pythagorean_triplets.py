


def has_pythagorean_triplet(nums):
    # Square each element in the list
    squares = [x**2 for x in nums]
    
    # Store the squared elements in a set for fast lookup
    squares_set = set(squares)
    
    # Iterate through pairs of squared elements
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
            if squares[i] + squares[j] in squares_set:
                return True
    
    return False

# Example usage
nums = [3, 5, 12, 5, 13]
print(has_pythagorean_triplet(nums))  # Output: True

