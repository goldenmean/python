'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
'''
from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]     
        if l1 is None and l2 is None:
            return None
            
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        #Traverse both lists and get the digits in arr1 and arr2 lists
        print(f"l1 is {l1}")
        print(f"l2 is {l2}")
        curr1=l1
        while curr1:
            print(f"l1:elements are {curr1.val}")
            arr1.append(curr1.val)
            curr1=curr1.next
            
        curr2=l2
        while curr2:
            print(f"l2:elements are {curr2.val}")
            arr2.append(curr2.val)
            curr2=curr2.next
            
        #reverse the 2 lists to get digits in correct order
        arr1.reverse()
        arr2.reverse()
        
        print(f"arr1 is {arr1}")
        print(f"arr2 is {arr2}")
        
        #Form 2 integer numbers from the digits in the two lists
        num1 = int(''.join([str(d) for d in arr1]))
        num2 = int(''.join([str(d) for d in arr2]))
        
        res=num1+num2
        reslist=[int(c) for c in str(res)]
        reslist.reverse()
        
        #Create the result linked list
        head = None
        current = None
        
        for d in reslist:
            # Create a new node with the current value
            new_node = ListNode(d)
            
            # If the head is None, set the head to the new node
            if head is None:
                head = new_node
                current = head
            else:
                # Otherwise, set the next of the current node to the new node
                # and update the current node to the new node
                current.next = new_node
                current = new_node
    
        # After the loop, set the next of the last node to None
        if current is not None:
            current.next = None
        
        return head 
            
        
## Driver code to test above solution ##        

#Create l1 and l2 lists
#Create List a and its 3 nodes, la1,la2,la3
la1 = ListNode(2)
la2 = ListNode(4)           
la3 = ListNode(3)           

#Create List b and its 3 nodes, lb1,lb2,lb3
lb1 = ListNode(5)
lb2 = ListNode(6)           
lb3 = ListNode(4)           

la1.next = la2
la2.next = la3
la3.next = None

lb1.next = lb2
lb2.next = lb3
lb3.next = None

print("List a:")
current_node = la1
while current_node:
    print(f"{current_node.val}-->", end="")
    current_node = current_node.next
print("None\n\n")

current_node = lb1
print("List b:")
while current_node:
    print(f"{current_node.val}-->", end="")
    current_node = current_node.next
print("None\n\n")    
    
soln = Solution()
reslist=soln.addTwoNumbers(la1, lb1)

print("Result list is:")
while reslist:
    print(f"{reslist.val}-->",end="")
    reslist=reslist.next    
print("None\n\n")


