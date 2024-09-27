r"""
A full binary tree is one in which every node except leaf nodes, has 2 child nodes.
# Given this tree:
#     1
#    / \ 
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \ 
#   0   3
#      / \
#     9   4

"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_to_full_binary_tree(node):
    if node is None:
        return None

    # Recursively convert left and right subtrees
    node.left = convert_to_full_binary_tree(node.left)
    node.right = convert_to_full_binary_tree(node.right)

    # If the node is a leaf or has two children, keep it
    if (node.left and node.right) or (node.left is None and node.right is None):
        return node

    # If the node has only one child, replace it with its child
    return node.left if node.left else node.right

def inorder_traversal(root):    
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(0)
root.right.left = TreeNode(9)
root.right.right = TreeNode(4)

# Convert to full binary tree
root = convert_to_full_binary_tree(root)

# Print the inorder traversal of the modified tree
print("Inorder traversal of output tree:")
inorder_traversal(root)