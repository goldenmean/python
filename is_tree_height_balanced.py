
'''
Given a binary tree, determine whether or not it is height-balanced.
A height-balanced binary tree can be defined as one in which the heights of
the two subtrees of any node never differ by more than one.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_balance(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)
        
        balanced = (left_balanced and right_balanced and 
                    abs(left_height - right_height) <= 1)
        
        return max(left_height, right_height) + 1, balanced
    
    _, is_tree_balanced = check_balance(root)
    return is_tree_balanced

# Test the function
# Balanced tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(is_balanced(root1))  # Should print True

# Unbalanced tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)

print(is_balanced(root2)) 

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.left.left.left = TreeNode(6)
root1.left.left.right = TreeNode(7)

print(is_balanced(root1)) 