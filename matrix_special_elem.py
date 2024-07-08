'''
Given an N x M matrix, containing distinct elements, return all special values.
Note: A special value in the matrix is an element that is the minimum element in
the its row and the maximum element in its column.

Ex: Given the following matrix…

matrix = [
  [1, 2],
  [3, 4]
], return [3].
Ex: Given the following matrix…

matrix = [
  [1, 2, 5],
  [4, 8, 3],
  [9, 7, 6]
], return [6].
'''

def special_elem(matrix) -> list:
    min_ele = [ ]
    max_ele = []
    res = [ ]
    for row in matrix:
        min_ele.append(min(row)  )
    for col in zip(*matrix):
        max_ele.append(max(col))
    
    for n in min_ele:
        if n in max_ele:
            res.append(n)
    return res


matrix = [
  [1, 2, 5],
  [2, 8, 3],
  [3, 4, 6]
]

print(special_elem(matrix))

