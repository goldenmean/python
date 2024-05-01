'''
There are 
N dishes in a row on a kaiten belt, with the 
ith dish being of type 
D[i]
​
 . Some dishes may be of the same type as one another.
You're very hungry, but you'd also like to keep things interesting. The 
N dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous 
K dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.
Please take care to write a solution which runs within the time limit.

Sample test case #1
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1
Expected Return Value = 5

Sample test case #2
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 2
Expected Return Value = 4

Sample test case #3
N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2
Expected Return Value = 2

'''
from typing import List

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    window = {}
    disheseaten = 0
  
    for i in range(N):
        if D[i] not in window or (disheseaten - window[D[i]]) > K:
            window[D[i]] = disheseaten
            disheseaten += 1
    print(window)
    return disheseaten 


#Below solution fails one test case for time limite exceeded 
'''
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    fixedszq = []
    disheseaten=0
    for i,d in enumerate(D): 
        if d not in fixedszq:
            disheseaten+=1
            if len(fixedszq) == K:
                fixedszq.pop(0)
            fixedszq.append(d)
    
    return disheseaten
'''
            
#N = 6; D = [1, 2, 3, 3, 2, 1]; K = 1
#N = 6; D = [1, 2, 3, 3, 2, 1]; K = 2
N = 7; D = [1, 2, 1, 2, 1, 2, 1]; K = 2

print(getMaximumEatenDishCount(N,D,K))


            

 



