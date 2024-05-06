import sys
import math

n, e = map(int, sys.stdin.readline().split())
total_sum = 0
r_arr = list(map(int, sys.stdin.readline().split()))

for r in r_arr:
    num = e / (2*r)
    if num < -1 or num > 1:
        total_sum += 1
        continue
    x = int(math.pi / math.asin(num) + 0.0000000001)
    total_sum += x

print(total_sum)
