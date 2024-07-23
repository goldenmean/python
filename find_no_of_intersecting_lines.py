'''
Find Intersecting line segments - Suppose you are given two lists of n points,
one list p1, p2, ..., pn on the line y = 0 and the other
list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting
each point pi to qi. Write an algorithm to determine how many pairs of the line 
segments intersect.  

'''

def count_intersecting_segments(P, Q):
    intersections = 0
    n = len(P)
    
    # Iterate through all pairs of line segments
    for i in range(n):
        for j in range(i+1, n):
            # Check if the segments intersect
            if (P[i] < P[j] and Q[i] > Q[j]) or (P[i] > P[j] and Q[i] < Q[j]):
                intersections += 1
                
    return intersections

# Example usage
P = [1, 3, 5, 2, 9]
Q = [4, 6, 2, 0, -1]
print(count_intersecting_segments(P, Q))

P = [1,2]
Q = [3,2]
print(count_intersecting_segments(P, Q))