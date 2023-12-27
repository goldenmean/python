import math

def findminrate(pile,h):
    l,r = 1,max(pile)
    while l < r:
        mid=l+(r-l)//2
        hrs=0
        for p in pile:
            hrs += math.ceil(p/mid)
      
        if hrs <= h: 
            r = mid 
        else:
            l = mid + 1
            
    return r
    

h=8
piles=[3,6,7,11]
print(findminrate(piles,h))
