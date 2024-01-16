'''
Given a binary tree, return the largest value in each of its levels. Ex: Given the following tree…

    2
   / \
  10  15
        \
         20

return [2, 15, 20]
Ex: Given the following tree…

          1
         / \
        5   6
       / \   \  
      5   3   7 

return [1, 6, 7]
'''

from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest_values_in_tree_levels(root):
    if not root:
        return []
    
    queue = deque([(root, 0)])  # The queue stores tuples of (node, level)
    level_to_max_value = {}  # A dictionary mapping level number to max value in that level
    
    while queue:
        node, level = queue.popleft()
        
        # If this level hasn't been seen before, or this node's value is larger than the max, update the max
        if level not in level_to_max_value or node.value > level_to_max_value[level]:
            level_to_max_value[level] = node.value
        
        # Add the node's children to the queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    # Return the max values in order of level
    return [level_to_max_value[i] for i in range(len(level_to_max_value))]

# Test the function with the provided examples
#root1 = Node(2, Node(10), Node(15, None, Node(20)))
'''
root = Node(1)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(7)
'''
root = Node(2)
root.left = Node(10)
root.right = Node(15)
root.right.right = Node(20)

print(largest_values_in_tree_levels(root))  

#root2 = Node(1, Node(5, Node(5), Node(3)), Node(6, None, Node(7)))
#print(largest_values_in_tree_levels(root2))  