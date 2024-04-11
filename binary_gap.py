

def binary_gap(num):
    maxgap=0
    res=0
    one_seen=False
    bn=bin(num)[2:]
    print(bn)
    for c in bn[::-1]:
        if one_seen == False:    
            if c == '0': 
                continue
            else:
                one_seen=True
        else:
            if c == '0':
                res+=1          
            else:
                maxgap=max(maxgap,res)
                res=0
                
    return maxgap
        
num=-1
print(binary_gap(num))      