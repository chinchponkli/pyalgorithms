from graph import Graph

def numPaths(graph, u, v):
    visited = dict.fromkeys(graph.graph.keys(), False)
    pathCount = [0]
    countPaths(graph, u, v, visited, pathCount)
    return pathCount[0]

def countPaths(graph, u, v, visited, pathCount):
    visited[u] = True
    if u == d:
        pathCount[0] += 1
    else:
        for i in graph.graph[u]:
           if not visited[i]:
               countPaths(graph, i, d, visited, pathCount)
    visited[u] = False

g = Graph()  
g.addEdge(0, 1)  
g.addEdge(0, 2)  
g.addEdge(0, 3)  
g.addEdge(2, 0)  
g.addEdge(2, 1)  
g.addEdge(1, 3)  
  
u = 2
d = 3
print(numPaths(g, u, d)) 
     