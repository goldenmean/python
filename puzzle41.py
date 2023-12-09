"""
Isolated conundrum #41

Consider the list of all four digit numbers that can be formed using the digits 1,2,3 and 4 without repetition. What is the sum of all the numbers in the list?

"""

from itertools import permutations

mynum=12345

allowednum = []

plist = permutations(str(mynum))

nlist = [int("".join(x)) for x in plist]
print(sum(nlist))



