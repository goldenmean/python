'''
Given root of a binary tree, return the deepest node . For given binary tree,
 deepest node(node at maximum depth) is d
 
 a
   / \
  b   c
 /
d

'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_deepest_node_bfs(root):
    if not root:
        return None

    queue = [root]
    deepest_node = None

    while queue:
        current_node = queue.pop(0)
        deepest_node = current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return deepest_node

def find_deepest_node_dfs(root):
    def dfs(node, depth):
        nonlocal max_depth, deepest_node
        if not node:
            return
        
        if depth > max_depth:
            max_depth = depth
            deepest_node = node
        
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    max_depth = -1
    deepest_node = None
    dfs(root, 1)
    print(f"Depth of deepest node is {max_depth}")
    return deepest_node

def find_deepest_node_dfs_iterative(root):
    if not root:
        return None

    stack = [(root, 1)]
    max_depth = -1
    deepest_node = None

    while stack:
        node, depth = stack.pop()
        if node:
            if depth > max_depth:
                max_depth = depth
                deepest_node = node
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

    print(f"Depth of deepest node is {max_depth}")
    return deepest_node


# Example usage:
# Constructing the tree:
#       a
#      / \
#     b   c
#    /
#   d

root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')

#deepest = find_deepest_node_bfs(root)
#deepest = find_deepest_node_dfs(root)
deepest = find_deepest_node_dfs_iterative(root)
print(f"The deepest node is: {deepest.value}")  