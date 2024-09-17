'''
Given a 2D matrix of 1s and 0s. For a element of value 1, if all other elements
in that row and column are 0, then that element is lonely.
Find and return the number of lonely elements in the matrix. 
'''



def count_lonely_indices(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    lonely_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # Check the row and column
                row = matrix[i]
                col = [arr[j] for arr in matrix]
                print(f"Row: {row}, Col: {col}")
                if all(row[k] == 0 for k in range(cols) if k != i) and \
                   all(col[k] == 0 for k in range(rows) if k != j):
                
                #if all(matrix[i][k] == 0 for k in range(cols) if k != j) and \
                #   all(matrix[k][j] == 0 for k in range(rows) if k != i):
                
                    lonely_count += 1
    
    return lonely_count

# Test cases
matrix1 = [
    [1, 0],
    [0, 1]
]
#print(count_lonely_indices(matrix1))  

matrix2 = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
]
#print(count_lonely_indices(matrix2))  

matrix6 = [
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]
print(count_lonely_indices(matrix6)) 

matrix8 = [
    [1, 0, 1, 0]
]
#print(count_lonely_indices(matrix8)) 
