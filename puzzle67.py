"""
In a new office, each person has their own telephone extension consisting of 3 digits, but not all extensions
 are in use. To try to prevent wrong numbers, no used numbers can be converted to another number just by swapping
 two of the digits. What is the largest possible number of extensions in use in the office?
"""


# def rotl(string, n):
    # return string[n:] + string[:n]

from itertools import permutations

inp = 100
#inp = 999
allowednum = []
bannednum = []

def swap01(string):
    res = string[1]+string[0]+string[2]
    #if string[1] != '0' and int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
    if int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
        bannednum.append(int(res))
        

def swap02(string):
    res = string[2]+string[1]+string[0]
    #if string[2] != '0' and int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
    if int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
        bannednum.append(int(res))

def swap12(string):
    res = string[0]+string[2]+string[1]
    #if string[0] != '0' and int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
    if int(string) != int(res) and int(res) not in bannednum and int(string) not in bannednum:
        bannednum.append(int(res))

# swap01(str(inp))
# swap02(str(inp))
# swap12(str(inp))

# while inp < 1000:
    # if inp not in bannednum:
        # swap01(str(inp))
        # swap02(str(inp))
        # swap12(str(inp))
        # allowednum.append(inp)        

while inp < 1000:
    #if inp not in bannednum:
    swap01(str(inp))
    swap02(str(inp))
    swap12(str(inp))
    if inp not in bannednum:
        allowednum.append(inp)
    inp = inp + 1
    #inp = inp - 1

print("Allowed numbers = %d" %(len(allowednum)) )   
print(sorted(allowednum)) 
print("Banned numbers = %d" %(len(bannednum)) )
print(sorted(bannednum))

# firstallowed = []

# # #Check if banner number list is greater, use that list as allowed numbers , Since we want maximum possible numbers
# # if len(bannednum) > len(allowednum):
    # # print("Bannednum list greater than Allowednum list")
    # # firstallowed = sorted(bannednum)
# # else:
    # # print("Allowednum list greater than Bannednum list")
    # # firstallowed = sorted(allowednum)

# firstallowed = sorted(allowednum)    
# bannednum = []
# allowednum = []
# print(bannednum)
# print(allowednum)
# print(firstallowed)
    
# for n in firstallowed:
    # if n not in bannednum: 
        # swap01(str(n))
        # swap02(str(n))
        # swap12(str(n))
        # allowednum.append(n)  
  
# print("Allowed numbers = %d" %(len(allowednum)) )   
# print(sorted(allowednum)) 
# print("Banned numbers = %d" %(len(bannednum)) )
# print(sorted(bannednum))