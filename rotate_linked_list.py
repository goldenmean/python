'''
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

'''

def rotate_right(lst, k):
    """Given a Python list lst , k rotate this list to right by k"""
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

def rotate_linked_list(head, k):
    inplist=[]
    curr = head
    while curr:
        inplist.append(curr.val)
        curr = curr.next
    #Rotate list elements right by K is same as rotate left by len(list) - K
    for i in range(k-1):
        inplist.append(inplist.pop(0))
    
    curr = head
    # Assign elements from rotated list as values to the Nodes of the linked list    
    while curr:
        curr.val = inplist.pop(0)
        curr = curr.next
    return head

## Test driver code

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
k=3
 
node = rotate_linked_list(root,k)

#print(olist)

#print the rotated list
while node:
    print(f"{node.val}->", end="")
    node = node.next
print("None")

##############################################################

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the length of the list and the last node
    length = 1
    last = head
    while last.next:
        last = last.next
        length += 1

    # Connect the last node with the head to make it circular
    last.next = head

    # Find the new tail: (length - k % length - 1)th node
    # and the new head: (length - k % length)th node
    steps_to_new_head = k % length
    new_tail = head
    for _ in range(length - steps_to_new_head - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Break the circle
    new_tail.next = None

    return new_head
    

root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
k=3

node = rotateRight(root,k)

#print the rotated list
while node:
    print(f"{node.val}->", end="")
    node = node.next
print("None")