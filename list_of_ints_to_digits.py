
# Convert a list of integers to a list of digits of those integers
a = [1, 23, 456]

# Convert the list of integers into a list of digits
digits = [int(digit) for number in a for digit in str(number)]


# Convert a list of digits to a number from those digits
d = [1, 2, 3]

# Convert the list of digits into a single number
number = int(''.join(map(str, d)))

print(number)
