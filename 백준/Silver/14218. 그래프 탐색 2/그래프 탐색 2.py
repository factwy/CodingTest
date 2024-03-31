import sys
from collections import defaultdict
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

    visited = [-1] * (n+1)
    queue = deque()
    visited[1] = 0
    queue.append(1)

    while queue:
        x = queue.popleft()

        for g in graph[x]:
            if visited[g] == -1 or visited[x]+1 < visited[g]:
                visited[g] = visited[x] + 1
                queue.append(g)

    for i in range(1, n+1):
        sys.stdout.write(str(visited[i]) + ' ')
    sys.stdout.write('\n')
    