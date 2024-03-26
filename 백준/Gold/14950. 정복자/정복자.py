import sys
import heapq
from collections import defaultdict

n, m, t = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, a, b])
    graph[b].append([c, b, a])

visited = [0] * (n+1)
visited[1] = 1
total_weight = 0
cnt = 0     # 정복 도시 수

candidate = graph[1]
heapq.heapify(candidate)
while candidate:
    w, u, v = heapq.heappop(candidate)

    if visited[v] == 0:
        visited[v] = 1
        total_weight += (w + cnt * t)
        cnt += 1

        for edge in graph[v]:
            if visited[edge[2]] == 0:
                heapq.heappush(candidate, edge)

sys.stdout.write(str(total_weight))
