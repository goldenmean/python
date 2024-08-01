

'''
Given an integer k and a binary search tree, find the floor (Largest value less than or equal to) of k,
and the ceiling (smallest value larger than or equal to) of k. 

'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


'''
# Recursive solutions 
#Time Complexity: O(logn) Space Complexity: O(logn)

def ceil_BST(root,k):
    if root is None:
        return -1
    if root.data == k:
        return root.data
    if root.data < k:
        print(f"entering right substree of {root.data}")
        return ceil_BST(root.right,k)
    if root.data > k:
        print(f"entering left substree of {root.data}")
        val = ceil_BST(root.left,k)
        # if val is found in left subtree, return that
        if val >= k:
            return val
        else:   
            # if val is not found in left subtree, return root.data
            return root.data
    

def floor_BST(root,k):
    if root is None:
        return -1
    if root.data == k:
        return root.data
    if root.data > k:
        print(f"entering left substree of {root.data}")
        return floor_BST(root.left,k)
    if root.data < k:
        print(f"entering right substree of {root.data}")
        val = floor_BST(root.right,k)
        # if val is found in right subtree, return that
        if val <= k and val != -1:
            return val
        else:   
            # if val is not found in right subtree, return root.data
            return root.data
'''

# Iterative solutions
# Time O(logn) | Space O(1)
def find_floor(root, k):
    # Initialize floor value as negative infinity (or None)
    floor_val = float('-inf')
    
    # Traverse the BST
    while root:
        # If root's value is less than or equal to k, update floor_val and go right
        if root.data <= k:
            floor_val = root.data
            root = root.right
        else:
            # If root's value is greater than k, go left
            root = root.left
    
    return floor_val if floor_val != float('-inf') else -1


def find_ceil(root, k):
    # Initialize ceil value as positive infinity (or None)
    ceil_val = float('inf')
    
    # Traverse the BST
    while root:
        # If root's value is greater than or equal to k, update ceil_val and go left
        if root.data >= k:
            ceil_val = root.data
            root = root.left
        else:
            # If root's value is less than k, go right
            root = root.right
    
    return ceil_val if ceil_val != float('inf') else -1

# Example program
'''
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(12)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)
k = 5
'''

root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)
k = 5

#print(f"Ceil of {k} is", ceil_BST(root,k))
#print(f"Floor of {k} is",floor_BST(root,k))
print(f"Floor of {k} is",find_floor(root,k))

print(f"Ceil of {k} is",find_ceil(root,k))