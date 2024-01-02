class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def diameter(root):
    diameter = [0]
    depth(root, diameter)
    return diameter[0]

def depth(node, diameter):
    if node is None:
        print("Leaf node")   
        return 0
    print(node.value)   
    left_depth = depth(node.left, diameter)
    right_depth = depth(node.right, diameter)

    diameter[0] = max(diameter[0], left_depth + right_depth)
    print(f"left_depth is {left_depth}, right_depth is {right_depth}")
    print(f"diameter[0] is {diameter[0]}, depth is {max(left_depth, right_depth) + 1}")
    return max(left_depth, right_depth) + 1

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))  # Output: 3