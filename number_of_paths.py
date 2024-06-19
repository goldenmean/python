'''
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, 
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a 
wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0


'''
def number_of_paths(matrix):
    """
    Returns the number of ways to get to the bottom right corner of the matrix.
    """
    n = len(matrix)
    m = len(matrix[0])
    table = [[0] * m for _ in range(n)]
    table[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i > 0 and matrix[i][j] == 0:
                table[i][j] += table[i-1][j]
            if j > 0 and matrix[i][j] == 0:
                table[i][j] += table[i][j-1]

    return table[-1][-1]
'''
grid = [[0,0,1],
        [0,0,1],
        [1,0,0] ]
'''
        
grid = [[0,0,0],
        [0,1,1],
        [0,0,0] ]

print(number_of_paths(grid))


