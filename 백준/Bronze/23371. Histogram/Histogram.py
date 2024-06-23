import sys

n, s, k = map(int, sys.stdin.readline().rstrip().split())
points = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [0 for _ in range(n)]

for point in points:
    num = point // s
    if point % s == 0:
        num -= 1
    arr[num] += 1

max_h = max(arr)

for h in range(max_h, -1, -1):
    for i in range(n):
        if h == 0:
            sys.stdout.write("-")
        elif arr[i] < h:
            sys.stdout.write(".")
        else:
            sys.stdout.write("#")
    print()
