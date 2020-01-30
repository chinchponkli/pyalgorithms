from undirectedgraph import Graph
from sieveoferatosthenes import primes

def findNumberOfTimesDigitChangeRequired(graph, p1, p2):
    visited = dict.fromkeys(graph.graph.keys(), False)
    q = [p1]
    visited[p1] = True
    count = 0
    levels = dict.fromkeys(graph.graph.keys(), False)
    while len(q) > 0:
        s = q.pop(0)
        count += 1
        for i in graph.graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                levels[i] = levels[s] + 1
                if i == p2:
                    return levels[i]

def differBySingleDigit(a, b):
    count = 0
    if a % 10 != b % 10:
        count += 1
    a, b = a // 10, b // 10
    if a % 10 != b % 10:
        count += 1
    a, b = a // 10, b // 10
    if a % 10 != b % 10:
        count += 1
    a, b = a // 10, b // 10
    if a % 10 != b % 10:
        count += 1
    return count == 1

start = 1000
end = 9999
primeList = primes(start, end)
g = Graph()

for i in range(len(primeList)):
    for j in range(i + 1, len(primeList)):
        if differBySingleDigit(primeList[i], primeList[j]):
            g.addEdge(primeList[i], primeList[j])

print (findNumberOfTimesDigitChangeRequired(g, 1033, 8179))