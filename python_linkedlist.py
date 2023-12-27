class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




#def MergeTwoLists



# Create a dummy node and a new node
dummy = ListNode(-1)
Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node5 = ListNode(5)

#Connect the  node next pointers to create linked list
dummy.next = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node5

ahead = behind = dummy
ahead = ahead.next
ahead = ahead.next
ahead = ahead.next
behind = behind.next
print(ahead.val)
print(behind.val)
print(dummy.val)
print(dummy.next)
print(dummy.next.val)

# Now tail points to the same object as dummy
#tail = dummy

#tail.next = Node5
#print(dummy.next.val)  # Outputs: 5


