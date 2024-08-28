'''
We're given a sorted singly linked list where nodes are in  increasing order. 
Convert this linked list to a binary search tree
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: ListNode) -> TreeNode:
    # Convert linked list to array
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    # Helper function to convert sorted array to BST
    def sortedArrayToBST(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(values[mid])
        node.left = sortedArrayToBST(left, mid - 1)
        node.right = sortedArrayToBST(mid + 1, right)
        return node
    
    return sortedArrayToBST(0, len(values) - 1)

# Helper function to print the tree in order
def inorderTraversal(root: TreeNode):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)

# Example usage
# Creating a sorted linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)
#head.next.next.next.next.next = ListNode(6)
#head.next.next.next.next.next.next = ListNode(7)

# Converting the sorted linked list to BST
bst_root = sortedListToBST(head)

# Printing the inorder traversal of the BST
inorderTraversal(bst_root)