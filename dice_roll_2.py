
import random

def roll_die():
    """Simulate a roll of a die."""
    return random.randint(1, 6)

def simulate_game(condition):
    """
    Simulate one game based on the given condition.
    
    :param condition: A tuple specifying the stopping condition (e.g., (5, 6) for the first game)
    :return: Number of rolls made in the game
    """
    rolls = 0
    last_roll = None
    
    while True:
        roll = roll_die()
        rolls += 1
        if last_roll == condition[0] and roll == condition[1]:
            break
        last_roll = roll
    
    return rolls

# Parameters for the simulations
num_simulations = 1000000
game_conditions = [(5, 6), (5, 5)]  # Conditions for the two games

# Initialize counters
total_rolls_first_game = 0
total_rolls_second_game = 0

for _ in range(num_simulations):
    # Simulate the first game
    num_rolls = simulate_game(game_conditions[0])
    total_rolls_first_game += num_rolls
    
    # Simulate the second game
    num_rolls = simulate_game(game_conditions[1])
    total_rolls_second_game += num_rolls

# Calculate the average number of rolls for each game
avg_rolls_first_game = total_rolls_first_game / num_simulations
avg_rolls_second_game = total_rolls_second_game / num_simulations
print(f"Total rolls for Game 1: {total_rolls_first_game}")
print(f"Total rolls for Game 2: {total_rolls_second_game}")
print(f"Average number of rolls for the first game: {avg_rolls_first_game:.2f}")
print(f"Average number of rolls for the second game: {avg_rolls_second_game:.2f}")

# Expected value calculation (assuming the cost is the number of rolls)
expected_value_first_game = avg_rolls_first_game * 1  # Cost is $1 per roll
expected_value_second_game = avg_rolls_second_game * 1  # Cost is $1 per roll

print(f"Expected value for the first game {game_conditions[0]}: ${expected_value_first_game:.2f}")
print(f"Expected value for the second game {game_conditions[1]}: ${expected_value_second_game:.2f}")