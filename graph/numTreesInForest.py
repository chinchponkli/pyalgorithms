from undirectedgraph import Graph

def dfs(graph, vertex, visited):
    visited[vertex] = True
    for i in graph.graph[vertex]:
        if not visited[i]:
            dfs(graph, i, visited)

def numTrees(graph):
    visited = dict.fromkeys(graph.graph.keys(), False)
    count = 0
    for vertex in graph.graph.keys():
        if not visited[vertex]:
            dfs(graph, vertex, visited)
            count += 1
    return count

g = Graph()
g.addEdge(0, 1)  
g.addEdge(0, 2)  
g.addEdge(3, 4)  
g.addEdge(0, 4)

print(numTrees(g))