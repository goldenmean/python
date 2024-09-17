'''
Given an array of a million integers between zero and a billion, out of order, how can
you efficiently sort it? Assume that you cannot store an array of a billion elements in
memory.
'''

import random
import heapq
import os
import tempfile

def external_sort(input_array, chunk_size):
    temp_files = []
    # Step 1: Divide and Sort Each Chunk
    for i in range(0, len(input_array), chunk_size):
        chunk = input_array[i:i + chunk_size]
        chunk.sort()
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_files.append(temp_file.name)
        with open(temp_file.name, 'w') as f:
            f.write('\n'.join(map(str, chunk)))
    
    # Step 2: Merge Sorted Chunks
    def iter_file(file):
        with open(file, 'r') as f:
            for line in f:
                yield int(line.strip())
    
    sorted_iterables = [iter_file(file) for file in temp_files]

    # if u want to write the elements in descending order 
    '''
     # To merge in descending order, we use negative values
    def negated_iter_file(file):
        for value in iter_file(file):
            yield -value

    negated_sorted_iterables = [negated_iter_file(file) for file in temp_files]

    with open('sorted_output_descending.txt', 'w') as output_file:
        for neg_value in heapq.merge(*negated_sorted_iterables):# Python heap is always minheap 
            output_file.write(f"{-neg_value}\n")  # Convert back to positive to write in descending order order
    
    '''

    with open('sorted_output.txt', 'w') as output_file:
        # K way merging using heapsort from heapq
        for value in heapq.merge(*sorted_iterables):
            output_file.write(f"{value}\n")
    
    # Clean up temp files
    print(temp_files)
    for file in temp_files:
        os.remove(file)

# Example usage
input_array = [random.randint(0, 10**9) for _ in range(10**4)]
chunk_size = 1000  # Adjust based on available memory
external_sort(input_array, chunk_size)