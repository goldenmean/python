'''
Stack stabilisation : 
https://www.metacareers.com/profile/coding_puzzles?puzzle=183894130288005

Sample test case #1
N = 5
R = [2, 5, 3, 6, 5]
Expected Return Value = 3

Sample test case #2
N = 3
R = [100, 100, 100]
Expected Return Value = 2

Sample test case #3
N = 4
R = [6, 5, 4, 3]
Expected Return Value = -1

'''

from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    shrinkdisk=0
    for i in range(N-2,-1,-1):
        if R[i] >= R[i+1]:
            shrinkdisk+=1
            R[i] = R[i+1]-1
            if R[i] <= 0:
                return -1

    return shrinkdisk

N = 5;R = [2, 5, 3, 6, 5]
#N = 3; R = [100, 100, 100]
#N = 4; R = [6, 5, 4, 3]
print(getMinimumDeflatedDiscCount(N,R))
