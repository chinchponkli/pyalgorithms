'''
Given a graph G and an integer K, K-cores of the graph are connected components that are left after 
all vertices of degree less than k have been removed 
'''
from undirectedgraph import Graph

def dfsUtil(graph, v, vDegree, visited, k):
    # mark node as visited
    visited[v] = True

    for i in graph.graph[v]:
        # if vDegree is less than k reduce the degree of adjacent node by 1
        if vDegree[v] < k:
            vDegree[i] -= 1
        # if adjacent node is not visited visit it and if its degree becomes less than k
        # decrease current's vertex degree by 1
        if not visited[i]:
            if (dfsUtil(graph, i, vDegree, visited, k)):
                vDegree[v] -= 1
    return vDegree[v] < k

def findKCores(graph, k):
    visited = dict.fromkeys(graph.graph.keys(), False)
    vDegree = {}
    # calculate and store degree for each vertex
    for vertex in graph.graph.keys():
        vDegree[vertex] = len(graph.graph[vertex])
    
    # modified dfs
    dfsUtil(graph, 0, vDegree, visited, k)

    for i in range(self.V): 
            if visited[i] ==False: 
                self.DFSUtil(i,k,vDegree,visited) 

    for vertex in graph.graph.keys():
        # print adjacency list only for nodes whose degree >= k
        if vDegree[vertex] >= k:
            print("[" + str(vertex) + "] ->", end = " ")
            # print a vertex only if its degree is >= k
            for i in graph.graph[vertex]:
                if vDegree[i] >= k:
                    print(i, end = " ")
            print()

k = 3
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(1, 5) 
g.addEdge(2, 3) 
g.addEdge(2, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
g.addEdge(3, 4) 
g.addEdge(3, 6) 
g.addEdge(3, 7) 
g.addEdge(4, 6) 
g.addEdge(4, 7) 
g.addEdge(5, 6) 
g.addEdge(5, 8) 
g.addEdge(6, 7) 
g.addEdge(6, 8) 

findKCores(g, k)