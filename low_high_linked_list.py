'''
Given a linked list, rearrange the node values such that they appear 
in alternating low -> high -> low -> high ... form. For example,
Given input: 1->3->4->8-7
output: 1->7->3->8->4
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print()

# Below code picks first node, then last node, then second node, then 
# second last node and so on
"""
def low_high(head):
    if not head or not head.next:
        return head

    # Find the middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    second_half = reverse(slow)
    first_half = head

    # Merge the two halves in an alternating way
    while second_half:
        temp_first_half = first_half.next
        temp_second_half = second_half.next

        first_half.next = second_half
        second_half.next = temp_first_half

        first_half = temp_first_half
        second_half = temp_second_half

def reverse(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

"""

def rearrange(head):
 
    # empty list
    if head is None:
        return None
 
    prev = head
    curr = head.next
 
    # start from the second node
    while curr:
 
        # if the previous node is greater than the current node, swap their values
        if prev.val > curr.val:
            temp = prev.val
            prev.val = curr.val
            curr.val = temp
 
        # if the next node is greater than the current node, swap their values
        if curr.next and curr.next.val > curr.val:
            temp = curr.next.val
            curr.next.val = curr.val
            curr.val = temp
 
        # update `prev` and `curr` node
        prev = curr.next
 
        if curr.next is None:
            break
 
        curr = curr.next.next
 
    return head

# Example code 
'''
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
'''

'''
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(8)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(1)
'''

#low_high(head)
#print_list(head)

#keys = [1, 2, 3, 4, 5, 6, 7, 8, 6]
keys = [ 3, 4, 8, 6, 1]
 
head = None
for i in reversed(range(len(keys))):
    head = ListNode(keys[i], head)

head = rearrange(head)
print_list(head)

# Create a linked list from a list 
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Test case
head = create_linked_list([3, 4, 8, 6, 1])