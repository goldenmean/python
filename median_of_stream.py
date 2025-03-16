'''
You are given a stream of numbers. Compute the median for each new element.
Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
'''

import heapq

class MedianFinder:
    def __init__(self):
        self.low = []  # Max-heap (simulated with negative values)
        self.high = [] # Min-heap

    def add_num(self, num):
        # Maintain the max-heap property for the lower half
        heapq.heappush(self.low, -num)
        
        # Ensure the largest number in the low is less than or equal to the smallest in high
        # if it is more, then pop it from the maxheap(lower half) and push it to the minheap(upper half)
        if self.low and self.high and (-self.low[0] > self.high[0]):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        
        # Balance the heaps if the sizes of the two differ by more than 1
        # So that at anytime, the two heap sizes differ only by 1 element
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low) + 1:
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)
        
    def find_median(self):
        #If lower half(maxheap) is bigger return the max element in that heap as median
        if len(self.low) > len(self.high):
            return -self.low[0]
        elif len(self.high) > len(self.low):
            return self.high[0]
        # If the sizes are equal, return the average of the top elements
        return (-self.low[0] + self.high[0]) / 2.0

def compute_median_stream(nums):
    median_finder = MedianFinder()
    result = []

    for num in nums:
        median_finder.add_num(num)
        result.append(median_finder.find_median())
    
    return result

# Test the function with an example
nums = [2, 1, 4, 7, 2, 0, 5]
print(compute_median_stream(nums))  