'''Reverse in-order traversal of a binary search tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseInOrderTraversal(root):
    if root is None:
        return
    
    # Visit right subtree
    reverseInOrderTraversal(root.right)
    
    # Visit root node
    print(root.val, end=' ')
    
    # Visit left subtree
    reverseInOrderTraversal(root.left)

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print("Reverse In-Order Traversal:")
reverseInOrderTraversal(root)