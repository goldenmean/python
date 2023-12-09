"""
Isolated conundrum #175

The number N is the product of the first 99 positive integers. The number M is the product of the first 99 positive integers after each has been reversed. That is, for example, the reverse of 8 is 8; of 17 is 71; of 20 is 02. 
What is the exact value of N÷M?

"""



prodnumr = 1
proddenr = 1
v1 = 2

while v1 <= 99:
    prodnumr = prodnumr * v1
    
    strnum = str(v1)
    v2 = int(strnum[::-1])
    proddenr = proddenr * v2
    v1 = v1 + 1    

print("Answer = %d " %(prodnumr/proddenr))