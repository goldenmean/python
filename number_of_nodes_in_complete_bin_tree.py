
'''
Given a complete binary tree, count the number of nodes in faster than O(n) time.
Recall that a complete binary tree has every level filled except the last, and the
nodes in the last level are filled starting from the left.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compute_tree_height(node):
    height = 0
    while node:
        height += 1
        node = node.left
    return height

def count_nodes(root):
    if not root:
        return 0
    
    left_height = compute_tree_height(root.left)
    right_height = compute_tree_height(root.right)
    print(f"Left height: {left_height}, Right height: {right_height}")
    
    if left_height == right_height:
        # Left subtree is a perfect binary tree
        print("Left height is equal to right height")
        return (1 << left_height) + count_nodes(root.right)
    else:
        # Right subtree is a perfect binary tree
        return (1 << right_height) + count_nodes(root.left)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Number of nodes:", count_nodes(root)) 

