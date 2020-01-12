"""Print a 2D array in a peculiar way as below
1] 1st column, 1st row
123
4
7

2] 2nd column, 1st row
123
  5
  8

3] 3rd column, 1st row 
123
    6
    9 
  
4] 1st column, 2nd row

5] 2nd column, 2nd row
 
6] 3rd column, 2rd row

7] 1st column, 3rd row

8] 2nd column, 3rd row
 
9] 3rd column, 3rd row 
 
"""

a=[[1,2,3],
    [4,5,6],
	[7,8,9]]

for k in xrange(0,3):
    for i in xrange(0,3):
        for j in xrange(0,3):
            print a[i][j]
	    print "\n"
		#Calculate no. of spaces to Print  - 1 or 2 or none depending upon which loop it is in
	    
		print a[i+1]
