
'''
Given an integer n, return whether or not it is a “magical” number. A magical number
is an integer such that when you repeatedly replace the number with the sum of the 
squares of its digits its eventually becomes one.

Ex: Given the following integer n…

n = 19, return true.
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1.

Ex: Given the following integer n…
n = 22, return false
'''

def isMagical(n):
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
        print(n)
    print(n)
    return n == 1

# Example usage
#print(isMagical(19))  # Expected: True
#print(isMagical(22))  # Expected: False
#print(isMagical(89))
print(isMagical(64))