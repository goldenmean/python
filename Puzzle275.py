"""
Isolated conundrum #275

For how many values of n are both n and 4^(((n-1)/(n+1))) integers?

"""

n = 0
#end = 100000

while True:
    idx1 = n-1
    idx2 = n+1
    exprn = 4**(idx1/idx2)
    
    if exprn == int(exprn):
        print(n)
    n+=1
       
