import sys

n = int(sys.stdin.readline().rstrip())
res = 0

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    money = 0

    if a == b == c:
        money = 10000 + a * 1000
    elif a == b:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    elif c == a:
        money = 1000 + c * 100
    else:
        money = max(a, b, c) * 100

    res = max(res, money)

sys.stdout.write(str(res))
