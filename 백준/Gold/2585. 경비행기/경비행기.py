import sys
from collections import deque

n, k = map(int ,sys.stdin.readline().split())
dist = [(0, 0, 0)]
for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().split())
    dist.append((i, x, y))
dist.append((n+1, 10000, 10000))

start, end = 1, 2000
min_k = end
while start <= end:
    mid = (start + end) // 2
    cnt_k = [-1] * (n+2)
    cnt_k[0] = 0
    queue = deque()
    queue.append(0)

    while queue:
        index = queue.popleft()
        x, y = dist[index][1], dist[index][2]

        for next_index, nx, ny in dist:
            now_dist = ((x - nx) ** 2 + (y - ny) ** 2) ** 0.5
            if now_dist > mid*10:
                continue

            if cnt_k[next_index] == -1 or cnt_k[index] + 1 < cnt_k[next_index]:
                cnt_k[next_index] = cnt_k[index] + 1
                queue.append(next_index)

    if cnt_k[n+1] != -1 and cnt_k[n+1] <= (k+1):
        min_k = min(min_k, mid)
        end = mid - 1
    else:
        start = mid + 1

sys.stdout.write(str(min_k))