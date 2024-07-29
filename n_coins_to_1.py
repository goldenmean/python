'''
You have n fair coins and you flip them all at the same time. Any that come up 
tails you set aside. The ones that come up heads you flip again. How many rounds
do you expect to play before only one coin remains?
Write a function that, given n, returns the number of rounds you'd expect to play
until one coin remains.
'''

# Simple solution - One each flip on average half the coins will be heads, other we keep aside as tails.
# So every toss the available coins get halved so ans is log2(number of coins at start)
import math

def expected_rounds_formula(n):
    if n <= 1:
        return 0
    else:
        #return math.ceil(math.log2(n))
        return math.log2(n)

# Example usage
n = 10
print("Expected number of rounds:", expected_rounds_formula(n))



# This solution is based on the expected number of rounds until one coin remains
# This uses multiple simulations to estimate the expected number of rounds
import random

def expected_rounds(n):
    # Number of simulations to average over
    num_simulations = 10000
    
    total_rounds = 0
    
    for _ in range(num_simulations):
        coins_left = n
        rounds = 0
        
        while coins_left > 1:
            # Flip all remaining coins
            heads = sum(1 for _ in range(coins_left) if random.choice([True, False]))
            
            # Update the number of coins left
            coins_left = heads
            
            # Increment the round counter
            rounds += 1
        
        total_rounds += rounds
    
    # Return the average number of rounds over all simulations
    return total_rounds / num_simulations

# Example usage
n = 10  # Start with 10 coins
print(f"Expected rounds until one coin remains: {expected_rounds(n)}")



