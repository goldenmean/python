'''
We are given a binary tree. The challenge is to count all the univalued subtrees in the tree.
Just to recall, a subtree is any node along with its descendants. The root and all its 
descendants form the entire tree. A univalued subtree is therefore a subtree in which all the nodes
have the same keys
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def univalued_subtrees(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    if root.left is not None and root.right is not None:
        if root.left.val == root.right.val and root.left.val == root.val:
            return univalued_subtrees(root.left) + univalued_subtrees(root.right) + 1
        else:
            return univalued_subtrees(root.left) + univalued_subtrees(root.right)
        
    if root.left is not None:
        if root.left.val == root.val:
            return univalued_subtrees(root.left) + 1
        else:
            return univalued_subtrees(root.left)
        
    if root.right is not None:
        if root.right.val == root.val:
            return univalued_subtrees(root.right) + 1
        else:
            return univalued_subtrees(root.right)

    

# Example code to test the function
root = TreeNode(9)
root.left = TreeNode(8)
root.right = TreeNode(9)
root.left.left = TreeNode(8)
root.left.right = TreeNode(7)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(7)

print(univalued_subtrees(root))