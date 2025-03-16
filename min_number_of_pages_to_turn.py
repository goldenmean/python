# Hackerrank problem minimum number of pages needed to tur
# https://www.hackerrank.com/challenges/drawing-book/problem


def min_pages_to_turn(n: int, p: int) -> int:
    # Calculate turns from the front
    front_turns = p // 2
    
    # Calculate turns from the back
    back_turns = (n // 2) - (p // 2)
    
    # Return the minimum of the two
    return min(front_turns, back_turns)

# Example usage
n = 6  # total number of pages
p = 2  # target page
print(min_pages_to_turn(n, p)) 