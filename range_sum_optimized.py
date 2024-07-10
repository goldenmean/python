'''
BST Range sum - find sum of nodes in a given range
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        


def optimized_range_sum(root, low, high):
    if root is None:
        return 0
    if root.data < low:
        return optimized_range_sum(root.right, low, high)
    elif root.data > high:
        return optimized_range_sum(root.left, low, high)
    else:
        return root.data + optimized_range_sum(root.left, low, high) + optimized_range_sum(root.right, low, high)
    
    