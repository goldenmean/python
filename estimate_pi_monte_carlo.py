'''
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

# Estimate value of Pi using Monte Carlo method
# Area of Circle / Area of circumscribed Square = pi*r^2 / 4*r^2 = pi / 4 
# So generate many random points , see if they fall within circle or not . points in circle/total points = pi/4

import random
import math

def estimate_pi(n_points):
    inside_circle_count = 0
    
    for _ in range(n_points):
        x = random.uniform(-1, 1)  # Random x coordinate
        y = random.uniform(-1, 1)  # Random y coordinate
        
        distance_from_origin = math.sqrt(x**2 + y**2)
        
        if distance_from_origin <= 1:
            inside_circle_count += 1
            
    pi_estimate = 4 * inside_circle_count / n_points
    #return round(pi_estimate, 3)
    return pi_estimate

# Estimate pi using 1 million random points
n_points = 1000
pi_estimate = estimate_pi(n_points)
print(f"Estimated value of π: {pi_estimate}")

