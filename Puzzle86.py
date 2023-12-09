"""
Isolated conundrum #86

I have thought of five numbers. If I add three of them in each possible way, the totals that I get are 10, 14, 15, 16, 17, 17, 18, 21, 22 and 24. What are my numbers?

"""

import itertools

#possinp = [0,0,1,1, 2,2, 3,3, 4,4, 5,5, 6,6, 7,7, 8,8,9,9, 10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20
possinp = [1,2,3,4,5,6,7,8,9,10]

#Below conditions give right solution of  result = [(2, 3, 5, 9, 10)]
result = [seq for seq in itertools.combinations(possinp, 5) if sum(seq) == 29 and sum(seq[2:]) == 24 and sum(seq[:3]) == 10 and sum(seq[1:4]) == 17 ]

#result = [seq for seq in itertools.combinations(possinp, 5) if sum(seq) == 29 and sum(seq[2:]) == 24 and sum(seq[:3]) == 10 and sum(seq[1:4]) == 17 and seq[0]+seq[1]+seq[3] == 14]

"""
inptot = [10,14,15,16,17,17,18,21,22,24]
tot = [0]*10
i = 0

import itertools


inp = [0] * 5

inp = itertools.combinations(possinp,5) 
for v in inp:
    flist = list(v)
    #print("5 digits are ",v)
    res = itertools.combinations(v,3)
    for x in res:
        #print("3 way combination is ",x)
        #print(x)
        tot[i] = sum(x)
        i = i + 1
    #print("Total is ",tot)
    if tot.sort() == inptot:
        print("Ans found inp is ", flist)
        break
    i = 0
"""