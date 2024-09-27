"""
An array of size N will contain elements from 0 to N-1
but in a jumbled order.
Given an array of clues, reconstruct the original array.
the clues are + which indicates element at that index is greater than 
previous element and - indicates element at that index is less than previous
Given this input of clues, reconstruct the original array of values from 0 to N-1

"""


def reconstruct_array(clues):
    N = len(clues)
    plus = 0
    ans=[0]*N

    for i in range(N):
        if clues[i] == '+':
            plus += 1

    firstelem = N-1-plus
    smaller = firstelem-1 
    larger = firstelem+1
    ans[0] = firstelem

    for i in range(1,N):
        if clues[i] == '+':
            ans[i] = larger
            larger += 1
        elif clues[i] == '-':
            ans[i] = smaller
            smaller -= 1
        
    return ans

# Test case
clues = [None, '+', '+', '-', '+']
result = reconstruct_array(clues )
print(result)