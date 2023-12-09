"""
Isolated conundrum #227

If the pattern shown below is continued, what will appear directly below 400?

			1			
		2	3	4		
	5	6	7	8	9	
10	11	12	13	14	15	16
"""
import math

diff = 3
res = 1

while res <= 600:
    res = res + diff
    diff += 2
    print(res)# This will print the last number(which will be a square number) in each row
