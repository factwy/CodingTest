import sys

n = int(sys.stdin.readline().rstrip())

color = [1] * (n+1)
color_type = 2

for i in range(2, n+1):
    if color[i] != 1:
        continue

    for j in range(i, n+1, i):
        if color[j] == 1:
            color[j] = color_type

    color_type += 1

sys.stdout.write(str(color_type - 1) + '\n')
for i in range(1, n+1):
    sys.stdout.write(str(color[i]) + ' ')
sys.stdout.write('\n')
