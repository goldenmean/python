from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  tot=R*C
  ships=0
  print(R,C)
  print(G)
  for i in range(R):
    for j in range(C):
      if G[i][j] == 1:
        print(G[i][j])
        ships+=1
        
  print(ships,tot)
  return ships/tot

R=2
C=3
G=[[0,0,1],[1,0,1]]

print(getHitProbability(R,C,G))

