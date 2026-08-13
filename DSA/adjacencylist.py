n = 5

graph = [[] for _ in range(n)]

edges = [[0, 1], [0, 2], [1, 3], [2, 4]]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)
