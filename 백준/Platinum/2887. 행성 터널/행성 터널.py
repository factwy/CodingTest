import sys, heapq
from collections import defaultdict

n = int(sys.stdin.readline())
planet = []

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append((i, x, y, z))

graph = defaultdict(list)
visited = [0] * n

for i in range(1, 4):
    planet.sort(key=lambda x: x[i])

    for j in range(n-1):
        a, x1, y1, z1 = planet[j]
        b, x2, y2, z2 = planet[j+1]

        dist = min(abs(x1 - x2), abs(y1- y2), abs(z1 - z2))

        graph[a].append([dist, a, b])
        graph[b].append([dist, b, a])


def prim(start=0):
    visited[start] = 1
    candidate = graph[start]
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


sys.stdout.write(str(prim()))