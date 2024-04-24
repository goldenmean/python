from collections import defaultdict

def isTree(n, edges):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize visited set and parent dictionary
    visited = set()
    parent = {1: None}
    
    # DFS function to check for cycles and connectivity
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                dfs(neighbor)
            elif parent[node] != neighbor:
                # If the neighbor is visited and it's not the parent of the current node,
                # it means there is a cycle
                return False
        return True
    
    # Start DFS from node 1
    if not dfs(1):
        return False
    
    # Check if all nodes are visited
    return len(visited) == n

# Example usage
n = 4
edges = [[1, 2], [2, 3], [3, 4]]
print(isTree(n, edges)) # Output: True

n = 4
edges = [[1, 2], [2, 3], [3, 4], [4, 1]]
print(isTree(n, edges)) # Output: False
