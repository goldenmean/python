"""Isolated conundrum #97

Zoe was born on her mother’s 24th birthday, so they share birthdays.  Assuming they both live long lives, on how many birthdays
 will Zoe’s age be a factor of her mother’s age?
"""

import math



a = 1 

while True:
    if ((a + 24) % a ) == 0:
        print("Zoe's Age %d is multiple of her mother's " %(a) )
    a = a + 1
	
