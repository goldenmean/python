
#Sort a 2D matrix - each row and column in ascending order


def sort_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    #Sort each row first in ascending order
    for i in range(n):
        matrix[i].sort()

    #For each column
    for j in range(m):
        #Pick the jth column from each row
        col = [row[j] for row in matrix]
        #Sort the jth column in ascending order
        col.sort()
        #Replace the jth column with the sorted column
        for i in range(n):
            matrix[i][j] = col[i]
    return matrix

a = [[6,7,3],[0,8,-4],[5,6,9]]

print(sort_matrix(a))
