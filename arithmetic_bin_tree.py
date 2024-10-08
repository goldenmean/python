r"""
You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an 
integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5

This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

"""


class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    if root.val == PLUS:
        return evaluate(root.left) + evaluate(root.right)   
    elif root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)   
    elif root.val == TIMES:
        return evaluate(root.left) * evaluate(root.right)   
    elif root.val == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)   
    else:
        return root.val


root = Node(DIVIDE)
root.left = Node(PLUS)
root.left.left = Node(3)
root.left.right = Node(2)
root.right = Node(PLUS)
root.right.left = Node(4)
root.right.right = Node(5)
print(evaluate(root))