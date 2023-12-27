from collections import deque

def isBipartite(graph):
    visited = [False for _ in range(len(graph))] 
    def bfs(root):
        queue = deque([root])   #used to store nodes in same set      	
        print(f"root is {root}")		
        curlevel = set([0])  #used to store nodes in same set   
        while queue:
            #print("queue is ",queue)			
            length = len(queue)
            print("queue length is ",length)			
            newlevel = set()
            for _ in range(length):           # for nodes in each level
                node = queue.popleft()
                for neighbor in graph[node]:
                    print(f"node is {node},neighbour is {neighbor}")				                    				
                    if neighbor in curlevel:  # edge connecting nodes on the same level
                        return False
                    if visited[neighbor]:
                        continue
                    newlevel.add(neighbor)
                    queue.append(neighbor)
                    visited[neighbor] = True
            curlevel = newlevel
            print(f"curlevel is {curlevel}")
            print("queue is ",queue)			
        return True
    for i in range(len(graph)):
        if not visited[i] and not bfs(i):
            return False
    return True
	
#graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]

print(isBipartite(graph))