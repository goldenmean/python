def gcd_euclid_algo(a, b):
    return a if b==0 else gcd_euclid_algo(b, a%b)


def gcd_successive_difference(a, b):
    if a == 0: return b
    if b == 0: return a
    a, b = abs(a), abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Test the function
#print(gcd_successive_difference(48, 18))  # Output: 6

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd_successive_difference(num1, num2)
print(f"The GCD of {num1} and {num2} using the method of successive differences is: {result}")