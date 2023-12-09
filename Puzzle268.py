"""
Isolated conundrum #268

Note that 1647/8235=1/5. Starting with 1647/8235, first delete one digit from the numerator and one digit from the denominator
 leaving a fraction A/B which is equivalent to the starting fraction. Then delete one digit from the new numerator A and one
 digit from the new denominator B leaving a fraction C/D which is equivalent to A/B. What is the value of the difference D-C?
"""

from itertools import permutations

num = 1647
den = 8235
ans = num/den

numperms = permutations(str(num),3)
denperms = permutations(str(den),3)

numlist = [int("".join(x)) for x in numperms]
denlist = [int("".join(x)) for x in denperms]

#First pass to find the equivalent fraction 
for i in numlist:
    for j in denlist: 
        newans = i/j
        if newans == ans:
            print(f" New numerator is {i}, New denominator is {j}")
            n1 = i
            d1 = j

#Second pass to use numerator and denominator obtained from first pass completion having same equivalent fractional value
#print(n1)
#print(d1)

newnum = n1
newden = d1
ans = newnum/newden

numperms = permutations(str(newnum),2)
denperms = permutations(str(newden),2)

numlist = [int("".join(x)) for x in numperms]
denlist = [int("".join(x)) for x in denperms]

for i in numlist:
    for j in denlist: 
        newans = i/j
        if newans == ans:
            print(f" Final numerator is {i}, Final denominator is {j}")
            n1 = i
            d1 = j


