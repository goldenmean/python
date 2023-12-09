"""
Isolated conundrum #272

A postman’s sack contains five letters, one each for the five houses in Cayley Close. Mischievously, he posts one letter
 through each door without looking to see if it is the correct address. In how many different ways could he do this so 
 that exactly two of the five houses receive the correct letters?
"""

#import snoop 
from itertools import permutations
import time
import timeit

#@snoop
def puzzle272(letter):
    print(f"Inside function puzzle272 ")
    a = permutations(letter,5)
    numlist = [("".join(x)) for x in a]
    cor_letters = 0
    correct = 0
    for i in numlist:
        if i[0] == '1':
            correct += 1
        if i[1] == '2':
            correct += 1
        if i[2] == '3':
            correct += 1
        if i[3] == '4':
            correct += 1
        if i[4] == '5':
            correct += 1

        if correct == 2:
           cor_letters += 1
        
        correct = 0

    print(f"Correct number of letters to exact two houses is {cor_letters}")
    #print(cor_letters)
       
letter = "12345"
t1=time.time()
#starttime = timeit.default_timer()
puzzle272(letter)
print(f"time elapsed in executing Function puzzle272 is {time.time() - t1}" )
#print(f"timeit number elapsed in executing Function puzzle272 is {timeit.default_timer() - starttime}" )

