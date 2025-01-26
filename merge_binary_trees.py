"""
Write a program to merge two binary trees. Each node in the new tree should hold a value equal to
the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree
should match that input node
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    # If one of the nodes is None, return the other node
    
    if not root1:
        return root2
    if not root2:
        return root1
    
    # Create a new node with sum of values
    new_node = TreeNode(root1.val + root2.val)
    
    # Recursively merge left and right subtrees
    new_node.left = mergeTrees(root1.left, root2.left)
    new_node.right = mergeTrees(root1.right, root2.right)
    
    return new_node

# Helper function to print the tree (for testing)
def printTree(node, level=0):
    if node:
        printTree(node.right, level + 1)
        print('  ' * level + str(node.val))
        printTree(node.left, level + 1)

# Example usage:
if __name__ == "__main__":
    # Create first tree
    #      1
    #     / \
    #    3   2
    #   /     
    #  5      
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    # Create second tree
    #      2
    #     / \
    #    1   3
    #     \   \
    #      4   7
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    print("Tree 1:")
    printTree(tree1)
    print("\nTree 2:")
    printTree(tree2)
    
    # Merge trees
    merged_tree = mergeTrees(tree1, tree2)
    print("\nMerged Tree:")
    printTree(merged_tree)