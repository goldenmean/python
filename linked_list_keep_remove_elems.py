



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linked_list_keep_remove_elems(head, m, n):
    if head is None:
        return head
    
    current = head

    while current:
        if m > 0:
            m -= 1
            prev = current
            current = current.next
        else:            
            while n > 0 and current:
                n -= 1
                current = current.next

            prev.next = current

    current = head        
    #print the resulting list
    while current:
        print(current.val, end = "->")
        current = current.next
    print(None)
    return head

# Test program 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)


res = linked_list_keep_remove_elems(head, 2, 2)