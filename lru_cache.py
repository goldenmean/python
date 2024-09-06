'''
Implement a LRU cache using a custom data structure 
A Doubly linked list to maintain the notion of recently used(head node) and least recently used(tail node)
and a dictionary of key value pairs to store the data
'''
class LinkedListNode:
    def __init__(self, pair):
        self.second = pair[1]
        self.first = pair[0]
        self.pair = pair
        self.next = None
        self.prev = None
        
#from linked_list_node import LinkedListNode

class LinkedList:

    # _init__ initialises the linkedL list type object
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # move_to_head will move the given node to head
    def move_to_head(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        # Insertion at head
        if not self.head:
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # Insert_at_head will insert the given pair at head
    def insert_at_head(self, pair):
        new_node = LinkedListNode(pair)
        if not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    # Insert_at_tail will insert the given pair at tail
    def insert_at_tail(self, pair):
        new_node = LinkedListNode(pair)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None

        self.size += 1

    # remove will remove the given pair from the LinkedList
    def remove(self, pair):
        i = self.get_head()
        while i:
            if i.pair == pair:
                self.remove_node(i)
                return
            i = i.next

    # remove_node will remove the given node from the LinkedList
    def remove_node(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        self.size = self.size - 1
        del node
        # return node

    # remove_head will remove the head of the linked list
    def remove_head(self):
        return self.remove_node(self.head)

    # remove_tail will remove the tail of the linked list
    def remove_tail(self):
        return self.remove_node(self.tail)

    # get_head will return the head of the linked list
    def get_head(self):
        return self.head

    # get tail will return the tail of the linked list
    def get_tail(self):
        return self.tail


#from linked_list import LinkedList

# We will use a linked list having pair of integers
# where the first integer will be the key
# and the second integer will be the value

class LRUCache:
    # Initializes an LRU cache with the capacity size
    def __init__(self, capacity):
        self.cache_capacity = capacity
        self.cache_map = {}
        self.cache_list = LinkedList()

    # Returns the value of the key, or -1 if the key does not exist.
    def get(self, key):
        # If the key doesn't exist, we return -1
        found_itr = None
        if key in self.cache_map:
            found_itr = self.cache_map[key]
        else:
            return -1

        list_iterator = found_itr

        # If the key exists, we must move it to the front of the list
        self.cache_list.move_to_head(found_itr)

        return list_iterator.pair[1]

    # Adds a new key-value pair or updates an existing key with a new value
    def set(self, key, value):
        # Check if the key exists in the cache hashmap
        # If the key exists
        if key in self.cache_map:
            found_iter = self.cache_map[key]
            list_iterator = found_iter

            # Move the node corresponding to key to front of the list
            self.cache_list.move_to_head(found_iter)

            # We then update the value of the node
            list_iterator.pair[1] = value
            return

        # If key does not exist and the cache is full
        if len(self.cache_map) == self.cache_capacity:
            # We will need to evict the LRU entry

            # Get the key of the LRU node
            # The first element of each cache entry is the key
            key_tmp = self.cache_list.get_tail().pair[0]

            # This is why we needed to store a <key, value> pair
            # in the cacheList. We would not have been able to get
            # the key if we had just stored the values

            # Remove the last node in list
            self.cache_list.remove_tail()

            # Remove the entry from the cache
            del self.cache_map[key_tmp]

        # The insert_at_head function inserts a new element at the front
        # of the list in constant time
        self.cache_list.insert_at_head([key, value])

        # We set the value of the key as the list begining
        # since we added the new element at head of the list
        self.cache_map[key] = self.cache_list.get_head()

    def print(self):
        print("Cache current size: ", self.cache_list.size,
              ", ", end="")
        print("Cache contents: {", end="")

        node = self.cache_list.get_head()
        while node:
            print("{", str(node.pair[0]), ",", str(node.pair[1]),
                  "}", end="")
            node = node.next
            if node:
                print(", ", end="")
        print("}")
        print("-"*100, "\n")


def main():
    # Creating a cache of size 2
    cache_capacity = 2
    cache = LRUCache(cache_capacity)
    print("Initial state of cache")
    print("Cache capacity: " + str(cache_capacity))
    cache.print()

    keys = [10, 10, 15, 20, 15, 25, 5]
    values = ["20", "get", "25", "40", "get", "85", "5"]

    for i in range(len(keys)):
        if values[i] == "get":
            print("Getting by Key: ", keys[i])
            print("Cached value returned: ", cache.get(keys[i]))
        else:
            print("Setting cache: Key: ", keys[i], ", Value: ", values[i])
            cache.set(keys[i], int(values[i]))
        cache.print()


if __name__ == '__main__':
    main()





