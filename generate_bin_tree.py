

import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate():
    def generate_node():
        value = random.randint(0, 100)
        left = (yield) if random.random() > 0.5 else None
        right = (yield) if random.random() > 0.5 else None
        return Node(value, left, right)

    gen = generate_node()
    next(gen)  # Prime the generator
    return gen.send(None)

# Example usage
root = generate()
print(root.value)


