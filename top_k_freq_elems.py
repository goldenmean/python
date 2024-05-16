'''
Return top K frequent values in a array

'''

'''
### Solution 1] Using dictionary of frequency of values and sorting it O(N*logN)
def top_k_freq_elems(arr,k):
    d={}
    res=[]
    for n in arr:
        d[n] = 1 + d.get(n,0)

    print(f"d is {d}")
    #Sort the dictionary by its value(which is frequncy of the number)
    sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print(f"Sorted dictionary is {sorted_by_values}")
    #add the number keys which indicate he numbers in highest order 
    for n in sorted_by_values.keys():
        res.append(n)
        print(f"res is {res}")
        if len(res)==k:
            return res
'''

'''
### Solution 2] Using a maxheap O(k*logN) in worst case could be O(N*logN) if k = N
import heapq

def top_k_freq_elems(arr,k):
       
    #Below code does not work as heapify does not order based on second value in tuple
    d={}
    res=[]
    newl=[]
    for n in arr:
        d[n] = 1 + d.get(n,0)

    for kv in d:
        newl.append(kv)
    
    heapq.heapify(newl)

    for i in range(k):
        heapq.heappop(heapq.heapify)
        print(f"")

'''

'''
Creating a heap based on the second value of a tuple in the list of tuples 
We use a wrapper class

import heapq

class TupleWrapper:
    def __init__(self, tup):
        self.tup = tup

    def __lt__(self, other):
        return self.tup[1] < other.tup[1]

newl = [(1, 3), (2, 2), (3, 5)]

# Convert the list of tuples to a list of TupleWrapper objects
wrapped_list = [TupleWrapper(t) for t in newl]

# Use heapq.heapify to create a min heap based on the second value of each tuple
heapq.heapify(wrapped_list)

# Now, the heap is based on the second value of each tuple
while wrapped_list:
    print(heapq.heappop(wrapped_list).tup)

'''


### Solution 3] Using a modified Bucket sort O(N)

def top_k_freq_elems(arr,k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                 return res
    
    


#nums=[1,1,1,2,2,3]; k=2
#nums=[1,1,1,2,2,3]; k=1
nums=[1,1,1,2,2,7,7,7,7,7]; k=2            
res=top_k_freq_elems(nums,k)
print(f"Top K frequent values are {res}")