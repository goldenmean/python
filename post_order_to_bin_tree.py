
'''
Given the sequence of keys visited by a postorder traversal of a binary search tree,
reconstruct the tree.
For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
 

'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructFromPostOrder(postorder):
    # Function to reconstruct BST from postorder traversal
    # Postorder traversal is: left, right, root
    #buildTree - list of nodes, starting index, ending index
    def buildTree(postorder, start, end):
        # Base case
        if start > end:
            return None
        
        # The last element of the current segment is the root
        root = TreeNode(postorder.pop())
        
        # Find the division point where right subtree begins
        division = start
        while division <= (end - 1) and postorder[division] < root.val:
            division += 1
        
        # Recursively build right and left subtrees
        # Note: Build the right subtree first since we're popping from the end
        root.right = buildTree(postorder, division, end - 1)
        root.left = buildTree(postorder, start, division - 1)
        
        return root
    
    return buildTree(postorder, 0, len(postorder) - 1)

# Helper function to print in-order traversal (for verification)
def inorderTraversal(node):
    if not node:
        return
    inorderTraversal(node.left)
    print(node.val, end=' ')
    inorderTraversal(node.right)

# Example usage
postorder = [2, 4, 3, 8, 7, 5]
tree = constructFromPostOrder(postorder)
inorderTraversal(tree)  # Output for verification: 2 3 4 5 7 8