"""
There are N couples sitting in a row of length 2 * N. They are currently ordered randomly,
but would like to rearrange themselves so that each couple's partners can sit side by side.
What is the minimum number of swaps necessary for this to happen.

e.g. consider arrangement as below where number is a couple and the letter 'a' is a husband 
and letter 'b' is the wife
So for initial random arrangement: 1a 2b 2a 1b
we can get to 1a 1b 2a 2b in exactly one swap.
"""


def min_swaps_for_couples(arrangement):
    n = len(arrangement) // 2  # Number of couples
    position = {}
    partner = {}
    swaps_needed = 0

    # Create dictionaries to store the position and partner of each person
    for i, person in enumerate(arrangement):
        position[person] = i
        couple_id = person[0]
        if couple_id not in partner:
            partner[couple_id] = person
        else:
            partner[person] = partner[couple_id]
            partner[partner[couple_id]] = person

    for i in range(0, len(arrangement), 2):
        person = arrangement[i]
        if position[partner[person]] != i + 1:
            swaps_needed += 1
            
            # Update the position of the swapped person
            swapped_person = arrangement[i + 1]
            arrangement[position[partner[person]]] = swapped_person
            position[swapped_person] = position[partner[person]]

    return swaps_needed


# Test the function
test_cases = [
    #['1a', '2b', '2a', '1b'],
    #['1a', '1b', '2a', '2b'],
    #['1a', '2a', '3a', '1b', '2b', '3b'],
    #['1a', '2b', '3c', '4a', '1b', '2c', '3a', '4b']
    ['1a', '2c', '1b', '4b', '3a', '2b', '3c', '4a']
]

for case in test_cases:
    print(f"Arrangement: {case}")
    print(f"Minimum swaps: {min_swaps_for_couples(case)}")
    print()