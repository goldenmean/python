'''
Find determinant of a square matrix 
'''

def determinant(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(n):
            det += matrix[0][i] * ((-1) ** (i)) * determinant([[matrix[j][k] for k in range(n) if k != i] for j in range(n) if j != 0])
        return det
    
#A = [[3, 1, -2], [-1, 2, 3], [2, 1, 4]]
#A = [[4, 1, -2], [1, 2, 3], [-2, 1, 4]]
#A = [[3, 1, 4], [-1, 2, 1], [2, 1, -2]]
#A = [[3, 4, -2], [-1, 1, 3], [2, -2, 4]]
A = [[0, 1, 2],[-2, 3, -1],[4, 0, 1]]

print(determinant(A))

