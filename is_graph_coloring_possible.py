'''
Given an undirected graph represented as an adjacency matrix and an integer k, write a function 
to determine whether each vertex in the graph can be colored such that no two adjacent vertices
share the same color using at most k colors.
'''
# Check if a vertex can be colored with a particular color
# graph - adjacency matrix, v - vertex, color - color array, c - current color
def is_safe(graph, v, color, c):
    # 
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

# Graph coloring using backtracking - arguments: graph, number of colors, 
# color array and current node
def graph_coloring_util(graph, m, color, v):
    #Base case - if v is the last node, all nodes are colored
    if v == len(graph):
        return True
    
    # For each possible color
    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    # If none of the colors is possible for node v, then return false
    return False

def graph_coloring(graph, m):
    # Initialize color array - all elements are 0 , its size is number of nodes in the graph
    color = [0] * len(graph)
    # 
    if graph_coloring_util(graph, m, color, 0):
        return True
    return False

# Example usage
'''
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
k = 3
'''

graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
k = 2
result = graph_coloring(graph, k)
if result:
    print(f"The graph can be colored with {k} colors.")
else:
    print(f"The graph cannot be colored with {k} colors.")