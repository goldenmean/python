"""
Isolated conundrum #180

Consider the sequence 5,55,555,5555,55555,… Are any of the numbers in this sequence divisible by 495; if so, what is the smallest such number?
"""

num = 5

while True:
    if (num % 495) == 0:
        print(num)
        print("quotient is %d " %(num/495))
        break
    num = int(str(num)+'5')
