"""
Isolated conundrum #108

Leap years occur every four years. However, years at the turn of the century are leap years only if they are multiples of 400. 
Therefore, 2000 was a leap year, but the year 1900 was not a leap year. How many leap years are there in the period from 2001 to 3001?

"""

import math

num_leap_years = 0
y1 = 2001
y2 = 3001

tmpy1 = y1

while tmpy1 <= y2:
    if (tmpy1 % 100) == 0:
        if (tmpy1 % 400) == 0:
            num_leap_years = num_leap_years + 1
            print(tmpy1)
        tmpy1 = tmpy1 + 1
        continue		
    if (tmpy1 % 4) == 0:
        num_leap_years = num_leap_years + 1
        print(tmpy1 )
    tmpy1 = tmpy1 + 1
		
print("Num of leap years between y1 = %d and y2 = %d is %d " %(y1, y2, num_leap_years ) )