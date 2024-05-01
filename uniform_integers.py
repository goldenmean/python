'''
https://www.metacareers.com/profile/coding_puzzles?puzzle=228269118726856
Find Number of uniform integers: 

Sample test case #1
A = 75
B = 300
Expected Return Value = 5

Sample test case #2
A = 1
B = 9
Expected Return Value = 9

Sample test case #3
A = 999999999999
B = 999999999999
Expected Return Value = 1
'''

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    uniformints=0
    for num in range(A,B+1):
        snum=str(num)
        if snum.count(snum[0]) == len(snum):
            uniformints+=1
    
    return uniformints   


#Below solution gave Time Limite Exceeded error for 12 test cases :(
'''
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    uniformints=0
    for num in range(A,B+1):
        digits=set()
        first=True
        breakhit=False        
        while num:
            #print(f"num is {num}")
            if first==True:
                digit=num % 10
                num//=10
                first=False
                #print(f"1st digit is {digit}")
                continue
            
            if first == False:
                if num % 10 != digit:
                    breakhit=True
                    break   
                #print(f"num %10 is {num %10}")
                num//=10
        if breakhit != True:
            uniformints+=1
        #print(f"uniform numbers is {uniformints}")
    return uniformints

    '''
            
A = 75; B = 300
#A=4; B=20
#A = 999999999997; B = 999999999998

print(getUniformIntegerCountInInterval(A,B))
                
            
        