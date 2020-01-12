def solution(A, B, C):
    lenC = len(C)
    if lenC==0:
        return 0	
	
    cumwt = [0]*lenC
    i=0 
    lut = [0]*lenC
    for v in C:
                    
        if v == -1:
            cumwt[i] = B[i]
            if cumwt[i] > A[i]:
                return i
            else:
               i = i + 1                           
        
        else:
            cumwt[i] = cumwt[i] + B[i] 
            if cumwt[i] > A[i]:
                return i			
            while v != -1:
                idx = v
                v =C[idx]
                cumwt[idx] = cumwt[idx] +  B[i]                                 
                if cumwt[idx] > A[idx]:
                    return i 
                              
            i = i + 1          
    
    return i    
       
def solution1(A,B,C):
    cumwt = [0]*len(A)
    for i in reversed(xrange(len(C))):
        if C[i] != -1:
            cumwt[C[i]] = cumwt[C[i]] + B[i]
        else:
            cumwt[i] = cumwt[i] + B[i]      

    i = 0
    for x in cumwt:
        if x > A[i]:
            return i
        else:
            i = i + 1
            
#D= [5,3,6,3,3]
#D=[4,3,1]
D=[]

#W=[2,3,1,1,2]
#W=[2,2,1]
W=[]

#P=[-1,0,-1,0,3]
#P=[-1,0,1]
P=[]

print solution(D,W,P)