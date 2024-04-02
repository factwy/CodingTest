import sys
from collections import defaultdict
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    graph = defaultdict(list)

    start_node = set()

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)

        start_node.add(x)
        if y in start_node:
            start_node.remove(y)

    target = int(sys.stdin.readline().rstrip())

    city = [i for i in time]

    queue = deque()
    for i in start_node:
        queue.append(i)
        city[i] = max(time[i], city[i])

        while queue:
            x = queue.popleft()

            for g in graph[x]:
                if city[g] == -1 or city[x] + time[g] > city[g]:
                    city[g] = city[x] + time[g]
                    queue.append(g)

    sys.stdout.write(str(city[target]) + '\n')
