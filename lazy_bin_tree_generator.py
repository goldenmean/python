

'''
class Node:
    pass  # Base class now doesn't initialize left and right

def generate():
    #This subclass LazyNode is overriding the attributes left and right of the super class Node
    class LazyNode(Node):
        def __init__(self):
            # Initialization is handled here, avoiding conflicts with property setters
            self._left = None
            self._right = None
        
        @property
        def left(self):
            if self._left is None:
                self._left = LazyNode()
            return self._left
        
        @property
        def right(self):
            if self._right is None:
                self._right = LazyNode()
            return self._right
    
    return LazyNode()

# Example usage
tree = generate()
print(tree.left.right.left)  # This should work without raising an AttributeError
tree.left.right.left = 99
#print(tree.left.right.left)  This causes error as no setter defined for attribute left, right 

'''



## Example with setters and getters defined to dynamically build a binary tree with lazy evaluation 

class Node:
    def __init__(self):
        self._left = None
        self._right = None
        self._value = None  # New attribute to hold the node's value
        #pass  # Base class remains empty, serving as a marker


class LazyNode(Node):
    def __init__(self):
        #invoke the super class __init__
        super().__init__()

    
    #getter for the left attribute
    @property
    def left(self):
        if self._left is None:
            self._left = LazyNode()
        return self._left
    
    # setter for the left attribute
    @left.setter
    def left(self, value):
        self._left = value
    
    @property
    def right(self):
        if self._right is None:
            self._right = LazyNode()
        return self._right
    
    @right.setter
    def right(self, value):
        self._right = value

def generate():
    return LazyNode()
    

# Example usage
tree = generate()
tree._value = "Root Node"

# Now, you can also assign nodes explicitly
tree.left = LazyNode()  # Setting a new node to the left property
tree.left._value = "Left Child Node"
tree.right = LazyNode()  # Setting a new node to the right property
tree.right._value = "Right Child Node"

print(tree._value, tree.left._value, tree.right._value)