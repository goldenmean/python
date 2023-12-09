"""
Isolated conundrum #172

A particular four-digit number N is such that the sum of N and 74 is a square; and the difference between N and 15 is also a square. What is N?

"""

import math

num = 1000

while num <= 9999:
    v1 = math.sqrt(num + 74)
    v2 = math.sqrt(num - 15)
    
    v3 = (int(v1+0.5))**2
    v4 = (int(v2+0.5))**2
    #print("v1=%f, v2=%f, v3=%d, v4=%d " %(v1,v2,v3,v4) )
    if v3 == (num+74) and  v4 == (num-15):
        print("########## number is %d, num + 74 is %d, num - 15 is %d " %(num, num+74, num-15) )
        print("v1=%f, v2=%f " %(v1,v2))
    #print("number is %d, num + 74 is %d, num - 15 is %d " %(num, num+74, num-15) )
    num = num + 1
    