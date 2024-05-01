import sys

n = int(sys.stdin.readline().rstrip())
arr = [[0 for _ in range(n)] for _ in range(2)]
for i in range(n):
    u, v = map(int, sys.stdin.readline().split())
    arr[0][i], arr[1][i] = u, v

hap = [[0 for _ in range(n)] for _ in range(2)]
tir = [[0 for _ in range(n)] for _ in range(2)]

hap[0][0] = arr[0][0]
hap[1][n-1] = arr[0][n-1]
tir[0][0] = arr[1][0]
tir[1][n-1] = arr[1][n-1]

for i in range(1, n):
    if arr[0][i] == 0:
        hap[0][i] = hap[0][i-1]
    elif hap[0][i-1] == 0:
        hap[0][i] = arr[0][i]
    else:
        hap[0][i] = min(hap[0][i-1], arr[0][i])

    if arr[1][i] == 0:
        tir[0][i] = tir[0][i-1]
    elif tir[0][i-1] == 0:
        tir[0][i] = arr[1][i]
    else:
        tir[0][i] = max(tir[0][i-1], arr[1][i])

    if arr[0][n-1-i] == 0:
        hap[1][n-1-i] = hap[1][n-i]
    elif hap[1][n-i] == 0:
        hap[1][n-1-i] = arr[0][n-1-i]
    else:
        hap[1][n-1-i] = max(hap[1][n-i], arr[0][n-1-i])

    if arr[1][n-1-i] == 0:
        tir[1][n-1-i] = tir[1][n-i]
    elif tir[1][n-1] == 0:
        tir[1][n-1-i] = arr[1][n-1-i]
    else:
        tir[1][n-1-i] = min(tir[1][n-i], arr[1][n-1-i])

for k in range(n-2, -1, -1):
    if hap[0][k] == 0 or hap[1][k+1] == 0 or hap[0][k] > hap[1][k+1]:
        if tir[0][k] == 0 or tir[1][k+1] == 0 or tir[0][k] < tir[1][k+1]:
            sys.stdout.write(str(k+1))
            exit(0)

if hap[0][n-1] == 0 and tir[0][n-1] == 0:
    sys.stdout.write(str(n-1))
    exit(0)

sys.stdout.write('-1')
