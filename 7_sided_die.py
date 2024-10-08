"""
https://www.interviewcake.com/question/python/simulate-7-sided-die
Simulate a 7 sided die, given a 5 sided die
"""
import random
def rand5():
    return random.randint(1,5)
    

def rand7_table():
    results = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0],
    ]

    while True:
        # Do our die rolls
        row = rand5() - 1
        column = rand5() - 1

        # Case: we hit an extraneous outcome
        # so we need to re-roll
        if row == 4 and column > 0:
            continue

        # Our outcome was fine. return it!
        return results[row][column]