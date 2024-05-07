import sys

n = int(sys.stdin.readline().rstrip())
arr = []
cnt = 0

for _ in range(n):
    _, y = map(int, sys.stdin.readline().split())

    if arr:
        while arr and arr[-1] > y:
            cnt += 1
            arr.pop()
        if arr and arr[-1] < y:
            arr.append(y)
        elif not arr:
            arr.append(y)
    else:
        arr.append(y)

cnt += len(arr)
if arr and arr[0] == 0:
    cnt -= 1

sys.stdout.write(str(cnt))