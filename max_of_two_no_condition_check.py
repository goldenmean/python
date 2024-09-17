'''
Find maximum of two numbers without using if-else, branching or comparisons

'''

def max_of_two_bitwise(a, b):
    return a - ((a - b) & ((a - b) >> 31))


def max_of_two_arithmetic(a, b):
    return (a + b + abs(a - b)) // 2

# Test cases
print(max_of_two_bitwise(5, 10))  # Should print 10
print(max_of_two_bitwise(-1, -5))  # Should print -1
print(max_of_two_bitwise(7, 7))  # Should print 7

# Test cases
print(max_of_two_arithmetic(5, 10))  # Should print 10
print(max_of_two_arithmetic(-1, -5))  # Should print -1
print(max_of_two_arithmetic(7, 7))  # Should print 7

