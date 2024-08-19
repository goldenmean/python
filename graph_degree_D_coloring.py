
'''
https://www.interviewcake.com/question/python3/graph-coloring?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23515:%20Graph%20Coloring&utm_medium=email&utm_medium=email
Given an undirected graph with maximum degree D, find a graph coloring using at most 
D+1 colors such that no two adjacent nodes have the same color.

The lowest number of colors we can use to legally color a graph is called the chromatic number.

There's no known polynomial time solution for finding a graph’s chromatic number.
It might be impossible, or maybe we just haven’t figured out a solution yet.

We can't even determine in polynomial time if a graph can be colored using a given 
k
k colors. Even if 
k
k is as low as 3.

We care about polynomial time solutions (
n
n raised to a constant power, like 
O
(
n
2
)
O(n 
2
 )) because for large 
n
ns, polynomial time algorithms are more practical to actually use than higher runtimes like exponential time (a constant raised to the power of 
n
n, like 
O
(
2
n
)
O(2 
n
 )). Computer scientists usually call algorithms with polynomial time solutions feasible, and problems with worse runtimes intractable.

The problem of determining if a graph can be colored with 
k colors is in the class of problems called NP (nondeterministic polynomial time). This means that in polynomial time, we can verify a solution is correct but we can’t come up with a solution. In this case, if we have a graph that's already colored with 
k colors we verify the coloring uses 
k colors and is legal, but we can't take a graph and a number 
k and determine if the graph can be colored with 
k colors.

If you can find a solution or prove a solution doesn't exist, you'll win a $1,000,000 Millennium Problem Prize.

For coloring a graph using as few colors as possible, we don’t have a feasible solution. For real-world problems, we'd often need to check so many possibilities that we’ll never be able to use brute-force no matter how advanced our computers become.

One way to reliably reduce the number of colors we use is to use the greedy algorithm but carefully order the nodes. For example, we can prioritize nodes based on their degree, the number of colored neighbors they have, or the number of uniquely colored neighbors they have.

'''


# Time Complexity O(V + E) 
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' %
                            node.label)

        # Get the node's neighbors' colors, as a set so we
        # can check if a color is illegal in constant time
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])

        # Assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break 

# Example program to test color_graph function    

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
a.neighbors.add(c)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)
c.neighbors.add(a)

graph = [a, b, c]

colors = [1, 2, 3]

color_graph(graph, colors)

for node in graph:
    print(node.label, node.color)   



'''
#print using %s, $d format specifier 
name = "Charlie"
age = 35
print("My name is %s and I am %d years old." % (name, age))
'''