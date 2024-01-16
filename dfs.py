
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Pre-Order Depth First searct traversal of a binary tree
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
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(bfs(root))  # Pre-Order DFS traversal(Ro,L,Ri): 1, 2, 4, 5, 3, 6
                  # In-order DFS traversal output(L,Ro,Ri): 4, 2, 5, 1, 3, 6
				  # Post-order DFS traversal output(L,Ri,Ro): 4, 5, 2, 6, 3, 1 
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.left.right.left.left = Node(10)
root.left.right.left.right = Node(11)
root.left.right.right.right = Node(12)
root.right.right = Node(13)
root.right.right.right = Node(14)

print(bfs(root))