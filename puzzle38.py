"""
Isolated conundrum #38

There are 120 ways of arranging the letters C,O,V,I,D. Consider an ordered list in alphabetical order starting with CDIOV.
What position in the list does VIDOC appear?

"""

from itertools import permutations

inp = "COVID"
perms = []

rlist = permutations(inp)

for idx,i in enumerate(rlist):
    word = i[0]+i[1]+i[2]+i[3]+i[4]
    #print("%d %s " %(idx+1, word) )
    perms.append(word)
	
perms.sort()

for idx, i in enumerate(perms):
    print("%d %s " %(idx+1, i) )

print("Index number for VIDOC is ",perms.index("VIDOC")+1 )


	
    

