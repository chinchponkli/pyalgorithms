from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

    def bfs(self, s):
        visited = dict.fromkeys(self.graph.keys(), False)
        q = [s]
        visited[s] = True
        while q:
            s = q.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
        print()

    def dfs(self, s):
        visited = dict.fromkeys(self.graph.keys(), False)
        self.dfsUtil(s, visited)
        print()

    def dfsUtil(self, s, visited):
        visited[s] = True
        print (s, end = " ")
        for i in self.graph[s]:
            if not visited[i]:
                self.dfsUtil(i, visited)

    def print(self):
        for vertex in self.graph.keys():
            print ("[" + str(vertex) + "] -> " + self.graph[vertex])