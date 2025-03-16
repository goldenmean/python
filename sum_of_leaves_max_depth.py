
"""
Given the reference to the root of a binary tree, return the sum of all leaves at the
deepest level.

Ex: Given the following tree…

      2
     / \
    4   5, return 9 (4 and 5 are at the deepest level and sum to 9).
Ex: Given the following tree…

      1
       \
        2
         \
          3, return 3.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepest_leaves_sum(root):
    def dfs(node, depth):        
        if not node:
            return 
        nonlocal max_depth, total_sum
        
        if depth > max_depth:
            max_depth = depth
            total_sum = node.val

        elif depth == max_depth:
            total_sum += node.val

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)


    max_depth = 0
    total_sum = 0
    dfs(root, 0)
    return total_sum

# Test cases
# Example 1
root1 = TreeNode(2)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
print(deepest_leaves_sum(root1))  # Output: 9

# Example 2
root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)
print(deepest_leaves_sum(root2))  # Output: 3

## Iterative solution using queue
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepest_leaves_sum_iterative(root):
    if not root:
        return 0
    
    queue = deque([(root, 0)])
    max_depth = 0
    level_sum = 0
    
    while queue:
        node, depth = queue.popleft()
        
        if depth > max_depth:
            max_depth = depth
            level_sum = node.val
        elif depth == max_depth:
            level_sum += node.val
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return level_sum