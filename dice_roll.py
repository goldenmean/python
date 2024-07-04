
'''
Alice wants to join her school's Probability Student Club. Membership dues are computed via
one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. 
Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to
simulate the two games and calculate their expected value.
'''



import random

def simulate_game(stop_condition):
    rolls = 0
    prev_roll = 0
    
    while True:
        rolls += 1
        current_roll = random.randint(1, 6)
        
        if prev_roll == 5 and current_roll == stop_condition:
            return rolls
        
        prev_roll = current_roll

def calculate_expected_value(stop_condition, num_simulations=10000):
    total_rolls = sum(simulate_game(stop_condition) for _ in range(num_simulations))
    if stop_condition == 6:
        print(f"Total rolls for Game 1: {total_rolls}")
    else:
        print(f"Total rolls for Game 2: {total_rolls}")
    return total_rolls / num_simulations

# Simulate both games

ev_game1 = calculate_expected_value(6)
ev_game2 = calculate_expected_value(5)

print(f"Expected value for Game 1 (5 then 6): ${ev_game1:.2f}")
print(f"Expected value for Game 2 (5 then 5): ${ev_game2:.2f}")

if ev_game1 < ev_game2:
    print("Alice should choose Game 1 (5 then 6)")
elif ev_game2 < ev_game1:
    print("Alice should choose Game 2 (5 then 5)")
else:
    print("Both games have the same expected value")