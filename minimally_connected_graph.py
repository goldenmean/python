
'''
A graph is minimally-connected if it is connected and there is no edge that can 
be removed while still leaving the graph connected. For example, any binary tree
is minimally-connected. Given an undirected graph, check if the graph is 
minimally-connected. You can choose to represent the graph as either an adjacency
matrix or adjacency list.

A graph is said to be minimally connected if removal of any one edge from it
disconnects the graph. Clearly, a minimally connected graph has no cycles.

'''

from collections import defaultdict

def is_minimally_connected(graph):
    def dfs(node, parent):
        visited.add(node)
        print(f"node: {node}, parent: {parent}, visited: {visited}")
        for neighbor in graph[node]:
            if neighbor != parent:  # Skip the edge to the parent to avoid going back
                if neighbor in visited:
                    print(f"Returning False node: {node}, parent: {parent}, visited: {visited}")
                    return False  # Found a cycle, so it is not minimally-connected
                if not dfs(neighbor, node):
                    return False
        print(f"returning True node:{node} ")
        return True

    visited = set()
    start_node = list(graph.keys())[0]
    return dfs(start_node, None) and len(visited) == len(graph)

# Example graph represented as an adjacency list
'''
graph = {
    0: [1],
    1: [0, 2],
    2: [1,3],
    3: [2,4],
    4: [3]
}
'''

'''
graph = {
    0: [1],
    1: [0, 2],
    2: [1,3],
    3: [4],
    4: [3]
}
'''
graph = {
    0:[1,2],
    1:[0,3],
    2:[0,3],
    3:[1,2]   
}


if is_minimally_connected(graph):
    print("The graph is minimally-connected.")
else:
    print("The graph is not minimally-connected.")