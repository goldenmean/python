


class MyGraph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list to store graph

    def add_edge(self, u, v):
        """Add an edge from u to v."""
        self.graph[u].append(v)

    def reverse_graph(self):
        """Reverse the directed graph."""
        reversed_graph = MyGraph(self.V)
        for u in self.graph:
            #print(f"{u} : {self.graph[u]}")
            for v in self.graph[u]:
                #print(u, v)
                reversed_graph.add_edge(v, u)
                #print(reversed_graph.graph)
        return reversed_graph

    def print_graph(self):
        """Print the graph."""
        for vertex in range(self.V):
            print(f"Vertex {vertex}:", end="")
            for connected_vertex in self.graph[vertex]:
                print(f" -> {connected_vertex}", end="")
            print()

# Example usage
if __name__ == "__main__":
    g = MyGraph(4)  # Create a graph with N vertices
    g.add_edge(0, 1)  # Add edge from vertex 0 to 1
    g.add_edge(1, 2)  # Add edge from vertex 1 to 2
    g.add_edge(1, 3)  

    print("Original graph:")
    g.print_graph()
    

    reversed_g = g.reverse_graph()
    print("Reversed graph:")
    reversed_g.print_graph()