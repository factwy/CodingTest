import sys

a, b = map(int, sys.stdin.readline().split())

prefix = [0] * (b+1)
num, cnt = 1, 0
for i in range(1, b+1):
    prefix[i] = prefix[i-1] + num
    cnt += 1

    if cnt == num:
        num += 1
        cnt = 0

res = prefix[b] - prefix[a-1]
sys.stdout.write(str(res))
