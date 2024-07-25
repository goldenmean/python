



class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def printInOrder(node):
    if node is not None:
        printInOrder(node.left)
        print(node.value, end=' ')
        printInOrder(node.right)

def deleteLeafNodesExceptRootandNonleafNodes(root):

    if root.left is None and root.right is None:
        return None

    root.left = deleteLeafNodesExceptRootandNonleafNodes(root.left)
    root.right = deleteLeafNodesExceptRootandNonleafNodes(root.right)
    
    return root

def deleteAllNodesExceptRoot(root):
    # Base case: if the node is None, simply return None
    if root is None:
        return None
    
    # Set left and right children of the root node to None
    root.left = None
    root.right = None
    
    # Return the root node itself, now without any children
    return root


def deleteAllNodes(root):

    if root.left is None and root.right is None:
        return None

    root.left = deleteAllNodes(root.left)
    root.right = deleteAllNodes(root.right)
    
    return None


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

print("Original tree (in-order traversal):")
printInOrder(root)
print("\n")

# Delete leaf nodes
root = deleteLeafNodesExceptRootandNonleafNodes(root)

print("Tree after deleting leaf nodes (in-order traversal):")
printInOrder(root)

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

root = deleteAllNodes(root)

print("\nTree after deleting all nodes including root (in-order traversal):")
printInOrder(root)  

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

root = deleteAllNodesExceptRoot(root)

print("\nTree after deleting all nodes except root (in-order traversal):")
printInOrder(root)

