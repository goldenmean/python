'''
Reverse a directed graph 
'''

from collections import defaultdict

def reverse_graph(graph):
    """
    Reverses a directed graph.
    
    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
                  Keys are nodes, and values are lists of nodes that the key node has edges to.
    
    Returns:
    dict: The reversed graph as an adjacency list.
    """
    reversed_graph = defaultdict(list)
    
    for start_node in graph:
        for end_node in graph[start_node]:
            reversed_graph[end_node].append(start_node)
    
    return dict(reversed_graph)

# Example usage
original_graph = {
    'A': ['B','D'],
    'B': ['C'],
    'C': []
}

reversed_graph = reverse_graph(original_graph)

print("Original graph:", original_graph)
print("Reversed graph:", reversed_graph)

