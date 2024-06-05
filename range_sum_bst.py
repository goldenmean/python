'''
Leetcode 938. Range Sum of BST https://leetcode.com/problems/range-sum-of-bst/description/

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def rangeSumBST( root: Optional[TreeNode], low: int, high: int) -> int:
    tot = 0
    #pre order traversal of binary tree

    def preorder(root):
        if root is None:
            return 
        
        nonlocal tot
        if low <= root.val <= high:
            tot += root.val
        
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return tot



