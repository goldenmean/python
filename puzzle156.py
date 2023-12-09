"""
Isolated conundrum #156

The year 1789 has exactly three adjacent digits (7, 8 and 9) that are consecutive integers in increasing order.
How many years between 1000 and 9999 have this property?

"""

start = 1000
end = 9999
ans = 0

year = start

while year <= end:
    strnum = str(year)
    d1 = int(strnum[0])
    d2 = int(strnum[1])
    d3 = int(strnum[2])
    d4 = int(strnum[3])
    
    #print(d1, d2, d3, d4)
    if ( (d2 - d1) == 1 and (d3 - d2) == 1 and (d4 - d3) != 1 ) or ( (d3 - d2) == 1 and (d4 - d3) == 1 and (d2 - d1) != 1 ):
        ans = ans + 1
        print(year)
    year = year + 1


print("Number of year satisfying the conditions are %d " %(ans))    