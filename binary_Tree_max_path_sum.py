
r'''
You are given the root of a binary tree. Find the path between 2 nodes that 
maximizes the sum of all the nodes in the path, and return the sum. 
The path does not necessarily need to go through the root
For given binary tree, the maximum path sum is 42
 (* denotes the max path)
       *10
       /  \
     *2   *10
     / \     \
   *20  1    -25
             /  \
            3    4

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    max_sum = float('-inf')
    
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        
        left_subtree_sum = max(max_gain(node.left), 0)
        right_subtree_sum = max(max_gain(node.right), 0)

        curr_max_sum = node.val + left_subtree_sum + right_subtree_sum
        max_sum = max(max_sum, curr_max_sum)

        return node.val + max(left_subtree_sum, right_subtree_sum)
    
    max_gain(root)
    return max_sum

# Example code

root = TreeNode(-10)
root.left = TreeNode(2)
root.right = TreeNode(10, right=TreeNode(-25, TreeNode(3), TreeNode(4)))
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)

print(max_path_sum(root))








