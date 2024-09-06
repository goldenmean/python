# Studying ggarbage collection

import gc
import sys 
class Node:
    def __init__(self):
        self.data = None
        self.next = None

def create_cycle():
    node1 = Node()
    node2 = Node()
    
    # Create a cycle
    node1.next = node2
    node2.next = node1
    
    # Return one of the nodes
    return node1

# Create a cycle
cycle_node = create_cycle()

print("Initial reference count:")
print(sys.getrefcount(cycle_node))

# Keep a reference to the cycle
ref_list = [cycle_node]

print("After adding reference:")
print(sys.getrefcount(cycle_node))

# Remove the reference
ref_list.clear()

print("After removing reference:")
print(sys.getrefcount(cycle_node))

# Manually trigger garbage collection
gc.collect()

print("After manual GC:")
print(sys.getrefcount(cycle_node))

## Clearing python variables/references

globals().clear()

x = 10
y = 20
# Delete variables x and y so gc collect them, nd free the memory 
del x, y