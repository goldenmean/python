'''
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binaryTreePaths(root):
    if not root:
        return []
    paths = []
    stack = [(root, str(root.val))]
    print(stack)
    while stack:        
        node, path = stack.pop()
        print(f"path is {path}")
        if not node.left and not node.right:
            print("both left and right are null")
            paths.append(list(map(int, path.split("->"))))
        if node.left:
            print(f"left is not null {node.left.val}")
            stack.append((node.left, path + "->" + str(node.left.val)))
        if node.right:
            print(f"right is not null {node.right.val}")
            stack.append((node.right, path + "->" + str(node.right.val)))
    return paths

# Create the binary tree from the problem statement
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Print all paths from the root to leaves
print(binaryTreePaths(root))
