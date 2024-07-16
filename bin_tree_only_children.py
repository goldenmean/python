'''
Given the reference to the root of a binary tree, return a list containing all the 
“only children”’s values. An “only child” is a node that is the sole node under its
parent node.
Note: The root node is not be considered an only child.

Ex: Given the following root…

        1
      /   \
     2     4
       \
        7, return [7].
Ex: Given the following root…

        1
      /   \
     2     3 return [].

'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findOnlyChildren(root):    
    if not root:
        return []
    
    only_children = []
    
    def dfs(node):
        if not node:
            return
        if node.left and not node.right:
            only_children.append(node.left.val)
        if node.right and not node.left:
            only_children.append(node.right.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return only_children

#Example code

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(7)

print(findOnlyChildren(root))