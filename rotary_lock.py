'''
Rotary lock 
https://www.metacareers.com/profile/coding_puzzles?puzzle=990060915068194

Sample test case #1
N = 3
M = 3
C = [1, 2, 3]

Expected Return Value = 2

Sample test case #2
N = 10
M = 4
C = [9, 4, 4, 8]
Expected Return Value = 11

'''

from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    cur = 1
    timetaken=0

    for d in C:
        timetaken += min((d-cur)%N, (cur-d)%N)
        cur=d
    return timetaken


#N = 3; M = 3; C = [1, 2, 3]
N = 10; M = 4; C = [9, 4, 4, 8]

print(getMinCodeEntryTime(N,M,C))

