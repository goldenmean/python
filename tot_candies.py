




def candies(cand, exchg):
    wrappers = cand
    totcand = cand
    while wrappers > exchg:
        exchcndy = wrappers // exchg
        totcand += exchcndy
        wrappers = exchcndy + wrappers % exchg  
    
    return totcand

# Example

cand = 8
exchg = 3
print(candies(cand, exchg))


    