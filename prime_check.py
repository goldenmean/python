def check_if_num_is_prime(num):
# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               #print(i,"times",num//i,"is",num)
               #break
               return False
       else:
           print(num,"is a prime number")
           return True
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")
       return False
	   
num = 12342 
isprime = check_if_num_is_prime(num)
print(isprime)