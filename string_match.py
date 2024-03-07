'''
Find a subsring within a string given and return index of first occurrence
'''


def det_subs(strg, substrg): 
    idx1=0 
    idx2=0 

    #print(strg) 

    while idx1 < len(strg): 
        if strg[idx1] == substrg[idx2]: 
            if idx2 == len(substrg)-1: 
                print(f"idx1 is {idx1}, idx2 is {idx2}") 
                return idx1-idx2 

            idx2+=1 

        else: 
            idx2=0 

        idx1+=1 
    return -1 
    
strg ="rayray"
subs ="ray"

print(det_subs(strg,subs))