import sys

n = int(sys.stdin.readline().rstrip())

min_squ = 5 * (10 ** 9)

for w in range(1, 70711):
    h = n // (w+1) - 1
    if h < 1:
        h = 1

    while (w+1)*(h+1) < n:
        h += 1

    min_squ = min(min_squ, 2*(w+h))

print(min_squ)
