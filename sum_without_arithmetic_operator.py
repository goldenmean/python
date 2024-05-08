

def sum_without_plus_minus(a, b):
    while b!= 0:
        # XOR to get the sum without considering the carry
        carry = a & b # carry in addition of a and b
        a = a ^ b # sum of a and b without carry being considered
        b = carry << 1
    return a

# Example usage
a = 5  # Binary: 101
b = 3  # Binary: 011
result = sum_without_plus_minus(a, b)
print(f"The sum of {a} and {b} without using + or - is: {result}")