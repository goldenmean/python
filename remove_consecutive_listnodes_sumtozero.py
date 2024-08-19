class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_consecutive_sum_zero(head):
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    sum_map = {0: dummy}

    current = head
    while current:
        prefix_sum += current.val
        if prefix_sum in sum_map:
            prev = sum_map[prefix_sum]
            to_remove = prev.next
            sum_to_remove = prefix_sum
            while to_remove != current:
                sum_to_remove += to_remove.val
                del sum_map[sum_to_remove]
                to_remove = to_remove.next
            prev.next = current.next
        else:
            sum_map[prefix_sum] = current
        current = current.next

    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Example usage:
# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
head = Node(10)
head.next = Node(5)
head.next.next = Node(-3)
head.next.next.next = Node(-3)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(-4)

# Remove consecutive nodes that sum up to 0
new_head = remove_consecutive_sum_zero(head)

# Output: 10
print_linked_list(new_head)