''' Remove nth node from the end of a linked list. Head of the list will be provided
as the argument to your function

'''

class Solution:
def removeNthFromEnd (self, head, n: int):
    dummy = ListNode(-1)
    dummy.next = head
    ahead = behind = dummy
    for _ in range(n + 1):
        ahead= ahead.next
    while ahead:
        ahead= ahead.next
        behind = behind.next
		
    behind.next = behind.next.next
	
return dummy.next