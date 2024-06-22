'''
We are given a matrix with m rows and n columns. For example:
Our goal is to traverse the matrix diagonally and return the elements in that order.

e.g if we are given a mxn matrix as a list of lists as below
[
  [1, 2, 3],
  [4, 5, 6], 
  [7, 8, 9]
]

output of the traversal should be [1, 2, 4, 7, 5, 3, 6, 8, 9]


'''
def matrix_diagonal_traversal(matrix):
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for i in range(rows + cols - 1):
        if i % 2 == 0:
            r, c = min(i, rows - 1), max(0, i - rows + 1)
            while r >= 0 and c < cols:
                result.append(matrix[r][c])
                r -= 1
                c += 1
        else:
            r, c = max(0, i - cols + 1), min(i, cols - 1)
            while r < rows and c >= 0:
                result.append(matrix[r][c])
                r += 1
                c -= 1
    return result

'''
arr=[
  [1, 2, 3],
  [4, 5, 6], 
  [7, 8, 9]
]
'''
arr =[
    [1,2,3],
    [4,5,6]
]
print(matrix_diagonal_traversal(arr))

