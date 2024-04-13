import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
already_create = list(map(int, sys.stdin.readline().split()))
create = [[] for _ in range(n+1)]
for i in range(1, n+1):
    create[i] = list(map(int, sys.stdin.readline().split()))[1:]

resource = [False] * (n+1)
resource_graph = [[] for _ in range(n+1)]
factory_indegree = [0] * (n+1)

for _ in range(n-m):
    input_data = list(map(int, sys.stdin.readline().split()))
    index = input_data[0]
    need_resource = input_data[2:]
    for r in need_resource:
        resource_graph[r].append(index)
        factory_indegree[index] += 1

res = []
queue = deque()
for a in already_create:
    queue.append((a, 0))

while queue:
    num, time = queue.popleft()
    if time <= t:
        res.append(num)

    for c in create[num]:
        if not resource[c]:
            resource[c] = True
            for f in resource_graph[c]:
                factory_indegree[f] -= 1
                if factory_indegree[f] == 0:
                    queue.append((f, time+1))

res.sort()
sys.stdout.write(str(len(res)) + '\n')
print(*res)
