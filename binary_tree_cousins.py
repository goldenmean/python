
r"""
Two nodes in a binary tree can be called cousins if they are on the same level of the
tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_cousins(root, target):
    if not root:
        return []

    queue = [(root, None, 0)]
    target_level = -1
    target_parent = None
    cousins = []

    while queue:
        level_size = len(queue)
        level_nodes = [] # since level_nodes is defined each time for a given level,
        # it will contain only the tuples: (node, parent) at that level

        for _ in range(level_size):
            node, parent, level = queue.pop(0)
            level_nodes.append((node, parent))

            if node.val == target:
                target_level = level
                target_parent = parent

            if node.left:
                queue.append((node.left, node, level + 1))
            if node.right:
                queue.append((node.right, node, level + 1))

        # print(f"A: size of level_nodes: {len(level_nodes)}")
        # for i,j in level_nodes:
        #     if j != None:
        #         print(i.val,j.val)
        #     else:
        #         print(i.val,'None')

        if target_level == level: 
            # print(len(level_nodes))           
            # for i,j in level_nodes:
            #     print(i.val,j.val)
            cousins = [node.val for node, parent in level_nodes if parent != target_parent and node.val != target]
            break

    return cousins
    

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

target = 6
result = find_cousins(root, target)
print(f"Cousins of node {target}: {result}")