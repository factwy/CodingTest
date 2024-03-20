import sys, heapq
from collections import defaultdict

n = int(sys.stdin.readline())
planet = [[0] * n for _ in range(n)]

for i in range(n):
    row_planet = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        planet[i][j] = row_planet[j]

graph = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        graph[i].append([planet[i][j], i, j])
        graph[j].append([planet[i][j], j, i])

visited = [0] * (n+1)


def prim(graph, node):
    visited[node] = 1
    candidate = graph[node]
    heapq.heapify(candidate)
    total_weight = 0

    while candidate:
        w, u, v = heapq.heappop(candidate)

        if visited[v] == 0:
            visited[v] = 1
            total_weight += w

            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)

    return total_weight


sys.stdout.write(str(prim(graph, 0)))