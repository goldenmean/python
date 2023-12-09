"""
Isolated conundrum #150

What is the smallest multiple of 35 whose digits are all the same as each other?

"""
import math

multiple = 1
num = 35

while True:
    res = multiple * num
    strres = str(res)
    if len(set(strres)) == 1:
        print(res)
        break
    multiple = multiple + 1
	