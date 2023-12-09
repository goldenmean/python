"""
How many pairs of numbers (a,b) exists such that the sum a +  b, the product ab and the quotient a/b of these two numbers are all equal?
"""


a = 1 
b = 1
inc = 0

while True:
    if a*b == (a+b) == a//b: 
        print("Found: a is %d , b is %d " %(a,b))
    a = a + 1
    inc = inc + 1
    if inc == 100:
        b = b + 1
        inc = 0
    #print("Searching... currrent a is %d, b is %d" %(a,b) )
