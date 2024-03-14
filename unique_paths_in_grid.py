

def unique_paths(m,n):

    ret = [ ]  #list of lists 2D array 

    for i in range(m): 
         ret.append([0]*n) 

    ret[0][0]=1 

    for i in range(m): 
        for j in range(n): 
            if i==0 and j==0: continue                 
            elif i==0: 
                ret[i][j] = ret[i][j-1] 
                #print("B")    
                #print(f"i is {i}, j is {j}, ret[i][j] is {ret[i][i]}")				
            else:  
                ret[i][j] = ret[i-1][j] + ret[i][j-1]  
                #print("C")                
                #print(f"{ret[i-1][j]} + {ret[i][j-1]}")				
                print(f"i is {i}, j is {j}, ret[i][j] is {ret[i][j]}")

    return  ret[-1][-1] 
    
m=5
n=5

print(unique_paths(m,n))    