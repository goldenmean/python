'''
You are given a starting state start, a list of transition probabilities for a Markov chain, 
and a number of steps num_steps. Run the Markov chain starting from start for num_steps and
compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition
probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }

'''
import random
def markov_chain(start, trans_probs, num_steps):
    # Convert transition probabilities list to a dictionary of dictionaries for easier access
    trans_dict = {}
    for src, dst, prob in trans_probs:
        if src not in trans_dict:
            trans_dict[src] = {}
        trans_dict[src][dst] = prob

    # Initialize state visit count dictionary
    state_counts = {state: 0 for state, _, _ in trans_probs}
    state_counts[start] += 1  # Count the initial state

    # Run the Markov chain
    current_state = start
    for _ in range(num_steps - 1):  # Adjust for the initial state count
        next_state = random.choices(
            population=list(trans_dict[current_state].keys()),
            weights=list(trans_dict[current_state].values())            
        )[0]
        state_counts[next_state] += 1
        current_state = next_state

    return state_counts

start = 'a'
transition_probs = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

'''
transition_probs = {
    'a': {'a': 0.9, 'b': 0.075, 'c': 0.025},
    'b': {'a': 0.15, 'b': 0.8, 'c': 0.05},
    'c': {'a': 0.25, 'b': 0.25, 'c': 0.5}
}
'''

num_steps = 5000        
print(markov_chain(start, transition_probs, num_steps))     

