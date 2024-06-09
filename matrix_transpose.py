

#Transpose a matrix - pythonic way using list comprehension
#returns a new matrix
def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


#Transpose using for loops in place
def transpose_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

A=[[1,2,3],[4,5,6],[7,8,9]]

print(transpose(A))





