# Detect a cycle in a undirected graph

from collections import defaultdict

class MyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Because the graph is undirected

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        #print(f"PrintA : v = {v}, parent = {parent}, visited = {visited}")
        # Recur for all vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            print(f"v = {v}, parent = {parent}, neighbor = {neighbor}, visited = {visited}")
            # If an adjacent vertex is not visited, then recur for that adjacent
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    print("PrintB")
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, then there is a cycle
            elif neighbor != parent:
                print(f"PrintC: v = {v}, parent = {parent}, neighbor = {neighbor}, visited = {visited}")
                return True

        return False

    def is_cyclic(self):
        visited = {node: False for node in self.graph}
        print(f"The adjacency list of graph = {self.graph}")
        # Call the recursive helper function to detect cycle in different DFS trees
        for node in self.graph:
            print(f"for loop for node = {node}")
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True

        return False

# Example usage:
g = MyGraph()
'''
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 4)
'''


g.add_edge(0, 1)
g.add_edge(1, 0)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle")