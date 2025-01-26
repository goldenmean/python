"""
mplement a queue using a set of fixed-length arrays.
The queue should support enqueue, dequeue, and get_size operations.
"""
class ArrayQueue:
    def __init__(self, array_size=5):
        self.array_size = array_size
        self.arrays = [[None] * array_size]  # List of fixed-length arrays
        self.front = 0  # Index of front element
        self.back = 0   # Index where next element will be inserted
        self.size = 0   # Current number of elements
        self.current_array = 0  # Index of current array

    def enqueue(self, item):
        if self.back == self.array_size:
            # Current array is full, create new array
            if self.current_array == len(self.arrays) - 1:
                self.arrays.append([None] * self.array_size)
            self.current_array += 1
            self.back = 0
            
        self.arrays[self.current_array][self.back] = item
        self.back += 1
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")

        item = self.arrays[0][self.front]
        self.arrays[0][self.front] = None
        self.front += 1
        self.size -= 1

        # If first array is empty, remove it and adjust indices
        if self.front == self.array_size:
            self.arrays.pop(0)
            self.current_array -= 1
            self.front = 0

        return item

    def get_size(self):
        return self.size
    

    # Example usage
queue = ArrayQueue(3)  # Create queue with arrays of size 3
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)  # First array full
queue.enqueue(4)  # Creates new array
print(queue.get_size())  # Output: 4
print(queue.dequeue())   # Output: 1
print(queue.get_size())  # Output: 3

