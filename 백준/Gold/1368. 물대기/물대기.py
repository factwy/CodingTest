import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())
cost = [int(sys.stdin.readline()) for _ in range(n)]

graph = defaultdict(list)
for i in range(n):
    cost_input = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1, n):
        graph[i].append([min(cost[j], cost_input[j]), i, j])
        graph[j].append([min(cost[i], cost_input[j]), j, i])

min_val, min_val_index = 10**5, 0
for i, c in enumerate(cost):
    if c < min_val:
        min_val = c
        min_val_index = i

candidate = graph[min_val_index]
heapq.heapify(candidate)
visited = [0] * n
visited[min_val_index] = 1
weight = min_val

while candidate:
    w, u, v = heapq.heappop(candidate)

    if visited[v] == 0:
        visited[v] = 1
        weight += w

        for edge in graph[v]:
            if visited[edge[2]] == 0:
                heapq.heappush(candidate, edge)

sys.stdout.write(str(weight))
