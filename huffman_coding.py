r"""
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned a variable-length binary string, such as 0101 or 
111110, where shorter lengths correspond to more common letters. 
To accomplish this, a binary tree is built such that the path from the 
root to any leaf uniquely maps to a character. When traversing the path,
 descending to a left child corresponds to a 0 in the prefix, while descending
right corresponds to 1.

Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and 
use it to determine a mapping between characters and their encoded binary
strings.
"""

import heapq
from collections import defaultdict, Counter

class TreeNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [TreeNode(char, freq) for char, freq in frequencies.items()]
    #Arranges the heap in ascending order based on frequency of the characters
    heapq.heapify(heap)
    #print(heap[0].freq)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        #print(left.freq, right.freq)
        merged = TreeNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(root):
    def _generate_codes(node, current_code):
        if node is None:
            return
        
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        _generate_codes(node.left, current_code + "0")
        _generate_codes(node.right, current_code + "1")

    codes = {}
    _generate_codes(root, "")
    return codes

def huffman_encoding(char_freq):
    root = build_huffman_tree(char_freq)
    return generate_huffman_codes(root)

# Example usage
frequencies = {    
    'c': 7,
    't': 10,
    's': 15,
    'z': 5
}

codes = huffman_encoding(frequencies)
print("Huffman Codes:", codes)

# Example encoding for "cats"
encoded_string = ''.join(codes[char] for char in "ctsz")
print("Encoded 'cats':", encoded_string)