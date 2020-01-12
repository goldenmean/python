def number_of_zeros(S):
    P = 1410000017
    Z = 0
    N = 0
    F = 0
    for j in xrange(len(S)):
        F = (10*F + N + P - Z*(9-int(S[j])) ) % P
        if S[j] == '0':
            Z += 1
        N = (10*N + int(S[j])) % P
    return ((1 + F) % P)
	

print number_of_zeros(str(23))