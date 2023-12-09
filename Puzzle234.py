"""
Isolated conundrum #234

In Autumn 2012, a school inaugurated a fundraising campaign to celebrate the 600th anniversary of its foundation. 
The actual date of this anniversary lies in the period from 2013 to 2099. The anniversary year is the product of a prime and the 
square of a different prime. The two primes involved have the same unit digits and this unit digit also happens to be the sum of 
the digits in the anniversary year. In what year was the school founded?

"""

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
	

st = 2013
while st <= 2099:
    factlist = prime_factors(st)
    print(factlist)
    st += 1

    