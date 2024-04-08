import sys

n, k = map(int, sys.stdin.readline().split())
input_data = list(map(int, sys.stdin.readline().split()))

dist = []
start = 0
for d in input_data:
    dist.append([start, start+d])
    start += d

total_size = sum(input_data)
if k > total_size:
    k = 2 * total_size - k

for i in range(n):
    if dist[i][0] <= k < dist[i][1]:
        sys.stdout.write(str(i+1))
        break
        