"""
Isolated conundrum #181

Miko always remembers his four-digit PIN because
•	It is a perfect square, and
•	It has the property that, when it is divided by 2, or 3, or 4, or 5, or 6, or 7, or 8, or 9, there is always a remainder of 1.
What is Miko’s PIN?

"""

i = 30

while True:
    sqr = i**2
    if len(str(sqr)) == 4:
        print(sqr)
    elif len(str(sqr)) > 4:
        break;

    i += 1

