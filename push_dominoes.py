'''
Leetcode: 838 Push dominoes
Given a string with the initial condition of dominoes, where:'.' represents that the domino is 
standing still 'L' represents that the domino is falling to the left side 'R' represents that 
the domino is falling to the right sideFigure out the final position of the dominoes. 
If there are dominoes that get pushed on both ends, the force cancels out and that domino 
remains upright.Input:  ..R...L..R.Output: ..RR.LL..RR

'''


def push_dominoes(dominoes: str) -> str:
    n = len(dominoes)
    forces = [0] * n

    # First pass: handle 'R' dominoes
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n  # A large number to simulate infinite force
        elif dominoes[i] == 'L':
            force = 0  # Reset force when encountering 'L'
        else:
            force = max(0, force - 1)  # Decrease force over distance

        forces[i] += force
    print(forces)

    # Second pass: handle 'L' dominoes
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n  # A large number to simulate infinite force
        elif dominoes[i] == 'R':
            force = 0  # Reset force when encountering 'R'
        else:
            force = max(0, force - 1)  # Decrease force over distance

        forces[i] -= force
    print(forces)

    # Build the final result based on the forces
    result = []
    for f in forces:
        if f > 0:
            result.append('R')
        elif f < 0:
            result.append('L')
        else:
            result.append('.')

    return ''.join(result)


# Example usage
input_dominoes = "..R...L..R."
output_dominoes = push_dominoes(input_dominoes)
print(output_dominoes)  # Output: ..RR.LL..RR