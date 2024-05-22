'''
Given a sorted(in ascending order) array, create a binary search tree from it

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr:
        return None
    
    # Find the middle index
    mid = len(arr) // 2
    
    # Make the middle element the root
    root = Node(arr[mid])
    
    # Left subtree of root has all values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])
    
    # Right subtree of root has all values >arr[mid]
    root.right = sortedArrayToBST(arr[mid+1:])
    
    return root

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)

# Utility function to print the preorder traversal of the BST
def preOrder(node):
    if not node:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)

# Print the PreOrder Traversal of the constructed BST
print("PreOrder Traversal of constructed BST:", end=" ")
preOrder(root)
print()