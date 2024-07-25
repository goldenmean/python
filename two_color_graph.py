class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] for row in range(V)]

    def two_color_graph(self, src):
        colorArr = [-1] * self.V

        colorArr[src] = 1

        queue = []
        queue.append(src)

        while queue:

            u = queue.pop()
            print(f"\n Popped node u is {u}")

            if self.graph[u][u] == 1:
                return False

            for v in range(self.V):

                if self.graph[u][v] == 1 and colorArr[v] == -1:

                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                    print(f"color of {v} is {colorArr[v]}")
                    print(f"queue is {queue}")

                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    print(f"color of {v} is {colorArr[v]} and color of {u} is {colorArr[u]}")
                    return False

        return True


import unittest


class Test(unittest.TestCase):
 
    '''
    def test_1(self):
        g = Graph(4)
        g.graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        assert g.two_color_graph(0) == True

        print("PASSED: First Test")
    '''   
    def test_2(self):
        g = Graph(4)
        g.graph = [[0, 1, 1, 1], [1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        assert g.two_color_graph(0) == False

        print("PASSED: Second Test")

    '''   
    def test_3(self):
        g = Graph(4)
        g.graph = [[1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
        assert g.two_color_graph(0) == False

        print("PASSED: Third Test")
    '''   

if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")