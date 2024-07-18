from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    K = len(lists)

    for i,node in enumerate(lists):
        if node:
            #heapq.heappush(heap, (node.val, i, node))
            heapq.heappush(heap, (node.val,  node))

    dummy = ListNode(0)
    cur = dummy

    while heap:
        #Get the node with minimum value
        #val, idx, node = heapq.heappop(heap)
        val,  node = heapq.heappop(heap)
        cur.next = node 
        cur = cur.next

        #push next node of the mimimum valued node to heap 
        if node.next:
            #heapq.heappush(heap, (node.next.val, idx, node.next))
            heapq.heappush(heap, (node.next.val,  node.next))

    return dummy.next

# Driver code to test the function mergeKLists

head1 = ListNode(1)
n11 = ListNode(10)
n12 = ListNode(25)
head1.next = n11
n11.next = n12

head2 = ListNode(-7)
n21 = ListNode(7)
n22 = ListNode(70)
head2.next = n21
n21.next = n22

head3 = ListNode(4)
n31 = ListNode(40)
n32 = ListNode(400)
head3.next = n31
n31.next = n32


res = mergeKLists([head1, head2, head3])


while res:
    print(f"{res.val} -->",end="")
    res = res.next
print(" None")