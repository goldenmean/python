'''
Given a binary number represented as a linked list, return its decimal value.

Ex: Given the following linked list…

1 -> 0 -> 0 -> 1, return 9 (1001 in decimal is 9).
Ex: Given the following linked list…

0 -> 0 -> 1, return 1.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    


def list_to_decimal(head):
    # Convert linked list to array
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    # Convert array to decimal
    decimal = 0
    power = 0
    for i in range(len(values) - 1, -1, -1):
        decimal += values[i] * (2**power)
        power += 1
    '''
    # Another way
    b=[str(i) for i in values]
    decimal=int("".join(b),2) # int('1010', 2) converts the string with binary representation to decimal

    hex(decimal) # gives hex value of decimal input 
    oct(decimal) # gives octal value of decimal
    bin(decimal) # gives binary representation of decimal

    '''

    return decimal

# Test program 
# Creating a linked list: 1 -> 0 -> 0 -> 1
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(0)
head.next.next.next = ListNode(1)       

print(list_to_decimal(head))

