'''
Given a two-dimensional integer array, matrix, return whether or not the matrix is a
Toeplitz matrix.
Note: A Toeplitz matrix is a matrix in which every diagonal from the top-left corner 
to the bottom-right hand corner of the matrix contains the same element.

Ex: Given the following matrix…
matrix = [
  [1, 2, 3],
  [4, 1, 2],
  [5, 4, 1]
], return true ([4, 4], [1, 1, 1], and [2, 2] are the diagonals and each diagonal has 
the same element)
'''

def is_toeplitz_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows):
        for col in range(cols):
            if row > 0 and col > 0 and matrix[row][col] != matrix[row - 1][col - 1]:
                return False
    return True

# Test cases
matrix1 = [
  [1, 2, 3],
  [4, 1, 2],
  [5, 4, 1]
]
print(is_toeplitz_matrix(matrix1))  # Should print True

matrix2 = [
  [1, 2],
  [2, 2]
]
print(is_toeplitz_matrix(matrix2))  # Should print False

matrix3 = [
  [3, 7, 0, 9],
  [5, 3, 7, 0],
  [9, 5, 3, 7],
  [6, 9, 5, 3]
]
print(is_toeplitz_matrix(matrix3))  # Should print True