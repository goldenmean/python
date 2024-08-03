
'''
Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less
than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution 
would be 1 -> 0 -> 5 -> 8 -> 3
'''

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def partition(head, k):
    less_head = less = Node()
    greater_head = greater = Node()
    
    current = head
    
    while current:
        if current.value < k:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    
    # Combine the two lists
    less.next = greater_head.next
    greater.next = None  # End the list
    
    return less_head.next

# Helper functions to create and print the linked list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(map(str, values)))

# Test the function
values = [5, 1, 8, 0, 3]
k = 3
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

partitioned_head = partition(head, k)
print("Partitioned list:")
print_linked_list(partitioned_head)