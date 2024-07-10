'''
Given a number n, return a list containing specific outputs for each value 
between one and n. For any number, if it is divisible by three and it is 
divisible by five, append “FizzBuzz” to your list. If it is divisible by only three, append “Fizz” to your list.
If it is divisible by only five, append “Buzz” to your list. If the number is not divisible by three or five,
simply append the number itself to the list.

Ex: Given the following value n…

n = 3, return ["1","2","Fizz"].
Ex: Given the following value n…

n = 5, return ["1","2","Fizz","4","Buzz"].
'''

def fizzbuzz(n):
    res = []
    
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

n=25

print(fizzbuzz(n))            
              
    