
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    if not head or not head.next:
        return head

    # Split the list into two halves
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None

    # Sort each half
    #print(head.val, mid.val)
    left = sortList(head)
    print(f"L:{left.val}")
    right = sortList(mid)
    print(f"R:{right.val}")

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    dummy = ListNode(0)
    current = dummy
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    current.next = left if left else right
    return dummy.next

# Helper function to print the list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
node1 = ListNode(4)
node2 = ListNode(1)
node3 = ListNode(-3)
node4 = ListNode(99)
node1.next = node2
node2.next = node3
node3.next = node4

sorted_list = sortList(node1)
printList(sorted_list) 