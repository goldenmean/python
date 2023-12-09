"""
Isolated conundrum #219

In how many different ways can seven different numbers be chosen from the numbers 1 to 9 inclusive so that the seven numbers have a total which is a multiple of 3?

"""

from itertools import combinations

inp = [1,2,3,4,5,6,7,8,9] 

comb = combinations(inp,7)
ans = 0

for c in comb:
    tot = sum(list(c))
    if (tot % 3) == 0:
        print("Sum %d divisble by 3. List = " %(tot), list(c))
        ans += 1

print(ans)

#Below code is to check if there is any combination involving 3,6,9 being present and still sum is not multiple of 9.
#comb = combinations(inp,7)
#for c in comb:
#    tot = sum(list(c))
#    if (3 in c) and (6 in c) and (9 in c) and (tot%3) != 0:
#        print(list(c))
        
        		