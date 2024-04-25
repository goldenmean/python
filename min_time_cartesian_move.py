'''
Given N points on a Cartesian plane, return the minimum time required to visit all points in the order that they’re given.
Note: You start at the first point and can move one unit vertically, horizontally, or diagonally in a single second.

Ex: Given the following points…

points = [[0, 0], [1,1], [2,2]], return 2.
In one second we can travel from [0, 0] to [1, 1]
In another second we can travel from [1, 1,] to [2, 2]
Ex: Given the following points…

points = [[0, 1], [2, 3], [4, 0]], return 5.
'''

def min_time(pts):
    npts = len(pts)
    diag=0
    for i in range(npts-1):
        x1,y1=pts[i]
        x2,y2=pts[i+1]

        diag+= max(abs(x2-x1),abs(y2-y1))

    return diag  


#points = [[0, 0], [1,1], [2,2]]
#points = [[0, 1], [2, 3], [4, 0]]

points = [[0, 1], [0, 1]]


print(min_time(points))

     
