import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

heap = []
for i, v in enumerate(arr):
    heapq.heappush(heap, (-v, i + 1))

res = []
while heap:
    v, i = heapq.heappop(heap)
    if v >= 0:
        continue

    if res and res[-1] == i and heap:
        nv, ni = heapq.heappop(heap)
        res.append(ni)
        if nv+1 < 0:
            heapq.heappush(heap, (nv+1, ni))
        heapq.heappush(heap, (v, i))
    else:
        res.append(i)
        heapq.heappush(heap, (v+1, i))

check = 1
last_val = res[0]
for val in res[1:]:
    if last_val == val:
        check = 0
        break
    last_val = val

if check:
    print(*res)
else:
    print(-1)