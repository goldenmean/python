''' 
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def prune_btree(root):
    if root is None:
        return None
    
    if root.val == 0:
        if root.left is None and root.right is None:
            return None
        root.left = prune_btree(root.left)
        root.right = prune_btree(root.right)
        return root if root.left or root.right else None
    else:
        root.left = prune_btree(root.left)
        root.right = prune_btree(root.right)
        return root


# driver code to test function prune_btree

def create_tree():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(0)
    root.right.left.left = TreeNode(0)
    root.right.left.right = TreeNode(0)
    return root


def print_tree(root):
    if root is None:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

tree = create_tree()
print(f"Original tree")

print_tree(tree)

pruned_tree = prune_btree(tree)

print(f"Pruned tree")
print_tree(pruned_tree)


