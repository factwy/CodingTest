import sys
from collections import deque

d, m = map(int, sys.stdin.readline().split())
height_dict = {}
queue = deque()
queue.append((0, 1))

for i in range(d):
    height_dict = {}
    while queue:
        h, t = queue.popleft()

        if h > 0:
            if (h-1) in height_dict.keys():
                height_dict[h-1] += t
            else:
                height_dict[h-1] = t
        if (h+1) in height_dict.keys():
            height_dict[h+1] += t
        else:
            height_dict[h+1] = t

        if i != d-1 and 0 in height_dict.keys():
            height_dict[0] = 0

    for x, y in height_dict.items():
        if y > 0:
            queue.append((x, y))

res = height_dict[0] % m
sys.stdout.write(str(res))