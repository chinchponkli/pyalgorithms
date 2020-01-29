from graph import Graph

def dfs(graph, s):
    visited = dict.fromkeys(graph.graph.keys(), False)
    stack = [s]
    while len(stack) > 0:
        v = stack.pop()
        # Graph may contain same vertex twice. 
        if not visited[v]:
            visited[v] = True
            print(v, end = " ")
        # Avoid appending if a vertex has already been visited
        for i in graph.graph[v]:
            if not visited[i]:
                stack.append(i)

g = Graph()
g.addEdge(1, 0)
g.addEdge(0, 2)  
g.addEdge(2, 1)  
g.addEdge(0, 3)  
g.addEdge(1, 4)

dfs(g, 0)
print()