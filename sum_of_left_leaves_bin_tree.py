
# Return the sum of only left leaves of a binary tree
# Given a binary tree, return the sum of all left leaves of the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_left_leaves(root):
    def is_leaf(node):
        return node and not node.left and not node.right
    
    def dfs(node, is_left):
        if not node:
            return 0
            
        # If current node is a left leaf, add its value
        if is_leaf(node) and is_left:
            return node.val
            
        # Recursively process left and right subtrees
        left_sum = dfs(node.left, True)
        right_sum = dfs(node.right, False)
        
        return left_sum + right_sum
    
    return dfs(root, False)


# root1 = TreeNode(5)
# root1.left = TreeNode(2)
# root1.right = TreeNode(12)
# root1.right.left = TreeNode(3)
# root1.right.right = TreeNode(8)

root1 = TreeNode(5)
root1.left = TreeNode(2)
root1.right = TreeNode(12)
root1.right.left = TreeNode(3)
root1.right.left.left = TreeNode(6)
root1.right.left.rightt = TreeNode(7)
root1.right.right = TreeNode(8)

print(sum_left_leaves(root1))  # Output: 5