


def odd_occurrence(A):

    if len(A)==1:
        return A[0]
    
    A.sort()
    N=len(A)
    for i in range(0,N-1,2):
        if A[i]!=A[i+1]:
            return A[i]
    
    if N % 2 == 0: return None
    return A[-1]
    
    
    
arr = [1,1,2,2]
print(odd_occurrence(arr))