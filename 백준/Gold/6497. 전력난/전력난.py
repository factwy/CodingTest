import sys, heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
while n != 0:
    graph = defaultdict(list)
    visited = [0] * (n+1)
    total_dist = 0

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append([c, a, b])
        graph[b].append([c, b, a])
        total_dist += c

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

    min_dist = prim(graph, 1)
    sys.stdout.write(str(total_dist - min_dist) + "\n")

    n, m = map(int, sys.stdin.readline().split())