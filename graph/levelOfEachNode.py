from graph import Graph

def levels(graph, v):
    visited = dict.fromkeys(graph.graph.keys(), False)
    levels = dict.fromkeys(graph.graph.keys(), 0)
    q = [v]
    visited[v] = True
    while len(q) > 0:
        s = q.pop(0)
        for i in graph.graph[s]:
            if not visited[i]:
                visited[i] = True
                levels[i] = levels[s] + 1
                q.append(i)

    return levels

g = Graph()  
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(6, 7)

print (levels(g, 0)) 
