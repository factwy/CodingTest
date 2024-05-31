import sys

n = int(sys.stdin.readline().rstrip())

visit = set([])
cnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if b == 0:
        if a in visit:
            visit.remove(a)
        else:
            cnt += 1
    else:
        if a in visit:
            cnt += 1
        else:
            visit.add(a)

cnt += len(visit)

print(cnt)