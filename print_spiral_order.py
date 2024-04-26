'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''

def print_spiral_order(matrix):
    while matrix:
        # print the first row
        for x in matrix.pop(0):
            print(f"--- {x}")

        # print the last element of each remaining row
        for row in matrix:
            if row:
                print(f"$$$ {row.pop()}")
                
        # if there are still rows remaining
        if matrix:
            # print the last row in reverse order
            for x in matrix.pop()[::-1]:
                print(f"<--- {x}")
            # print the first element of each remaining row in reverse order
            for row in matrix[::-1]:
                if row:
                    print(f"^^^ {row.pop(0)}")


matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

print_spiral_order(matrix)