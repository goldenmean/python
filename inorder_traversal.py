class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#Recursive inorder traversal        
def helper_inorder( root ):
    res = [] 
    
    def in_order(node):
        if node == None:
            return 
        in_order(node.left)
        res.append(node.value)
        in_order(node.right)
        
    in_order(root)
    print("Recursive function:",res)
    
#Iterative inorder traversal            
def helper_iterative_inorder( root ):
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.value)
        current = current.right
    
    print("Iterative function:",result)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

helper_inorder(root)
helper_iterative_inorder(root)
