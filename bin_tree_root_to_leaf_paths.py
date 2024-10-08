


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    def construct_paths(node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:  # if leaf node
                paths.append(path)  # add path to result
            else:
                path += '->'  # extend the current path
                construct_paths(node.left, path)
                construct_paths(node.right, path)

    paths = []
    construct_paths(root, "")
    return paths

# Example usage:
# Construct a binary tree:
#     1
#    / \
#   2   3
#    \
#     5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binaryTreePaths(root)) 
