import random

"""
The sum of 10 distinct positive integers is 100. What is the largest possible value of any of the 10 integers?
"""

""" 
Usefule URLS:
https://stackoverflow.com/questions/16655089/python-random-numbers-into-a-list
"""
#Python3 installation folder location:
#C:\Users\ajitd\AppData\Local\Programs\Python\Python37\



a = [0]*10
suma = 0
agblmax = -999

while suma != 100:
    a =random.sample(range(1,52), 10)
    if max(a) <= agblmax:
        continue
    suma = sum(a)
    if suma == 100:
        maxa = max(a)
        if maxa > agblmax:
            agblmax = maxa
            print(f"Maximum value of a is %d " %(agblmax) )
            print("All the integers are ",a)
        suma = 0

