class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        

def find_largest(root_node):
    if root_node is None:
        raise ValueError('Tree must have at least 1 node')
    if root_node.right is not None:
        return find_largest(root_node.right)
    return root_node.value


def find_second_largest(root_node):
    if root_node:
        print(root_node.value)	 
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    # Case: we're currently at largest, and largest has a left subtree,
    # so 2nd largest is largest in said subtree
    if root_node.left and not root_node.right:
        return find_largest(root_node.left)

    # Case: we're at parent of largest, and largest has no left subtree,
    # so 2nd largest must be current node
    if (root_node.right and
            not root_node.right.left and
            not root_node.right.right):
        return root_node.value

    # Otherwise: step right
    return find_second_largest(root_node.right)


n = BinaryTreeNode(5)
n.insert_left(3)
n.insert_right(8)
n.left.insert_left(1)
n.left.insert_right(4)
n.right.insert_left(7)
n.right.insert_right(9)
    
print(find_second_largest(n))


    
    
        