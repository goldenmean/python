'''
Shortest Clear Path
A clear path is a path in a binary grid from the top-left cell (0, 0) to the bottom-right cell (n - 1, n - 1)
such that,
All the visited cells of the path have a value of 0.(you cannot visit a cell with value as 1)
All the adjacent cells of the path are 8-directionally connected (they are different and share an 
edge or a corner).
Consider an n x n binary grid where each cell is either 0 (empty) or 1 (obstacle). 
Find the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

Here, n = row = column. The length of a clear path is the number of visited cells through this path.
e.g.
1] For belwo binary matrix , shortest clear path length is 2
0  1
1  0

2] For below matrix length of shortest clear path is 4 
0  0  0
1  1  0
1  1  0


'''
from collections import deque

def shortest_clear_path(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    # 8 directions: down,   up,    right,  left,    diagonal down-right, diagonal down-left, diagonal up-right and diagonal up-left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    #Queue to store the nodes to be visited with path length
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0]=1
    while queue: #BFS algorithm
        #Pop the top node from the queue
        r, c, path_length = queue.popleft()
        #If the current node is the bottom right node, return the path length
        if (r, c) == (n-1, n-1):
            return path_length
        #Add all adjacent nodes to the queue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc # next row, next column
            # Check if the next node is within the grid and not an obstacle
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                print(f"r is {r} c is {c} dr is {dr} dc is {dc} path_length is {path_length}")
                # If the next node is not an obstacle, mark it as visited and add it to the queue
                grid[nr][nc] = 1  
                queue.append((nr, nc, path_length + 1))
                
    # If no clear path is found, return -1
    return -1
    
'''
grid = [ 
[0,  0,  0],
[1,  1,  0],
[1,  1,  0]]
'''

grid = [
[0,  1],
[1,  0]]


print(shortest_clear_path(grid))







