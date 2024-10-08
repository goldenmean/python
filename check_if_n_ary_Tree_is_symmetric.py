
# Find if a N-ary tree is symmetric 

from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

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

res=level_order_N_ary(root)

def check_if_n_ary_tree_is_symmetric(res):
    for level in res:
        if level != level[::-1]:
            return False
    return True 

print(check_if_n_ary_tree_is_symmetric(res))