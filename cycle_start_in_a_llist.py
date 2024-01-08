'''
This question is asked by Apple. Given a potentially cyclical linked list where each value is unique, 
return the node at which the cycle starts. If the list does not contain a cycle, return null.

Ex: Given the following linked lists...

1->2->3, return null
1->2->3->4->5->2 (5 points back to 2), return a reference to the node containing 2
1->9->3->7->7 (7 points to itself), return a reference to the node containing 7
'''

def start_node_of_cycle(head):
    fast = head 	
	slow = head
	while fast and fast.next:
	    fast = fast.next.next
		slow = slow.next
		if fast == slow:
		    return slow.next
	
	return None
	