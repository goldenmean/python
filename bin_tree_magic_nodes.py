
r"""
      5
    /   \
   4     9
  / \
 8   7

 """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def magic_nodes(root):
    def is_magic(node, max_so_far):
        if not node:
            return 0
        
        # Current node is magic if its value is >= maximum value seen so far
        count = 1 if node.value >= max_so_far else 0
        
        # Update maximum value seen for child paths
        new_max = max(max_so_far, node.value)
        
        # Recursively check left and right subtrees
        left_count = is_magic(node.left, new_max)
        right_count = is_magic(node.right, new_max)
        
        return count + left_count + right_count
    
    return is_magic(root, float('-inf'))


# Create the tree from the example
root = Node(5)
root.left = Node(4)
root.right = Node(9)
root.left.left = Node(8)
root.left.right = Node(7)

result = magic_nodes(root)
print(f"Number of magic nodes: {result}")  # Should print 4