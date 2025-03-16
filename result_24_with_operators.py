"""
The 24 game is played as follows. You are given a list of four integers, 
each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / 
between the numbers, and grouping them with parentheses, determine whether it
is possible to reach the value 24.
"""
from itertools import permutations, product

def evaluate(a, b, operator):
    if operator == '+': return a + b
    if operator == '-': return a - b
    if operator == '*': return a * b
    if operator == '/' and b != 0: return a / b
    return None

def solve_24_game(nums):
    operators = ['+', '-', '*', '/']
    
    for nums_perm in permutations(nums):
        for ops in product(operators, repeat=3):
            a, b, c, d = nums_perm
            
            # Pattern 1: ((a op1 b) op2 c) op3 d
            result1 = evaluate(a, b, ops[0])
            if result1 is not None:
                result2 = evaluate(result1, c, ops[1])
                if result2 is not None:
                    final = evaluate(result2, d, ops[2])
                    if final is not None and abs(final - 24) < 0.0001:
                        print(f"Solution 1: (({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d}")
                        return True

            # Pattern 2: (a op1 b) op2 (c op3 d)
            result1 = evaluate(a, b, ops[0])
            result2 = evaluate(c, d, ops[2])
            if result1 is not None and result2 is not None:
                final = evaluate(result1, result2, ops[1])
                if final is not None and abs(final - 24) < 0.0001:
                    print(f"Solution 2: ({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d})")
                    return True

            # Pattern 3: a op1 (b op2 (c op3 d))
            result1 = evaluate(c, d, ops[2])
            if result1 is not None:
                result2 = evaluate(b, result1, ops[1])
                if result2 is not None:
                    final = evaluate(a, result2, ops[0])
                    if final is not None and abs(final - 24) < 0.0001:
                        print(f"Solution 3: {a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d}))")
                        return True
                    
    return False

# Example usage
test_cases = [
    [5, 2, 7, 8],  # True
    [4, 1, 8, 7],  # True
    [1, 1, 1, 1],  # False
    [24, 24, 24, 24],  # True
]

for test in test_cases:
    print(f"Input {test}: {solve_24_game(test)}")