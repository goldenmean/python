'''
Return kth largest element from a array
'''

import heapq
'''
def kth_largest(nums,K):
    N=len(nums)
    heapq.heapify(nums)
    i=0
    while i < (N-K+1):
        res=heapq.heappop(nums)
        i+=1

    return res


nums=[2,3,6,4,1,5]; K=1

print(kth_largest(nums,K))
'''

def kth_smallest(nums,K):
    N=len(nums)
    heapq.heapify(nums)
    i=0
    while i < (K):
        res=heapq.heappop(nums)
        i+=1

    return res


nums=[2,3,6,4,1,5]; K=5


print(kth_smallest(nums,K))