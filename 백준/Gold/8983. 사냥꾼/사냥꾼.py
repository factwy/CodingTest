import sys

input = lambda: sys.stdin.readline().strip()

m, n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(0, n):
    x, y = map(int, input().split())

    start, end = 0, m
    while start <= end:
        mid = (start + end) // 2

        if abs(x - arr[mid]) + y <= l:
            break

        if x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if abs(x - arr[(start + end) // 2]) + y <= l:
        cnt += 1

print(cnt)