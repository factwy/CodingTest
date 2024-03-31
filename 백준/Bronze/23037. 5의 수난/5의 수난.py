import sys

numbers = [i**5 for i in range(10)]

num = int(sys.stdin.readline())
res = 0

for _ in range(5):
    now = num % 10
    res += numbers[now]
    num = num // 10

sys.stdout.write(str(res))
