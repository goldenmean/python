"""
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t),
describing the time t it takes for a message to be sent from node a to node b.
Whenever a node receives a message, it immediately passes the message on to a neighboring
node, if possible.
Assuming all nodes are connected, determine how long it will take for every node to receive
a message that begins at node 0.
For example, given N = 5, and the following edges:
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take 
3+1+5 = 9 and by that time all nodes 2,3,1,4 and 5 would have received the message.
"""

import heapq

def network_delay_time(N, edges):
    graph = {i: [] for i in range(N)}
    for u, v, w in edges:
        graph[u].append((v, w))
        #graph[v].append((u, w))  # Add this line if the graph is undirected

    # Min-heap to store (time, node)
    min_heap = [(0, 0)]
    visited = set()
    max_time = 0

    while min_heap:
        time, node = heapq.heappop(min_heap)
        print(f"A: time = {time}, node = {node}")
        if node in visited:
            continue
        visited.add(node)
        max_time = max(max_time, time)
        print(f"B: max_time = {max_time}, visited = {visited}")
        

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (time + weight, neighbor))
                print(f"C: neighbour = {neighbor}, weight = {weight}, time + weight = {time + weight}, min_heap = {min_heap}")
    
    return max_time if len(visited) == N else -1

# Example usage
N = 6
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

print(network_delay_time(N, edges))  # Output: 9