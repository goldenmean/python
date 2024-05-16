

'''
countsay(1)="1" is the base case always
countsay(n) = the string represenation of way you would say the digit string in countsay(n-1)

Given n , we have to apply this recurrence relation until n=4 and then return that digit representation as result

'''

def looksay(N):
    if N < 0: return ""
    res = "1"
    if N == 1: return res
    
    def helper(strng):
        temp = ""
        count = 1
        slen = len(strng)
        #print(f"slen is {slen}")
        for i in range(slen):
            if i == slen-1 or strng[i] != strng[i+1]:                
                temp += str(count)+strng[i]
                count=1
                #print(f"inside if i is {i}, strng[i] is {strng[i]}, count is {count}, temp is {temp} ")
            else:
                count+=1
                #print(f"inside else i is {i}, strng[i] is {strng[i]}, count is {count} ")
        return temp

    for j in range(2,N+1):
        #print(f"Before: helper res is {res}")
        res = helper(res)
       # print(res)
   
    return res
    
            

N=7
print(looksay(N))



    

    
