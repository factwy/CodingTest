import sys, heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
graph = defaultdict(list)
dist = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))


def prim(start):
    visited[start] = 1
    candidate = graph[start]
    heapq.heapify(candidate)
    total_weight = 0

    while candidate:
        w, u, v = heapq.heappop(candidate)

        if visited[v] == 0:
            visited[v] = 1
            total_weight += w
            dist[u].append([v, w])
            dist[v].append([u, w])

            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)

    return total_weight


def dfs(now, target):
    visit[now] = True
    for nex, weight in dist[now]:
        if visit[nex]:
            continue
        visit[nex] = True
        if nex == target:
            return weight

        res = dfs(nex, target)
        if res != -1:
            return max(res, weight)
    return -1


t = prim(1)
q = int(sys.stdin.readline())
for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    visit = [False] * (n+1)
    maxDist = dfs(a, b)
    # 팀장들이 연결될 수 있는 간선들 중 최대 가중치의 간선을 끊게 된다면
    # 팀원들 끼리 연결되어 있으나 다른 팀의 팀원과는 연결되어 있지 않음.
    sys.stdout.write(str(t - maxDist) + "\n")