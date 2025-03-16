"""
You are given a two-dimensional matrix containing only ones and zeroes 
representing a computer network. Every one in the matrix represents a server
and every zero represents an empty space. Two servers within the network can
communicate if they are either in the same row or the same column. 
Return the total number of servers that can communicate with at least one 
other server.

Ex: Given the following matrix…

matrix = [
  [1, 0],
  [1, 0],
], return 2 (both servers are in the same column and can therefore communicate
with one another).
Ex: Given the following matrix…

matrix = [
  [1, 0],
  [0, 1],
], return 0.

"""

def count_communicating_servers(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    row_counts = [0] * rows
    col_counts = [0] * cols

    # Count servers in each row and column
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                row_counts[i] += 1
                col_counts[j] += 1

    # Count servers that can communicate
    communicating_servers = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                communicating_servers += 1

    return communicating_servers


# Test cases
matrix1 = [
    [1, 0],
    [1, 0]
]
print(count_communicating_servers(matrix1))  # Output: 2

matrix2 = [
    [1, 0],
    [0, 1]
]
print(count_communicating_servers(matrix2))

matrix3 = [
    [1, 1],
    [1, 0]
]
print(count_communicating_servers(matrix3))
