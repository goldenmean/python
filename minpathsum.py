from typing import List

def minpathsum(grid: List[List[int]]) -> int:
    m,n=len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if i==j==0:
                continue
            left_path = up_path = float('inf')
            if j!=0:
                left_path=grid[i][j] + grid[i][j-1]
            if i!=0:
                up_path=grid[i][j] + grid[i-1][j]
                
            grid[i][j]=min(left_path,up_path)
    
    return grid[-1][-1]
    

arr=[[1,3,1],[1,5,1],[4,2,1]]
minp=minpathsum(arr)
print(f"minimum path sum is {minp}")
print("original array updated with minimum path values is ",arr)