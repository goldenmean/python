"""
12345 can be expressed as the sum of two primes in exactly one way. What is the larger of the two primes?
Algorithm:

"""

def check_if_num_is_prime(num):
# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               #print(num,"is not a prime number")
               #print(i,"times",num//i,"is",num)
               #break
               return False
       else:
           #print(num,"is a prime number")
           return True
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       #print(num,"is not a prime number")
       return False
       
   
num = 12345
cntnum = 2
checknum = num - cntnum
#check_if_num_is_prime(num)
largestPrime = -9999

while checknum != 0:
    
    isChecknumPrime = check_if_num_is_prime(checknum)
    iscntNumPrime = check_if_num_is_prime(cntnum)
    if isChecknumPrime and iscntNumPrime:
        if checknum > largestPrime:
            largestPrime = 	checknum	
            print(" Largest prime number is %d , smaller prime number is %d, Sum = %d " %(largestPrime, cntnum, (checknum+cntnum)))
    
    cntnum = cntnum + 1
    checknum = num - cntnum
        