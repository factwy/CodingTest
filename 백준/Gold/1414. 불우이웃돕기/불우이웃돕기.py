import sys, heapq
from collections import defaultdict

n = int(sys.stdin.readline())
graph = defaultdict(list)
visited = [0] * n
total_line = 0

for i in range(n):
    row_line = list(sys.stdin.readline())
    for j in range(n):
        if row_line[j] == '0':
            continue

        # 랜선 길이 변환
        size = ord(row_line[j])
        if size < 97:
            size -= 38
        else:
            size -= 96

        graph[i].append([size, i, j])
        graph[j].append([size, j, i])

        total_line += size


def prim(start):
    visited[start] = 1
    candidate = graph[start]
    heapq.heapify(candidate)
    total_weight = 0
    connect_pc = 1

    while candidate:
        w, u, v = heapq.heappop(candidate)

        if visited[v] == 0:
            visited[v] = 1
            total_weight += w
            connect_pc += 1

            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)

    # PC들이 모두 연결되었는지 확인
    if connect_pc != n:
        return -1
    return total_weight


min_line = prim(0)

if min_line == -1:
    sys.stdout.write(str(-1))
else:
    # 기부 랜선 = 총 랜선 - MST 랜선
    sys.stdout.write(str(total_line - min_line))