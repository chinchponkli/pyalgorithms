from graph import Graph

def dfsUtil(graph, v, visited):
    visited[v] = True
    for i in graph.graph[v]:
        if not visited[i]:
            dfsUtil(graph, i, visited)

def motherVertex(graph):
    vertices = graph.graph.keys()
    visited = dict.fromkeys(vertices, False)
    possibleMotherVertex = None
    for vertex in vertices:
        if not visited[vertex]:
            dfsUtil(graph, vertex, visited)
            possibleMotherVertex = vertex
    
    visited = dict.fromkeys(vertices, False)
    dfsUtil(graph, possibleMotherVertex, visited)
    print(visited)
    if any(not visited[i] for i in visited.keys()):
        return None
    else:
        return possibleMotherVertex

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0) 

print(motherVertex(g))
