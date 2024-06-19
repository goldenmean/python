'''
Given a N-ary tree where each edge has a weight, compute the length of the longest path in the tree.
The path does not have to pass through the root, and each node can have any amount of children.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path 
would be c -> a -> d -> f, with a length of 17.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def dfs(node, longest_path):
    if not node.children:
        return 0
    
    max_path, second_max = 0, 0
    for child in node.children:
        child_path = dfs(child, longest_path) + edge_weights[(node.val, child.val)]
        print(f"edge {node.val}--> {child.val} has weight {edge_weights[(node.val, child.val)]}")
        print(f"child_path is {child_path}")
        if child_path > max_path:
            second_max = max_path
            max_path = child_path
        elif child_path > second_max:
            second_max = child_path
        print(f"max_path is {max_path} & second_max is {second_max}")
    longest_path[0] = max(longest_path[0], max_path + second_max)
    print(f"longest_path[0] is {longest_path[0]}")
    return max_path

# Example tree structure
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.children = [b, c, d]
d.children = [e, f]
e.children = [g, h]

# Example edge weights
edge_weights = {
    ('a', 'b'): 3,
    ('a', 'c'): 5,
    ('a', 'd'): 8,
    ('d', 'e'): 2,
    ('d', 'f'): 4,
    ('e', 'g'): 1,
    ('e', 'h'): 1
}

longest_path = [0]
dfs(a, longest_path)
print(longest_path[0])


'''
# Sample output logs after adding print statements and executing above test case
edge a--> b has weight 3
child_path is 3
max_path is 3 & second_max is 0
edge a--> c has weight 5
child_path is 5
max_path is 5 & second_max is 3
edge e--> g has weight 1
child_path is 1
max_path is 1 & second_max is 0
edge e--> h has weight 1
child_path is 1
max_path is 1 & second_max is 1
longest_path[0] is 2
edge d--> e has weight 2
child_path is 3
max_path is 3 & second_max is 0
edge d--> f has weight 4
child_path is 4
max_path is 4 & second_max is 3
longest_path[0] is 7
edge a--> d has weight 8
child_path is 12
max_path is 12 & second_max is 5
longest_path[0] is 17
17
'''
