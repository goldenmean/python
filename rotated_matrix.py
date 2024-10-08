'''
Rotate a matrix
'''






m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#transpose of a 2D nxn matrix
tm=list(map(list,zip(*m)))

#reverse the rows of the transposed matrix to get rotated matrix rm
rm = [rows[::-1] for rows in tm]


# another way to transpose the matrix
def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


