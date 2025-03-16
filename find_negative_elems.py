"""
Given an MxN matrix, which is sorted in decreasing order (row-wise and column-wise),
return the total number of negative values in the array.

Ex: Given the following matrix…

matrix = [
  [3, -1],
  [2, -2]
], return 2 (-1 and -2 are negative).
Ex: Given the following matrix…

matrix = [
  [4, 3],
  [2, 1]
], return 0.

"""

def find_negative_elements(matrix):

    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    count = 0
    row, col = m - 1, 0 # start from bottom left corner element
    
    while row >= 0 and col < n:
        if matrix[row][col] < 0: 
            count += n - col # The whole row from this column onwards is -ve
            row -= 1 # move row up in same column
        else:
            col += 1 # move to next column right in same row
    
    return count  

# Test 
matrix = [
  [3, -1],
  [2, -2]
]
print(find_negative_elements(matrix))

