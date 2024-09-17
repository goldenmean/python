'''
Given a binary string, binary, return the maximum score of the string. The score of a
string is given by splitting the string at a specific index and summing the total number
of zeroes in the left substring and the total number of ones in the right substring.
Note: Both the left and right substring after the split must have at least a single character.

Ex: Given the following string binary…
binary = "10", return 0.
Ex: Given the following string binary…
binary = "0011", return 4
'''

def max_score(binary):
    n = len(binary)
    if n < 2:
        return 0  # There's no valid split if the string length is less than 2

    # Initialize score by considering the first split
    left_score = 0 if binary[0] == '1' else 1
    right_score = binary[1:].count('1')
    max_score = left_score + right_score

    for i in range(1, n - 1):
        if binary[i] == '0':
            left_score += 1
        else:
            right_score -= 1
        max_score = max(max_score, left_score + right_score)

    return max_score

# Test cases
print(max_score("10"))     # Should print 0
print(max_score("0011"))   # Should print 4
print(max_score("011101")) # Additional test case, should print 5