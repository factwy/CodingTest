import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
res, size = [], 0
queue = deque()
queue.append((arr, 0))

while queue:
    order, index = queue.popleft()
    order_size = len(order)

    if size == index:
        res.append([])
        size += 1

    if order_size == 1:
        res[index].append(order[0])
        continue

    res[index].append(order[order_size // 2])

    queue.append((order[:order_size//2], index+1))
    queue.append((order[(order_size//2 + 1):], index+1))

for r in res:
    print(*r)
