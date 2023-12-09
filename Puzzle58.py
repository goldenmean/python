"""
The first term in a sequence of positive integers is 6. The other terms follow these rules:
•	If a term is even then divide it by 2 to obtain the next term.
•	If a term is odd then multiply by 5 and subtract 1 to obtain the next term.
For what values of n is the nth term equal to n?

"""

n = 1
T = 6

while True:
    if (T % 2) == 0:
        T = T/2
    else:
        T = 5*T - 1
    n = n + 1
    if n == T:
        print("Condition met n = %d  same as Nth term = %d " %(n, T) )
	
