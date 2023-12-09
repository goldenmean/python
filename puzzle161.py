"""
Isolated conundrum #161

A befuddled bank cashier transposed the pounds and pence when he cashed a check for Ms Smith, 
giving her pounds instead of pence and pence instead of pounds.  Ms Smith started with only the 
money the cashier gave her, after buying a newspaper for 50 pence, she noticed that she had exactly 
three times as much as the original check was worth left.  What was the amount of the check?  
"""

i = 1
j = 1

while j < 100 and i < 100:
    rhs = 299*i + 50
    lhs = 97*j
    #print("1:  rhs is %d, lhs is %d " %(rhs, lhs) )  
    #print("1:  X is %d, Y is %d " %(i, j) )  
    if lhs > rhs:
        i = i + 1
        j = 1
        #print("2: X is %d, Y is %d " %(i, j) )  
        continue
    if (rhs / lhs) == 1 and ( j > i):
        print(" ##### SOLUTION X is %d, Y is %d " %(i, j) ) 
        break
    j = j + 1
       
    if j == 100:
        i = i + 1
        j = 1
        #print("4: X is %d, Y is %d " %(i, j) )
		
