'''
Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an 
error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
'''
import heapq

class Stack:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item):
        heapq.heappush(self.heap, (-self.count, item))
        self.count += 1

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("pop from an empty stack")
        item = heapq.heappop(self.heap)
        return item

    
stk_as_heap = Stack()
stk_as_heap.push(7)
stk_as_heap.push(5)
stk_as_heap.push(3)

print(stk_as_heap.pop()[1])
print(stk_as_heap.pop()[1])
print(stk_as_heap.pop()[1])
      