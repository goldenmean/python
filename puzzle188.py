"""
Isolated conundrum #188

In how many whole numbers between 100 and 999 is the middle digit equal to the sum of the other two digits?
"""

st = 100
ans = 0

while st <= 999:
    strnum = str(st)
    d1 = int(strnum[0])
    d2 = int(strnum[1])
    d3 = int(strnum[2])
    if d2 == (d1+d3):
        ans += 1
    st += 1
    
print(ans)