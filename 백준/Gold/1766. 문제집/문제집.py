import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    indegree[v] += 1

heap = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    num = heapq.heappop(heap)
    sys.stdout.write(str(num) + ' ')

    for g in graph[num]:
        indegree[g] -= 1
        if indegree[g] == 0:
            heapq.heappush(heap, g)
