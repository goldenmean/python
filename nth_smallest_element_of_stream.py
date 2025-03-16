'''
Given a stream of numbers with an infinite length, can you find the nth smallest
element at each point of the streaming?
'''

import heapq

class NthSmallest:
    def __init__(self, n):
        self.n = n #Always return nth smallest element of the stream
        self.max_heap = []

    def add(self, num):
        if len(self.max_heap) < self.n:
            heapq.heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                heapq.heappushpop(self.max_heap, -num)

    def get_nth_smallest(self):
        if len(self.max_heap) < self.n:
            return None  # Not enough elements in the stream
        return -self.max_heap[0] # The maximum element at root of the heap is always the Nth smallest

# Example usage
#n = 3 #Always return 3rd smallest element of the stream
#stream = [5, 2, 10, 4, 3, 1, 7]
n = 2
stream = [2,6,4]
nth_smallest_tracker = NthSmallest(n)

for num in stream:
    nth_smallest_tracker.add(num)
    nth_smallest = nth_smallest_tracker.get_nth_smallest()
    print(f"After adding {num}, the {n}rd smallest element is {nth_smallest}")