import sys, heapq

n, x = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))

start, end = 1, n
min_k = n

while start <= end:
    mid = (start + end) // 2

    line = []
    for i in item[:mid]:
        heapq.heappush(line, i)

    index = mid
    time = 0
    while line:
        t = heapq.heappop(line)
        time = max(time, t)

        if index == n:
            continue
        heapq.heappush(line, t+item[index])
        index += 1

    if time <= x:
        min_k = min(min_k, mid)
        end = mid - 1
    else:
        start = mid + 1

sys.stdout.write(str(min_k))