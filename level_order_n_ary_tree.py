'''
Given an n-ary tree, return its level order traversal.
Note: an n-ary tree is a tree in which each node has no more than N children.

Ex: Give the following n-ary tree…

    8
  / | \
 2  3  29
return [[8], [2, 3, 29]]
Ex: Given the following n-ary tree…

     2
   / | \
  1  6  9
 /   |   \
8    2    2
   / | \
 19 12 90
return [[2], [1, 6, 9], [8, 2, 2], [19, 12, 90]]

'''

# Level order traversal of N-ary tree

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


from collections import deque
def level_order_N_ary(root):
    res=[]
    q = deque()
    q.append(root)

    while q:
        qlen = len(q)
        level = []

        for i in range(qlen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.extend(node.children)

        if level:
            res.append(level)    

    return res

# Example program
'''
root = Node(2)
root.children = [
        Node(1, [Node(8)]),
        Node(6, [Node(2), Node(19), Node(12), Node(90)]),
        Node(9)
    ]
'''

root = Node(2)
root.children = [
        Node(1, [Node(8)]),
        Node(6, [Node(2)]),
        Node(9, [Node(3)])
    ]

root.children[1].children[0].children.append(Node(19))
root.children[1].children[0].children.append(Node(12))
root.children[1].children[0].children.append(Node(90))
root.children[1].children[0].children[0].children.append(Node(99))

print(level_order_N_ary(root))