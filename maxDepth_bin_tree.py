'''
return maximum depth of a binary tree
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right


def maxDepth(root):
    if root is None:
        return 0
    leftd = maxDepth(root.left)
    rightd = maxDepth(root.right)
    print(f"Depth of node {root.val} is {1 + max(leftd, rightd)}")
    return 1 + max(leftd, rightd)


root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.left.left = TreeNode(5) 
root.left.left.right = TreeNode(6)

print(maxDepth(root))
