def TennisTourn(P, C):
    # write your code in Python 2.7
    
    
    while C != 0:
        mp = C * 2
        if mp > P:
            C = C - 1
        else:
            return C
        
    return C
            
print TennisTourn   (5,3)
print TennisTourn   (10,3)
print TennisTourn   (1,3)
print TennisTourn   (4,1)