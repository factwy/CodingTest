import sys
from collections import deque

n, m, k, X = map(int, sys.stdin.readline().split())
origin_graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

start, end = 0, X
res = X
while start <= end:
    mid = (start + end) // 2
    graph = [[origin_graph[i][j] for j in range(m)] for i in range(n)]
    cnt = 0

    queue = deque()
    check = False
    for x in range(n):
        for y in range(m):
            if graph[x][y] == X:
                continue

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if graph[nx][ny] > graph[x][y] and abs(graph[nx][ny] - graph[x][y]) > mid:
                    graph[x][y] = X
                    cnt += 1
                    queue.append((x, y))
                    break

    while queue:
        x, y = queue.popleft()
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if abs(X - graph[nx][ny]) > mid:
                graph[nx][ny] = X
                cnt += 1
                queue.append((nx, ny))

    if cnt <= k:
        res = min(res, mid)
        end = mid - 1
    else:
        start = mid + 1

print(res)
