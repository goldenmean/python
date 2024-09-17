
r"""
Given the root of a binary tree that contains only unique values, and two tree values x and y, return whether or not the nodes containing values x and y are cousins.
Note: Two nodes in a tree are cousins if they have the same depth but different parents.

Ex: Given the following root, x, and y…
      1
    /   \
   2     3, x = 2, y = 3, return false (2 and 3 are on the same level but have the same parent).
Ex: Given the following root, x, and y…
      5
    /   \
   3     2
  / \   / \
 4  7  9   8, x = 8, y = 4, return true.

 """

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_bin_tree_nodes_cousins(root, x, y):
    if not root:
        return False

    def dfs(node, parent, depth, val, result):
        if not node:
            return
        if node.val == val:
            result.extend([parent, depth])
            return
        dfs(node.left, node, depth + 1, val, result)
        dfs(node.right, node, depth + 1, val, result)

    x_info = []
    y_info = []
    dfs(root, None, 1, x, x_info)
    dfs(root, None, 1, y, y_info)

    return x_info[1] == y_info[1] and x_info[0] != y_info[0]

# Example usage:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

x = 8
y = 4
print(are_bin_tree_nodes_cousins(root, x, y)) # Output: True

x = 2
y = 3
print(are_bin_tree_nodes_cousins(root, x, y)) 