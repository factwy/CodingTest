import sys

n, t = map(int, sys.stdin.readline().split())
time = [0] * 100001

for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    for _ in range(k):
        s, e = map(int, sys.stdin.readline().split())
        time[s] += 1
        time[e] -= 1

prefix = [0] * 100002
for i in range(1, 100002):
    prefix[i] = prefix[i-1] + time[i-1]
for i in range(1, 100002):
    prefix[i] += prefix[i-1]

res = 0
index = -1
for i in range(t, 100002):
    val = prefix[i] - prefix[i-t]

    if val > res:
        res = val
        index = i

sys.stdout.write(str(index-t) + ' ' + str(index))
