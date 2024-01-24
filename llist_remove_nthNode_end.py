''' Remove nth node from the end of a linked list. Head of the list will be provided
as the argument to your function

'''

class Solution:
def removeNthFromEnd (self, head, n: int):
    dummy = ListNode(-1)
    dummy.next = head
    ahead = behind = dummy

'''
Assume L is length of the list with the dummy node counted, 
there are L traversals starting from dummy node until we reach none/null

The logic behind the initial for loop to increment ahead pointer is: 
We need the ahead pointer to be incremented that many times such that
it is sitting a such a node from where there are just (L-(N+1)) traversals
remaining till ahead pointer reaches none/null. 
So if there are L traversals in all from dummy node to none/null
the forward traversals needed from ahead pointer starting from dummy node are:
(L - (L-(N+1) ) ) = L - L + N + 1 = (N + 1) traversals 
hence the 1st for loop runs till n + 1, so ahead pointer gets incremented
n+1 times from dummy at start.
'''


    for _ in range(n + 1):
        ahead= ahead.next

    while ahead:
        ahead= ahead.next
        behind = behind.next
		
    behind.next = behind.next.next
	
return dummy.next