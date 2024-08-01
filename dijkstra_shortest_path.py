'''
Dijkstra's shortest path algorithm
'''

import heapq

def dijkstra(graph, start):
    #Dictionary of distances from start node to all other nodes
    distances = {node: float('infinity') for node in graph}  # Initialize distances dictionary
    distances[start] = 0  # Distance from start to itself is 0
    #Priority storing distance to the node 
    # Priority queue is a min heap. It which stores element with shortest distance from start
    # node, that distance is 1st element of the tuple stored in the Priority queue(min heap)
    # So the min heap sorts the elements by the first element of the tuple - shortest distance first
    queue = [(0, start)]  # Initialized with distance to the start node from itself is 0

    visited = set()
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get node with smallest distance
        print(f"current_distance: {current_distance}, current_node: {current_node}")
        visited.add(current_node)
        
        # Skip if the node has already been visited        
        if distances[current_node] < current_distance:
            print("Skipping")
            continue
        
        # Update distances to neighboring nodes
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                print(f"Visited node {neighbor}, skip it")
                continue
            distance = current_distance + weight
            print(f"Neighbour of {current_node} is {neighbor} with distance {distance} ")
            
            # Only update if new distance is shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
  
    return distances

# Example usage:
#Dictionary of dictionaries. All values are dictionaries Adjacency list representation of graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 2, 'E': 3},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 3, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

graph = {
    'A': {'B': 1, 'C': 1},
    'B': {'A': 1, 'D': 2, 'E': 3},
    'C': {'A': 1, 'F': 1},
    'D': {'B': 2},
    'E': {'B': 3, 'F': 1},
    'F': {'C': 1, 'E': 1}
}


start_node = 'A'

distances = dijkstra(graph, start_node)
print(distances) # {'A': 0, 'B': 1, 'C': 3, 'D': 3, 'E': 4, 'F': 5}