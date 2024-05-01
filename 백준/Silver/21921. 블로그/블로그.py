import sys

n, x = map(int, sys.stdin.readline().split())
visit = list(map(int, sys.stdin.readline().split()))
visit = [0] + visit

for i in range(1, n+1):
    visit[i] += visit[i-1]

max_visited, cnt = 0, 0

for i in range(n+1-x):
    visit_now = visit[i+x] - visit[i]
    if visit_now > max_visited:
        max_visited = visit_now
        cnt = 1
    elif visit_now == max_visited:
        cnt += 1

if max_visited == 0:
    sys.stdout.write("SAD")
else:
    sys.stdout.write(str(max_visited) + '\n' + str(cnt))
