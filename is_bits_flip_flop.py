
'''
Given a positive integer N, return whether or not it has alternating bit values.
Ex: Given the following value for N…
N = 5, return true.
5 in binary is 101 which alternates bit values between 0 and 1.

Ex: Given the following value for N…
N = 8, return false
8 in binary is 1000 which does not alternate bit values between 0 and 1.

'''

def check_bits_flip_flop(num):
    numlen=num.bit_length()-1
    mask=0x1
    shft=0
    prevbit=num & mask    
    while numlen!=0:  
        print(f"prevbit is {prevbit}")  
        print(f"shft is {shft}")        
        shft+=1         
        mask=1<<shft
        print(f"shft is {shft}")
        print(f"mask is {hex(mask)}")       
        currbit=(num & mask)>>shft
        print(f"currbit is {currbit}")
        if currbit == prevbit:
            print("Before returning False")     
            return False
            
        numlen-=1
        print(f"numlen is {numlen}")                 
        prevbit=currbit
    
    return True

'''
def check_bits_flip_flop(num):
    
    numlen=8 #Assumed that give num is 32 bit or 8 nibbles(4 bits)
    mask=0x0
    while numlen!=0:
        res=num | mask
        print("res is ",res)    
        #print(f"{res!=0x5}")       
        #print(f"{res!=0xA}")       
        if num !=0 and res!=0x5 and res!=0xA:
            print("Before returning False")     
            return False
        numlen-=1
        num=num>>4
        if num==0: 
            return True
        print("numlen is ",numlen)
        print("num is ",num)    
        
    return True
'''

N=int(input("Enter the number:"))
    
r=check_bits_flip_flop(N)

if r:
    print(f"Number {N} has alternating 0/1 bit values")
else:
    print(f"Number {N} does not have alternating 0/1 bits")