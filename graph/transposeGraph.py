'''
Transpose of a directed graph G is another directed graph on the same set of vertices with all of the edges 
reversed compared to the orientation of the corresponding edges in G. That is, if G contains an edge (u, v) 
then the converse/transpose/reverse of G contains an edge (v, u) and vice versa.
'''
from graph import Graph

def transposeGraph(graph):
    transpose = Graph()
    for vertex in graph.graph.keys():
        for i in graph.graph[vertex]:
            transpose.addEdge(i, vertex)
    return transpose

g = Graph()
g.addEdge(0, 1)  
g.addEdge(0, 4)  
g.addEdge(0, 3)  
g.addEdge(2, 0)  
g.addEdge(3, 2)  
g.addEdge(4, 1)  
g.addEdge(4, 3)  

transposeGraph(g).print()