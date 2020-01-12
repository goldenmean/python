def warehouse(A):
    b=A
    b.sort()
    gaps = [None] * (len(A) - 1)
    for i in range(len(A) - 1):
        gaps[i] = abs(b[i] - b[i+1] - 1)
        
    moves=0
    print gaps
    lgaps=len(gaps) - 1
    for j in range(len(gaps)):
        if gaps[j] > lgaps:
            continue
        elif:
             if moves < gaps[j]:
                 moves = gaps[j]
                 #print moves
                 #print gaps[j]
            
    return moves
        
        
        
       
    
    
arr = [6,4,1,7,10]
print warehouse(arr) #answer should be 2
