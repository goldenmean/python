

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_binary_tree_boring(root):
    #If the tree is empty, it is boring
    if root is None:
        return True
    #If a Node has no substrees, it is a boring binary tree
    if root.left is None and root.right is None:
        return True
    #If a Node has both substrees , then check each subtree
    if root.left is not None and root.right is not None:
        if root.val == root.left.val and root.val == root.right.val:
            return is_binary_tree_boring(root.left) and is_binary_tree_boring(root.right)
        else:
            return False
    #If a Node has only one subtree: left substree
    if root.left is not None:
        if root.val == root.left.val:
            return is_binary_tree_boring(root.left)
        else:
            return False
    #If a Node has only one subtree: right substree
    if root.right is not None:
        if root.val == root.right.val:
            return is_binary_tree_boring(root.right)
        else:
            return False
        

#root = TreeNode(7, TreeNode(7), TreeNode(7))
#root = TreeNode(8, None, TreeNode(8, None, TreeNode(8, None, TreeNode(8))))
#root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(5, None, TreeNode(5, None, TreeNode(5, TreeNode(5), TreeNode(5))))

print(is_binary_tree_boring(root))
