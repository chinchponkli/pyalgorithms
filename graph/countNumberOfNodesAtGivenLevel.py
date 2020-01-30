from graph import Graph

def numberOfNodesAtLevel(graph, l, v):
    visited = dict.fromkeys(graph.graph.keys(), False)
    levels = dict.fromkeys(graph.graph.keys(), 0)
    visited[v] = True
    q = [v]
    while len(q) > 0:
        s = q.pop(0)
        for i in graph.graph[s]:
            if not visited[i]:
                q.append(i)
                levels[i] = levels[s] + 1
                visited[i] = True

    count = 0
    for node in levels.keys():
        if levels[node] == l:
            count += 1
    
    return count


g = Graph() 
g.addEdge(0, 1)
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 4) 
g.addEdge(2, 5) 
  
print (numberOfNodesAtLevel(g, 2, 0))