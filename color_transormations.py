
'''
On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.
Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
'''

"""
In the solution below
The conversion from list to tuple is essential for two key reasons:

Hashability:
Tuples are hashable in Python while lists are not
A hashable object can be used as a dictionary key or added to a set
The object's hash value never changes during its lifetime
Tuples are immutable (can't be modified after creation), which makes them hashable
Lists are mutable (can be modified), which makes them non-hashable
Memoization with @lru_cache:
The @lru_cache decorator internally uses a dictionary to store previous function calls and their results
Dictionary keys must be hashable
When our function gets called with the same input again, it looks up the cached result instead of recalculating
This dramatically improves performance by avoiding redundant calculations
"""

from functools import lru_cache

def min_remaining_quxes(quxes):
    # Convert list to tuple for hashability in memoization
    quxes = tuple(quxes)
    
    @lru_cache(maxsize=None)
    def transform(current_quxes): #curent_quxes is a tuple of colors 
        if len(current_quxes) <= 1:
            return len(current_quxes)
        # to start with set the minimum possible to the length of the current quxes   
        min_quxes = len(current_quxes)
        
        # Try all possible adjacent pairs
        for i in range(len(current_quxes) - 1): #i takes values until len - 2 as we use i+1 and i+2
            # get the two adjacent colors 
            q1, q2 = current_quxes[i], current_quxes[i + 1]
            
            # Skip if colors are the same, cannot combine, so skip
            if q1 == q2:
                continue
                
            # Get the third color
            third_color = get_third_color(q1, q2)
            
            # Create new arrangement after combining of two different colors
            new_arrangement = current_quxes[:i] + (third_color,) + current_quxes[i+2:]
            
            # Recursively try this new arrangement to transform() and get the result
            # update the min_quxes if the result is less than the current min_quxes            
            result = transform(new_arrangement)
            min_quxes = min(min_quxes, result)
            
        return min_quxes
    
    return transform(quxes)

def get_third_color(c1, c2):
    colors = {'R', 'G', 'B'}
    colors.remove(c1)
    colors.remove(c2)
    return colors.pop()

# Test cases
def test_qux_transformer():
    test_cases = [
        ['R', 'G', 'B', 'G', 'B'],
        ['R', 'G', 'B'],
        ['R', 'R', 'G', 'B', 'B'],
        ['G', 'G', 'B', 'G', 'B', 'R'],
        ['R', 'R', 'R']
    ]
    
    for case in test_cases:
        result = min_remaining_quxes(case)
        print(f"Input: {case}")
        print(f"Minimum remaining Quxes: {result}\n")

if __name__ == "__main__":
    test_qux_transformer()