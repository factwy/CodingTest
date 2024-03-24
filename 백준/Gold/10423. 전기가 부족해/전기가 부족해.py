import sys
import heapq
from collections import defaultdict

n, m, k = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
elect = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([w, u, v])
    graph[v].append([w, v, u])

candidate = []
for e in elect:
    visited[e] = 1
    for g in graph[e]:
        heapq.heappush(candidate, g)

total_weight = 0
while candidate:
    w, u, v = heapq.heappop(candidate)

    if visited[v] == 0:
        visited[v] = 1
        total_weight += w

        for edge in graph[v]:
            if visited[edge[2]] == 0:
                heapq.heappush(candidate, edge)

sys.stdout.write(str(total_weight))
