'''
Sum of Perfect Squares
A perfect square is a number made by squaring a whole number.

Some examples include 1, 4, 9, or 16, and so on -- because they are the squared results of 1, 2, 3, 4, etc. For example:

SNIPPET
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
...
However, 15 is not a perfect square, because the square root of 15 is not a whole or natural number.

Perfect Square  Factors
1   1 * 1
4   2 * 2
9   3 * 3
16  4 * 4
25  5 * 5
36  6 * 6
49  7 * 7
64  8 * 8
81  9 * 9
100 10 * 10
Given some positive integer n, write a method to return the fewest number of perfect square numbers which sum to n.

The follow examples should clarify further:

var n = 28
howManySquares(n);
// 4
// 16 + 4 + 4 + 4 = 28, so 4 numbers are required
On the other hand:

var n = 16
howManySquares(n);
// 1
// 16 itself is a perfect square
// so only 1 perfect square is required
'''
res=[]
def fewest_sq_numbers(n):
    if n <= 3:
        return n;
 
    # fewest_sq_numbers rest of the table 
    # using recursive formula
    # Maximum squares required 
    # is n (1 * 1 + 1 * 1 + ..)
    res = n 
 
    # Go through all smaller numbers
    # to recursively find minimum
    for x in range(1, n + 1):
        temp = x * x;
        print(f"n is {n}, x is {x}, temp is {temp}")
        if temp > n:
            break
        else:
            print(f"res is {res}, and n-temp is {n-temp}")
            res = min(res, 1 + fewest_sq_numbers(n 
                                  - temp))
    
    print(f"returning res = {res}")	
    return res; 
 
n=int(input("Enter a positive integer: "))
print(fewest_sq_numbers(n))


