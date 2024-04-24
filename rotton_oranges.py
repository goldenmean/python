'''
Given a 2D array each cells can have one of three values. Zero represents an empty cell, one represents a healthy person, and two represents a sick person. Each minute that passes, any healthy person who is adjacent to a sick person becomes sick. Return the total number of minutes that must elapse until every person is sick.
Note: If it is not possible for each person to become sick, return -1.

Ex: Given the following 2D array grid…

grid = [
    [1,1,1],
    [1,1,0],
    [0,1,2]
], return 4.
[2, 1] becomes sick at minute 1.
[1, 1] becomes sick at minute 2. 
[1, 0] and [0, 1] become sick at minute 3.
[0, 0] and [0, 2] become sick at minute 4.
Ex: Given the following 2D array grid…

grid = [
    [1,1,1],
    [0,0,0],
    [2,0,1]
], return -1.
'''
from typing import List
from collections import deque

def rotten_oranges(grid: List[List[int]]) -> int: 
    q = deque()
    minutes, fresh = 0,0
    ROWS, COLS = len(grid), len(grid[0])
    # add rotten oranges  at start to the queue and count fresh oranges
    for m in range(ROWS):
        for n in range(COLS):
            if grid[m][n] == 1: 
                fresh +=1
            elif grid[m][n] == 2: # m corresponds to row so y coordinate, n corresponds to column so x coordinate on a grid
                q.append([m,n])

    # 4 directions we can traverse from a rotten orange cell
    directions =[[0,1],[0,-1],[1,0],[-1,0]]

    print(f"q is {q}")
    print(f"fresh oranges are {fresh}")
    
    # run this algo until there are rotten oranges in the queue or no fresh oranges remaining
    while q and fresh > 0:
        for i in range(len(q)):
            y,x =q.popleft()
            for dy, dx in directions:
                row,col = y+dy, x+dx
                #check if it is not a fresh orange or row, col are out of bounds of original grid dimension
                if (row < 0 or row == ROWS) or \
                   (col < 0 or col == COLS) or \
                   grid[row][col]!=1:
                    continue
                #this is a fresh orange neighbouring a rotten one, so set this to rotten
                grid[row][col] = 2
                q.append([row,col])
                fresh -= 1

        #after going through neighbouring locations of each existing rotten orange, increment time by 1
        minutes+=1       

    return minutes if fresh == 0 else -1


#grid = [[2,1,1],[1,1,0],[0,1,1]] # should output 4
#grid = [[2,1,1],[0,1,1],[1,0,1]] # should output -1
grid = [[0,2]] # should output 0 since no fresh orange present

print(rotten_oranges(grid))