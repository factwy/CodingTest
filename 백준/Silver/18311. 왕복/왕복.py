import sys

n, k = map(int, sys.stdin.readline().split())
input_data = list(map(int, sys.stdin.readline().split()))

total_size = sum(input_data)
if k > total_size:
    k = 2 * total_size - k

start = 0
for i, d in enumerate(input_data):
    if start <= k < start + d:
        sys.stdout.write(str(i+1))
        break
    start += d
