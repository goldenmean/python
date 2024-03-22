'''
Pascals triangle
'''

def pascal_triangle(numrows):
    triangle=[]
    if numrows == 0:
        return triangle
        
    firstrow=[1]
    triangle.append(firstrow)
    
    for i in range(1,numrows):
        prevrow=triangle[i-1]
        currow=[]
        currow.append(1)
        for j in range(1,i):
            currow.append(prevrow[j-1]+prevrow[j])    
         
        currow.append(1)
        triangle.append(currow)
     
    return triangle
    
    
rows=6
res=pascal_triangle(rows)

for i in range(len(res)):
    print(res[i])
    
    