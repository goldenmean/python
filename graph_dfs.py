#Recursive DFS traversal of a Graph
def graph_dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(f"Visiting {node}")
    for neighbor in graph[node]:
        if neighbor not in visited:
            graph_dfs_recursive(graph, neighbor, visited)
    return visited


#Iterative DFS traversal of a Graph
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(f"Visiting {node}")
            # Add neighbors to stack
            stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    return visited