'''
https://www.interviewquery.com/questions/nightly-job?solution=true&utm_medium=email&utm_source=weekly_question 
Every night between 7 pm and midnight, two computing jobs from two different sources are 
randomly started with each one lasting an hour.

Unfortunately, when the jobs simultaneously run, they cause a failure in some of the company’s
 other nightly jobs, resulting in downtime for the company that costs $1000. 

The CEO, who has enough time today to hear one word, needs a single number representing the
 annual (365 days) cost of this problem.

Note: Write a function to simulate this problem and output an estimated cost 

Bonus - How would you solve this using probability?

'''

#Solution
'''
We can model out this scenario by implementing two random number generators across a 
spectrum from 0 to 300 minutes, modeling the time in minutes between 7 pm and midnight.

We can simulate this scenario some N number of times to get an approximation of the 
probability that overlap will occur between the two processes. Looping through the 
simulation N number of times, we can generate two random numbers and check to see if 
they overlap and append the values 1 or 0 to our array.

Then at the end, we just take the mean to get the simulated probabilities.
'''

import random
import numpy as np

# Simulate_overlap( ) returns the probability of overlap on a given single day
def simulate_overlap(n=365):
    times = []
    for i in range(0, n):
        first_process = random.randint(0,300)
        second_process = random.randint(0,300)
        overlap = 0
        fi = (second_process > first_process and second_process <= first_process + 60)
        si = (first_process > second_process and first_process <= second_process + 60)
        if fi or si:
            overlap = 1
        times.append(overlap)

    return np.mean(times)

overlap_percentage = simulate_overlap(1000)
print(overlap_percentage)
cost = overlap_percentage * 365 * 1000  

print(cost)