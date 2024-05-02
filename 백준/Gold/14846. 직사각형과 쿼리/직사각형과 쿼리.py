import sys

n = int(sys.stdin.readline().rstrip())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

prefix = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(11)]

for i in range(n):
    for j in range(n):
        prefix[arr[i][j]][i+1][j+1] += 1

for num in range(1, 11):
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix[num][i][j] += prefix[num][i-1][j] + prefix[num][i][j-1] - prefix[num][i-1][j-1]

q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    cnt = 0
    for num in range(1, 11):
        word = prefix[num][x2][y2] - prefix[num][x1-1][y2] - prefix[num][x2][y1-1] + prefix[num][x1-1][y1-1]
        if word > 0:
            cnt += 1

    sys.stdout.write(str(cnt) + '\n')
