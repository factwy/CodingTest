import sys

n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + a[i-1]

prefix_power = [0] * (n+1)
for i in range(1, n+1):
    prefix_power[i] = prefix_power[i-1] + a[i-1] ** 2

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())

    total = ((prefix_sum[r] - prefix_sum[l-1]) ** 2) - (prefix_power[r] - prefix_power[l-1])
    total = total // 2

    sys.stdout.write(str(total) + '\n')
    