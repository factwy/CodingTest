import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append((i, 1))

while queue:
    index, height = queue.popleft()
    indegree[index] = height

    for g in graph[index]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append((g, height+1))

print(*indegree[1:])
