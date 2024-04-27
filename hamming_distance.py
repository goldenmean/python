'''
Given two integers x and y, return the hamming distance between the two numbers.
Note: The hamming distance between two numbers is the number of bit positions in which the bits differ.

Ex: Given the following integers x and y…

x = 2, y = 4, return 2.
2 in binary is 0 0 1 0
4 in binary is 0 1 0 0
therefore the number of positions in which the bits differ is two.
'''

def binary_hamming_dist(N1,N2):
    hdist = 0
    N = 32 #32bit numbers assumed
    i=0
    while i < N:
        #print(N1 & 0x1)
        #print(N2 & 0x1)
        if N1 & 0x1 != N2 & 0x1:
            hdist +=1
        N1 = N1 >> 1
        N2 = N2 >> 1
        i+=1

    return hdist 

#N1=2; N2=4
N1=8; N2=7
print(binary_hamming_dist(N1,N2))

