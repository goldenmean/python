'''
A cafeteria table consists of a row of 
N seats, numbered from 
1
1 to N from left to right. Social distancing guidelines require that every diner be seated such that 
K seats to their left and 
K seats to their right (or all the remaining seats to that side if there are fewer than 
K) remain empty.
There are currently M diners seated at the table, the ith of whom is in seat 
S i
No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3
Sample test case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1

'''

from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    newd = 0
    newdiners = 0
    S.sort()
    #print(N,K)
    for i in range(M):
        if i == 0:
            avail_tables = S[i] - (K+1)
            avail_tables = avail_tables if avail_tables >= 0 else 0
            #print(f"i is {i}, avail_tables is {avail_tables}, S[i] is {S[i]}")
        else:
            avail_tables = S[i] -(K+1) - (S[i-1]+K)
            avail_tables = avail_tables if avail_tables >= 0 else 0
            #print(f"i is {i}, avail_tables is {avail_tables}, S[i] is {S[i]}")        
        newdiners += (avail_tables + K)//(K+1)
        #print(f"newdiners is {newdiners}")        

    #print("loop finished")
    avail_tables = N - (S[-1]+K)
    avail_tables = avail_tables if avail_tables >= 0 else 0
    newdiners += (avail_tables + K)//(K+1)

    return newdiners

#N=10; K=1; M=2; S=[2,6] 
N = 15;K = 2;M = 3;S = [11, 6, 14]

print("New diners that can be accomodated")
print(getMaxAdditionalDinersCount(N,K,M,S))