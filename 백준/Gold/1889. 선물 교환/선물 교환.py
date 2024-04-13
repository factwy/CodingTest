import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
student = set([i for i in range(1, n + 1)])

for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[i].append(a)
    graph[i].append(b)

    indegree[a] += 1
    indegree[b] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] < 2:
        queue.append(i)

while queue:
    s = queue.popleft()
    if s in student:
        student.remove(s)
    else:
        continue

    for g in graph[s]:
        indegree[g] -= 1
        if indegree[g] < 2:
            queue.append(g)

sys.stdout.write(str(len(student)) + '\n')
print(*list(student))
