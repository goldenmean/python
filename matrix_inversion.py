'''
matrix_inversion using Cofactors(A) and determinant(A) method 
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


def inverse_matrix(matrix):
    n = len(matrix)
    inverse = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            #inverse[i][j] = (matrix[j][i] * (-1)**(i+j)) / determinant(matrix)
            # First find cofactors , then Adjugate is transpose of cofactor matrix 
            # And then divide each element of Adjugate matrix by determinant(A) 
            # cofactor is found for [i][i] but since we need to transpose, we write that
            # cofactor[i][j] / determinant(A) to location inverse[j][i] , as we need to transpose the cofactor
            cofactor = determinant([[matrix[k][l] for l in range(n) if l != j] for k in range(n) if k != i]) * ((-1) ** (i + j))
            inverse[j][i] = cofactor / determinant(matrix)
    return inverse

#A = [[0, 1, 2],[-2, 3, -1],[4, 0, 1]]
A = [[3, 0, 2], [2, 0, -2], [0, 1, 1]]
print(inverse_matrix(A))


