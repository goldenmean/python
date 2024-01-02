
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#PRe-Order Depth First searct traversal of a binary tree
def bfs(root):
    if root is None:
        return []
		
    queue = []
    queue.append(root)
    result = []

    while queue:
        node = queue.pop()
        result.append(node.value)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        

    return result

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(bfs(root))  # Output: 