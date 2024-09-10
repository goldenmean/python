'''
You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.
e.g. for below binary tree, return answer as 7,4,9
       5
      / \
     6   7
    /   / \
  2   4   9

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root):
    def helper(node):
        if not node:
            return (0, float('inf'), float('-inf'), None)  # size, min, max, subtree
        #dfs approach to find size of left and right subtree and check if current node is valid bst 
        left_size, left_min, left_max, left_subtree = helper(node.left)
        right_size, right_min, right_max, right_subtree = helper(node.right)

        if left_max < node.val < right_min:
            size = left_size + right_size + 1
            subtree = node
            print(f"size: {size}, min: {min(left_min, node.val)}, max: {max(right_max, node.val)}")
            return (size, min(left_min, node.val), max(right_max, node.val), subtree)
        else:
            if left_size > right_size:
                #return (left_size, float('-inf'), float('inf'), left_subtree)
                return (left_size, left_min, left_max, left_subtree)
            else:
                #return (right_size, float('-inf'), float('inf'), right_subtree)
                return (right_size, right_min, right_max, right_subtree)
            
    size, _, _, subtree = helper(root)
    return subtree

# Example usage:
# Construct the tree
root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(9)

# Find the largest BST subtree
largest_bst = largestBSTSubtree(root)

# Function to print the subtree in pre-order traversal
def printPreOrder(node):
    if not node:
        return
    print(node.val, end=' ')
    printPreOrder(node.left)
    printPreOrder(node.right)

printPreOrder(largest_bst)  