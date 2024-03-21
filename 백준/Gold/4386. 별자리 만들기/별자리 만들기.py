import sys, heapq
from collections import defaultdict

n = int(sys.stdin.readline())
star = []
visited = [0] * n

for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    star.append((x, y))

graph = defaultdict(list)
for i in range(n):
    for j in range(i+1, n):
        xi, yi = star[i]
        xj, yj = star[j]

        dist = ((xi-xj) ** 2 + (yi-yj) ** 2) ** 0.5
        graph[i].append([dist, i, j])
        graph[j].append([dist, j, i])


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


sys.stdout.write("{:.2f}".format(prim(graph, 0)))