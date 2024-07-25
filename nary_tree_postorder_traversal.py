'''
Given an n-ary tree, return a list containing the post order traversal of the tree.
Write your solution iteratively.
Ex: Given the following n-ary tree...

        1
      / | \
     2  3  4, return [2, 3, 4, 1]
     
'''



class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def postorder(root):
    if not root:
        return []
    
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(node.children)
        print(f"result: {result}, stack: {[n.val for n in stack]}")
    #Reverse the result because stack.pop appends the children from the right to left , but we need left to right in postorder
    return result[::-1]

# Example n-ary tree
root = Node(1, [Node(2), Node(3), Node(4)])
root.children[0].children = [Node(5), Node(6), Node(7)]
root.children[1].children = [Node(8), Node(9), Node(10)]
root.children[2].children = [Node(11), Node(12), Node(13)]
result = postorder(root)
print(result)  