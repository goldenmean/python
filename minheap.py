class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert_key(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        print("decrease_key-1",self.heap,new_val,end='\n')
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
        print("decrease_key-2",self.heap,end='\n')

    def extract_min(self):
        root = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.min_heapify(0)
        else:
            self.heap.pop()
        return root

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        print("min_heapify-1",self.heap,end='\n')		
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
        print("min_heapify-2",self.heap,end='\n')

def top_k_elements(lst, k):
    heap = MinHeap()
    for num in lst:
        if len(heap.heap) < k:
            heap.insert_key(num)
            print("print1",heap.heap,end='\n')
        else:
            if num > heap.heap[0]:
                heap.decrease_key(0, num)
                heap.min_heapify(0)
    return heap.heap


lst = [40, 20, 30, 150, 50, 70, 10, 80, 90, 60 ]
k = 3
print(top_k_elements(lst, k))  # Output: [80, 90, 150] => MinHeap gives k maximum elements 

'''
Sure, let's go through the `MinHeap` class and its methods:

- `__init__(self)`: This is the constructor method which is called when an object of `MinHeap` is created. It initializes an empty list `self.heap` which will be used to store the elements of the heap.

- `parent(self, i)`: This method returns the index of the parent of the node at index `i`. In a heap represented as an array, for any element at index `i`, the parent element can be found at index `(i - 1) // 2`.

- `left_child(self, i)`: This method returns the index of the left child of the node at index `i`. In a heap represented as an array, for any element at index `i`, the left child element can be found at index `2 * i + 1`.

- `right_child(self, i)`: This method returns the index of the right child of the node at index `i`. In a heap represented as an array, for any element at index `i`, the right child element can be found at index `2 * i + 2`.

- `insert_key(self, k)`: This method inserts a new key `k` into the heap. It appends the key at the end of the heap and then calls `_bubble_up` to move the key to its correct position in the heap.

- `increase_key(self, i, new_val)`: This method increases the value of key at index `i` to `new_val`. It assumes that `new_val` is larger than `self.heap[i]`. The method replaces the key at index `i` with `new_val` and then calls `_bubble_up` to move the key to its correct position in the heap.

- `extract_min(self)`: This method removes and returns the root of the heap (which is the minimum element). It replaces the root with the last element in the heap, removes the last element, and then calls `min_heapify` to move the new root to its correct position in the heap.

- `min_heapify(self, i)`: This is a helper method which ensures that the heap property is maintained when the root is replaced. It compares the key at index `i` with its children and if the key is larger than either child, it swaps the key with the smallest child. This process is repeated until the key is at its correct position.

The `top_k_elements` function uses the `MinHeap` to find the top `k` elements in a list. It works by pushing each element of the list onto the heap. If the size of the heap exceeds `k`, it pops off the minimum element. This ensures that the heap always contains the top `k` elements seen so far. When all elements have been processed, the heap contains the top `k` elements of the list. 

I hope this helps! Let me know if you have any other questions.
'''