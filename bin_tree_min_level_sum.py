'''
Given a binary tree, return the level of the tree with minimum sum.

'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_with_min_sum(root):
    if not root:
        return -1

    queue = deque([(root, 0)])  # (node, level)
    level_sum = {}
    
    while queue:
        node, level = queue.popleft()
        
        if level not in level_sum:
            level_sum[level] = 0
        level_sum[level] += node.val
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    print(level_sum)
    #Below will return the level with minimum sum
    min_sum_level = min(level_sum, key=lambda x: level_sum[x])
    #Below will return the level with maximum sum
    #min_sum_level = max(level_sum, key=lambda x: level_sum[x])
    min_sum = level_sum[min_sum_level]
    return min_sum_level,min_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print(level_with_min_sum(root))

