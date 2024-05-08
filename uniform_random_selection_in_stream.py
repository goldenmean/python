'''
https://www.interviewquery.com/questions/random-number

Given a stream of numbers, select a random number from the stream with equal probability and 
O(1) space in selection.

Input:

def random_number(x, y=0, count=1):
    pass
x is the new value from the stream.
y is the previously selected value.
count is the size of the stream.

Proof that the below code always generates uniform random numer: 

Say a stream size is 6 currently (i.e. 6th input value has been received)
So random.randrange will generate a random number between 0,1,2,3,4,5
if it is 5 select 
res = x (new input) probability of this would be 1/6
else
if the value that was selected in previous input iteration in stream is now selected, then probability of
that is is 
5/6 * 1/5 = 1/6
explanation:
5/6 is the probability that the previous value is selected in the 6th input in the stream 
and 1/5 was the probability that in the previous 5th input that 5th value was selected as output 
So total probability that the 5th value is selected as output in the 6th input iteration, is 
5/6*1/5 = 1/6 which is still uniform probability for 6 values in the stream so far

'''


import random

# A function to randomly select an item 
# from stream[0], stream[1], .. stream[i-1] 
def random_number(x, y=0, count=1):
    # x is the new value
    # y is the old value, default 0
    
    # If this is the first element 
    # from stream, return it 
    if (count == 1): 
        res = x; 
    else: 
        
        # Generate a random number between 0 to count - 1 (inclusive)
        rnd = random.randrange(count); 

        # Replace the prev random number 
        # with new number with 1/count 
        # probability 
        if (rnd == count - 1): 
            res = x
        else: 
            res = y
            
    return res