'''
Given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u, v) 
in the given graph. Here reachable mean that there is a path from vertex u to v. 
The reach-ability matrix is called transitive closure of a graph.

For example, consider below graph:

0---->1---->2----->3
^           ^
|___________|

Also, a node is always reachable from itself.

Transitive closure of above graphs is 
     1 1 1 1 
     1 1 1 1 
     1 1 1 1 
     0 0 0 1 
'''
from graph import Graph

def dfsUtil(graph, s, v, tc):
    tc[s][v] = 1
    for i in graph.graph[v]:
        if tc[s][i] == 0:
            dfsUtil(graph, s, i, tc)

def transitiveClosure(graph, n):
    tc = [[0 for i in range(n)] for j in range(n)]
    for vertex in graph.graph.keys():
        dfsUtil(graph, vertex, vertex, tc)
    return tc

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

n = len(g.graph.keys())
print(transitiveClosure(g, n))