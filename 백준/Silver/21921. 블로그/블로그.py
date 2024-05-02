import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix = [0 for _ in range(n+1)]

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

max_visited, cnt = 0, 0
for i in range(n+1-x):
    visited = prefix[i+x] - prefix[i]

    if visited > max_visited:
        max_visited = visited
        cnt = 1
    elif visited == max_visited:
        cnt += 1

if max_visited > 0:
    sys.stdout.write(f"{max_visited}\n{cnt}\n")
else:
    sys.stdout.write("SAD\n")
    