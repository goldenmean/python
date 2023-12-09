"""
Isolated conundrum #203

Sixty 20p coins are lined up side by side. Every second 20p coin is then replaced by a 10p coin. 
Then every third coin in the row is replaced by a 5p coin. Finally every fourth coin in the row is replaced by a 2p coin. 
What is the final value of the line?

"""


inp = [20]*60 
print(sum(inp))
#inp = [10 if (idx % 2) != 0 else val for idx,val in enumerate(inp) ] 
inp = [10 if ((idx+1) % 2) == 0 else val for idx,val in enumerate(inp) ] 
print(inp)
print(sum(inp))
inp = [5 if ((idx+1) % 3) == 0 else val for idx,val in enumerate(inp) ] 
print(inp)
print(sum(inp))
inp = [2 if ((idx+1) % 4) == 0 else val for idx,val in enumerate(inp) ] 
print(inp)
print(sum(inp))