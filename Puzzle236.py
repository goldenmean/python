"""
Isolated conundrum #236

A positive integer is said to be ‘four-twelve--jiggly’ if it has four digits, all non-zero, and no matter how you arrange these digits you always obtain a multiple of 12. How many ‘four-twelve-jiggly’ positive integers are there?
"""
from itertools import permutations

num = 1000
soln = [ ]
solnfound = True 
basenum = 0
while num <= 9999:
    solnfound = True
    strnum = str(num)
    perm = permutations(strnum)
    for i in list(perm):
        if '0' not in i: 
            num2 = int(i[0]+i[1]+i[2]+i[3])
            if (num2 % 12) == 0:
                pass
                #print(num)
                #if num2 not in soln:
            else:
                solnfound = False
        else:
            solnfound = False
    #print(num)
    #print(solnfound)    
    if solnfound == True:
        if '0' not in strnum:
            soln.append(num)
            print(num)
    num += 1

print(soln)
#setsoln = set(soln)
# for i in soln:
    # print(i)

print("Total such numbers", len(soln))



